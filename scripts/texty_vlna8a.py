"""sporteka.cz — winter: poles, socks, accessories hub, skates hub (3. 11. 2026). General true facts only, no prices.
Search phrases from Marketing Miner (cs, 11/2026). Brands from the live catalogue. Short entries."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

NEW['lyzarske-hole'] = dict(short=True,
    title='Lyžařské hole – sjezdové, běžecké a skialpové | Sporteka',
    desc='Lyžařské hole pro sjezd, běžky i skialp, dětské i pro dospělé. Porovnejte ceny a délky v českých obchodech a vyberte hole podle výšky.',
    intro='<p><strong>Lyžařské hole</strong> pomáhají s rovnováhou, rytmem zatáčení a u běžek i s pohonem. Správná délka a lehký, pevný materiál rozhodují o pohodlí celého dne. Vybírejte podle výšky a disciplíny.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů. K holím patří <a href="/sjezdove-lyze/">lyže</a> a <a href="/lyzarske-rukavice/">rukavice</a>, pro běžky také <a href="/bezecke-lyzovani/">běžecké vybavení</a>.</p>',
    guide='<h2>Jak vybrat lyžařské hole</h2>'
          '<p>Hlavní je délka. U sjezdových holí postavte hůl vzhůru nohama za košík, chyťte pod ním rukojeť a loket by měl svírat zhruba pravý úhel. Běžecké hole jsou delší a sjezdové kratší, proto je nevyměňujte.</p>'
          '<h3>Délka podle výšky u sjezdových holí</h3>'
          + T(['Výška lyžaře', 'Orientační délka hole'], [['140 cm', '100 cm'], ['150 cm', '105–110 cm'], ['160 cm', '110–115 cm'], ['170 cm', '115–120 cm'], ['180 cm', '120–125 cm'], ['190 cm', '125–130 cm']]) +
          '<h3>Materiál</h3>'
          '<ul><li><strong>Hliník:</strong> pevný, odolný a cenově dostupný, vhodný pro rekreační jízdu.</li>'
          '<li><strong>Karbon:</strong> lehčí a tužší, ocení ho náročnější jezdci a běžkaři.</li>'
          '<li><strong>Kompozit:</strong> kombinace, kompromis mezi hmotností a cenou.</li></ul>'
          '<h3>Typy holí</h3>'
          '<p>Sjezdové hole mají zahnutou rukojeť a malý košík. Běžecké bývají delší, lehčí a mají větší košík a poutko, které drží ruku. Skialpové a teleskopické hole se dají zkrátit na sjezd a prodloužit na stoupání.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou hole značek {B(("komperdell", "Komperdell"), ("head", "Head"), ("leki", "Leki"), ("oneway", "OneWay"), ("rossignol", "Rossignol"), ("swix", "Swix"), ("atomic", "Atomic"))}.</p>'
          '<h3>Časté chyby</h3>'
          '<p>Nejčastěji se kupují hole příliš dlouhé „na jistotu“, ve kterých jsou ramena zbytečně zvednutá. U dětí je lepší raději kratší hole než ty na vyrůstání.</p>'
          '<h3>Péče</h3>'
          '<p>Po jízdě hole osušte, zkontrolujte poutko a košík a nenechávejte teleskopické mechanismy zamrzlé.</p>',
    faq=[('Jak dlouhé lyžařské hole vybrat?', 'Postavte hůl vzhůru nohama, chyťte pod košíkem a loket by měl svírat pravý úhel.'),
         ('Jsou běžecké a sjezdové hole stejné?', 'Ne. Běžecké jsou delší a lehčí, sjezdové kratší s menším košíkem.'),
         ('Hliník, nebo karbon?', 'Hliník je odolný a levnější, karbon lehčí a tužší. Rekreačním jezdcům stačí hliník.'),
         ('Jak vybrat hole pro dítě?', 'Podle výšky dítěte, raději kratší než příliš dlouhé.'),
         ('Co jsou teleskopické hole?', 'Hole s nastavitelnou délkou, užitečné na skialp a túry.')],
)

NEW['lyzarske-ponozky'] = dict(short=True,
    title='Lyžařské ponožky – merino a funkční ponožky | Sporteka',
    desc='Lyžařské ponožky pro sjezd, běžky i snowboard, merino i syntetika. Porovnejte ceny a velikosti v českých obchodech a vyberte ponožky do bot.',
    intro='<p><strong>Lyžařské ponožky</strong> jsou tenké, vysoké a udržují nohu v suchu a teple. V lyžácích je málo místa, takže špatná ponožka vede k otlakům a studeným prstům. Dvě vrstvy nebo bavlna jsou častá chyba.</p>'
          '<p>Na Sportece porovnáte nabídku českých obchodů. K ponožkám patří <a href="/lyzarske-boty/">boty</a> a <a href="/lyzarske-termopradlo/">termoprádlo</a>.</p>',
    guide='<h2>Jak vybrat lyžařské ponožky</h2>'
          '<p>Ponožka má sahat nad horní okraj boty, aby se okraj nedřel o holeň. Švy by měly být ploché a ponožka v botě nesmí dělat záhyby. Vybírejte podle velikosti nohy a tloušťky určené pro lyžařské boty.</p>'
          '<h3>Materiál</h3>'
          '<ul><li><strong>Merino:</strong> hřeje i vlhké a méně zapáchá, hodí se na celodenní jízdu.</li>'
          '<li><strong>Syntetika:</strong> rychle schne a je odolná, vhodná pro aktivní jezdce.</li>'
          '<li><strong>Směs s elastanem:</strong> lépe drží tvar a nesjíždí.</li></ul>'
          '<h3>Tloušťka a vyztužení</h3>'
          '<p>Pro sjezdové boty stačí tenčí až střední ponožky se zesílením na holeni a patě. Do běžeckých bot patří tenčí, do snowboardových střední. Příliš silná ponožka tlačí a krevní oběh se zhorší.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou značky {B(("lasting", "Lasting"), ("smartwool", "Smartwool"), ("icebreaker", "Icebreaker"), ("relax", "Relax"), ("rossignol", "Rossignol"), ("accezzi", "Accezzi"), ("falke", "Falke"))}.</p>'
          '<h3>Časté chyby</h3>'
          '<p>Nejčastěji lidé oblékají dva páry ponožek pro teplo, ale vlhkost se pak hromadí a nohy studí. Další chybou je bavlněná ponožka, která se promáčí.</p>'
          '<h3>Praní</h3>'
          '<p>Perte podle štítku bez aviváže. Merino a směsi nesušte na radiátoru, aby se nesrazily.</p>',
    faq=[('Jaké ponožky do lyžařských bot?', 'Tenké až střední, vysoké, z merina nebo syntetiky, bez bavlny.'),
         ('Mohu obléknout dvě ponožky?', 'Nedoporučuje se, tlačí a zhoršují prokrvení. Jedna kvalitní ponožka stačí.'),
         ('Jak vysoká má být ponožka?', 'Nad horní okraj boty, aby se okraj nedřel o holeň.'),
         ('Merino, nebo syntetika?', 'Merino méně zapáchá, syntetika rychleji schne.'),
         ('Jak prát lyžařské ponožky?', 'Podle štítku, bez aviváže a mimo radiátor.')],
)

NEW['lyzarske-doplnky'] = dict(short=True,
    title='Lyžařské doplňky – vosky, vaky, chrániče | Sporteka',
    desc='Doplňky pro lyžování: vosky, vaky na lyže a boty, chrániče a drobnosti na hory. Porovnejte ceny v českých obchodech a vyberte vybavení na svah.',
    intro='<p><strong>Lyžařské doplňky</strong> nenahradí lyže ani boty, ale zlepšují péči o výbavu a pohodlí na svahu. Patří sem vosky na skluznice, vaky a tašky pro přepravu a další drobné pomůcky.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů. Základní vybavení najdete v kategoriích <a href="/zimni-sporty/">Zimní sporty</a>, <a href="/sjezdove-lyze/">sjezdové lyže</a> a <a href="/lyzarske-boty/">boty</a>.</p>',
    guide='<h2>Jak vybrat lyžařské doplňky</h2>'
          '<p>Doplňky se vybírají podle toho, co potřebujete řešit: přepravu, péči o skluznici nebo ochranu. Začněte tím, co se vám při lyžování nejvíc hodí a co už máte.</p>'
          '<h3>Hlavní skupiny</h3>'
          '<ul><li><a href="/lyzarske-vosky/">Vosky</a>: zlepšují klouzavost a chrání skluznici.</li>'
          '<li><a href="/lyzarske-vaky-a-tasky/">Vaky a tašky</a>: ochrana při přepravě lyží, snowboardu a bot.</li>'
          '<li>Chrániče a ochranné prvky: pro děti a začátečníky na svahu.</li>'
          '<li>Pomůcky pro údržbu: škrabky, kartáče, pásky na lyže.</li></ul>'
          '<h3>Co se hodí na první výjezd</h3>'
          '<p>Pásek na spojení lyží usnadní přenášení, zámek lyží zabrání krádeži a obal na boty ochrání vnitřek tašky před vlhkem. Přidejte kapesní vosk nebo sprej.</p>'
          '<h3>Servis před sezónou</h3>'
          '<p>Před zimou zkontrolujte lyže, hrany a vázání, případně využijte servis. Doplňky na údržbu se hodí těm, kdo si chtějí péči zajistit sami.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Najdete zde značky {B(("swix", "Swix"), ("toko", "Toko"), ("holmenkol", "Holmenkol"), ("rossignol", "Rossignol"), ("dynafit", "Dynafit"), ("head", "Head"))}.</p>'
          '<h3>Časté chyby</h3>'
          '<p>Lidé často koupí vosk bez teplotního označení nebo vak, do kterého se lyže nevejdou. Před nákupem změřte délku lyží a přečtěte popis výrobce.</p>',
    faq=[('Jaké doplňky k lyžím potřebuji?', 'Základem je vak na přepravu a vosk. K tomu pásek na lyže a ochrana pro děti.'),
         ('Kolik stojí údržba lyží?', 'Cenu určuje servis a typ. Domácí voskování vyžaduje vosk, žehličku a škrabku.'),
         ('Co patří do výbavy začátečníka?', 'Lyže, boty, hole, helma, brýle a ochrana kolen nebo zad.'),
         ('Potřebuji vak na lyže?', 'Chrání lyže při přepravě a usnadňuje nošení, hlavně v autě nebo ve vlaku.'),
         ('Kdy lyže voskovat?', 'Před sezónou a podle používání během zimy.')],
)

NEW['brusle'] = dict(short=True,
    title='Brusle – lední, hokejové, krasobrusle, inline | Sporteka',
    desc='Brusle pro děti i dospělé: rekreační lední, hokejové, krasobrusle a inline. Porovnejte ceny a velikosti v českých obchodech a vyberte brusle na led.',
    intro='<p><strong>Brusle</strong> se liší podle toho, kde a jak bruslíte. Na kluziště se hodí rekreační lední brusle, pro hokej hokejové, pro piruety krasobrusle a na asfalt inline brusle. Vybírejte podle povrchu, velikosti a úrovně.</p>'
          '<p>Na Sportece najdete nabídku českých obchodů rozdělenou do kategorií: <a href="/rekreacni-brusle/">rekreační brusle</a>, <a href="/hokejove-brusle/">hokejové</a>, <a href="/krasobruslarske-brusle/">krasobruslařské</a> a <a href="/inline-brusle/">inline brusle</a>.</p>',
    guide='<h2>Jak vybrat brusle</h2>'
          '<p>Nejdřív určete, kde budete bruslit. Lední brusle mají ocelový nůž a nesmí se používat na tvrdém povrchu, inline mají kolečka a hodí se na asfalt. Potom zvolte velikost, tvar boty a úroveň podpory.</p>'
          '<h3>Typy bruslí</h3>'
          '<ul><li><strong>Rekreační lední:</strong> pohodlné boty pro bruslení na kluzišti, pro děti často nastavitelná velikost.</li>'
          '<li><strong>Hokejové:</strong> pevná bota s oporou kotníku a krátkým nožem pro rychlé změny směru.</li>'
          '<li><strong>Krasobruslařské:</strong> vyšší bota a nůž se zoubky na špičce pro skoky a piruety.</li>'
          '<li><strong>Inline:</strong> bota s kolečky pro bruslení venku.</li></ul>'
          '<h3>Velikost</h3>'
          '<p>Brusle by měly sedět pevně v patě a prsty mají mít jen malou rezervu. Zkoušejte je v tenké ponožce. Značky mohou mít různé velikostní řady, proto se řiďte tabulkou výrobce.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou značky {B(("tempish", "Tempish"), ("sulov", "Sulov"), ("winnwell", "Winnwell"), ("roces", "Roces"), ("fila", "Fila"), ("botas", "Botas"), ("powerslide", "Powerslide"))}.</p>'
          '<h3>Bezpečnost</h3>'
          '<p>Při bruslení se hodí helma a chrániče, hlavně pro děti a začátečníky. Led na rybníku vždy ověřte, jestli je dost silný a bezpečný.</p>'
          '<h3>Péče</h3>'
          '<p>Nůž po každém použití osušte a nasaďte ochranný kryt. Brusle skladujte větrané, ne v uzavřeném plastu.</p>',
    faq=[('Jaké brusle koupit na rekreační bruslení?', 'Pohodlné lední brusle přesně padnoucí s oporou kotníku.'),
         ('Čím se liší hokejové a krasobruslařské brusle?', 'Hokejové mají kratší nůž, krasobruslařské delší se zoubky na špičce.'),
         ('Mohu v ledních bruslích chodit po zemi?', 'Jen s ochranným krytem na noži, jinak se nůž poškodí.'),
         ('Jak poznám správnou velikost brusle?', 'Pata sedí pevně, prsty se lehce dotýkají špičky a nic netlačí.'),
         ('Jsou inline a lední brusle zaměnitelné?', 'Ne, určení je odlišné: inline jedou po asfaltu, lední po ledu.')],
)
