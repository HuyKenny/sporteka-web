"""sporteka.cz — brand texts wave 211: lacoste, 4f, kilpi, dare2b.
Only what follows from the catalogue (categories, product names); no prices, counts, history or invented technologies."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ lacoste
NEW['lacoste'] = dict(
    title='Lacoste: tenisky, polokošile, trička a mikiny pro každý den',
    desc='Lacoste v katalogu Sporteky: tenisky, polokošile, trička, mikiny a tepláky pro muže i ženy. Jak vybrat velikost, barvu a kdy hledat slevy.',
    intro='<p>Lacoste je v katalogu Sporteky hlavně značka městské a volnočasové módy se sportovním nádechem. Nejobsáhlejší skupinou jsou <a href="/tenisky/">tenisky a volnočasové boty</a>, za nimi následují <a href="/sportovni-tricka/">trička</a>, <a href="/polokosile/">polokošile</a>, <a href="/mikiny/">mikiny</a> a <a href="/teplaky/">tepláky</a>. Menší část tvoří žabky, kraťasy, plavky, čepice a ponožky.</p>'
          '<p>Nabídka míří téměř rovným dílem na muže a ženy, dětských kousků je podstatně méně. Barevně vládne bílá, daleko za ní jsou černá, modrá a béžová. Stránka vysvětluje, jak se v takovém sortimentu orientovat, čím se liší jednotlivé typy bot a oblečení, jak volit velikosti, jak o věci pečovat a v jakých chvílích se vyplatí porovnávat obchody a sledovat slevy.</p>',
    guide='<h2>Co Lacoste v katalogu nabízí</h2>'
          '<p>Když si necháte vypsat zboží této značky, zjistíte, že oblečení a obuv jsou tu v jiném poměru než u klasických sportovních výrobců. Převažuje obuv na každodenní nošení, zatímco výkonnostní vybavení na konkrétní disciplínu tu téměř chybí. To je důležitá informace: Lacoste kupujete spíš kvůli stylu, střihu a kvalitě zpracování než kvůli specializovanému výkonu. Přehled hlavních skupin ukazuje tabulka.</p>'
          + T(['Skupina', 'Co v ní hledat', 'Pro koho se hodí'], [
              ['<a href="/tenisky/">Tenisky a volnočasové boty</a>', 'kožené i textilní modely, nízké kousky s bílou podrážkou, plošinové varianty', 'každodenní nošení ve městě, kancelář s uvolněným dresscodem'],
              ['<a href="/sportovni-tricka/">Trička a tílka</a>', 'bavlněné basic střihy, crop topy, kousky s drobným logem', 'jako základ šatníku i pod mikinu'],
              ['<a href="/polokosile/">Polokošile</a>', 'klasické polo střihy s límečkem a knoflíkovou légou', 'smart casual, golf, léto, cestování'],
              ['<a href="/mikiny/">Mikiny</a>', 'mikiny s kapucí, bez kapuce, oversize střihy', 'chladnější dny, vrstvení'],
              ['<a href="/teplaky/">Tepláky</a>', 'úzké a rovné střihy, měkké úpletové materiály', 'doma, na cesty, ke sportovnímu stylu'],
              ['<a href="/sportovni-kratasy/">Kraťasy</a> a <a href="/plavky/">plavky</a>', 'šortky s bavlnou, plavecké šortky', 'léto, dovolená, bazén'],
              ['<a href="/pantofle-a-zabky/">Pantofle a žabky</a>', 'lehká obuv k vodě a do domu', 'koupaliště, hotel, domácí použití']]) +
          '<p>Z názvů produktů je vidět, že se hodně pracuje s přírodními materiály. Ve výpisu se opakují slova bavlněné, s bavlnou a lněné, což ladí s letním a přechodovým charakterem sortimentu. Najdete tu ale i péřovou bundu nebo kožené boty, takže značka pokrývá celý rok, jen těžiště leží v teplejší půlce.</p>'
          '<h2>Pro koho je značka v katalogu určená</h2>'
          '<p>Rozdělení podle pohlaví je na stránce vyrovnané. Pánských a dámských kousků je přibližně stejně, zatímco dětské a unisex modely jsou spíš doplněk. Praktický dopad je jasný. Pokud hledáte dárek pro dospívajícího nebo mladého dospělého, máte výběr široký. Pro malé děti je nabídka užší a vyplatí se kontrolovat dostupnost velikostí napříč obchody. U unisex kousků si většinou vystačíte s tabulkou velikostí a lehce volnějším střihem.</p>'
          '<p>Vedle pohlaví pomáhá filtr podle barvy. Bílá převažuje zcela zjevně, což odpovídá charakteru bot a polokošil. Pokud ale nechcete bílé tenisky, které se rychle špiní, dívejte se na černé, modré nebo béžové varianty. Pro ucelený outfit se hodí kombinace jedné neutrální barvy a jedné světlejší. Tmavé boty snesou deštivý podzim, světlé jsou ideální na suché měsíce.</p>'
          '<h2>Tenisky: nejdůležitější kategorie</h2>'
          '<p>Lacoste tenisky patří k tomu, o co se zájem opírá nejvíc. V názvech se opakují modely Carnaby, Ziane nebo Elite Active, ve výpisu se objevují i kožené kousky, které mají jednoduchý minimalistický vzhled. Při výběru ověřte tři věci. Za prvé materiál svršku: kůže drží tvar a dá se otřít, textil dýchá lépe a je lehčí. Za druhé podrážku: plošinová je módní, plochá a tenčí se lépe hodí na delší chůzi. Za třetí šněrování nebo zapínání, protože od něj záleží, jak dobře se bota přizpůsobí nártu.</p>'
          '<ul><li><strong>Na každodenní chůzi:</strong> hledejte model s měkkou stélkou a pružnou podrážkou, ať vás nebolí chodidla po delším dni ve městě.</li>'
          '<li><strong>Do kanceláře:</strong> kožený nízký model v bílé, černé nebo tmavě modré, který se hodí k chinos kalhotám.</li>'
          '<li><strong>K sukni nebo šatům:</strong> plošinová bota přidá výšku a oživí jednoduchý outfit.</li>'
          '<li><strong>Na léto:</strong> textilní nebo perforovaná varianta s lepším odvětráním.</li></ul>'
          '<p>Další obuv tohoto typu najdete také u jiných módních značek, například ' + B(('adidas', 'Adidas'), ('puma', 'Puma'), ('nike', 'Nike')) + '. Lacoste se mezi nimi odlišuje spíš elegantním, čistým vzhledem než výrazným technickým designem. Pokud potřebujete tenisky na běh nebo trénink, jsou na místě specializované kategorie, nikoli módní obuv.</p>'
          '<h2>Polokošile a trička: jak vybrat střih</h2>'
          '<p>Polokošile je typický kousek, který se na pomezí sportu a společenského oblečení nosí nejlépe. Zvolte klasický střih, pokud ji budete nosit pod sako, nebo rovnější sportovní střih, pokud ji budete nosit k šortkám. Na kvalitu poznáte stejnoměrný šev u límce, pevné knoflíky a materiál, který se po vyprání nedeformuje. Konkrétní výběr podle pohlaví a barvy najdete v landingu <a href="/lacoste-polokosile/">Lacoste polokošile</a>.</p>'
          '<p>U triček je důležitější délka a střih než logo. Bavlněné basic kousky nosíte pod vrstvy nebo samostatně. Crop top se kombinuje s kalhotami s vysokým pasem. Pokud tričko perete často, vybírejte tmavší nebo středně sytou barvu, na bílé se rychle projeví potu a drobné skvrny. Pro srovnání s jinými značkami si prohlédněte i ' + B(('polo-ralph-lauren', 'Polo Ralph Lauren'), ('tommy-hilfiger', 'Tommy Hilfiger')) + ', které nabízejí podobné klasické střihy.</p>'
          '<h2>Mikiny, tepláky a ostatní oblečení</h2>'
          '<p>Mikiny z bavlny nebo směsi s bavlnou jsou měkké, příjemné na kůži a dobře se perou. Mikina s kapucí je praktičtější na chladnější dny, bez kapuce působí upraveněji a hodí se k košili. Oversize střih pro ženy je vhodný k legínám i k šortkám, ale u něj počítejte s tím, že na velikosti odpovídající běžné konfekci bude vypadat volněji, než je zvykem. Podobně u tepláků: zúžené se hodí k teniskám, rovné působí klidněji a jsou pohodlnější doma.</p>'
          '<p>Zbylé kategorie doplňují letní nebo cestovní šatník. <a href="/cepice-a-celenky/">Čepice a kšiltovky</a> se hodí jako doplněk k jednoduchému outfitu, <a href="/sportovni-ponozky/">ponožky</a> jsou praktickým dárkem, <a href="/kosile/">košile</a> z lnu patří k horkým dnům. Na dovolenou přidejte <a href="/plavky/">plavky</a> a žabky.</p>'
          '<h2>Velikosti a střihy</h2>'
          '<p>Oblečení se u módních značek často liší od standardní sportovní konfekce. Polokošile mívají přiléhavější střih a u mikin nebo triček záleží na tom, zda jde o regular, slim nebo oversize. Z názvu produktu a popisu zjistíte, o jaký střih jde. Pokud váháte mezi dvěma velikostmi, vezměte tu větší u bavlněných kousků, protože se mohou po praní mírně srazit, a menší u elastických materiálů.</p>'
          + T(['Typ zboží', 'Na co se zaměřit', 'Rada při váhání'], [
              ['Tenisky', 'délka chodidla v centimetrech, šířka nártu', 'změřte nohu večer, kdy je největší'],
              ['Polokošile', 'šířka ramen a délka rukávu', 'zvolte podle ramen, ne podle pasu'],
              ['Trička', 'délka a střih (regular, crop, oversize)', 'přečtěte si popis střihu'],
              ['Mikiny a tepláky', 'volnost v pasu a délka nohavic', 'bavlněné modely berte raději o číslo větší'],
              ['Kraťasy a plavky', 'obvod pasu, délka nad kolena', 'u plavek zkontrolujte vnitřní podšívku']]) +
          '<h2>Péče a životnost</h2>'
          '<p>Bavlněné a lněné kousky perte na doporučené teplotě a obracejte je naruby, ať se neotírá potisk. Polokošile nesušte v sušičce, límeček si udrží tvar lépe při sušení na ramínku. Kožené boty pravidelně otírejte vlhkým hadříkem a občas ošetřete krémem, textilní čistěte kartáčkem a jemným mýdlem. Tenisky nepeřte v pračce, jen ve výjimečných případech a na šetrný program podle štítku. Díky péči vydrží kvalitní kousky několik sezón a koupě dražšího kusu se vyplatí.</p>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>U módních značek se slevy opakují hlavně na konci sezóny. Letní tenisky, trička a plavky zlevňují na přelomu léta a podzimu, mikiny a péřové bundy po zimě. Mezi obchody bývají velké rozdíly, protože každý má jinou zásobu a jinou strategii. Na Sporteka.cz proto porovnejte stejný produkt napříč nabídkami a hlídejte, zda je dostupná vaše velikost. Nejrychleji mizí nejoblíbenější barvy, tedy bílá a černá, takže na ně nečekejte příliš dlouho.</p>'
          '<p>Jestli hledáte příbuzné produkty, projděte i jiné módní nebo volnočasové značky: ' + B(('adidas', 'Adidas'), ('puma', 'Puma'), ('nike', 'Nike')) + '.</p>',
    faq=[
        ('Co vlastně Lacoste v katalogu nabízí?',
         'Největší část tvoří tenisky a volnočasové boty, za nimi trička, polokošile, mikiny a tepláky. Menší skupiny jsou žabky, kraťasy, plavky, čepice, košile a ponožky. Je to tedy značka městského a volnočasového oblečení, ne specializovaného výkonnostního vybavení.'),
        ('Je zboží určené spíš mužům, nebo ženám?',
         'V katalogu je poměr téměř vyrovnaný, pánských kousků je jen o něco víc než dámských. Dětských modelů je výrazně méně a unisex jen málo. Pro děti proto kontrolujte dostupnost velikostí u více obchodů.'),
        ('Jak vybrat velikost tenisek?',
         'Změřte chodidlo v centimetrech večer a porovnejte s tabulkou výrobce. Kožené boty se časem trochu přizpůsobí, textilní se tolik nerozšíří. Pokud máte širší nárt, zkoušejte raději větší číslo, nebo model s pružnějším svrškem.'),
        ('Jaký je rozdíl mezi polokošilí a tričkem?',
         'Polokošile má límeček a knoflíkovou légu, takže působí upraveněji a snese kombinaci se sakem nebo chino kalhotami. Tričko je jednodušší, kratší a hodí se pod mikinu nebo samostatně. Obě varianty jsou z bavlny nebo směsi.'),
        ('Kterou barvu zvolit, aby se zboží nejméně špinilo?',
         'Tmavé a středně sytě barvené kousky skryjí drobné skvrny, ale bílá patří k charakteru značky. U bílých bot pomáhají impregnace a pravidelné otírání. U bílých triček počítejte s častějším praním.'),
        ('Jak pečovat o kožené tenisky?',
         'Po každém nošení je otřete vlhkým hadříkem a vyjměte stélky, aby vyschly. Jednou za čas použijte krém na kůži odpovídající barvy. Nesušte je na radiátoru, kůže by popraskala. Do pračky je nedávejte.'),
        ('Dají se kousky této značky nosit i při sportu?',
         'Na lehkou rekreační aktivitu, například procházku nebo golf s polokošilí, ano. Pro běh, fitness nebo týmové sporty ale sáhněte po obuvi a oblečení s technickými materiály, které lépe odvádějí pot a drží tvar. Hodí se k tomu jiné kategorie.'),
        ('Kdy bývají kousky nejlevnější?',
         'Typicky při výprodeji sezónního zboží: letní věci na konci léta, zimní po zimě. Zlevňují také starší barvy a velikosti, které už nejsou ve všech obchodech. Nejvíc ušetříte, když porovnáte více obchodů najednou.'),
        ('Jak rozeznat originální kus od padělku?',
         'Kupujte v ověřených obchodech, které zboží uvádějí s oficiální kategorizací a vracejí zboží ve lhůtě. Pozor na neobvykle nízkou cenu, špatný šev nebo logo se zkomolenou podobou. Sporteka zobrazuje nabídky pouze od ověřených prodejců.'),
        ('Do jaké kategorie spadají ostatní kusy, které nejsou oblečení?',
         'Ve výpisu najdete také čepice, kšiltovky, sportovní ponožky a pantofle. Jde o doplňky, které rozšiřují outfit. Vyplatí se je kombinovat s hlavním kusem, například kšiltovku k tričku.')])

# ------------------------------------------------------------------ 4f
NEW['4f'] = dict(
    title='4F: sportovní oblečení, legíny, trička a lyžařské bundy',
    desc='4F v katalogu Sporteky: trička, tepláky, legíny, mikiny, plavky a zimní oblečení pro ženy, muže i děti. Jak vybírat, prát a hlídat slevy.',
    intro='<p>4F je v katalogu Sporteky široká značka sportovního oblečení pro každodenní pohyb. Největší skupinou jsou <a href="/sportovni-tricka/">sportovní trička</a>, následují <a href="/teplaky/">tepláky</a>, <a href="/tenisky/">tenisky</a>, <a href="/sportovni-kratasy/">kraťasy</a>, <a href="/mikiny/">mikiny</a> a <a href="/leginy/">legíny</a>. Zajímavě silné jsou také <a href="/cepice-a-celenky/">čepice</a>, <a href="/plavky/">plavky</a> a zimní doplňky.</p>'
          '<p>Z hlediska pohlaví vede dámský sortiment, ale velkou část zboží tvoří i pánské a hlavně dětské kousky. Barevně převažuje černá, hned za ní modrá a šedá. Značka tak pokrývá celý rok, od letních šortek po zimní čepice a rukavice. Tento průvodce ukazuje, co v nabídce hledat, jak volit mezi typy oblečení, jak zvolit velikost pro děti a dospělé, jak o věci pečovat a jak sledovat slevy napříč obchody.</p>',
    guide='<h2>Z čeho se sortiment 4F skládá</h2>'
          '<p>Ve výpisu značky se potkává základní sportovní šatník s lehkou zimní vrstvou. Na rozdíl od specializovaných lyžařských nebo outdoorových značek tu nenajdete jednu dominantní disciplínu, ale pestrou paletu věcí pro běžný aktivní den. Proto je vhodné nejprve rozhodnout, k čemu zboží potřebujete, a až poté vybírat konkrétní kus.</p>'
          + T(['Kategorie', 'Co v ní najdete', 'Typické použití'], [
              ['<a href="/sportovni-tricka/">Trička a tílka</a>', 'sportovní trička z rychleschnoucích i bavlněných materiálů', 'trénink, běh, každodenní nošení'],
              ['<a href="/teplaky/">Tepláky</a>', 'volné i úzké střihy, často s lemem u kotníků', 'doma, na cesty, na trénink'],
              ['<a href="/leginy/">Legíny</a>', 'úzké a vysoké střihy, sportovní podprsenky', 'fitness, jóga, běh, volný čas'],
              ['<a href="/mikiny/">Mikiny</a>', 'tréninkové mikiny se zipem, mikiny s kapucí', 'rozcvička, chladnější dny'],
              ['<a href="/sportovni-bundy-jaro-podzim/">Jarní a podzimní bundy</a>', 'lehké bundy a vesty', 'přechodová období, město'],
              ['<a href="/termopradlo/">Funkční prádlo</a>', 'spodní vrstva pod lyžařské a zimní oblečení', 'lyže, zimní běh, túry'],
              ['<a href="/cepice-a-celenky/">Čepice a čelenky</a>', 'zimní čepice, kšiltovky, čelenky', 'celý rok podle typu']]) +
          '<p>Z názvů vzorového zboží je patrné, že sortiment zahrnuje také lyžařské kalhoty, rukavice a dětské lyžařské bundy. Zimní část je tedy zastoupená, ale nejde o její jádro. Pokud plánujete náročnější lyžování, porovnejte nabídku s <a href="/lyzarske-bundy/">lyžařskými bundami</a> a <a href="/lyzarske-kalhoty/">lyžařskými kalhotami</a> od specializovaných značek, jako jsou ' + B(('kilpi', 'Kilpi'), ('dare2b', 'Dare2b')) + '.</p>'
          '<h2>Pro koho se 4F hodí</h2>'
          '<p>V katalogu je nejvíc dámského zboží, ale pánský a dětský sortiment není zanedbatelný. Zvláště děti mají velký podíl, což je pro značku charakteristické: najdete tu chlapecké žabky, dětské lyžařské bundy i dětské plavky. Při nákupu pro rostoucí dítě je praktické vybírat o jednu velikost větší, zejména u bund a kalhot. U triček a plavek raději zvolte přesnou velikost, aby neplandaly.</p>'
          '<p>Pro dospělé je důležité sledovat označení střihu. Dámské kousky bývají přiléhavější, pánské rovnější. Unisex modely jsou doplněk a hodí se hlavně k čepicím a doplňkům. Pokud nosíte mezivelikost, zkontrolujte tabulku rozměrů u konkrétního produktu, protože střih se může lišit i uvnitř jedné řady.</p>'
          '<h2>Trička a tílka: základ šatníku</h2>'
          '<p>Trička jsou největší kategorií značky. Najdete mezi nimi jednoduché kousky s logem i sportovní trička z hladké, rychleschnoucí pleteniny. Na trénink se vyplatí syntetika, protože odvádí pot a rychle schne. Na běžné nošení bude příjemnější bavlna nebo směs. Pokud trička často perete, zvolte tmavší odstín, který snese víc praní. K tomu se hodí také <a href="/tilka/">tílka a topy</a>, kterých je v nabídce dost, zejména pro ženy.</p>'
          '<ul><li><strong>Na běh:</strong> hladké švy, lehká tkanina, střih, který se nehrne.</li>'
          '<li><strong>Do posilovny:</strong> pružnější materiál a volnější proporce kolem paží.</li>'
          '<li><strong>Na každý den:</strong> měkká bavlněná směs, která se příjemně nosí i po praní.</li>'
          '<li><strong>Pod mikinu:</strong> tenčí tričko, které se nebude kupit na zádech.</li></ul>'
          '<h2>Legíny, tepláky a kraťasy</h2>'
          '<p>Legíny patří k nejčastějším kouskům ženského sportovního šatníku. Vysoký pas drží břicho, širší gumička se nesroluje při pohybu. Zkoušejte je v dřepu: pokud látka nepropouští světlo a neklouže, je materiál dost hustý. Sportovní podprsenky vybírejte podle intenzity pohybu. Pro jógu stačí lehká podpora, pro běh potřebujete pevnější model. Tepláky dostanete jak v úzkém střihu k teniskám, tak ve volnějším pro odpočinek. Kraťasy se hodí na létě, pro běh mají vnitřní podšívku, pro fitness bývají kratší a pružnější.</p>'
          '<p>Při výběru nohavic zohledněte svoji výšku. Dlouhé legíny mohou být na nižší postavě zbytečně dlouhé a trochu se skládají, kratší pak zase nezakryjí kotník u vyšších lidí. Kalhoty se zúženým lemem jsou praktické do zimy, protože zůstávají nad botou a nezachytávají sníh.</p>'
          '<h2>Zima, vrstvení a funkční prádlo</h2>'
          '<p>Zimní část značky se dá využít jako cenově dostupnější vrstva pro rekreační lyžování a pro zimní procházky. Základem je správné vrstvení: spodní <a href="/termopradlo/">termoprádlo</a>, střední vrstva z fleecu nebo mikiny a vrchní bunda, která chrání před větrem a sněhem. Nejvíc se prádlo uplatní při pohybu. Při sezení v zimě nebo na vleku ocení vaše tělo další teplejší vrstvu.</p>'
          + T(['Vrstva', 'Úkol', 'Co vybrat'], [
              ['Spodní', 'odvádí pot od kůže', 'funkční triko a kalhoty z hladkého materiálu, ne bavlna'],
              ['Střední', 'drží teplo', '<a href="/fleecove-mikiny/">fleecová mikina</a> nebo lehká mikina'],
              ['Vrchní', 'chrání před větrem a sněhem', 'lyžařská nebo zimní bunda, kalhoty s membránou'],
              ['Doplňky', 'chrání extrémní místa', 'čepice, rukavice, nákrčník, ponožky']]) +
          '<p>Pro děti je důležité, aby dětské lyžařské bundy měly zesílená ramena, pevný zip a hlavně dostatečně dlouhé rukávy, které se dají upravit. Při výběru zvolte velikost s mírnou rezervou a ověřte, že bunda nebude bránit pohybu paží. Neprofukující materiál ocení děti i při dlouhých dnech na svahu.</p>'
          '<h2>Tenisky a volnočasová obuv</h2>'
          '<p>Ve výpisu najdete také <a href="/tenisky/">tenisky a volnočasové boty</a>, které doplňují sportovní styl. Hodí se na každodenní chůzi, do školy nebo na procházku, ne na náročný běh. Dobrou volbou je lehká bota s pružnou podrážkou, která netlačí ani při delším dni. U dětí vybírejte obuv s prostorem pro prsty a pevnou špičkou, protože rostoucí noha potřebuje volnost. Pokud bota v obchodě tlačí, nespoléhejte na to, že se rozchodí.</p>'
          '<h2>Plavky, žabky a letní kousky</h2>'
          '<p>Do letní nabídky patří <a href="/plavky/">plavky</a>, <a href="/pantofle-a-zabky/">žabky</a> a lehké kraťasy. Plavky vybírejte podle pohybu: pro plavání v bazénu se hodí pevnější střih, který drží při odrazu, na pláž stačí pohodlnější. Dětské plavky mají zpravidla pružnou gumičku v pase a sušší se rychle. Žabky z pěny nebo gumy jsou ideální k vodě, ale na dlouhou chůzi nejsou vhodné. Pro delší cesty v teple použijte raději sandály nebo sportovní obuv.</p>'
          '<h2>Čepice, doplňky a drobnosti</h2>'
          '<p>Čepice a čelenky tvoří překvapivě velkou část nabídky. Zimní čepice se prodávají v mnoha barvách, od černé po bílou a růžovou, a často mají jednoduché logo. Při výběru zkontrolujte podšívku: jednovrstvé pletené modely jsou lehké, dvouvrstvé a s fleecem hřejí víc. Kšiltovky jsou praktické na slunce a pro běh, čelenka chrání uši při běhu v chladu a nezpůsobí přehřátí. Rukavice vybírejte podle činnosti, lyžařské s dostatečně dlouhou manžetou, běžecké tenké a pružné. Drobné doplňky jsou dobrý dárek, protože nemusíte řešit velikost a barva se snadno kombinuje.</p>'
          '<p>Podobně praktické jsou i ponožky a podprsenky ve výpisu. Sportovní podprsenku zkoušejte v pohybu, pásek pod prsy nesmí řezat a ramínka nemají klouzat. Pokud ji kupujete online, vezměte si obvod hrudníku a porovnejte s tabulkou, nikoli podle velikosti běžné konfekce.</p>'
          '<h2>Velikosti, péče a životnost</h2>'
          '<p>Značka vyrábí pro širokou škálu postav, proto doporučujeme vždy zkontrolovat tabulku velikostí u produktu. Sportovní prádlo perte při teplotě uvedené na štítku, bez aviváže, která zhoršuje odvod potu, a nesušte na radiátoru. Legíny a plavky perte v pytlíku proti zachytávání. Zimní bundy periodicky obnovte impregnací podle pokynů a před uložením je dobře vysušte, aby nezplesnivěly.</p>'
          '<h2>Jak hledat slevy</h2>'
          '<p>Slevy se u této značky objevují nejvíc na konci sezóny, ale široký sortiment znamená, že se v průběhu roku najde výhodný kousek téměř vždy. Zimní bundy, rukavice a čepice zlevňují na jaře, plavky a žabky na konci léta. Cenový rozdíl mezi obchody se může u stejné mikiny výrazně lišit, proto porovnejte více nabídek najednou. Pokud potřebujete konkrétní velikost, nenechávejte nákup na poslední chvíli, protože nejčastěji se rozprodají základní barvy.</p>'
          '<p>Pro srovnání s dalšími značkami, které nabízejí podobné sportovní oblečení, otevřete také ' + B(('adidas', 'Adidas'), ('puma', 'Puma'), ('nike', 'Nike')) + '.</p>',
    faq=[
        ('Jaké zboží 4F v katalogu převažuje?',
         'Největší skupinou jsou sportovní trička, následují tepláky, tenisky, kraťasy, mikiny a legíny. Silně jsou zastoupeny také čepice, plavky a žabky. Zimní zboží, jako jsou lyžařské bundy, kalhoty a rukavice, tvoří menší, ale znatelnou část.'),
        ('Je značka vhodná i pro děti?',
         'Ano, dětský sortiment je výrazný. Najdete v něm žabky, plavky, lyžařské bundy a sportovní oblečení. U dětí vybírejte raději o něco větší velikost u bund a kalhot, protože rychle rostou.'),
        ('Jak vybrat správné legíny?',
         'Zvolte vysoký pas s širší gumičkou, látku, která se v dřepu nestává průsvitnou, a délku podle výšky. Na běh se hodí rychleschnoucí materiál, na jógu spíš měkčí. Před koupí zkontrolujte tabulku velikostí.'),
        ('Dají se věci použít na lyžování?',
         'Pro rekreační lyžování ano, zejména dětské bundy, kalhoty a rukavice. Pro náročný terén nebo celodenní pobyt na svahu zvažte specializované lyžařské značky, které mají víc zimních kategorií a spolehlivější membrány.'),
        ('Jak prát sportovní oblečení, aby vydrželo?',
         'Perte při teplotě na štítku, bez aviváže a bez bělidel. Oblečení obracejte naruby, aby se šetřil potisk. Sušte na vzduchu, ne na radiátoru. Legíny a plavky dávejte do pytlíku, aby se nezachytily o suchý zip.'),
        ('Jaká barva se nejlépe hodí?',
         'Černá je nejuniverzálnější a skryje skvrny. Šedá a modrá se dobře kombinují. Světlé odstíny, jako je růžová nebo bílá, působí svěže, ale potřebují častější praní a ošetření.'),
        ('Co si vybrat na zimu pod bundu?',
         'Funkční spodní prádlo odvádí pot a udrží teplo. Nad ním použijte fleecovou nebo tenčí mikinu. Bavlněné tričko pod bundu nedávejte, vlhkost drží u těla a rychle ochladí.'),
        ('Kdy se vyplatí čekat na slevu?',
         'Zimní kousky zlevňují na jaře, letní na konci sezóny. U základních kusů, například triček nebo tepláků, se sleva objevuje průběžně. Porovnejte více obchodů, jejich ceny se liší nezávisle na sobě.'),
        ('Mohu na jedné stránce porovnat i podobné značky?',
         'Ano, na stránkách značek najdete odkazy na další výrobce sportovního oblečení. Stačí kliknout a porovnat nabídky, střihy a barvy. Pomůže také filtr podle pohlaví a velikosti.'),
        ('Jak poznat, zda je oblečení dost kvalitní?',
         'Zkontrolujte šev, zip a gumičku v pase. Materiál by se neměl po vyprání deformovat. U sportovních kousků hledejte údaj o materiálu ve složení. Čím víc elastanu, tím větší pružnost, ale pozor na přílišné napínání.')])

# ------------------------------------------------------------------ kilpi
NEW['kilpi'] = dict(
    title='Kilpi: lyžařské bundy, kalhoty a outdoorové oblečení',
    desc='Kilpi v katalogu Sporteky: lyžařské kalhoty a bundy, jarní bundy, softshell, fleece i cyklooblečení. Jak vybrat vrstvy, velikost a slevy.',
    intro='<p>Kilpi je v katalogu Sporteky outdoorová a zimní značka s důrazem na oblečení do hor i na výlety. Největší skupinou jsou <a href="/lyzarske-kalhoty/">lyžařské a snowboardové kalhoty</a>, těsně za nimi <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>. Silné je i oblečení pro celoroční aktivity: <a href="/sportovni-kalhoty/">sportovní kalhoty</a>, <a href="/sportovni-tricka/">trička</a>, <a href="/lyzarske-bundy/">lyžařské bundy</a>, <a href="/softshellove-bundy/">softshelly</a> a <a href="/fleecove-mikiny/">fleecové mikiny</a>.</p>'
          '<p>Rozdělení podle pohlaví je vyrovnané mezi dámy a pány, přibývá také dětských a unisex kousků. Barevně převažuje černá, následuje modrá a zelená. Ve vzorku zboží se objevují i hybridní bundy se zateplením, nepromokavé skořepiny a trička z merino vlny. Stránka vysvětluje, jak vybírat zimní a přechodové vrstvy, jak číst názvy modelů, jak pečovat o membrány a kdy sledovat slevy.</p>',
    guide='<h2>Co Kilpi v katalogu nabízí</h2>'
          '<p>Kilpi vyniká tím, že pokrývá téměř celý rok. V zimě tu najdete lyžařské kalhoty a bundy včetně softshellových variant a hybridních modelů se zateplením, na jaře a na podzim lehčí bundy a softshell, v létě trička, kraťasy a cyklistické oblečení. V názvech se často vyskytují označení jako W pro dámské modely a M pro pánské, což pomáhá ve výpisu rychle rozlišit střih. Tabulka shrnuje hlavní oblasti.</p>'
          + T(['Oblast', 'Kategorie', 'K čemu se hodí'], [
              ['Lyžování a snowboarding', '<a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>, <a href="/lyzarske-bundy/">lyžařské bundy</a>', 'sjezdovka, freeride, zimní výlety'],
              ['Přechodové období', '<a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>, <a href="/softshellove-bundy/">softshell</a>', 'město, procházky, krátké túry'],
              ['Outdoor', '<a href="/outdoorove-kalhoty/">outdoorové kalhoty</a>, <a href="/sportovni-kalhoty/">sportovní kalhoty</a>', 'turistika, kemping, cestování'],
              ['Střední vrstva', '<a href="/fleecove-mikiny/">fleecové mikiny</a>, <a href="/mikiny/">mikiny</a>', 'pod bundu nebo samostatně'],
              ['Léto a kolo', '<a href="/cyklisticke-obleceni/">cyklistické oblečení</a>, <a href="/cyklo-prislusenstvi/">příslušenství</a>, <a href="/sportovni-kratasy/">kraťasy</a>', 'kolo, výlety, běžný provoz'],
              ['Spodní vrstva', '<a href="/sportovni-tricka/">trička</a>, termoprádlo, merino', 'pod vrstvy i samostatně']]) +
          '<p>Ve vzorku zboží vidíte i prvky, které se vyplatí číst v názvu: softshell u kalhot a bund, hybridní lyžařská bunda se zateplením Primaloft, nepromokavá bunda nebo tričko z merino vlny. Tyto údaje pomáhají odhadnout, k čemu je kus určen, ještě než otevřete detail.</p>'
          '<h2>Pro koho je značka určená</h2>'
          '<p>Dámský a pánský sortiment je téměř vyrovnaný, takže u obou pohlaví najdete široký výběr. Dětské kousky tvoří znatelnou část, hlavně lyžařské bundy, kalhoty a oblečení na zimní hrátky. Unisex modely se vyskytují u doplňků a u některých triček a mikin. Pokud hledáte oblečení pro celou rodinu, můžete většinu nákupu udělat na jednom místě a v jedné řadě barev, což je praktické při společných výletech.</p>'
          '<p>U barev dominuje černá, která je univerzální a nenápadná. Modré a zelené tóny se hodí do přírody, růžová a červená jsou dobře vidět na svahu, což je důležité především u dětí. Světlé barvy se snáz najdou ve sněhu, tmavé zase skryjí špínu při cestách do práce.</p>'
          '<h2>Lyžařské kalhoty a bundy</h2>'
          '<p>Zimní oblečení je nejsilnější doménou značky. Při výběru zvažte tři parametry: zateplení, nepromokavost a prodyšnost. Zateplení určuje, jak moc vás zahřeje. Nepromokavost chrání při mokrém sněhu a dešti. Prodyšnost je klíčová, pokud se hodně hýbete, protože vlhkost z těla musí někam odejít. Na sjezdovku se obvykle volí bunda a kalhoty s membránou, které vydrží několik hodin ve sněhu.</p>'
          + T(['Typ zimní bundy', 'Charakter', 'Pro koho'], [
              ['Zateplená lyžařská bunda', 'vyšší zateplení, sněžná zástěra, kapuce přes helmu', 'pomalejší lyžování, děti, sezení na vleku'],
              ['Hybridní bunda', 'zateplení v jádru, pružné boky', 'aktivní pohyb, běžky, skialp'],
              ['Softshellová bunda', 'tenčí, pružná, odolná proti větru', 'sportovní lyžování, přechodové dny'],
              ['Nepromokavá skořepina', 'tenká vrstva bez zateplení', 'navrstvení nad fleecem, mokré počasí']]) +
          '<p>Lyžařské kalhoty vybírejte s vysokým pasem nebo s laclem, pokud se často padá. Zesílený lem na nohavici chrání před hranami lyží. Praktické jsou větrací zipy na stehnech, kterými vypustíte přebytečné teplo při stoupání. Pro děti se hodí kalhoty s regulací délky nohavic a gumovou manžetou kolem bot. Podrobnější průvodce najdete v landingu <a href="/kilpi-lyzarska-bunda/">Kilpi lyžařská bunda</a>.</p>'
          '<h2>Jarní, podzimní a softshellové bundy</h2>'
          '<p>Přechodové období vyžaduje lehčí vrstvu, kterou můžete sbalit do batohu. Softshell zadrží vítr a mírný déšť a zároveň je pružný při chůzi. Pokud počítáte s vydatnějším deštěm, zvolte <a href="/nepromokave-bundy/">nepromokavou bundu</a> s přelepenými švy. Při delším pohybu ocení prodyšnou podšívku. Ve výpisu najdete i prošívané modely, které se hodí do chladnějších dnů ve městě a na krátké procházky.</p>'
          '<ul><li><strong>Na každý den:</strong> softshell nebo lehká prošívaná bunda s kapucí.</li>'
          '<li><strong>Na túru:</strong> nepromokavá bunda s větracími zipy v podpaží.</li>'
          '<li><strong>Na běh nebo běžky:</strong> tenká větrovka nebo běžecký softshell s pružnými boky.</li>'
          '<li><strong>Na cestování:</strong> bunda, která se dá sbalit do vlastní kapsy.</li></ul>'
          '<h2>Střední vrstva a spodní prádlo</h2>'
          '<p>Správně zvolená střední vrstva rozhoduje o komfortu víc než samotná bunda. <a href="/fleecove-mikiny/">Fleecové mikiny</a> jsou lehké, rychle schnou a dobře izolují. Pokud potřebujete větší teplo, hledejte model s hustším vlasem. Spodní vrstva by měla odvádět pot od kůže, proto se hodí merino vlna nebo syntetika. Bavlna zůstává vlhká a při pobytu v zimě rychle zchladí.</p>'
          '<p>Mezi vzorky zboží je i dámské tričko z merina, které je příjemné na kůži a méně zachytává pachy, takže se hodí na vícedenní túry. Termoprádlo můžete porovnat v kategorii <a href="/termopradlo/">funkční prádlo</a>.</p>'
          '<h2>Kalhoty do přírody a do města</h2>'
          '<p>Outdoorové kalhoty bývají z pružného materiálu s odolnou úpravou proti vodě, takže zvládají i lehký déšť. <a href="/outdoorove-kalhoty/">Outdoorové kalhoty</a> mají často kapsy se zipy a zesílená kolena. Sportovní kalhoty jsou volnější a hodí se na běžný provoz. U dámských modelů zkontrolujte střih v bocích, aby kalhoty nesvíraly při chůzi do kopce. Pokud kalhoty zkracujete, vyhněte se lemu, který se při dešti nasákne.</p>'
          '<h2>Cyklistické oblečení a příslušenství</h2>'
          '<p>Kilpi nabízí také cyklistické oblečení a menší příslušenství. Cyklodresy by měly být prodyšné a lehce přiléhavé, aby nemávaly ve větru. Kalhoty s vložkou se hodí na delší trasy. Na pohodovou jízdu po městě stačí volnější kraťasy. Při výběru zkontrolujte délku zad, protože v předklonu se kratší trička vysunou nad kalhoty. Pro srovnání s dalšími značkami použijte kategorie <a href="/cyklisticke-obleceni/">cyklistické oblečení</a>.</p>'
          '<h2>Jak číst názvy modelů</h2>'
          '<p>Název produktu obvykle obsahuje typ oblečení, jméno řady, písmeno pro pohlaví a barvu. Například pánské softshellové lyžařské kalhoty nesou označení M, dámská běžecká bunda W. Díky tomu poznáte rovnou účel: běžecká bunda bude lehčí a pružnější než lyžařská, hybridní kombinuje zateplení s pružnými panely. Pokud název obsahuje slovo nepromokavá, hledejte v popisu údaj o vodním sloupci a přelepených švech. Pokud je tam softshell, počítejte s odolností proti větru, ale menší izolací. Takové krátké čtení ušetří čas při porovnání desítek podobných modelů.</p>'
          '<p>Praktické je také sledovat, zda je kus prodáván v několika barvách. Stejný model se často objevuje v černé, modré i tmavě zelené, a ceny i dostupnost se mezi barvami liší. Proto se vyplatí otevřít více variant, než se rozhodnete.</p>'
          '<h2>Velikosti a střihy</h2>'
          '<p>Rozměry se u outdoorových značek mohou lišit od městských. Dámské modely mají v názvu písmeno W, pánské M. Při výběru bundy zkuste ji nasadit přes mikinu, abyste měli dost místa pro vrstvu. Rukávy by měly po zvednutí paží stále zakrývat zápěstí. U kalhot zkontrolujte délku nohavic a obvod pasu. Dětské modely vybírejte s rezervou kvůli růstu, ale neděste se příliš velké, protože může propouštět vítr.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Membránové bundy perte šetrně a bez aviváže, která zalepuje póry. Po vyprání je vhodné je obnovit impregnací. Zip čistěte měkkým kartáčkem a občas přejeďte silikonovou tyčinkou. Softshell nesušte při vysoké teplotě, aby nedošlo k poškození membrány. Fleece se nesmí žehlit. Po zimní sezóně bundu vyperte a uložte suchou, ne stlačenou v pytli.</p>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Zimní oblečení bývá nejlevnější na jaře, kdy obchody uvolňují sklady, a na konci ledna. Jarní bundy zlevňují v létě, trička a kraťasy na konci sezóny. Mezi obchody bývají rozdíly, takže stejný model se prodává za různé ceny. Na Sporteka.cz proto porovnejte nabídky a kontrolujte, zda je dostupná vaše velikost. Nejoblíbenější barvy a velikosti se rozprodají jako první.</p>'
          '<p>Pro srovnání zimních vrstev se podívejte také na ' + B(('dare2b', 'Dare2b'), ('4f', '4F')) + '.</p>',
    faq=[
        ('Co je v nabídce Kilpi nejsilnější?',
         'Největší skupinou jsou lyžařské kalhoty a jarní a podzimní bundy, za nimi sportovní kalhoty, trička, lyžařské bundy, kraťasy a mikiny. Najdete také softshell, fleece a cyklistické oblečení.'),
        ('Co znamená písmeno W nebo M v názvu?',
         'Obvykle označuje dámský nebo pánský střih. W bývá dámské, M pánské. Pomáhá rychle třídit výpis a vybrat správný střih, ale přesné rozměry vždy ověřte v tabulce u produktu.'),
        ('Jaký je rozdíl mezi softshellem a lyžařskou bundou?',
         'Softshell je tenčí, pružnější a dobře odolává větru. Lyžařská bunda je silnější, zateplená a často má sněžnou zástěru. Na sjezdovku zvolte lyžařskou bundu, na aktivnější pohyb softshell.'),
        ('Jak vybrat lyžařské kalhoty pro dítě?',
         'Hledejte regulaci délky nohavic, pružný pas, zesílené kolena a manžetu přes boty. Velikost volte s malou rezervou. Důležité je, aby dítě mělo volný pohyb a kalhoty neklouzaly.'),
        ('Je merino vlna lepší než syntetika?',
         'Merino je příjemné na kůži, zadržuje méně pachů a hřeje i vlhké. Syntetika rychleji schne a vydrží víc praní. Pro vícedenní túry je merino pohodlnější, pro intenzivní sport bývá praktičtější syntetika.'),
        ('Jak pečovat o membránovou bundu?',
         'Perte ji šetrně bez aviváže a po vyprání obnovte impregnaci. Zip udržujte čistý. Pokud voda přestane perlit, čas obnovit úpravu. Skladujte ji suchou a zavěšenou, ne zmačkanou v pytli.'),
        ('Dají se oblečení použít i pro běžné nošení ve městě?',
         'Ano, softshellové a prošívané bundy, fleece a sportovní kalhoty se hodí i do města. Výhodou je praktičnost a odolnost proti větru a dešti. Dbejte na střih a barvu, aby působil upraveně.'),
        ('Kdy se vyplatí čekat na výprodej?',
         'Zimní zboží zlevňuje na jaře a koncem zimy, jarní bundy v létě. Pokud potřebujete konkrétní velikost, nečekejte příliš dlouho. Základní barvy, jako černá, se rozprodají nejdřív.'),
        ('Jak vybrat vrstvy na zimní túru?',
         'Použijte tři vrstvy: funkční spodní, fleecovou nebo teplou střední a bundu proti větru a sněhu. Podle teploty vrstvy přidávejte nebo odebírejte. Pomůže nepromokavé kalhoty a čepice s rukavicemi.'),
        ('Jak velkou rezervu mám nechat u bundy?',
         'Bunda by měla sedět přes mikinu, ale neměla by být o dvě velikosti větší. Zvedněte ruce nad hlavu, rukávy nemají vyjet nad zápěstí. Ramena a hrudník nesmí tlačit.')])

# ------------------------------------------------------------------ dare2b
NEW['dare2b'] = dict(
    title='Dare2b: lyžařské bundy, funkční mikiny a oblečení do hor',
    desc='Dare2b v katalogu Sporteky: lyžařské bundy a kalhoty, funkční a fleecové mikiny, jarní a nepromokavé bundy. Jak vybrat vrstvy a hlídat slevy.',
    intro='<p>Dare2b je v katalogu Sporteky outdoorová a lyžařská značka s širokou nabídkou bund a mikin. Nejpočetnější jsou <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a> a <a href="/lyzarske-bundy/">lyžařské bundy</a>, následují <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>, <a href="/funkcni-mikiny/">funkční mikiny</a>, <a href="/mikiny/">mikiny</a>, <a href="/nepromokave-bundy/">nepromokavé bundy</a> a <a href="/fleecove-mikiny/">fleecové mikiny</a>.</p>'
          '<p>Zboží míří zhruba stejně na ženy a muže, významnou část tvoří i děti. Barevně vede černá, za ní modrá a zelená. V nabídce jsou také dětské kombinézy, termosety a zateplené sukně. Většina kousků je v tmavých a praktických odstínech, takže se dobře kombinují mezi sebou. Stránka vysvětluje, jak se v sortimentu orientovat, kterou vrstvu zvolit, jak číst názvy modelů, jak o oblečení pečovat a kdy hledat slevy mezi obchody.</p>',
    guide='<h2>Co Dare2b v katalogu nabízí</h2>'
          '<p>Značka se soustředí na oblečení pro pohyb v přírodě a ve sněhu. Z kategorií je vidět, že těžiště leží na bundách: jarních, lyžařských, zimních a nepromokavých. K nim se přidává střední vrstva v podobě fleecových a funkčních mikin a dále kalhoty pro lyže i pěší túry. Najdete také termoprádlo, funkční trička a kraťasy. Přehled ukazuje, k čemu která skupina slouží.</p>'
          + T(['Skupina', 'Co obsahuje', 'Typické použití'], [
              ['<a href="/sportovni-bundy-jaro-podzim/">Jarní a podzimní bundy</a>', 'lehké bundy, prošívané modely, větrovky', 'procházky, město, přechodové období'],
              ['<a href="/lyzarske-bundy/">Lyžařské bundy</a> a <a href="/zimni-bundy/">zimní bundy</a>', 'zateplené bundy pro sjezdovku a zimu', 'lyžování, zima ve městě'],
              ['<a href="/lyzarske-kalhoty/">Lyžařské kalhoty</a>', 'kalhoty s membránou, dětské kombinézy', 'svah, hry ve sněhu'],
              ['<a href="/nepromokave-bundy/">Nepromokavé bundy</a>', 'skořepiny proti dešti', 'výlety, déšť, cestování'],
              ['<a href="/funkcni-mikiny/">Funkční</a> a <a href="/fleecove-mikiny/">fleecové mikiny</a>', 'střední vrstva, mikiny s polovičním zipem', 'pod bundu, na túru, na trénink'],
              ['<a href="/outdoorove-kalhoty/">Outdoorové</a> a <a href="/sportovni-kalhoty/">sportovní kalhoty</a>', 'turistické kalhoty, pružné materiály', 'túry, kemp, cesty'],
              ['<a href="/funkcni-tricka/">Funkční trička</a>, termoprádlo', 'spodní vrstva', 'sport, zima']]) +
          '<p>Z názvů je znát, že modely mají často vlastní jména, třeba Ventura, Sprint, Lowline, Exchange nebo Piste. Název řady většinou následuje barva a označení pohlaví. Ve výpisu vidíte také popisy typu termoset, kombinéza nebo zateplená sukně, což ukazuje, že sortiment obsahuje i netradiční kousky.</p>'
          '<h2>Pro koho se značka hodí</h2>'
          '<p>Dámské a pánské zboží je téměř vyrovnané, takže u obou pohlaví je z čeho vybírat. Dětský sortiment je velmi výrazný: v nabídce jsou lyžařské bundy, zimní kombinézy a fleecové mikiny. Kombinézy jsou výhodné pro nejmenší děti, protože chrání záda a zabraňují vnikání sněhu. Pro školní děti je lepší dvoudílná sestava, která se snáz obléká a svléká. Unisex modely jsou spíše výjimkou.</p>'
          '<p>Při výběru si všimněte označení řady. Starší děti často preferují střihy podobné dospělým, malé ocení výrazné barvy, které je na svahu snadno rozpoznatelné. Dospělým stačí vybrat střih podle sportu: úzký pro rychlejší pohyb, volnější pro vrstvení a pohodlí.</p>'
          '<h2>Lyžařské bundy a kalhoty</h2>'
          '<p>Zimní bundy jsou největším lákadlem značky. Při výběru se rozhodujte podle způsobu pohybu. Pro pomalejší lyžování a rodinné výlety se hodí silnější zateplení, pro aktivnější jízdu raději tenčí vrstva a teplejší střední vrstva pod ní. Praktické jsou sněžná zástěra, kapuce přes helmu, kapsa na skipas a větrání v podpaží. Důležité jsou také manžety s palcovými průvleky, které uzavřou rukáv pod rukavicí.</p>'
          + T(['Prvek', 'K čemu slouží', 'Na co si dát pozor'], [
              ['Sněžná zástěra', 'brání vniknutí sněhu při pádu', 'musí se dobře zapínat i v rukavicích'],
              ['Kapuce přes helmu', 'chrání hlavu před větrem', 'měla by jít stáhnout bez zakrytí výhledu'],
              ['Větrací zipy', 'odvádí přebytečné teplo', 'u pohodlných modelů nechybí'],
              ['Zesílený lem kalhot', 'chrání před hranou lyže', 'u dětí obzvlášť důležitý'],
              ['Nastavitelný pas', 'přizpůsobí kalhoty při růstu', 'hodí se hlavně u dětských modelů']]) +
          '<p>Chcete-li nasadit kalhoty na stejné lyžování jako bundu, hledejte u nich stejné parametry nepromokavosti a prodyšnosti. Příliš těsný střih omezuje pohyb při pádu a v chladu nezbývá místo na další vrstvu. Naopak široký střih může při jízdě mávat. Zkuste proto kalhoty v dřepu a při zvednutí kolene.</p>'
          '<h2>Funkční a fleecové mikiny</h2>'
          '<p>Mikiny jsou druhou největší oblastí značky. <a href="/funkcni-mikiny/">Funkční mikiny</a> jsou tenké, rychleschnoucí a často mají polovinu nebo celý zip. Dají se nosit samostatně při pohybu nebo jako střední vrstva pod bundu. <a href="/fleecove-mikiny/">Fleecové mikiny</a> jsou o něco teplejší a objemnější, příjemné na kůži a rychle schnou. Pokud vás čeká dlouhý den venku, vezměte si nejprve tenčí variantu a teplejší nechte v batohu.</p>'
          '<ul><li><strong>Na túru:</strong> tenčí funkční mikina s polovičním zipem, která se dá otevřít při stoupání.</li>'
          '<li><strong>Na lyže:</strong> fleecová mikina pod bundu, ideálně s vysokým límcem.</li>'
          '<li><strong>Do města:</strong> střih bez výrazných logo prvků, v tmavé barvě.</li>'
          '<li><strong>Pro děti:</strong> měkký fleece s plným zipem, který se snadno obléká.</li></ul>'
          '<h2>Jarní, nepromokavé a zimní bundy</h2>'
          '<p>Nejpočetnější kategorie značky nabízí množství lehčích bund. Pro jaro a podzim stačí tenká prošívaná bunda nebo větrovka, kterou sbalíte do batohu. <a href="/nepromokave-bundy/">Nepromokavé bundy</a> zvolte, pokud počítáte s deštěm. Při jejich výběru ověřte, zda jsou švy přelepené a zda má kapuce stahování. Pro zimní město se hodí <a href="/zimni-bundy/">zimní a péřové bundy</a>, které nemusí mít technické vlastnosti lyžařských modelů, ale musí hřát a odolávat větru. V nabídce najdete i prošívanou zimní bundu v elegantnějším střihu.</p>'
          '<h2>Kalhoty, sukně a termoprádlo</h2>'
          '<p>Turistické a outdoorové kalhoty z pružného materiálu jsou praktické pro celoroční nošení. Hledejte kapsy na zip, zesílená kolena a nohavice, které se dají upravit. Zateplená sukně je vhodná pro studenější dny ve městě nebo na procházku. Funkční termoprádlo patří pod lyžařské a zimní oblečení. Nosí se těsně na těle, aby odvádělo pot, a nesmí být z bavlny. Termoset, tedy komplet horní a spodní díl, je pohodlné řešení na celý zimní den.</p>'
          '<h2>Jak číst názvy a řady</h2>'
          '<p>Dare2b používá pro modely vlastní jména a za nimi často římskou číslici, například ii nebo iv. Ta obvykle označuje novější generaci stejného kusu, ale detaily se mohou lišit, proto vždy čtěte popis. Pokud najdete starší i novější verzi, porovnejte materiál, zateplení a barvy. Starší řada bývá levnější, ale nemusí být dostupná ve všech velikostech. V názvu najdete také pohlaví a věkovou skupinu. Dětské kousky mají velikost uvedenou číslem výšky, například 98 nebo 110, nebo věkem, třeba 11-12Y. Vyplatí se zkontrolovat, který systém obchod používá, aby nedošlo k záměně.</p>'
          '<h2>Velikosti a střihy</h2>'
          '<p>U oblečení pro děti si velikost obvykle odvozujete podle výšky, u dospělých podle obvodu hrudníku a pasu. Dětské modely jsou označeny číselně, třeba 98 nebo 110, dospělí používají S až XL. Zkuste bundu přes mikinu, aby měla dost místa na vrstvení. U lyžařských kalhot zkontrolujte délku nohavic při pokrčení kolen. U dětských kombinéz nechte rezervu na růst, ale pamatujte, že příliš velká kombinéza brání pohybu.</p>'
          + T(['Zboží', 'Jak měřit', 'Poznámka'], [
              ['Bunda', 'obvod hrudníku a délka rukávu', 'zkoušejte přes mikinu'],
              ['Lyžařské kalhoty', 'obvod pasu, bokové linie, délka nohavice', 'ověřte pohyb při dřepu'],
              ['Mikina', 'obvod hrudníku a délka zad', 'střih bývá přiléhavější'],
              ['Dětská kombinéza', 'výška dítěte', 'nechte rezervu pro vrstvu pod ní'],
              ['Termoprádlo', 'těsný střih', 'volte přesnou velikost, ne větší']]) +
          '<h2>Péče a životnost</h2>'
          '<p>Membránové a zateplené bundy perte šetrně a bez aviváže. Po každém několikátém praní obnovte impregnaci, aby voda dál perlila. Fleece nežehlete a nesušte na radiátoru. Zipy čistěte kartáčkem a udržujte nezanesené. Zimní oblečení před uložením vysušte a nechte zavěšené, ne sbalené v pytli. Dětské oblečení často nese stopy bláta a sněhu, ale pravidelné čištění prodlouží jeho životnost i pro mladšího sourozence.</p>'
          '<h2>Kdy hledat slevy</h2>'
          '<p>Nejvíc se zimní oblečení zlevňuje po skončení sezóny, tedy na jaře, a před začátkem zimy při obměně kolekcí. Jarní a podzimní bundy se prodávají levněji v letním období. Slevy se mezi obchody liší, proto porovnejte více nabídek najednou. Dětské velikosti mizí rychleji, protože o ně je největší zájem. Sledujte proto dostupnost a nenechávejte nákup na poslední týden před výjezdem.</p>'
          '<p>Pro srovnání dalších lyžařských a outdoorových značek se podívejte na ' + B(('kilpi', 'Kilpi'), ('4f', '4F')) + '.</p>',
    faq=[
        ('Jaké zboží Dare2b v katalogu převažuje?',
         'Největší skupinou jsou jarní a podzimní bundy a lyžařské bundy, dále lyžařské kalhoty, funkční mikiny, mikiny a nepromokavé bundy. Významné jsou i fleecové mikiny, zimní bundy a outdoorové kalhoty.'),
        ('Pro koho je sortiment určen?',
         'Pro ženy a muže téměř rovným dílem. Značná část nabídky je dětská, hlavně lyžařské bundy a kombinézy. Unisex modelů je málo.'),
        ('Co je lepší pro dítě: kombinéza, nebo dvoudílná sestava?',
         'Kombinéza je praktická pro nejmenší, protože chrání záda a brání vniknutí sněhu. Starší děti obvykle preferují dvoudílnou sestavu, která se lépe obléká a svléká a snáz se upravuje velikost.'),
        ('Jak poznám, že bunda bude dost teplá?',
         'Podívejte se na zateplení, délku a kapuci. Teplo ale závisí hlavně na vrstvení pod bundou. Doporučujeme funkční spodní prádlo a fleece. Při pohybu je lepší lehčí bunda, při stání teplejší.'),
        ('Jaký je rozdíl mezi funkční a fleecovou mikinou?',
         'Funkční mikina je tenčí, hladká a rychle schne, vhodná při pohybu. Fleecová je teplejší, měkká a objemnější, lépe izoluje při pobytu venku. Obě se dají nosit jako střední vrstva.'),
        ('Jak pečovat o impregnaci?',
         'Po několika vypráních obnovte impregnaci sprejem nebo prostředkem do pračky. Bundu perte bez aviváže. Pokud voda přestane perlit, je čas na obnovu. Nechte ji dobře vyschnout.'),
        ('Dají se věci nosit i ve městě?',
         'Ano, hlavně jarní bundy, zimní prošívané modely, fleecové mikiny a outdoorové kalhoty. Pozor na střih, který by neměl být příliš technický. Tmavé barvy působí upraveněji.'),
        ('Jak vybrat velikost dětské bundy?',
         'Podle výšky dítěte a podle toho, kolik vrstev bude mít pod ní. Počítejte s malou rezervou na růst, ne s příliš velkou. Rukávy mají sahat ke kloubu palce, nesmí se přehrnovat.'),
        ('Kdy se vyplatí kupovat?',
         'Zimní oblečení nejlevněji na jaře a na konci sezóny, jarní bundy v létě. Dětské velikosti rychle mizí, proto si hlídejte dostupnost už na začátku sezóny a porovnejte více obchodů.'),
        ('Co vybrat pod lyžařskou bundu?',
         'Funkční termoprádlo, na něj tenký fleece nebo funkční mikinu. Při větší zimě přidejte teplejší vrstvu. Vyhněte se bavlně, která drží vlhkost a rychle ochladí.')])
