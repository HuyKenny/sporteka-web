"""sporteka.cz — extra intro / guide sections for texty_vlna10d (4. 11. 2026)."""
EXTRA = {}


def _x(slug, intro, guide):
    EXTRA[slug] = dict(intro='<p>' + intro + '</p>', guide=guide)


_x('muskareni', 'Nabídka pokrývá začátečníky i zkušené muškaře, od hotových mušek po materiály na vlastní vázání.',
   '<h3>Kde a kdy lovit</h3><p>Pstruhy a lipany lovíte na řekách od jara do podzimu, nejlépe za soumraku, kdy hmyz líhne. Štiky a okouny na streamery se chytají i na jezerech a přehradách. Před výpravou si ověřte povolenku a pravidla revíru. Vhodné jsou brodicí boty nebo prsačky, polarizační brýle a čepice s kšiltem, které omezují odlesky vody a chrání oči před háčkem.</p>'
   '<h3>Časté chyby</h3><ul><li>Prut a šňůra různých tříd.</li><li>Příliš velká muška pro opatrné pstruhy.</li><li>Hrubé zacházení s rybou před vypuštěním.</li></ul>')
_x('skateboardy', 'V nabídce jsou kompletní boardy pro děti i dospělé a samostatné díly na vlastní sestavení.',
   '<h3>Jak board sestavit sám</h3><p>Začněte deskou podle šířky a stylu jízdy, přidejte osy odpovídající šířce a kola s tvrdostí podle povrchu. Ložiska a šrouby se kupují zvlášť, grip tape se nalepí na horní stranu desky. Sestavení zvládnete za půl hodiny a získáte board přesně podle sebe.</p>'
   '<h3>Péče</h3><p>Po jízdě v mokru ložiska vysušte a občas promažte. Opotřebovaná kola otočte, aby se opotřebovávala rovnoměrně, a včas je vyměňte, jakmile ztratí kruhový tvar.</p>')
_x('vysoke-trekove-boty', 'V nabídce jsou pánské i dámské modely s membránou i bez ní, od lehkých po zimní.',
   '<h3>Ponožky a vložky</h3><p>Na trek volte ponožky bez tlustých švů z merina nebo syntetiky, které odvádějí vlhkost. Bavlněné ponožky vlhnou a způsobují puchýře. Pokud vás boty tlačí v klenbě, vyzkoušejte jiné vložky, protože stélky z výroby jsou často jen základní.</p>'
   '<h3>Péče</h3><p>Po túře boty vytáhněte z batohu, vyjměte stélky a nechte oschnout mimo topení. Přímé teplo poškozuje lepidlo a kůži.</p>'
   '<h3>Časté chyby</h3><ul><li>Nové boty bez rozchození na dlouhou túru.</li><li>Příliš velká bota, v níž nohy při sestupu narážejí na špičku.</li></ul>')
_x('outdoorove-kalhoty', 'Najdete pánské, dámské i dětské modely od lehkých letních po teplé zimní, často s odepínacími nohavicemi.',
   '<h3>Kdy který typ</h3><p>Na horké dny a rychlé schnutí zvolte tenký nylon, ve větru softshell a v mrazu zateplený model s fleecovou podšívkou. Pro cestování se hodí odepínací kalhoty, které se vejdou do malého prostoru a nahradí kraťasy. Na vícedenní túry vyberte materiál odolný proti otěru, který snese batoh i kameny.</p>'
   '<h3>Velikost a střih</h3><p>Vyzkoušejte si dřep a vysoký krok, protože kalhoty nesmí tahat v rozkroku. Delší nohavici zkraťte, aby se nešlapala při chůzi.</p>')
_x('inline-brusle', 'V nabídce jsou dětské, dámské i pánské modely, od rekreačních po rychlostní.',
   '<h3>Jak se naučit</h3><p>Začněte na rovném hladkém povrchu bez provozu. Naučte se stát v mírném předklonu s pokrčenými koleny, pak odrážet jednou nohou a nakonec brzdit patní brzdou. Pádů se nevyhnete, takže chrániče na zápěstí jsou nejdůležitější.</p>'
   '<h3>Údržba</h3><p>Po jízdě na mokru brusle vysušte, ložiska občas vyčistěte a naolejujte. Kola pravidelně prohazujte, protože vnější hrana se opotřebovává rychleji.</p>')
