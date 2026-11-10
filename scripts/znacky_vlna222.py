"""sporteka.cz — brand page texts wave 222: reima, alpine-pro, siroko, armani-exchange.
Only what follows from the catalogue categories and product names; no history, prices or counts."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ reima
NEW['reima'] = dict(
    title='Reima: dětské bundy, kombinézy, sněhule a rukavice',
    desc='Reima v katalogu sporteky: dětské bundy, kombinézy, zimní boty, rukavice, čepice a ponožky. Jak vybrat velikost na růst, vrstvení a kdy hledat slevy.',
    intro='<p>Reima je v našem katalogu téměř výhradně dětská značka. Dětské oblečení a obuv tvoří prakticky celou nabídku, dospělých kusů je jen hrstka. Největší skupinu tvoří <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a>, hned za nimi jsou čepice, zimní boty, kombinézy, rukavice a tenisky. '
          'Najdete tu také kalhoty, barefoot boty, trekovou obuv, nepromokavé bundy, zimní bundy a ponožky. Zboží je tedy rozloženo tak, aby dítě mohlo od podzimu do jara projít celý den venku bez vyměňování celé výbavy. '
          'Na této stránce vysvětlujeme, jak v nabídce Reimy vybírat podle ročního období, jak řešit velikost, když dítě rychle roste, a jak vrstvit, aby se nepotilo ani nemrzlo. Přidáváme tipy na péči a na sledování slev bez nutnosti hlídat každý obchod zvlášť.</p>',
    guide='<h2>Co Reima v katalogu nabízí</h2>'
          '<p>Když si projdete filtr „Pro koho“, uvidíte, že dětské kousky tvoří drtivou většinu a dospělých modelů je tak málo, že na ně nelze spoléhat. Reima je proto vhodná pro rodiče, kteří potřebují sladěnou výbavu pro školku, družinu, hřiště i sjezdovku. Sortiment se dá rozdělit do několika logických celků, které odpovídají tomu, co dítě venku skutečně nosí.</p>'
          + T(['Část výbavy', 'Co v katalogu najdete', 'Kdy ji dítě potřebuje'], [
              ['Bundy', 'jarní a podzimní, nepromokavé, zimní a membránové', 'od první chladné vlny po mrazy'],
              ['Celé obleky', 'kombinézy, overaly, lyžařské kalhoty', 'sníh, bláto, hrabání na zahradě'],
              ['Obuv', 'zimní boty a sněhule, tenisky, sandály, trekové a barefoot boty', 'celý rok podle počasí'],
              ['Doplňky', 'čepice, čelenky, rukavice a palčáky, ponožky, termoprádlo', 'vrstvení a ochrana prstů, uší a krku']]) +
          '<p>Z barev převažuje modrá a černá, hned za nimi následuje růžová a fialová. Zelená, hnědá, červená, šedá a bílá tvoří menší část. Barva sama o sobě ale není rozhodující. Jasné odstíny se na dětech lépe hledají v dešti, na sněhu nebo při večerní procházce, takže u nejmenších se vyplatí vybrat něco, co je na dálku vidět.</p>'
          '<h2>Bundy: jaro, podzim, déšť a mráz</h2>'
          '<p>Bunda je tady největší kategorie a každá její podoba slouží jinak. <a href="/sportovni-bundy-jaro-podzim/">Jarní a podzimní bunda</a> je lehčí a pohodlná na každodenní nošení, drží vítr a zvládne i drobný déšť. Pokud ale prší opravdu vydatně, hodí se <a href="/nepromokave-bundy/">nepromokavá bunda</a> se zaklížovanými švy, protože děti se rády zastavují v loužích a vydrží stát venku mnohem déle než dospělí. Na mrazy je určená <a href="/zimni-bundy/">zimní bunda</a>, kterou doplníte čepicí, rukavicemi a vrstvou termoprádla pod ní.</p>'
          '<p>V názvech modelů se opakují označení jako membránová, zateplená nebo zimní. Membrána znamená, že bunda propouští páru z těla a zároveň zadržuje vodu zvenku. Zateplení naopak určuje, jak vydatně bunda hřeje, ale nezaručuje nepromokavost. Proto si u každého kousku přečtěte popis a ověřte, zda platí obě vlastnosti, pokud je potřebujete současně. Kapuci zvažte hlavně u menších dětí, protože u starších žáků bývá často nepoužívaná.</p>'
          '<h2>Kombinézy, overaly a kalhoty</h2>'
          '<p>Kategorie <a href="/kombinezy/">kombinézy a overaly</a> je pro rodiče malých dětí nejpraktičtější. Jeden kus obleku nahrazuje bundu i kalhoty, takže se nikde nezvedne záda a sníh se nedostane za pas. U batolat se oceňují zipy na nohavicích, díky nimž se dítě dá obléknout i v botách, a ochranné manžety na rukávech a kotnících. U větších dětí se častěji volí dvoudílný komplet, protože se hůře ušpiní a jde ho lépe kombinovat.</p>'
          '<p>Na lyže nebo sáňky se hodí <a href="/sportovni-kalhoty/">sportovní kalhoty</a> s laclem nebo vysokým pasem a zesílenými koleny. Dětské lyžařské kalhoty patří mezi nejčastěji nabízené kousky a tvoří dobrý protipól bundě. Výhodou jsou stahovací poutka na kotnících a gumové ochranné zadní dílce, které nepouštějí sníh pod botu. Kalhoty volte jednu velikost nad, protože děti rostou hlavně do délky.</p>'
          '<h2>Zimní boty, sněhule a celoroční obuv</h2>'
          '<p>Hned za bundami se prodává obuv. <a href="/zimni-obuv/">Zimní boty a sněhule</a> mají silnější podrážku, vyšší svršek a teplou výstelku. Značka v katalogu ukazuje několik řad s odlišnými názvy, takže při výběru sledujte popis: nepromokavá membrána, zateplení a výška svršku rozhodují, zda bota bude na rozbředlém sněhu, nebo na suchém mrazu. Pro nejmenší jsou k dispozici boty pro batolata s pevnou patou a snadným zapínáním.</p>'
          '<p>Pro jarní a podzimní dny se hodí <a href="/tenisky/">tenisky a volnočasové boty</a> a <a href="/trekova-obuv/">trekové boty</a>. Ty druhé mají pevnější podrážku s hrubým vzorem a vyšší kotník, vhodný na lesní cesty a kameny. Samostatnou skupinu tvoří <a href="/barefoot-obuv/">barefoot boty</a>. Mají širší špičku, tenkou ohebnou podrážku a minimální převýšení paty. Jsou pro děti, které už chodí samostatně a rodiče chtějí chodidlo ponechat přirozené. Při přechodu z klasické boty dejte nohám čas, aby si zvykly.</p>'
          + T(['Obuv', 'Podrážka a svršek', 'Vhodné použití'], [
              ['Zimní bota, sněhule', 'tlustá, hrubý vzorek, vysoký svršek', 'sníh, mráz, zimní procházky'],
              ['Treková obuv', 'pevná podrážka, výztuha špičky', 'lesní stezky, výlety, neúrodný terén'],
              ['Barefoot', 'tenká ohebná podrážka, široká špička', 'denní chůze, hřiště, suchý terén'],
              ['Tenisky', 'lehká, ohebná, prodyšná', 'škola, město, suché dny'],
              ['Sandály', 'otevřené, upevnění na suchý zip', 'léto, voda, kempy']]) +
          '<h2>Rukavice, čepice a ponožky</h2>'
          '<p>Doplňky jsou důležitější, než se zdá. Většina dětí zmrzne dřív na prstech nebo na uších než v trupu. <a href="/sportovni-rukavice/">Rukavice</a> se v katalogu dělí na prstové, palčáky a lyžařské s prodlouženou manžetou. Palčáky jsou teplejší a jednodušší na oblékání, což u batolat vyhrává. Lyžařské rukavice mají zpevněnou dlaň a manžetu přes rukáv bundy. K modelům najdete také odkaz na landing <a href="/reima-rukavice/">rukavice Reima</a>. <a href="/cepice-a-celenky/">Čepice a čelenky</a> kryjí uši a krk, často mají podšívku, která nechá hlavu dýchat.</p>'
          '<p>Ponožky Reima mají v názvech označení jako atleetti nebo Villalla. Neznamenají nic zásadního, jen odlišují řady. Při výběru si všímejte složení: směs vlny nebo syntetiky s elastanem drží tvar a odvádí vlhkost, čistá bavlna vlhne a v zimní botě chladí. Poslední vrstvou je termoprádlo, které se nosí na kůži a drží teplo bez objemu.</p>'
          '<h2>Jak vrstvit a kolik místa nechat na růst</h2>'
          '<p>Základní pravidlo pro děti zní: o jednu vrstvu víc než pro dospělého při stání a o jednu méně při pohybu. Dítě, které běhá, se potí, a mokrá vrstva pak hřeje jen do chvíle, než se zastaví. Proto použijte tři vrstvy: termoprádlo na kůži, střední teplou mikinu nebo flís a vrchní bundu proti větru a vodě. Pokud je počasí proměnlivé, bunda se dá sundat a prádlo zůstane.</p>'
          '<ul><li><strong>Velikost:</strong> vybírejte podle výšky dítěte, ne podle věku. Označení bývá v centimetrech a počítá s pár centimetry navíc.</li>'
          '<li><strong>Prostor na vrstvy:</strong> bunda má být o něco volnější, aby pod ní bylo místo na mikinu, ale rukávy nesmí zakrývat prsty.</li>'
          '<li><strong>Nastavitelné konce:</strong> stahovací manžety a nohavice se přizpůsobí růstu o jednu sezónu navíc.</li>'
          '<li><strong>Boty:</strong> palec by měl mít před špičkou mezi půl a jedním centimetrem rezervy, zjistíte ji vložením prstu za patu při stoji.</li></ul>'
          '<h2>Jak se Reima liší od konkurence</h2>'
          '<p>Většina velkých sportovních značek v katalogu cílí na dospělé a dětskou řadu má jen jako doplněk. U Reimy je tomu naopak: dítě je hlavním zákazníkem a celé portfolio ho vybavuje od hlavy až po paty. Podobně zaměřené jsou například <a href="/znacka/loap/">Loap</a> a <a href="/znacka/kilpi/">Kilpi</a>, které ale mají i velké dospělé řady. Univerzální značky jako <a href="/znacka/nike/">Nike</a> či <a href="/znacka/adidas/">Adidas</a> zase nabízejí hlavně sportovní oblečení a tenisky, nikoli kompletní zimní výbavu. Rozdíl poznáte tím, že u Reimy najdete všechno od termoprádla po sněhule na jednom místě.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Dětské oblečení se špiní rychle, a proto potřebuje jednoduchou péči. Bundy a kalhoty s membránou perte podle štítku při nízké teplotě a bez aviváže, která ucpává póry. Po několika praních obnovte impregnaci sprejem nebo prostředkem do pračky. Boty po zimě vyčistěte kartáčem, vyndejte vložky a nechte vyschnout při pokojové teplotě, nikdy ne na topení, které lepidlo stárne a svršek deformuje. Vydrží-li oblečení jednu sezónu, může jít k mladšímu sourozenci, takže cena za kus klesá.</p>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Zimní bundy, kombinézy a sněhule se zlevňují nejvíc na konci zimy, zatímco jarní a podzimní kousky na podzim a po Vánocích. Protože děti rostou, vyplatí se koupit velikost o stupeň větší na další sezónu. Porovnejte nabídku více obchodů a sledujte, zda je skladem právě vaše velikost, protože u dětí zmizí nejdřív ty nejčastější. Cenové alarmy a srovnání na naší stránce vám ušetří čas s hledáním.</p>',
    faq=[
        ('Je Reima jen dětská značka?', 'V katalogu sporteky tvoří dětské modely téměř celou nabídku. Dospělých nebo unisex kusů je jen velmi málo a nelze na ně spoléhat. Pokud hledáte oblečení pro dospělé, podívejte se spíše na jiné značky.'),
        ('Které kategorie jsou u Reimy největší?', 'Nejvíc zboží spadá do jarních a podzimních bund. Následují čepice a čelenky, zimní boty a sněhule, kombinézy a overaly, rukavice, tenisky, sportovní kalhoty a barefoot boty. Menší skupinu tvoří trekové boty, nepromokavé bundy, zimní bundy a ponožky.'),
        ('Jak vybrat velikost, když dítě rychle roste?', 'Řiďte se výškou dítěte v centimetrech podle tabulky u konkrétního kusu. Bundu volte o něco volnější kvůli vrstvám, kalhoty raději o jednu velikost víc a nastavte je stahovacími prvky. Boty ověřte měřením chodidla, rezerva by měla být asi centimetr.'),
        ('Čím se liší nepromokavá bunda od zimní?', 'Nepromokavá bunda chrání před vodou díky membráně a zaklížovaným švům, ale může být tenká. Zimní bunda je zateplená a hřeje, jenže nemusí odolat dešti. Pro proměnlivé počasí hledejte model, který má obě vlastnosti, a podrobnosti si přečtěte v popisu.'),
        ('Je lepší kombinéza, nebo bunda s kalhotami?', 'Kombinéza se hodí pro batolata a nejmenší děti, protože sníh se nedostane pod oblečení a rychle se obléká. Větší děti raději nosí dvoudílný komplet, který se lépe kombinuje a snadněji se obléká na toaletu.'),
        ('Hodí se barefoot boty pro děti?', 'Barefoot boty mají širokou špičku, tenkou ohebnou podrážku a minimální převýšení paty, takže chodidlo pracuje přirozeněji. Hodí se pro děti, které už chodí samy. Na sníh a mráz zvolte zimní model nebo teplou ponožku, jinak se promrzne podrážkou.'),
        ('Kolik vrstev dítě venku potřebuje?', 'Tři jsou obvykle ideální: termoprádlo na kůži, teplá střední vrstva a vrchní bunda proti větru a vodě. Při pohybu dítě svlékněte o vrstvu, jinak se zpotí a po zastavení promrzne.'),
        ('Jak pečovat o bundy a boty?', 'Bundy perte při nízké teplotě bez aviváže a občas obnovte impregnaci. Boty po zimě vyčistěte, vyndejte vložky a sušte při pokojové teplotě. Dobře udržované kusy vydrží i pro mladšího sourozence.'),
        ('Kdy se vyplatí kupovat zimní oblečení?', 'Nejvíc zlevňuje na konci zimy a na jaře. Protože děti rostou, kupujte větší velikost na další sezónu a před objednávkou porovnejte nabídku více obchodů. Dostupnost velikostí se mění rychle.'),
    ],
)

# ------------------------------------------------------------------ alpine-pro
NEW['alpine-pro'] = dict(
    title='Alpine Pro: outdoorové oblečení a obuv pro celou rodinu',
    desc='Alpine Pro v katalogu sporteky: trička, trekové boty, mikiny, kalhoty, lyžařské a zimní bundy pro dámy, pány i děti. Jak vybírat a kdy hledat slevy.',
    intro='<p>Alpine Pro v našem katalogu patří mezi nejširší outdoorové značky. Dámské, pánské a dětské modely jsou zastoupeny zhruba vyrovnaně, unisex kusů je méně. Největší skupinu tvoří <a href="/sportovni-tricka/">trička a tílka</a>, po nich následují <a href="/trekova-obuv/">trekové boty</a>, zimní obuv, sportovní kalhoty a mikiny. '
          'V nabídce nechybí tenisky, jarní a podzimní bundy, sukně a šaty, outdoorové kalhoty, lyžařské i zimní bundy a kraťasy. Takže si lze od jedné značky pořídit většinu výbavy na túru, na hory i na každý den. '
          'Na této stránce se dozvíte, jak se v nabídce orientovat podle sezóny, co znamenají zkratky u membrán, jak zvolit střih pro ženy, muže a děti a kdy se vyplatí čekat na slevu. Žádné konkrétní ceny neuvádíme, protože se mění, ale postup výběru platí stále.</p>',
    guide='<h2>Co Alpine Pro v katalogu nabízí</h2>'
          '<p>Z pohledu sortimentu je to značka celoroční. V létě se prodávají trička, tílka, kraťasy a sukně, na přelomu sezón jarní bundy a outdoorové kalhoty, v zimě lyžařské a péřové bundy, zimní obuv a teplé mikiny. Díky tomu se dá vybavit na celý rok, aniž byste museli střídat značku a hledat jiné velikosti. Podle filtru „Pro koho“ jsou nejčastější dámské modely, těsně za nimi pánské a výrazná část patří i dětem.</p>'
          + T(['Oblast', 'Kategorie v katalogu', 'Typické použití'], [
              ['Léto', 'trička a tílka, kraťasy, sukně a šaty', 'túra, kolo, město, dovolená'],
              ['Přechodové období', 'jarní a podzimní bundy, outdoorové kalhoty, mikiny', 'výlety, vycházky, práce kolem domu'],
              ['Zima', 'lyžařské a péřové bundy, zimní obuv', 'sjezdovka, procházky, mráz'],
              ['Obuv', 'trekové boty, tenisky, zimní boty', 'stezky, město, sníh'],
              ['Děti', 'bundy, obuv, trička, kalhoty', 'škola, hřiště, rodinné výlety']]) +
          '<p>Barevně dominuje černá, která je v téměř polovině zboží. Za ní následuje modrá, zelená a šedá, menší zastoupení má bílá, vícebarevná, červená a růžová. Praktická volba pro každý den je tmavý odstín, protože snese špínu a lépe se kombinuje, kdežto výraznější barvy se hodí na hory, kde chcete být vidět.</p>'
          '<h2>Trička, mikiny a spodní vrstvy</h2>'
          '<p>Trička jsou největší kategorie a názvy ukazují, že se dělí na několik druhů: rychleschnoucí, z organické bavlny a outdoorová. Rychleschnoucí tričko z umělých vláken odvádí pot a nemusí se prát po každém použití tak často, protože neabsorbuje zápach tolik jako bavlna. Bavlněné tričko je příjemné na dotek a vhodné do města, ale při pocení zůstává mokré a chladí. Pro aktivní pohyb si vyberte funkční materiál, pro klid bavlnu.</p>'
          '<p>V kategorii <a href="/mikiny/">mikiny</a> najdete lehké rychleschnoucí modely i teplejší kusy s výplní, třeba s merino složkou. Merino je teplé a vlhkost zadržuje déle než umělé vlákno, ale mnohem pomaleji zapáchá. Rychleschnoucí mikina je lepší do pohybu, mikina s teplou výplní zase na večery v kempu. Pod bundu ji volte jako střední vrstvu, nikoli jako vrchní.</p>'
          '<h2>Bundy: od jara po lyžování</h2>'
          '<p>U bund se nejvíc pracuje se zkratkou PTX, kterou značka používá pro membránu. Podle názvů se objevuje u pánských, dámských i dětských modelů. Membrána brání vodě, aby pronikla dovnitř, a zároveň vypouští páru, takže se v ní netropíte. Před koupí vždy porovnejte údaje o vodním sloupci a prodyšnosti v popisu, protože různé modely se v hodnotách liší.</p>'
          + T(['Typ bundy', 'Kdy ji vybrat', 'Na co si dát pozor'], [
              ['Jarní a podzimní', 'chladné dny, vítr, lehký déšť', 'nemusí mít zateplení, doplňte vrstvou pod ní'],
              ['Lyžařská a snowboardová', 'sjezdovka, sníh, vítr', 'sněhová sukně, zesílený rukáv, odvětrání v podpaží'],
              ['Zimní a péřová', 'mrazy, procházky, město', 'péří bez membrány nesnese mokro'],
              ['Outdoorová s membránou', 'túra v nepohodě', 'prodyšnost a kapuce nastavitelná přes helmu']]) +
          '<p>Pro sjezdovku se orientujte na <a href="/lyzarske-bundy/">lyžařské a snowboardové bundy</a>, které mají sněhovou sukni a zesílená místa. Pokud hledáte konkrétní typ, použijte landing <a href="/alpine-pro-lyzarska-bunda/">lyžařská bunda Alpine Pro</a>. Na mrazivé dny v městě slouží <a href="/zimni-bundy/">zimní bundy</a>, a když počasí zrovna nehřeje, pomůže lehká <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bunda</a>.</p>'
          '<h2>Kalhoty, kraťasy, sukně a šaty</h2>'
          '<p>Spodní část těla pokrývá několik kategorií. <a href="/sportovni-kalhoty/">Sportovní kalhoty</a> jsou pružnější a lehčí, hodí se na běh, fitness a volný čas. <a href="/outdoorove-kalhoty/">Outdoorové kalhoty</a> mají pevnější tkaninu, zesílená kolena a kapsy se zipy, a proto se hodí na túry a práci venku. Pro teplé dny je tu <a href="/sportovni-kratasy/">kraťasy</a> a pro ženy také <a href="/sportovni-sukne-a-saty/">sportovní sukně a šaty</a>, které často obsahují vnitřní šortky.</p>'
          '<p>U kalhot rozhoduje střih v pase a délka nohavice. Dlouhé nohavice lze zkrátit, ale nikdy ne prodloužit, takže raději volte sedící délku. Stahovací pasy a nastavitelné konce nohavic pomáhají přizpůsobit kalhoty pohybu. Pokud počítáte s vrstvami pod kalhotami, vezměte si i zimní termoprádlo při měření.</p>'
          '<h2>Obuv: trek, zimní boty a tenisky</h2>'
          '<p>Druhou největší kategorií jsou <a href="/trekova-obuv/">trekové boty</a>. V názvech se často objevuje označení ptx membrána, které je u lesních cest a mokra velmi užitečné. Membránová bota je teplejší a hůř větraná, takže na horké letní túry se může hodit spíše lehčí varianta bez membrány. U dětí se prodává outdoorová obuv i zimní modely. Vždy zkoušejte botu s ponožkou, kterou na túru použijete, a ověřte rezervu před palcem.</p>'
          '<p>Kategorie <a href="/zimni-obuv/">zimní boty a sněhule</a> nabízí vyšší svršek a teplou výstelku, <a href="/tenisky/">tenisky a volnočasové boty</a> pak patří spíš do města a na cesty bez náročného terénu. Pro silný mráz volte botu o půl čísla větší, aby zůstal vzduch kolem prstů a boty nesvíraly krevní oběh.</p>'
          '<h2>Velikosti, střihy a děti</h2>'
          '<p>Dámské střihy jsou užší v pase a v ramenou, pánské rovnější, dětské počítají s růstem. U všech skupin je vhodné zkontrolovat tabulku konkrétního modelu, protože velikost S, M či L se mezi řadami může lišit. Měřte obvod hrudníku, pasu a boků, a pokud jste mezi velikostmi, rozhodněte podle vrstev, které budete nosit.</p>'
          '<ul><li><strong>Bundy:</strong> nechte prostor na mikinu, ale rukávy by neměly přesahovat prsty.</li>'
          '<li><strong>Trička:</strong> pro aktivní sport zvolte přiléhavý střih, pro volný čas volnější.</li>'
          '<li><strong>Děti:</strong> volte raději větší velikost a využijte nastavitelné konce.</li>'
          '<li><strong>Obuv:</strong> zkoušejte odpoledne, kdy je noha nejširší.</li></ul>'
          '<h2>Jak se Alpine Pro liší od konkurence</h2>'
          '<p>Alpine Pro nabízí širokou škálu pro celou rodinu a jednu značku v mnoha sezónách. V tom je podobná značkám <a href="/znacka/loap/">Loap</a>, <a href="/znacka/kilpi/">Kilpi</a> a <a href="/znacka/hannah/">Hannah</a>. Specializované značky jako <a href="/znacka/the-north-face/">The North Face</a> a <a href="/znacka/columbia/">Columbia</a> zaměřují na outdoorový segment s vlastními technologiemi, zatímco Alpine Pro se soustředí na univerzální výbavu s membránou PTX. Rozdíl ve střihu, barvách a řadách si ověřte u konkrétních kusů.</p>'
          '<h2>Jak číst názvy modelů a plánovat nákup</h2>'
          '<p>Alpine Pro pojmenovává modely krátkými jmény psanými velkými písmeny, například NOGER, GREMA, TERMES nebo OLADA, a doplňuje je číslem verze. Jméno samo o sobě nic neříká, užitečné je až slovo před ním: rychleschnoucí, outdoorové, s membránou, z organické bavlny, s merino výplní. Právě ono určuje, zda kus patří na horký den, nebo do deště. Číslo za jménem označuje novější revizi téže řady, proto se starší verze při porovnávání obchodů občas zdají jako jiné zboží, ačkoli se liší jen drobnostmi.</p>'
          '<p>Nákup si rozdělte podle sezóny. Na jaře koupíte lehké bundy, trekové boty a trička, na podzim mikiny a outdoorové kalhoty, a zimní výbavu pořizujte tak, aby vám ji nepřekvapilo první sněžení. Děti potřebují nové velikosti obvykle každý rok, takže ty zahrňte do plánu samostatně.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Bundy s membránou perte při nízké teplotě bez aviváže a občas obnovte impregnaci. Trička z funkčních vláken nesušte na topení, mohla by se poškodit. Boty vyčistěte po každém výletu, vyndejte vložky a sušte při pokojové teplotě. Dodržením těchto pravidel prodloužíte životnost oblečení i obuvi o několik sezón.</p>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Zimní bundy a lyžařské kousky bývají levnější na konci zimy, letní trička a kraťasy po sezóně. Alpine Pro nabízí řady, které se obnovují po sezónách, proto jsou starší barvy často zlevněné. Porovnávejte více obchodů, sledujte dostupnost velikostí a nevybírejte jen podle ceny, ale i podle materiálu a využití.</p>',
    faq=[
        ('Pro koho je Alpine Pro v katalogu určená?', 'Zboží se dělí na dámské, pánské, dětské a unisex modely. Dámských a pánských je nejvíc, děti mají vlastní řady oblečení i obuvi a unisex kusů je méně.'),
        ('Které kategorie jsou největší?', 'Nejvíc je triček a tílek, dále trekové boty, zimní obuv, sportovní kalhoty, mikiny a tenisky. Významná je také nabídka bund, sukní, outdoorových kalhot a kraťasů.'),
        ('Co znamená označení PTX u bund a bot?', 'Jde o označení membrány, kterou značka používá u svých modelů. Má zadržet vodu zvenku a zároveň pustit páru z těla. Konkrétní hodnoty vodního sloupce a prodyšnosti najdete v popisu produktu.'),
        ('Hodí se bundy Alpine Pro na lyže?', 'V katalogu jsou lyžařské a snowboardové bundy s membránou. Při výběru sledujte sněhovou sukni, zesílená místa a odvětrání. Pro mrazivé dny doplňte vrstvu termoprádla a teplou mikinu.'),
        ('Jak vybrat velikost?', 'Změřte obvod hrudníku, pasu a boků a porovnejte s tabulkou u konkrétního kusu. Dámské střihy jsou užší, dětské počítají s růstem. Pokud jste mezi velikostmi, vezměte větší a využijte stahování.'),
        ('Je lepší tričko z bavlny, nebo funkční?', 'Bavlna je příjemná do města, ale při pocení vlhne. Funkční tričko odvádí pot a rychleji schne, proto se hodí na sport a túry. Organická bavlna je kompromis pro volnější dny.'),
        ('Mám volit trekovou obuv s membránou?', 'Membrána pomáhá v dešti a na mokrých cestách, ale hůř větrá. Na horké suché túry může být lepší lehčí bota bez membrány. Vždy ji zkoušejte s ponožkou, kterou na túru použijete.'),
        ('Jak pečovat o bundu s membránou?', 'Perte ji při nízké teplotě bez aviváže a po několika praních obnovte impregnaci. Nesušte ji na topení. Správná péče prodlouží životnost o několik sezón.'),
        ('Kdy bývají zimní kousky nejlevnější?', 'Zpravidla na konci zimy a na jaře, letní oblečení po sezóně. Sledujte srovnání obchodů a dostupnost své velikosti, protože nejčastější velikosti se vyprodají nejdřív.'),
        ('Co znamenají čísla za jménem modelu?', 'Obvykle označují novější verzi stejné řady. Starší verze se proto při porovnání obchodů může jevit jako jiné zboží, ačkoli se liší jen drobnostmi. Rozhodující jsou slova v názvu a popis materiálu.'),
    ],
)

# ------------------------------------------------------------------ siroko
NEW['siroko'] = dict(
    title='Siroko: cyklistické oblečení, tretry a lyžařské bundy',
    desc='Siroko v katalogu sporteky: cyklistické dresy, tretry, kraťasy, ponožky, brýle a lyžařské a snowboardové oblečení. Jak vybírat a kdy hledat slevy.',
    intro='<p>Siroko je v našem katalogu především cyklistická značka, ale s výrazným zimním doplňkem. Největší skupinu zboží tvoří <a href="/cyklisticke-obleceni/">cyklistické oblečení</a>, hned za ním jsou lyžařské a snowboardové bundy a kalhoty. Doplňují je kraťasy, trička, čepice, zimní bundy, ponožky, tílka, brýle a dresy. '
          'V názvech se opakují označení řad jako M2, M3, SRX nebo W1 a W4, které odlišují typ oblečení a použití. Pánské a dámské modely jsou zastoupeny téměř vyrovnaně, unisex a dětské kousky tvoří menší část. '
          'Na této stránce vysvětlujeme, jak v nabídce rozlišit silniční, gravelové a zimní kusy, jak vybírat dres, kalhoty a tretry, na co se zaměřit u snowboardového oblečení a jak využít porovnání obchodů. Žádné konkrétní ceny neuvádíme.</p>',
    guide='<h2>Co Siroko v katalogu nabízí</h2>'
          '<p>Z pohledu sortimentu tvoří značku dvě hlavní větve. První je cyklistika: dresy s krátkým i dlouhým rukávem, kalhoty, ponožky, termokalhoty, kompresní kalhoty a tretry. Druhá je zimní sport: snowboardové a lyžařské bundy a kalhoty, často z tvrdého hardshellu. K nim se přidává běžné sportovní oblečení: trička, tílka, kraťasy a čepice. Díky tomu lze od jedné značky pořídit výbavu pro cyklistický i lyžařský rok.</p>'
          + T(['Skupina', 'Co v ní najdete', 'Typické použití'], [
              ['Cyklistika', 'dresy, kalhoty, termokalhoty, ponožky, brýle, tretry', 'silnice, gravel, trénink, závody'],
              ['Zima', 'lyžařské a snowboardové bundy a kalhoty, zimní bundy', 'sjezdovka, snowpark, mráz'],
              ['Každodenní sport', 'trička, funkční trička, tílka, kraťasy', 'běh, fitness, léto'],
              ['Doplňky', 'čepice, ponožky, sportovní a sluneční brýle', 'ochrana, vzhled, pohodlí']]) +
          '<p>Barevně převládá černá, následuje modrá, zelená a bílá, ale vedle nich je tu i béžová, červená a růžová. Oproti jiným značkám tu najdete i neobvyklejší odstíny. U cyklistických dresů je výrazná barva praktická, protože zvyšuje viditelnost na silnici.</p>'
          '<h2>Cyklistické dresy a kalhoty</h2>'
          '<p>Kategorie <a href="/cyklisticke-obleceni/">cyklistické oblečení</a> je nejširší. Zahrnuje <a href="/cyklisticke-dresy/">cyklistické dresy</a>, kalhoty s vložkou a termokalhoty na chladné dny. V názvech se opakuje označení ultralehký, které se používá pro tenké a prodyšné materiály vhodné na teplo. Dres s krátkým rukávem se hodí na léto, dlouhý rukáv na jaro a podzim. Dámské modely jsou užší v ramenou a s jiným střihem v pase.</p>'
          '<p>U cyklistického dresu rozhoduje střih. Závodní střih těsně přiléhá a snižuje odpor vzduchu, ale není tak pohodlný při delším sezení. Volnější, takzvaný relaxovaný střih, je lepší pro dlouhé jízdy. Zip na hrudi umožňuje větrání a kapsy na zádech uvezou jídlo, mobil i klíče. Kalhoty s vložkou se nosí bez spodního prádla, aby nedocházelo k otlakům.</p>'
          + T(['Prvek', 'Na co se zaměřit', 'Proč je důležitý'], [
              ['Dres', 'materiál, střih, zip, kapsy', 'komfort a odvětrání při jízdě'],
              ['Kalhoty', 'vložka, šle, lemy nohavic', 'brání otlakům a posouvání'],
              ['Termokalhoty', 'zateplení, odolnost proti větru', 'chladné dny, ranní jízdy'],
              ['Ponožky', 'výška, materiál, švy', 'pohodlí a sucho v tretrách'],
              ['Brýle', 'zorné pole, filtr, těsnost', 'ochrana očí před větrem a slunce']]) +
          '<h2>Tretry a ponožky</h2>'
          '<p>Siroko nabízí tretry pro různé jezdce: silniční, gravelové a zimní. Silniční tretry mají tuhou podrážku pro maximální přenos síly. Gravelové mají vzorek, který umožní krátkou chůzi, a jsou univerzálnější. Zimní tretry bývají vyšší a zateplené. Před koupí zkontrolujte typ kolíků, tedy systém zapínání do pedálu, protože musí odpovídat vašim pedálům. U velikostí zvažte širší nohu, protože tuhé tretry se po koupi už neroztáhnou.</p>'
          '<p>K tretrám patří <a href="/sportovni-ponozky/">sportovní ponožky</a>. Cyklistické jsou tenké, často vyšší nad kotník a z materiálu, který odvádí vlhkost. Nepoužívejte tlusté bavlněné ponožky, protože v těsné obuvi způsobí otlaky a vlhko.</p>'
          '<h2>Lyžařské a snowboardové oblečení</h2>'
          '<p>Druhým pilířem jsou <a href="/lyzarske-bundy/">lyžařské a snowboardové bundy</a> a <a href="/lyzarske-kalhoty/">lyžařské a snowboardové kalhoty</a>. V názvech se opakuje označení hardshell, což znamená tvrdou nepromokavou skořepinu, která chrání před vodou i větrem. Hardshell nemá vlastní zateplení, takže pod něj patří termoprádlo a mikina nebo lehké zateplení. Dámské i pánské střihy jsou často volnější, jak je u snowboardu běžné.</p>'
          '<p>Při výběru sledujte sněhovou sukni, výztuhy kolen, ventilaci v podpaží a přístup do kapes bez sundání batohu. Pro nízké teploty doplňte <a href="/zimni-bundy/">zimní bundy</a> nebo teplou vrstvu pod bundu. Základem je vrstvení: termoprádlo, střední vrstva, vrchní vrstva.</p>'
          + T(['Vrstva', 'Úkol', 'Příklad'], [
              ['Základní', 'odvádí pot od kůže', 'funkční prádlo, termokalhoty'],
              ['Střední', 'zadržuje teplo', 'mikina, lehká bunda'],
              ['Vrchní', 'chrání před vodou a větrem', 'hardshellová bunda a kalhoty']]) +
          '<h2>Trička, kraťasy a doplňky</h2>'
          '<p>Mezi běžnějšími kategoriemi je <a href="/sportovni-tricka/">trička a tílka</a>, <a href="/funkcni-tricka/">funkční trička</a>, <a href="/tilka/">tílka a topy</a> a <a href="/sportovni-kratasy/">kraťasy</a>. V názvech se objevují atletické scuba kraťasy a funkční kompresní kalhoty. Funkční trička jsou z tenkého materiálu, který rychle schne a vhodně se nosí pod dres nebo samostatně. Kompresní oblečení přiléhá k tělu a podle výrobců podporuje svaly, ale pocit je individuální.</p>'
          '<p>Z doplňků se vyplatí <a href="/cepice-a-celenky/">čepice a čelenky</a> pod helmu a <a href="/sportovni-bryle/">sportovní a sluneční brýle</a>. Brýle při jízdě chrání oči před větrem, hmyzem a prachem, a proto by měly dobře těsnit a mít zorné pole bez rušivých rámečků.</p>'
          '<h2>Velikosti a střihy</h2>'
          '<p>Velikosti se mohou lišit od běžných českých. Vždy zkontrolujte tabulku u konkrétního kusu a měřte obvod hrudníku, pasu a boků. U cyklistických dresů zvolte takovou velikost, aby se neshrnovala záda při předklonu. U snowboardového oblečení si nechte prostor na vrstvy, u tretry zkontrolujte délku chodidla v milimetrech.</p>'
          '<ul><li><strong>Dres:</strong> v předklonu nesmí být záda nad pasem odhalená.</li>'
          '<li><strong>Kalhoty:</strong> vložka má sedět pod sedacími kostmi, ne uprostřed zadku.</li>'
          '<li><strong>Tretry:</strong> měřte chodidlo večer a počítejte s tenkou ponožkou.</li>'
          '<li><strong>Snowboard:</strong> kalhoty musí přes boty, aby nenabíraly sníh.</li></ul>'
          '<h2>Jak se Siroko liší od konkurence</h2>'
          '<p>Zatímco <a href="/znacka/castelli/">Castelli</a> nebo <a href="/znacka/rogelli/">Rogelli</a> jsou čistě cyklistické značky, Siroko spojuje cyklistiku se zimním sportem a běžným sportovním oblečením. Široké sportovní značky jako <a href="/znacka/nike/">Nike</a> a <a href="/znacka/adidas/">Adidas</a> cyklistiku skoro nenabízejí. Siroko je proto zajímavé pro sportovce, kteří chtějí v létě jezdit na kole a v zimě na sněhu a nechtějí hledat dvě značky.</p>'
          '<h2>Jak číst názvy řad a vybírat podle použití</h2>'
          '<p>V názvech se u Siroko opakují krátké kódy jako M2, M3, S1, W1, W4, P2 nebo SRX. Z nich lze odvodit orientačně, o co jde: písmeno M se objevuje u cyklistických dresů, S u ponožek, W u snowboardových a lyžařských bund a P u kalhot. Přesný význam kódů značka nevysvětluje, a proto se spoléhejte spíš na slova v názvu a popis. Za kódem často následuje jméno trati, místa nebo barvy, které odlišuje potisk a barevnou verzi téhož střihu.</p>'
          '<p>Pokud kupujete první cyklistickou výbavu, začněte dresem a kalhotami s vložkou, potom přidejte ponožky a brýle. Tretry pořizujte až když máte jasno v pedálech. Pro zimu vyberte nejdřív termoprádlo a kalhoty, protože ty se nosí nejčastěji. Pro snowboard je prvním nákupem bunda s kalhotami ze stejné řady, aby barvy a střih ladily a zip na spojení případně seděl.</p>'
          '<p>Nakonec si ujasněte, kolik času u sportu skutečně strávíte. Příležitostný jezdec nepotřebuje nejlehčí dres ani nejtužší tretru, spokojí se s univerzálnějším kusem. Závodník naopak ocení každý detail střihu, a proto se vyplatí věnovat výběru víc pozornosti. Stejně to platí pro lyžaře a snowboardisty: kdo jezdí jen týden v roce, nemusí kupovat výbavu do nejvyšších hor.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Cyklistické oblečení perte na nízké teplotě, bez aviváže a bez sušení v sušičce, aby vložka a pružné materiály držely tvar. Hardshell bundy perte podle štítku a po několika praních obnovte impregnaci. Tretry po jízdě vyndejte ze špíny, vyčistěte a sušte při pokojové teplotě. Kalhoty s vložkou vyperte po každé jízdě, protože vlhko a pot vložku poškozují.</p>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Letní cyklistické oblečení bývá zlevněné na podzim, zimní bundy a kalhoty na jaře. Protože Siroko obnovuje barevné řady, jsou starší kusy často levnější a dokonale funkční. Porovnejte více obchodů, sledujte velikosti a nenakupujte jen kvůli slevě, pokud kus nesedí.</p>',
    faq=[
        ('Co je u Siroko největší kategorií?', 'Největší je cyklistické oblečení, tedy dresy, kalhoty a doplňky. Dále následují lyžařské a snowboardové bundy, kraťasy, lyžařské kalhoty a trička. Významné jsou také čepice, ponožky a brýle.'),
        ('Pro koho je Siroko?', 'Pánské a dámské modely jsou zastoupeny zhruba stejně. Unisex a dětské kusy tvoří menší část nabídky. U dětí dávejte pozor na velikostní tabulku.'),
        ('Jaký je rozdíl mezi silničními a gravelovými tretrami?', 'Silniční tretry mají tuhou podrážku pro maximální přenos síly. Gravelové mají hrubší vzorek a hodí se i na krátkou chůzi. Před koupí ověřte kompatibilitu s vašimi pedály.'),
        ('Co znamená ultralehký dres?', 'Je to tenký prodyšný dres vhodný na horké dny. V chladu ho doplňte spodní vrstvou nebo vestou. Pro delší jízdy zvažte kapsy a zip.'),
        ('Hodí se Siroko na snowboard?', 'V katalogu jsou snowboardové bundy a kalhoty, často typu hardshell. Pod ně patří termoprádlo a střední vrstva, protože samotný hardshell nehřeje. Zkontrolujte sněhovou sukni a ventilaci.'),
        ('Jak vybrat velikost cyklistického dresu?', 'Změřte obvod hrudníku a porovnejte s tabulkou. Dres má přiléhat, ale nesmí tlačit v ramenou, a záda musí v předklonu zakrývat pas. Dámské modely mají jiný střih než pánské.'),
        ('Jak prát oblečení s vložkou?', 'Perte při nízké teplotě bez aviváže a nesušte v sušičce. Vložka se tak neposune a materiál drží tvar. Perte po každé jízdě.'),
        ('Dá se Siroko nosit i mimo sport?', 'Trička, tílka, kraťasy a čepice se hodí do města. Cyklistické dresy a kalhoty jsou ale určené na jízdu, a proto jsou přiléhavé.'),
        ('Kdy hledat slevy?', 'Letní cyklistické kousky po sezóně na podzim, zimní oblečení na jaře. Porovnejte obchody a sledujte dostupnost velikostí.'),
        ('Čím začít, když teprve začínám jezdit na kole?', 'Pořiďte dres a kalhoty s vložkou, potom ponožky a brýle. Tretry kupujte až po výběru pedálů. Příležitostný jezdec nepotřebuje nejlehčí závodní kus, stačí pohodlný univerzální model, který dobře sedí a odvádí pot.'),
        ('Můžu cyklistické brýle použít i na lyže?', 'Záleží na modelu. Sportovní brýle chrání před větrem a slunce, ale lyžařská maska lépe těsní a drží teplo kolem očí. Zkontrolujte filtr, těsnost a to, zda se vejdou pod helmu.'),
    ],
)

# ------------------------------------------------------------------ armani-exchange
NEW['armani-exchange'] = dict(
    title='Armani Exchange: tenisky, trička, mikiny a tepláky',
    desc='Armani Exchange v katalogu sporteky: tenisky, trička, mikiny, tepláky, polokošile, košile a brýle pro pány i dámy. Jak vybrat střih a kdy hledat slevy.',
    intro='<p>Armani Exchange je v našem katalogu módní značka s dominantní pozicí obuvi a oblečení do města. Největší kategorií jsou <a href="/tenisky/">tenisky a volnočasové boty</a>, hned za nimi <a href="/sportovni-tricka/">trička a tílka</a>, sportovní kalhoty a <a href="/mikiny/">mikiny</a>. '
          'Dále najdete košile, tepláky, kraťasy, čepice, jarní a podzimní bundy, polokošile, brýle a menší počet zimních bund. Pánské modely převládají, dámské tvoří výraznou část. Barvy jsou střídmé: černá, bílá, modrá a béžová. '
          'Na této stránce vysvětlujeme, jak v nabídce rozlišit sportovně laděné kousky od elegantnějších, jak vybírat tenisky a mikiny, jak číst označení modelů a kdy se vyplatí čekat na slevu. Cenové údaje neuvádíme, protože se mění.</p>',
    guide='<h2>Co Armani Exchange v katalogu nabízí</h2>'
          '<p>Na rozdíl od klasických sportovních značek tu nejde o výkonnostní výbavu, ale o stylové oblečení a obuv, které se nosí do města, do kanceláře s uvolněným dresscodem i na víkend. Základ sortimentu tvoří obuv, dále tričkové kousky, kalhoty, mikiny a doplňky. Podle filtru „Pro koho“ jsou k dispozici pánské i dámské modely, přičemž pánských je asi o polovinu víc. Dětské oblečení ani unisex tu nenajdete.</p>'
          + T(['Skupina', 'Kategorie v katalogu', 'Typické použití'], [
              ['Obuv', 'tenisky a volnočasové boty, sandály', 'město, kancelář s volným dresscodem, léto'],
              ['Horní díly', 'trička, tílka, polokošile, košile, mikiny', 'každodenní nošení, vrstvení'],
              ['Spodní díly', 'sportovní kalhoty, tepláky, kraťasy, plavkové šortky', 'volný čas, dovolená'],
              ['Bundy', 'jarní a podzimní, zimní a péřové', 'chladné dny, město'],
              ['Doplňky', 'čepice, kšiltovky, sluneční brýle', 'styl, ochrana před sluncem']]) +
          '<p>Z barev dominuje černá, hned za ní je bílá, modrá a béžová. Hnědá, zelená a šedá tvoří menší část, růžová a červená se objevují spíš výjimečně. Tmavé tóny se snadno kombinují, bílé tenisky jsou módní, ale vyžadují údržbu. Béžová a hnědá se hodí do podzimních kombinací.</p>'
          '<h2>Tenisky: největší kategorie</h2>'
          '<p>Tenisky tvoří téměř třetinu celé nabídky. V názvech se opakují označení modelů začínající písmeny XM nebo XW, za nimiž následují číselné kódy, a také barva. XM obvykle označuje pánské modely a XW dámské, což ale vždy ověřte v popisu. Číselný kód slouží hlavně k přesné identifikaci, takže ho použijte při porovnávání obchodů, aby šlo o stejný kus.</p>'
          '<p>Tenisky Armani Exchange jsou módní obuv a nejsou určené pro náročný sport. Pro běh, fotbal nebo turistiku se lépe hodí specializovaná obuv, například <a href="/trekova-obuv/">trekové boty</a>. Pro město a víkend jsou ale vhodné: nižší podrážka, čistý vzhled a různé varianty barev. Při výběru sledujte materiál svršku, protože kůže a syntetika jinak snášejí vlhko, a podrážku, která určuje trakci a pohodlí.</p>'
          + T(['Vlastnost', 'Na co se zaměřit', 'Proč na tom záleží'], [
              ['Materiál svršku', 'kůže, textil, syntetika', 'údržba, prodyšnost, odolnost vůči mokru'],
              ['Podrážka', 'tloušťka, vzorek, pružnost', 'pohodlí při dlouhé chůzi'],
              ['Barva', 'tmavá, bílá, stříbrná', 'kombinovatelnost a špinění'],
              ['Velikost', 'tabulka u modelu, evropská čísla', 'střih se liší model od modelu'],
              ['Zapínání', 'tkaničky, suchý zip', 'pohodlí při nasazení']]) +
          '<h2>Trička, polokošile a košile</h2>'
          '<p>Druhá největší skupina jsou <a href="/sportovni-tricka/">trička a tílka</a>, vedle nich <a href="/polokosile/">polokošile</a> a <a href="/kosile/">košile</a>. V názvech se opakuje bavlněné pánské a dámské tričko, polo bavlněné a polo s elastanem. Bavlna je příjemná na dotek a prodyšná, ale při pocení vlhne. Příměs elastanu dodá pružnost a tvar, což je výhodné u přiléhavých střihů.</p>'
          '<p>Polokošile je univerzální: sluší na kalhoty, džíny i kraťasy a hodí se do kanceláře s uvolněným dresscodem. Košile je formálnější, ale i tu lze nosit rozhalenou přes tričko. Při výběru zvažte střih: úzký zdůrazňuje postavu, volnější je pohodlnější. Zkontrolujte délku rukávu, aby končil v zápěstí.</p>'
          '<h2>Mikiny, tepláky a kalhoty</h2>'
          '<p>Kategorie <a href="/mikiny/">mikiny</a> zahrnuje rozepínací modely s kapucí s příměsí bavlny i klasické přes hlavu. Rozepínací mikina je praktická jako střední vrstva, protože se dá snadno sundat. Pro chladné dny volte hustší materiál a pro teplé lehčí. Samostatně stojí za pozornost <a href="/teplaky/">tepláky</a>, které se nosí pohodlně doma i ven, a <a href="/sportovni-kalhoty/">sportovní kalhoty</a>, které jsou štíhlejší a vypadají upraveněji.</p>'
          '<p>Při výběru kalhot zkontrolujte pas, délku nohavice a materiál. Bavlna s elastanem pružně přiléhá a nemačká se. Tepláky se šňůrkou umožňují nastavit pas, což je u modelů se širším střihem užitečné. Na dovolenou se hodí <a href="/sportovni-kratasy/">kraťasy</a> a plavkové šortky. Plavkové šortky mají rychleschnoucí materiál a podšívku, kterou nelze nahradit běžnými kraťasy.</p>'
          '<h2>Bundy, čepice a brýle</h2>'
          '<p>Menší skupinu tvoří <a href="/sportovni-bundy-jaro-podzim/">jarní a podzimní bundy</a> a <a href="/zimni-bundy/">zimní bundy</a>, mezi nimiž je i péřová bunda. Péří hřeje při nízké hmotnosti, ale při mokru ztrácí účinnost, proto se hodí hlavně na suchý mráz. Jarní bundy chrání před větrem a lehkým deštěm. Z doplňků jsou k dispozici <a href="/cepice-a-celenky/">čepice a kšiltovky</a>, například bavlněná čepice, a <a href="/sportovni-bryle/">sluneční brýle</a>.</p>'
          '<p>U brýlí sledujte ochranu proti UV záření, tedy označení kategorie filtru, a rozměr obrouček, aby seděly na obličej. Módní brýle nenahrazují sportovní, které mají lepší těsnost a odolnost proti nárazu.</p>'
          '<h2>Velikosti a střihy</h2>'
          '<p>U módní značky se velikosti mohou lišit od sportovních. Evropské číslování tenisek se obvykle drží běžné stupnice, u oblečení ale střihy mohou sedět užší nebo kratší než běžné sportovní. Vždy zkontrolujte tabulku u konkrétního kusu a změřte obvod hrudníku, pasu a boků.</p>'
          '<ul><li><strong>Trička:</strong> přiléhavý střih nesmí tlačit v ramenou ani nad pasem.</li>'
          '<li><strong>Kalhoty:</strong> změřte pas a délku nohavice na kalhotách, které vám sedí.</li>'
          '<li><strong>Tenisky:</strong> měřte chodidlo večer a počítejte s ponožkou, kterou budete nosit.</li>'
          '<li><strong>Bundy:</strong> počítejte s mikinou pod bundou, pokud je chcete nosit spolu.</li></ul>'
          '<h2>Jak se Armani Exchange liší od konkurence</h2>'
          '<p>Sportovní značky jako <a href="/znacka/nike/">Nike</a>, <a href="/znacka/adidas/">Adidas</a> nebo <a href="/znacka/puma/">Puma</a> kladou důraz na výkon, technologie a sportovní obuv. Armani Exchange je naopak módní značka, kde je klíčový design, střih a kombinovatelnost s běžným oblečením. Podobný módní směr mají i <a href="/znacka/emporio-armani/">Emporio Armani</a>, <a href="/znacka/guess/">Guess</a> či <a href="/znacka/tommy-hilfiger/">Tommy Hilfiger</a>. Pro sport proto volte specializovanou značku a pro město stylovou.</p>'
          '<h2>Jak sestavit oblečení z jedné značky</h2>'
          '<p>Výhodou módní značky v katalogu je, že kusy spolu ladí. Základem může být pár černých nebo bílých teniskek, k nim tmavé sportovní kalhoty, tričko a rozepínací mikina. Na teplejší dny přijdou na řadu kraťasy a polokošile, na chladnější bunda a čepice. Dvě až tři barvy stačí: černá, bílá a jeden doplňkový tón, třeba modrá nebo béžová. Výrazné logo na hrudi je v nabídce časté, a proto ho nekombinujte s dalším velkým potiskem.</p>'
          '<p>Chcete-li působit upraveněji, zvolte košili nebo polokošili s tmavými kalhotami a bílými teniskami. Pro víkend naopak stačí tepláky, mikina a čepice. Pamatujte, že kus oblečení se nosí tak často, jak často s ním dokážete něco sladit, takže u každého nákupu zvažte alespoň tři kombinace, které z něj vytvoříte.</p>'
          '<h2>Na co si dát pozor u zboží s módním logem</h2>'
          '<p>Oblečení s výrazným logem se často prodává po celém světě, a proto se na trhu objevují i padělky. Kupujte u ověřených obchodů, které jsou na naší stránce srovnané, a porovnávejte číselné kódy modelů. Podezřelé jsou kusy výrazně levnější než ostatní nabídky, neúplné popisy a chybějící kódy. Zkontrolujte také možnost vrácení zboží, protože u módního oblečení se velikost vyplatí vyzkoušet doma.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Bavlněné oblečení perte na doporučenou teplotu a ostatní kusy otočené naruby, aby potisk a logo vydržely. Mikiny sušte volně, aby se nezmačkaly. Tenisky čistěte vlhkým hadříkem, kůži ošetřete krémem a neperte je v pračce, pokud to štítek nedovoluje. Bílou podrážku čistěte jemným kartáčkem. Dobrá péče udrží vzhled i několik sezón.</p>'
          '<h2>Kdy a jak hledat slevy</h2>'
          '<p>Módní značky se zlevňují na konci sezóny. Zimní bundy a mikiny bývají levnější na jaře, letní trička, kraťasy a sandály na podzim. Tenisky mají často starší barevné varianty ve slevě po celý rok. Porovnávejte více obchodů, sledujte skladovost velikostí a používejte číselný kód modelu k ověření, že jde o stejný kus.</p>',
    faq=[
        ('Co je u Armani Exchange největší kategorií?', 'Tenisky a volnočasové boty. Následují trička a tílka, sportovní kalhoty, mikiny, košile, tepláky a kraťasy. Menší část tvoří čepice, bundy, polokošile, brýle a zimní bundy.'),
        ('Je Armani Exchange sportovní značka?', 'Spíše módní. Sortiment tvoří městské oblečení a obuv, které se nosí denně. Pro výkonnostní sport se hodí specializované značky. Zde vybírejte kvůli stylu a kombinovatelnosti.'),
        ('Pro koho je nabídka určena?', 'Zboží se dělí na pánské a dámské modely, pánských je zhruba o polovinu víc. Dětské oblečení ani unisex kusy v katalogu nejsou.'),
        ('Co znamenají kódy XM a XW v názvech tenisek?', 'Jde o označení modelu, obvykle pánského a dámského. Číselný kód slouží k přesné identifikaci kusu. Použijte ho při porovnávání obchodů, ale pohlaví ověřte v popisu.'),
        ('Hodí se tenisky Armani Exchange na sport?', 'Jsou určené do města a na volný čas. Pro běh, fotbal nebo turistiku zvolte specializovanou obuv s odpovídající podrážkou a tlumením.'),
        ('Jak vybrat velikost?', 'Podívejte se na tabulku u konkrétního kusu, změřte obvod hrudníku, pasu a boků. U tenisek měřte chodidlo večer. Pokud jste mezi velikostmi, vezměte větší.'),
        ('Jak pečovat o bílé tenisky?', 'Čistěte je vlhkým hadříkem a jemným kartáčkem, kůži ošetřete krémem. Nesušte na topení a pokud to štítek nedovoluje, neperte v pračce.'),
        ('Jaký je rozdíl mezi polokošilí a tričkem?', 'Polokošile má límec a knoflíky, a proto vypadá formálněji. Tričko je pohodlnější a sportovnější. Obojí se vyrábí z bavlny, často s příměsí elastanu.'),
        ('Kdy bývají zimní bundy levnější?', 'Obvykle na jaře, letní trička a kraťasy po sezóně. Porovnejte více obchodů a sledujte dostupnost velikostí.'),
        ('Jak poznám padělek?', 'Podezřelé jsou výrazně nižší ceny, chybějící číselný kód modelu a neúplný popis. Kupujte u ověřených obchodů, porovnejte kód s ostatními nabídkami a před koupí si přečtěte podmínky vrácení.'),
        ('Mohu kusy kombinovat mezi sebou?', 'Ano, značka drží střídmou paletu, takže tričko, mikina, tepláky i tenisky spolu obvykle ladí. Nejlépe fungují dvě až tři barvy, například černá, bílá a jeden doplňkový tón.'),
    ],
)
