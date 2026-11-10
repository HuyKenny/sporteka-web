"""sporteka.cz — hand-written buying guides and FAQs of the most searched categories (8. vlna, 2. 11. 2026).

TEXTY[slug] = {'guide': html, 'faq': [(question, answer), …]} → written by katalog.py finalize into categories.guide_html / faq_json
(Kategorie.astro renders the guide under the listing and the FAQ as FAQPage). Tone: matter-of-fact like Heureka, a bit more personal and
sporty; no price slogans — the topic is how to choose. Keep claims general and true; slugs that do not exist in the tree are skipped."""
import html
import json


def G(title, intro, items=(), outro=''):
    h = f'<h2>{html.escape(title)}</h2><p>{intro}</p>'
    if items:
        h += '<ul>' + ''.join(f'<li><strong>{html.escape(a)}:</strong> {b}</li>' for a, b in items) + '</ul>'
    if outro:
        h += f'<p>{outro}</p>'
    return h


TEXTY = {
    'sportovni-obuv': {
        'guide': G('Jak vybrat sportovní obuv', 'Nejdřív rozhodněte, co v botách budete dělat. Běžecká bota je odpružená a lehká, trekovou drží kotník a chrání před kameny, tréninková obuv je stabilní do strany a na sál patří podrážka, která nešmouhá.',
                   [('Velikost', 'měřte chodidlo večer, kdy je nejširší, a nechte rezervu 0,5 až 1 cm před špičkou. Každá značka střihá trochu jinak, proto se řiďte její tabulkou.'),
                    ('Povrch', 'asfalt, les, hala nebo sníh jsou čtyři různé podrážky. Boty na špatný povrch rychle ztrácejí přilnavost.'),
                    ('Sezóna', 'membrána (GORE-TEX a podobné) drží vodu venku, ale hůř odvádí pot. V létě se obvykle vyplatí prodyšná síťovina.')],
                   'Filtry vlevo zúží výběr podle značky, velikosti, určení (pánské, dámské, dětské) a ceny. U každého produktu uvidíte velikosti, které obchod právě drží skladem.'),
        'faq': [('Jaká je správná velikost sportovní obuvi?', 'Změřte chodidlo večer a přičtěte 0,5 až 1 cm. U běžeckých a trekových bot počítejte spíš s větší rezervou, protože noha při zátěži otéká. Přesné rozměry najdete v tabulce konkrétní značky.'),
                ('Jaký je rozdíl mezi běžeckou a tréninkovou obuví?', 'Běžecká bota je odpružená pro pohyb dopředu, tréninková (fitness) má plošší a stabilnější podrážku pro boční pohyb a zvedání činek.'),
                ('Kdy vyměnit běžecké boty?', 'Zhruba po 600 až 800 kilometrech, dřív při velké váze běžce nebo tvrdém povrchu. Znamením je ztvrdlá mezipodešev a nerovnoměrné ošoupání podrážky.')],
    },
    'bezecka-obuv': {
        'guide': G('Jak vybrat běžecké boty', 'Dobré běžecké boty poznáte podle toho, že na ně zapomenete. Vybírejte podle povrchu, váhy a toho, jak došlapujete.',
                   [('Silnice nebo terén', 'silniční boty mají hladší podrážku a více odpružení, trailové mají hrubý vzorek a pevnější špičku proti kamenům.'),
                    ('Odpružení', 'těžší běžci a delší tratě ocení měkčí mezipodešev, rychlé tréninky a závody lehčí a pružnější botu.'),
                    ('Vyšší pronace', 'pokud se vám kotník při došlapu hodně propadá dovnitř, zvažte stabilnější model; pro většinu rekreačních běžců stačí neutrální bota.'),
                    ('Velikost', 'bota by měla mít před palcem asi centimetr rezervy, pata nesmí podjíždět.')],
                   'Pro porovnání vyberte značku nebo velikost ve filtru. Silniční a trailové modely najdete i v samostatných podkategoriích.'),
        'faq': [('Jak poznám, jestli jsou boty na běhání dost velké?', 'Při došlapu nesmí palec narážet na špičku a pata nesmí vyklouzávat. Rezerva asi 1 cm před prsty je běžná, protože chodidlo se při běhu roztahuje.'),
                ('Potřebuji speciální boty na trail?', 'Na lesní a kamenité cesty ano: hrubší vzorek podrážky lépe drží na bahně a mokrých kořenech a výztuž špičky chrání prsty.'),
                ('Kolik kilometrů vydrží běžecké boty?', 'Obvykle 600 až 800 km. Podle toho, jak je používáte, se ale životnost může lišit.')],
    },
    'trekova-obuv': {
        'guide': G('Jak vybrat trekové boty', 'Trekové boty musí držet nohu při dlouhé chůzi s batohem po nerovném terénu. Vybírejte podle typu túr a ročního období.',
                   [('Nízké nebo vysoké', 'nízké boty jsou lehčí a stačí na značené cesty a jednodenní výlety, vysoké drží kotník a hodí se do skal, s těžším batohem a na vícedenní túry.'),
                    ('Membrána', 'GORE-TEX a podobné membrány zaženou vodu, v horku ale hůř odvádějí pot. Na léto a suchá místa bývá lepší prodyšná varianta.'),
                    ('Podrážka', 'vzorek by měl být hluboký a samočistící; kvalitní podrážky (Vibram aj.) drží i na mokrých kamenech.'),
                    ('Velikost', 'na sestupech nesmí palec narážet na špičku, takže počítejte s rezervou kolem 1 cm a zkoušejte s trekovými ponožkami.')],
                   'Boty rozchoďte před první delší túrou, aby nedošlo k puchýřům.'),
        'faq': [('Je lepší nízká nebo vysoká trekova obuv?', 'Pro lehký batoh a pěšiny stačí nízká a lehčí obuv. Do skalnatého terénu a s těžkým batohem je vhodnější vysoká, která stabilizuje kotník.'),
                ('Potřebuji botu s membránou GORE-TEX?', 'Pokud chodíte i za deště a v mokru, vyplatí se. V letním suchu je pohodlnější prodyšná bota bez membrány.'),
                ('Jak rozchodit nové trekové boty?', 'Noste je doma a na krátkých procházkách a teprve potom na delší túru. Používejte ponožky, v nichž budete chodit i v horách.')],
    },
    'sportovni-obleceni': {
        'guide': G('Jak vybrat sportovní oblečení', 'Sportovní oblečení má odvádět pot, držet teplo a nepřekážet. Nejlépe funguje princip vrstev: spodní vrstva odvádí vlhkost, střední hřeje, vrchní chrání před větrem a deštěm.',
                   [('Spodní vrstva', 'funkční syntetika nebo merino. Bavlna nasákne potem a studí.'),
                    ('Střední vrstva', 'fleece nebo lehká izolace podle teploty.'),
                    ('Vrchní vrstva', 'větrovka, softshell nebo nepromokavá bunda s membránou podle počasí.'),
                    ('Velikost', 'u sportovního střihu počítejte s přiléhavějším tvarem. Kompresní kousky mají sedět těsně, outdoorové s rezervou na vrstvení.')],
                   'Vyberte kategorii nebo použijte filtry značky, velikosti a určení. U produktu vidíte skladem dostupné velikosti.'),
        'faq': [('Proč nenosit bavlnu na sport?', 'Bavlna nasákne potem, pomalu schne a při zastavení rychle chladí. Funkční materiály a merino odvádějí vlhkost od těla.'),
                ('Co je vrstvení oblečení?', 'Tři vrstvy s odlišnou funkcí: spodní odvádí pot, střední izoluje, vrchní chrání před větrem a deštěm. Můžete je podle počasí přidávat a ubírat.'),
                ('Jak poznám správnou velikost?', 'Porovnejte vlastní míry s tabulkou velikostí značky. Střihy se liší, takže stejné označení M nemusí sedět stejně.')],
    },
    'sportovni-bundy': {
        'guide': G('Jak vybrat sportovní bundu', 'Vyberte podle počasí a aktivity: do deště nepromokavou s membránou, na vítr lehkou větrovku, na chladný den softshell nebo izolovanou bundu.',
                   [('Nepromokavost', 'sloupec vody kolem 10 000 mm stačí na běžný déšť, na celodenní lijáky a hory hledejte víc a zalepené švy.'),
                    ('Prodyšnost', 'při námaze je důležitá stejně jako voděodolnost; větrací zipy pod paží pomáhají.'),
                    ('Izolace', 'peří je lehké a teplé, ale ve vlhku slábne; syntetická výplň hřeje i mokrá.'),
                    ('Střih', 'nechte rezervu na vrstvu pod bundou a ověřte délku rukávů při zvednutých rukou.')]),
        'faq': [('Jaký je rozdíl mezi softshellem a hardshellem?', 'Softshell je pružný, prodyšný a odolá lehkému dešti a větru. Hardshell s membránou je plně nepromokavý a patří do deště a hor.'),
                ('Kolik mm vodního sloupce má mít bunda?', 'Na běžný déšť obvykle stačí 10 000 mm, na horské túry a lijáky volte 15 000 mm a víc a zalepené švy.')],
    },
    'termopradlo': {
        'guide': G('Jak vybrat funkční a termo prádlo', 'Funkční prádlo se nosí přímo na kůži a odvádí pot. Podle aktivity a teploty vyberte tloušťku a materiál.',
                   [('Syntetika', 'rychle schne, je lehká a odolná, vhodná na běh a intenzivní sporty.'),
                    ('Merino', 'hřeje i mokré, méně zapáchá a hodí se na vícedenní túry a chlad, bývá ale dražší a méně odolné.'),
                    ('Gramáž', 'lehké prádlo (kolem 150 g/m²) je na jaro a podzim, střední a silné na zimu.'),
                    ('Střih', 'má přiléhat k tělu, jinak neodvádí pot.')]),
        'faq': [('Jaký je rozdíl mezi merinem a syntetikou?', 'Merino hřeje i mokré a pomalu zapáchá, syntetika rychleji schne a lépe snáší oděr. Obojí odvádí pot lépe než bavlna.'),
                ('Má funkční prádlo sedět těsně?', 'Ano, aby se pot dostal do materiálu. Příliš volné prádlo funguje hůř.')],
    },
    'outdoor': {
        'guide': G('Jak vybavit outdoorovou túru', 'Základ jsou boty, vrstvy oblečení, batoh a ochrana před počasím. Pak přichází spaní, jídlo, orientace a první pomoc, podle délky výletu.',
                   [('Na jeden den', 'pohodlné boty, nepromokavá vrstva, voda, svačina, čelovka a lékárnička.'),
                    ('Na víkend', 'navíc batoh 30 až 50 litrů, spací pytel, karimatka a stan nebo plachta, vařič a nádobí.'),
                    ('Na zimu', 'teplejší spací pytel, izolace pod tělo a vrstvy, které zvládnou pot i mráz.')],
                   'Podkategorie níže vás dovedou ke konkrétnímu vybavení a v každé se dá filtrovat podle značky a ceny.'),
        'faq': [('Co nezapomenout na jednodenní túru?', 'Vodu, jídlo, nepromokavou vrstvu, mapu nebo offline navigaci, čelovku, lékárničku a nabitý telefon.'),
                ('Jak velký batoh na víkendovou túru?', 'Většinou 30 až 50 litrů; záleží na tom, jestli spíte pod stanem a kolik vezete jídla.')],
    },
    'turisticke-batohy': {
        'guide': G('Jak vybrat turistický batoh', 'Batoh musí sedět na zádech a rozložit váhu na boky. Velikost vybírejte podle délky výletu.',
                   [('Objem', 'do 20 l na půlden, 25 až 35 l na den s vrstvami, 40 až 60 l na víkend a víc na vícedenní túry.'),
                    ('Délka zad', 'přesná velikost zad je důležitější než litry; zkuste batoh naložený, ne prázdný.'),
                    ('Zádový systém', 'odvětrávaný zádový panel hřeje méně, přiléhavý nese váhu lépe.'),
                    ('Detaily', 'pláštěnka, bederní popruh s kapsami a přístup do spodní části pomáhají na túře.')]),
        'faq': [('Kolik litrů má mít batoh na jednodenní túru?', 'Obvykle 20 až 35 litrů, podle ročního období a množství oblečení.'),
                ('Jak poznám správnou velikost batohu?', 'Změřte délku zad od sedmého krčního obratle k bederním kostem a porovnejte s tabulkou značky.')],
    },
    'stany': {
        'guide': G('Jak vybrat stan', 'Při výběru stanu rozhoduje počet lidí, období a způsob přepravy. Vždy počítejte s o osobu víc, než kolik vás ve stanu spí.',
                   [('Sezóna', 'tříroční stany jsou nejuniverzálnější, čtyřsezónní vydrží vítr a sníh, ale jsou těžší.'),
                    ('Vodní sloupec', 'u plachty 3 000 mm a víc, u podlahy 5 000 mm a víc.'),
                    ('Hmotnost', 'na pěší túry se vyplatí stan do 3 kg pro dvě osoby, u autokempingu vás váha tolik netrápí.'),
                    ('Konstrukce', 'tunelové stany jsou lehké a prostorné, kupolové stojí samy, rodinné mají předsíň.')]),
        'faq': [('Kolik lidí má stan pojmout?', 'Volte kapacitu o jednu osobu větší, než kolik vás bude spát. Tím získáte místo na batohy.'),
                ('Kolik mm vodního sloupce je potřeba?', 'Plachta by měla mít aspoň 3 000 mm a podlaha 5 000 mm.')],
    },
    'spaci-pytle': {
        'guide': G('Jak vybrat spací pytel', 'Rozhoduje komfortní teplota a hmotnost. Pytel s komfortní teplotou kolem 0 °C je pro většinu českého kempování univerzální.',
                   [('Komfortní teplota', 'je to teplota, při které se nebudete třást. Limitní teplota je mez přežití a nemá se brát jako cíl.'),
                    ('Výplň', 'peří má nejlepší poměr váhy a tepla, syntetika snáší vlhko a bývá levnější na údržbu.'),
                    ('Tvar', 'mumie je lehká a teplá, deková forma volnější a pohodlnější.')]),
        'faq': [('Jaká je komfortní teplota spacáku?', 'Je to teplota, při které by měl průměrný spáč v pohodě přečkat noc. Je důležitější než limitní teplota.'),
                ('Peří, nebo syntetika?', 'Peří je lehčí a teplejší na váhu, syntetika je odolnější vůči vlhku.')],
    },
    'karimatky-a-matrace': {
        'guide': G('Jak vybrat karimatku nebo matraci', 'Karimatka izoluje od země, takže rozhoduje její R-hodnota, tloušťka a velikost po složení.',
                   [('R-hodnota', 'na léto stačí 2, na jaro a podzim 3 až 4, na zimu 5 a víc.'),
                    ('Typ', 'pěnová je odolná a levnější, samonafukovací pohodlnější, nafukovací nejlehčí a nejmenší po složení.'),
                    ('Rozměr', 'standardní délka je 183 cm, delší a širší modely pohodlněji drží ramena.')]),
        'faq': [('Co znamená R-hodnota karimatky?', 'Udává tepelný odpor: čím vyšší, tím líp izoluje od zmrzlé nebo studené země.')],
    },
    'trekove-hole': {
        'guide': G('Jak vybrat trekové hole', 'Hole šetří klouby při sestupu a pomáhají v kopcích. Vybírejte podle hmotnosti, materiálu a systému skládání.',
                   [('Materiál', 'hliník je odolný, karbon lehčí a lépe tlumí, ale při nárazu snáz praskne.'),
                    ('Délka', 'při chůzi po rovině má být loket v pravém úhlu, v kopci hůl zkraťte, z kopce prodlužte.'),
                    ('Zajištění', 'vnější západka drží spolehlivěji než šroubovací systém.')]),
        'faq': [('Jak nastavit délku trekových holí?', 'Na rovině svírá loket zhruba pravý úhel, do kopce hole zkraťte, z kopce prodlužte.')],
    },
    'kemping': {
        'guide': G('Jak vybavit kemp', 'Základ kempu je střecha, spaní, vaření a světlo. Podle toho, zda jedete autem nebo pěšky, vybírejte velikost a váhu vybavení.',
                   [('Spaní', 'stan, spacák a karimatka nebo nafukovací matrace; u rodin se hodí předsíň a větší stan.'),
                    ('Vaření', 'vařič, plynová kartuše nebo gril, nádobí a chladicí box.'),
                    ('Pohodlí', 'skládací stůl a židle, lampa, nabíječka a příruční lékárnička.')]),
        'faq': [('Co si vzít na první kempování?', 'Stan, spací pytel, karimatku, vařič, nádobí, lampu a základní lékárničku. Stan si předem zkuste postavit doma.')],
    },
    'cyklistika': {
        'guide': G('Jak vybrat vybavení na kolo', 'Kolo je jen začátek. Přilba, světla, zámek a pohodlné oblečení rozhodují o tom, jak často budete jezdit.',
                   [('Kolo', 'horské do terénu, silniční na asfalt, gravel na obojí, elektrokolo do kopců a na dojíždění.'),
                    ('Bezpečí', 'přilba, přední a zadní světlo a kvalitní zámek.'),
                    ('Komfort', 'cyklistické kalhoty se vložkou, dres a rukavice se vyplatí od první delší jízdy.')]),
        'faq': [('Jakou velikost rámu zvolit?', 'Řiďte se tabulkou výrobce podle výšky postavy a délky nohou, nejlépe po zkušební jízdě.')],
    },
    'cyklisticke-helmy': {
        'guide': G('Jak vybrat cyklistickou helmu', 'Helma musí dobře sedět a mít platnou certifikaci. Vybírejte podle typu jízdy a obvodu hlavy.',
                   [('Velikost', 'změřte obvod hlavy nad obočím a vyberte model s nastavitelným kolečkem vzadu.'),
                    ('Typ', 'silniční helmy jsou lehké a větrané, MTB mají delší kšilt a zakrývají týl, městské bývají odolnější.'),
                    ('Ochrana', 'MIPS a podobné systémy snižují rotační síly při dopadu.')]),
        'faq': [('Jak poznám správnou velikost helmy?', 'Helma sedí, když nepadá do očí, pásek se dá dotáhnout pod bradu na dva prsty a při zatřesení hlavou se nehýbe.')],
    },
    'zimni-sporty': {
        'guide': G('Jak vybrat vybavení na zimní sporty', 'Sjezdovka, běžky nebo snowboard: každý sport má vlastní vybavení, ale základ je stejný. Boty a oblečení vybírejte pečlivěji než lyže.',
                   [('Boty', 'musí sedět přesně, ne být velké. Obujte je ve skladu a zkuste v nich dojít po obchodě.'),
                    ('Oblečení', 'třívrstvé: termoprádlo, izolace, nepromokavá bunda a kalhoty.'),
                    ('Ochrana', 'helma a brýle patří k vybavení každého lyžaře i snowboardisty.')]),
        'faq': [('Co si vzít na lyže poprvé?', 'Půjčovna řeší lyže a boty, vlastní byste měli mít termoprádlo, rukavice, brýle a helmu.')],
    },
    'lyzarske-bundy': {
        'guide': G('Jak vybrat lyžařskou bundu', 'Lyžařská bunda musí hřát, odvádět pot a nepustit vodu. Vyberte podle intenzity jízdy a toho, jak vám bývá zima.',
                   [('Izolace', 'zateplená bunda hřeje sama, nezateplená s membránou je univerzálnější a vrství se.'),
                    ('Voděodolnost', 'od 10 000 mm výš, pro jízdu v mokrém sněhu i víc.'),
                    ('Detaily', 'kapsa na skipas, sněhová zástěra a větrací zipy se hodí.')]),
        'faq': [('Zateplená bunda, nebo vrstvení?', 'Zateplená je pohodlná na chladné dny, nezateplená s teplou mikinou se přizpůsobí počasí a intenzitě jízdy.')],
    },
    'fitness': {
        'guide': G('Jak vybavit fitness doma', 'Pro domácí cvičení stačí pár kusů, které se vejdou do police. Podle cíle vybírejte váhy, odpor a podložku.',
                   [('Síla', 'činky a kettlebelly, odporové gumy, na vyšší zátěž osa s kotouči.'),
                    ('Kardio', 'švihadlo, bicykl nebo běžecký pás.'),
                    ('Pohodlí', 'podložka, ručník a pohodlné oblečení.')]),
        'faq': [('Jakou činku si koupit na začátek?', 'Nastavitelná sada nebo dva páry činek 2 až 8 kg pro základní cviky.')],
    },
    'sportovni-vyziva': {
        'guide': G('Jak vybrat sportovní výživu', 'Doplňky nenahradí pestrou stravu. Vybírejte podle cíle: regenerace, růst svalů, energie při výkonu.',
                   [('Protein', 'syrovátkový se rychle vstřebává, kaseinový pomaleji a hodí se na noc, rostlinné směsi jsou bez laktózy.'),
                    ('Energie', 'gely, tyčinky a iontové nápoje při delším výkonu.'),
                    ('Kreatin', 'nejlépe prozkoumaný doplněk na sílu; stačí monohydrát.')],
                   'Před dlouhodobým užíváním doplňků se poraďte s lékařem nebo výživovým poradcem.'),
        'faq': [('Jaký protein vybrat?', 'Pro většinu lidí je volbou syrovátkový koncentrát nebo izolát; při nesnášenlivosti laktózy rostlinný protein.')],
    },
    'plavky': {
        'guide': G('Jak vybrat plavky', 'Plavky na bazén jsou odolnější proti chloru a lépe drží tvar, plážové jsou pohodlné a vzorované. Velikost zkoušejte i v sedě.',
                   [('Bazén', 'materiál s chlorovzdorností (např. polyester) vydrží víc plavání.'),
                    ('Střih', 'sportovní střih drží při pohybu, plážové jsou volnější.')]),
        'faq': [('Jaké plavky na plavání?', 'Sportovní jednodílné nebo pevné plavky z chlorovzdorného materiálu.')],
    },
    'kopacky': {
        'guide': G('Jak vybrat kopačky', 'Kopačky se liší podle povrchu: lisovky na přírodní trávu, turfy a halovky na umělku a sál. Špatný typ znamená horší stabilitu a vyšší riziko zranění.',
                   [('Lisovky (FG/SG)', 'na přírodní trávu, SG s vyměnitelnými kolíky na měkký terén.'),
                    ('Umělka (AG, TF)', 'na umělou trávu a antuku.'),
                    ('Dětské', 'rostoucí noha potřebuje rezervu, počítejte s výměnou každou sezónu.')]),
        'faq': [('Jaké kopačky na umělku?', 'Označení AG nebo TF; lisovky FG na umělce rychle ničí podrážku.')],
    },
    'barefoot-obuv': {
        'guide': G('Jak vybrat barefoot boty', 'Barefoot boty mají širokou špičku, tenkou podešev bez klopení a minimální tlumení. Chodidlo se v nich chová přirozeněji, ale na přechod je potřeba čas.',
                   [('Šířka', 'prsty se mají rozevírat, špička je široká.'),
                    ('Podrážka', 'tenká a pružná, 3 až 8 mm; silnější je kompromis pro město.'),
                    ('Přechod', 'noste je zpočátku jen krátce a postupně přidávejte.')]),
        'faq': [('Jsou barefoot boty vhodné pro každého?', 'Většině zdravých lidí vyhovují, ale přechod má být postupný. S potížemi chodidel se poraďte s lékařem.')],
    },
    'jizdni-kola': {
        'guide': G('Jak vybrat jízdní kolo', 'Kolo vybírejte podle terénu, ve kterém budete jezdit nejčastěji. Správná velikost rámu je důležitější než výbava.',
                   [('Horské', 'do lesa, s odpružením a širokými pláštěmi.'),
                    ('Silniční a gravel', 'rychlé na asfaltu; gravel zvládne i polňačky.'),
                    ('Trekové a městské', 'komfortní, s blatníky a nosičem.'),
                    ('Velikost', 'řiďte se výškou postavy a velikostní tabulkou výrobce.')]),
        'faq': [('Jak vybrat velikost rámu?', 'Podle výšky postavy a délky nohou v tabulce výrobce; nejlepší je krátká zkušební jízda.')],
    },
    'elektrokola': {
        'guide': G('Jak vybrat elektrokolo', 'U elektrokola rozhoduje motor, baterie a to, kde pojedete. Dojezd závisí na terénu, váze jezdce a stupni asistence.',
                   [('Motor', 'středový motor má lepší rozložení váhy a hodí se do kopců, motor v zadním náboji je jednodušší a levnější.'),
                    ('Baterie', 'kapacita v Wh určuje dojezd: 400 až 500 Wh na běžné okruhy, víc na horské túry.'),
                    ('Využití', 'město, trekking nebo horské, rám i výbava se liší.')]),
        'faq': [('Jaký dojezd má elektrokolo?', 'Podle baterie a terénu zhruba 40 až 120 km. Záleží na stupni asistence a profilu trasy.')],
    },
}


def write(db, tree):
    """Fill guide_html / faq_json for the categories we have texts for; returns the number of categories written."""
    n = 0
    for slug, t in TEXTY.items():
        row = db.execute('SELECT id FROM categories WHERE slug = ?', (slug,)).fetchone()
        if not row:
            continue
        db.execute('UPDATE categories SET guide_html = ?, faq_json = ? WHERE id = ?',
                   (t['guide'], json.dumps([{'q': q, 'a': a} for q, a in t.get('faq', [])], ensure_ascii=False), row[0]))
        n += 1
    return n