_x('cyklo-tasky-a-nosice', 'Najdete brašny na nosiče, tašky na rám a řídítka i košíky pro městská kola.',
   '<h3>Cyklotůra s brašnami</h3><p>Na vícedenní túru vyberte dvě boční brašny kolem dvaceti litrů a přidejte tašku na řídítka na drobnosti. Těžší věci dávejte do zadních brašen, lehké do předních. Zkoušejte jízdu naloženým kolem předem, protože se chová jinak.</p>'
   '<h3>Městské použití</h3><p>Do města se hodí brašna přes nosič, která se dá sundat a nosit jako taška. Košík na řídítka pojme nákup, ale nenakládejte jej příliš, aby neovlivnil řízení.</p>')
_x('salova-obuv', 'Najdete modely pro děti i dospělé, na florbal, volejbal, házenou i tělocvik.',
   '<h3>Jak sedí správná obuv</h3><p>Zkoušejte boty se sportovními ponožkami a ověřte, že pata nesjíždí při změně směru. Prsty musí mít volnost, ale chodidlo nesmí v botě klouzat. Pro děti vybírejte se zhruba půlcentimetrovou rezervou na růst, větší rozdíl zhoršuje stabilitu.</p>'
   '<h3>Kdy vyměnit</h3><p>Když se podrážka na špičce a patě sjede do hladka nebo začne boty propouštět tlumení, sníží se přilnavost a vzroste riziko zranění kotníku.</p>'
   '<h3>Časté chyby</h3><ul><li>Venkovní běžecké boty v hale.</li><li>Obuv bez opory pro volejbal.</li></ul>')
_x('merino-pradlo', 'Najdete pánské, dámské i dětské modely, od lehkých triček po teplé legíny.',
   '<h3>Kdy ho použít</h3><p>Na zimní sporty, běžky a túry se hodí jako první vrstva, na kterou přijde fleece a bunda. Při nízké aktivitě, například na pozorování zvěře, zvolte těžší gramáž. V létě stačí lehké merino na kolo i do hor, protože nesmrdí.</p>'
   '<h3>Merino nebo syntetika</h3><p>Syntetika schne rychleji a je odolnější, merino je teplejší a pohodlnější. Směsi spojují výhody obojího.</p>'
   '<h3>Časté chyby</h3><ul><li>Praní na vysoké teplotě, které vlnu srazí.</li><li>Příliš volný střih, který nehřeje.</li></ul>')
_x('sportovni-sukne-a-saty', 'Najdete modely v různých délkách a barvách pro dámy i dívky.',
   '<h3>Jak vybrat délku</h3><p>Kratší sukně se hodí na tenis a padel, kde potřebujete volný pohyb. Delší střih zvolte na golf nebo na každodenní nošení. Vnitřní šortky by měly mít silikonový lem, který se neposouvá.</p>'
   '<h3>Kombinace s obuví</h3><p>Ke sportovní sukni se hodí nízké ponožky a lehká obuv. Na golf zvolte tmavší elegantní boty, na tenis světlou podrážku.</p>'
   '<h3>Časté chyby</h3><ul><li>Příliš těsná sukně, která brání kroku.</li><li>Šortky pod sukní z jiného materiálu, které se vymačkávají.</li></ul>')
_x('rybarske-navijaky', 'Najdete navijáky na přívlač, feeder, kapry i na moře od různých výrobců.',
   '<h3>Správný párování</h3><p>Naviják vybírejte spolu s prutem tak, aby sestava seděla v rovnováze. Příliš těžký naviják na lehký prut unaví ruku, příliš lehký vychýlí rovnováhu opačně. Na cívku naviňte vlasec těsně pod okraj, aby se při hodu nesvíjel.</p>'
   '<h3>Brzda</h3><p>Brzdu nastavte na asi třetinu nosnosti vlasce a ověřte, že se při zátahu plynule uvolňuje. Po lovu brzdu povolte, aby se podložky nestlačily.</p>'
   '<h3>Časté chyby</h3><ul><li>Příliš utažená brzda, která roztrhne návazec.</li><li>Neopláchnutý naviják po moři.</li></ul>')
_x('sedla-a-gripy', 'Najdete sedla pro silniční, horská i městská kola, gripy a omotávky.',
   '<h3>Jak poznat správné sedlo</h3><p>Správné sedlo nepřiškrcuje, nezpůsobuje otlaky a podepírá sedací kosti. Pokud po jízdě bolí měkké tkáně, zkuste sedlo s výřezem nebo jiné šířky. Dámská sedla bývají širší vzadu a kratší vpředu.</p>'
   '<h3>Výměna gripů</h3><p>Gripy se nasazují s pomocí stlačeného vzduchu nebo vody s mýdlem. Šroubovací modely upevníte objímkou a vydrží i při tvrdé jízdě.</p>'
   '<h3>Časté chyby</h3><ul><li>Příliš měkké sedlo na dlouhé trasy.</li><li>Špatně nastavený sklon sedla.</li></ul>')
_x('soupravy', 'Najdete modely pro muže, ženy a děti, od tepláků po fitness komplety.',
   '<h3>Souprava na trénink</h3><p>Na trénink se hodí lehčí materiál, který nebrání pohybu a odvádí pot. Před zápasem a po něm se hodí zateplená souprava, která udrží svaly v teple. Pokud hrajete v týmu, zvolte jednotné barvy a zkontrolujte, že souprava vydrží časté praní.</p>'
   '<h3>Souprava na volný čas</h3><p>Pohodlná bavlněná souprava se hodí domů, na výlet i na cestu. Zvolte univerzální barvu a střih, který pasuje k dalšímu oblečení.</p>'
   '<h3>Časté chyby</h3><ul><li>Příliš těsná souprava, která omezuje pohyb.</li></ul>')
_x('joga-a-pilates', 'Najdete pomůcky pro začátečníky i pokročilé, od podložek po meditační vybavení.',
   '<h3>První kroky</h3><p>Na první lekce stačí podložka a pohodlné oblečení. Postupně přidáváte blok a popruh, které pomáhají s nepříjemnými pozicemi. Pilates pomůcky, jako míč nebo kruh, přicházejí na řadu s pokročilými cviky.</p>'
   '<h3>Jak cvičit doma</h3><p>Vyberte klidné místo s dostatkem prostoru, vypněte telefon a cvičte alespoň čtvrt hodiny. Pravidelnost je důležitější než délka.</p>'
   '<h3>Časté chyby</h3><ul><li>Příliš tenká podložka na tvrdé podlaze.</li><li>Skluzná podložka při dynamické józe.</li></ul>')
_x('ostatni-doplnky-stravy', 'Najdete široký výběr od základních vitaminů po specializované doplňky, často v kapslích i v prášku.',
   '<h3>Jak číst etiketu</h3><p>Zaměřte se na obsah účinné látky v jedné dávce a doporučené denní množství. Zkontrolujte přídatné látky, plniva a alergeny. U bylinných doplňků zjistěte, jaká část rostliny se použila a v jaké formě.</p>'
   '<h3>Kdy začít</h3><p>Nejprve upravte jídelníček a spánek, doplňky přidávejte postupně a po jednom, abyste poznali, co vám sedí. U sportovců se doplňky volí podle zátěže a ročního období.</p>'
   '<h3>Časté chyby</h3><ul><li>Kombinace příliš mnoha přípravků najednou.</li><li>Překračování doporučené dávky.</li></ul>')

MORE = {
 'skateboardy': ('', '<h3>Kde jezdit</h3><p>Začátečníci jezdí na hladkém asfaltu nebo na skateparku mimo provoz. Chodník s mezerami a štěrk jsou nevhodné, protože kola se zastaví a hrozí pád.</p>'),
 'vysoke-trekove-boty': ('', '<h3>Kdy boty vyměnit</h3><p>Když se rozlepí podešev, vzor zmizí do hladka nebo boty přestanou držet kotník, je čas na novou dvojici.</p>'),
 'outdoorove-kalhoty': (' Vybírejte je podle sezóny a terénu.', '<h3>Barvy a styl</h3><p>Zemité odstíny se hodí do lesa a nezvýrazní špínu, tmavé do města. Světlé barvy odrážejí slunce, ale rychleji se zašpiní.</p><h3>Doplňky</h3><p>K túře patří i pásek, návleky nebo ponožky přes kalhoty, které chrání před klíšťaty.</p>'),
 'inline-brusle': (' Vyberte podle zkušeností.', '<h3>Kde bruslit</h3><p>Hodí se asfaltové cyklostezky, hladké parky a prázdné parkoviště. Vyhněte se silnici s provozem a drsnému povrchu, který kola brzdí.</p><h3>Velikost u dětí</h3><p>Dětské brusle s nastavitelnou velikostí vydrží dvě až tři sezóny, ale zkontrolujte po každém nastavení, že jsou dobře zajištěné.</p>'),
 'cyklo-tasky-a-nosice': (' Vybírejte podle kola.', '<h3>Montáž nosiče</h3><p>Nosič se přišroubuje k okům na rámu a vidlici. Zkontrolujte dotažení šroubů po prvních kilometrech a ověřte volnou patu u nohy při šlapání.</p><h3>Bezpečnost</h3><p>Přidejte zadní světlo a reflexní prvky, aby brašny nezakrývaly viditelnost.</p>'),
 'salova-obuv': (' Vybírejte podle sportu.', '<h3>Barva a design</h3><p>Světlé a barevné podrážky jsou v sálech povoleny, černé gumové mohou zanechat stopy. Ověřte pravidla haly, kde hrajete.</p><h3>Zkoušení</h3><p>Při zkoušce udělejte krok do strany a krátký výskok, abyste ověřili oporu.</p>'),
 'merino-pradlo': (' Vybírejte podle teploty.', '<h3>Velikost</h3><p>Merino by mělo přiléhat, ale netlačit. Při dvou velikostech zvolte menší, protože se vlna lehce natáhne.</p><h3>Doplňky</h3><p>K prádlu se hodí merino ponožky, čepice a nákrčník, které doplní teplo na celé tělo.</p>'),
 'sportovni-sukne-a-saty': (' Vybírejte podle sportu.', '<h3>Velikost a pohodlí</h3><p>Zkuste se předklonit, zvednout nohu a dřepnout, abyste ověřili, že sukně nikde netahá. Pas by neměl vtlačovat ani klouzat dolů.</p><h3>Barvy</h3><p>Světlé barvy se hodí na tenis a léto, tmavé zakryjí pot.</p>'),
 'rybarske-navijaky': (' Vybírejte podle prutu.', '<h3>Čištění</h3><p>Navijáky nerozebírejte bez znalosti. Stačí opláchnout, osušit a nanést kapku oleje na rukojeť a ložiska podle návodu.</p><h3>Pravák a levák</h3><p>Většina navijáků má přehoditelnou kličku, takže si ji nastavíte na stranu, která vám vyhovuje.</p>'),
 'sedla-a-gripy': (' Vybírejte podle kola.', '<h3>Šířka sedla</h3><p>Změřte vzdálenost sedacích kostí a podle ní vyberte šířku. Mnoho obchodů nabízí měřicí podložku, která velikost určí během minuty.</p><h3>Údržba</h3><p>Sedlo čistěte vlhkým hadrem, kožené ošetřete přípravkem. Gripy vyměňte, když ztratí povrch.</p>'),
 'soupravy': (' Vybírejte podle účelu.', '<h3>Velikost</h3><p>Při výběru počítejte s vrstvami pod soupravu a s růstem u dětí. Zkontrolujte i délku rukávů a nohavic, které se po praní mírně zkrátí.</p><h3>Kvalita</h3><p>Dobrá souprava má pevné švy, kvalitní zip a nepoužívá se jen na jedno praní.</p>'),
 'joga-a-pilates': (' Vybírejte podle cvičení.', '<h3>Oblečení</h3><p>Na cvičení se hodí pružné legíny a přiléhavé tričko, které nepřekáží v poloze hlavou dolů. Cvičí se naboso nebo v protiskluzových ponožkách.</p><h3>Péče o tělo</h3><p>Po cvičení se protáhněte a dodržujte pitný režim.</p>'),
 'ostatni-doplnky-stravy': ('', '<h3>Skladování</h3><p>Doplňky skladujte v suchu mimo slunce a mimo dosah dětí. Po otevření dodržujte dobu spotřeby uvedenou na obalu.</p><h3>Spolehlivost obchodu</h3><p>Kupujte od prověřeného obchodu, který uvádí šarži a datum spotřeby.</p>'),
}
for _s, (_i, _g) in MORE.items():
    EXTRA[_s]['intro'] = EXTRA[_s]['intro'][:-4] + _i + '</p>' if _i else EXTRA[_s]['intro']
    EXTRA[_s]['guide'] += _g

_TAIL = {
 'inline-brusle': 'Zkontrolujte před jízdou stav šroubů. Brusle po sezóně uložte suché a mimo mráz. Pro bezpečnost vybírejte výrazné barvy.',
 'cyklo-tasky-a-nosice': 'Po dešti brašny vysušte, aby uvnitř nevznikla plíseň. Zkontrolujte zipy, popruhy a suché zipy, které se časem opotřebují.',
 'salova-obuv': 'Dvě sady obuvi, jedna na trénink a druhá na zápas, vydrží déle. Boty po hře vyvětrejte a nenechávejte je v tašce.',
 'merino-pradlo': 'Prádlo po sundání vyvěste na čerstvý vzduch, nemusí se prát po každém použití. Díry u nohavic opravte hned, aby se nerozšířily.',
 'sportovni-sukne-a-saty': 'Před nákupem zkontrolujte kapsy a to, zda šortky uvnitř nejsou příliš těsné. Pro děti vybírejte pevné švy.',
 'rybarske-navijaky': 'Rezervní cívku s jiným vlascem mějte po ruce. Naviják nenoste v ruce za kličku, ale za tělo, aby se neohnula.',
 'sedla-a-gripy': 'Při změně sedla jezděte nejprve kratší trasy. Pokud vás bolí kolena nebo záda, upravte výšku i sklon, ne jen vyměňte sedlo.',
 'joga-a-pilates': 'Pokud cvičíte na koberci, položte pod podložku protiskluzovou vložku. Pro meditaci si přidejte tichou hudbu nebo aplikaci.',
 'ostatni-doplnky-stravy': 'Doplněk neberte bez poradenství, pokud užíváte léky na předpis, a po otevření dodržujte pokyny k uchování.',
}
for _s, _t in _TAIL.items():
    EXTRA[_s]['guide'] += '<p>' + _t + '</p>'
EXTRA['inline-brusle']['intro'] = EXTRA['inline-brusle']['intro'][:-4] + ' Ceny porovnáte pohromadě.</p>'
EXTRA['cyklo-tasky-a-nosice']['intro'] = EXTRA['cyklo-tasky-a-nosice']['intro'][:-4] + ' Ceny porovnáte pohromadě.</p>'
EXTRA['salova-obuv']['intro'] = EXTRA['salova-obuv']['intro'][:-4] + ' Ceny porovnáte pohromadě.</p>'
EXTRA['merino-pradlo']['intro'] = EXTRA['merino-pradlo']['intro'][:-4] + ' Ceny porovnáte pohromadě.</p>'
EXTRA['sportovni-sukne-a-saty']['intro'] = EXTRA['sportovni-sukne-a-saty']['intro'][:-4] + ' Ceny porovnáte pohromadě.</p>'
EXTRA['rybarske-navijaky']['intro'] = EXTRA['rybarske-navijaky']['intro'][:-4] + ' Ceny porovnáte pohromadě.</p>'
EXTRA['sedla-a-gripy']['intro'] = EXTRA['sedla-a-gripy']['intro'][:-4] + ' Ceny porovnáte pohromadě.</p>'
EXTRA['soupravy']['intro'] = EXTRA['soupravy']['intro'][:-4] + ' Ceny porovnáte pohromadě.</p>'
EXTRA['joga-a-pilates']['intro'] = EXTRA['joga-a-pilates']['intro'][:-4] + ' Ceny porovnáte pohromadě. Pomůcky doplňujte postupně.</p>'
EXTRA['ostatni-doplnky-stravy']['intro'] = EXTRA['ostatni-doplnky-stravy']['intro'][:-4] + ' Ceny porovnáte pohromadě.</p>'
