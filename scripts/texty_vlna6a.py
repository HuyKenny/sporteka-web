"""sporteka.cz — texts of the winter section (3. 11. 2026): hub, clothing, skis, boots, helmets, goggles, snowboard, cross-country, ski touring.
Same rules as texty_vlna1a.py: general true facts, no prices, no superlatives, no invented statistics. Brands come from the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

NEW['zimni-sporty'] = dict(
    title='Zimní sporty – lyže, snowboardy, oblečení | Sporteka',
    desc='Vybavení na zimu: sjezdové a běžecké lyže, snowboardy, lyžařské oblečení, boty, helmy a brýle. Porovnejte ceny a velikosti skladem v českých obchodech.',
    intro='<p><strong>Zimní sporty</strong> potřebují vybavení, které vydrží mráz, vlhko i pád. Základ tvoří <a href="/sjezdove-lyze/">sjezdové lyže</a> nebo <a href="/snowboarding/">snowboard</a>, '
          '<a href="/lyzarske-boty/">boty</a>, <a href="/lyzarske-helmy/">helma</a> a <a href="/lyzarske-bryle/">brýle</a>. Stejně důležité je <a href="/lyzarske-obleceni/">oblečení</a>: bunda, kalhoty, rukavice a spodní vrstva rozhodují o tom, '
          'jestli vás zima na svahu bude bavit. Kdo se vydává do stopy, vybere <a href="/bezecke-lyzovani/">běžecké lyžování</a>, kdo do kopců <a href="/skialpinismus/">skialpinismus</a>.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů u stejného zboží, uvidíte slevy a skladové velikosti. Výběr zúžíte podle značky, velikosti, délky lyží nebo vodního sloupce u bund.</p>',
    guide='<h2>Jak se vybavit na zimní sezónu</h2>'
          '<p>Nejdřív si ujasněte, co budete dělat. Sjezdovka, stopa a skialpový výstup mají jiné nároky na vybavení i rozpočet. Pro začátek se vyplatí koupit věci, na kterých záleží bezpečnost a pohodlí: boty, helmu a oblečení. Lyže a snowboard si můžete nejdřív půjčit.</p>'
          '<h3>Co kam patří</h3>'
          + T(['Aktivita', 'Základ výbavy', 'Kam kliknout'], [['Sjezdové lyžování', 'lyže s vázáním, boty, hole, helma, brýle', '<a href="/sjezdove-lyze/">sjezdové lyže</a>, <a href="/lyzarske-boty/">boty</a>, <a href="/lyzarske-hole/">hole</a>'], ['Snowboarding', 'snowboard s vázáním, boty, helma, brýle, chrániče', '<a href="/snowboardy/">snowboardy</a>, <a href="/snowboardove-boty/">boty</a>'], ['Běžky', 'lyže, boty, vázání, hole, vosky', '<a href="/bezecke-lyze/">běžecké lyže</a>, <a href="/bezecke-boty/">boty na běžky</a>'], ['Skialpinismus', 'lehké lyže, pásy, boty s režimem chůze, lavinová výbava', '<a href="/skialpinismus/">skialpinismus</a>']]) +
          '<h3>Vrstvení oblečení</h3>'
          '<ul><li><strong>Spodní vrstva:</strong> přiléhavé <a href="/lyzarske-termopradlo/">termoprádlo</a> odvádí pot od těla. Bavlna se nehodí, nasákne a ochlazuje.</li>'
          '<li><strong>Střední vrstva:</strong> fleece nebo lehká izolace, která drží teplo.</li>'
          '<li><strong>Vrchní vrstva:</strong> <a href="/lyzarske-bundy/">bunda</a> a <a href="/lyzarske-kalhoty/">kalhoty</a> s membránou chrání před větrem a mokrým sněhem.</li>'
          '<li><strong>Doplňky:</strong> <a href="/lyzarske-rukavice/">rukavice</a>, <a href="/lyzarske-ponozky/">ponožky</a>, <a href="/lyzarske-cepice-a-nakrcniky/">čepice a nákrčníky</a>.</li></ul>'
          '<h3>Bezpečnost</h3>'
          '<p>Helma je dnes samozřejmost, u dětí povinná. Hledejte certifikaci a ověřte velikost podle obvodu hlavy. K ochraně patří také <a href="/snowboardove-chranice/">chrániče zad a boků</a> a při jízdě mimo sjezdovku lavinová výbava a znalost terénu.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V zimním sortimentu najdete {B(("rossignol", "Rossignol"), ("head", "Head"), ("fischer", "Fischer"), ("atomic", "Atomic"), ("salomon", "Salomon"), ("alpina", "Alpina"), ("swix", "Swix"), ("uvex", "Uvex"))} a další. '
          'Každá značka má silnější stránku, třeba běžecké lyže, helmy nebo oblečení, proto se vyplatí hledat podle potřeby, ne podle loga.</p>'
          '<h3>Kdy kupovat</h3>'
          '<p>Nejvíc zboží se rozprodává po vánocích a v únoru. V listopadu jsou nejlépe skladem velikosti, ale ceny bývají vyšší. Lyže a snowboardy předchozí sezóny mají většinou stejné parametry za nižší cenu.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Koupě lyžáků o číslo menších kvůli „lepšímu držení“. Bota má sedět, ne bolet.</li>'
          '<li>Příliš dlouhé lyže pro začátečníka. Hůř se ovládají a zbytečně unavují.</li>'
          '<li>Bunda bez membrány při mokrém sněhu. Za hodinu promokne.</li></ul>',
    faq=[('Co potřebuji na první lyžování?', 'Lyžařské boty, lyže s vázáním, hole, helmu, brýle, bundu, kalhoty, rukavice a termoprádlo. Lyže a boty lze na začátku půjčit, helmu a oblečení raději mít vlastní.'),
         ('Jak vybrat velikost lyží?', 'Podle výšky, hmotnosti a úrovně. Začátečníci volí kratší lyže zhruba po bradu až nos, pokročilí delší. Přesné hodnoty udává tabulka výrobce.'),
         ('Kdy se vyplatí kupovat lyžařské vybavení?', 'Po vánocích a na konci sezóny bývají slevy nejvyšší. Modely předchozí sezóny mají obvykle stejné parametry za nižší cenu.'),
         ('Co je vodní sloupec u lyžařské bundy?', 'Udává odolnost látky proti tlaku vody v milimetrech. Pro suchý sníh stačí kolem 5 000 mm, do mokrého počasí se hodí 10 000 mm a víc.'),
         ('Jak se obléknout na lyže?', 'Po vrstvách: termoprádlo, fleece nebo izolace a bunda s membránou. Nenoste bavlnu, nasákne potem a ochlazuje.'),
         ('Je lepší lyže, nebo snowboard?', 'Záleží na stylu. Lyže se rychleji učí a jsou univerzálnější, snowboard je oblíbený u freestylu a freeridu. Můžete začít půjčením obojího.'),
         ('Hodí se zimní vybavení pro děti k rozprodeji?', 'Ano, děti rychle rostou, takže vybavení z loňské sezóny je zajímavá volba. U helmy a bot ovšem dbejte na správnou velikost, ne na vyrůstání.'),
         ('Jak pečovat o lyže po sezóně?', 'Očistěte skluznici, naneste konzervační vosk a uložte na suchém místě bez zatížení. Hrany ošetřete a vázání nechte před sezónou zkontrolovat v servisu.')],
)

NEW['lyzarske-obleceni'] = dict(short=True,
    title='Lyžařské a snowboardové oblečení | Porovnání cen',
    desc='Lyžařské oblečení: bundy, kalhoty, kombinézy, rukavice, termoprádlo, čepice a ponožky. Porovnejte ceny a velikosti v českých obchodech.',
    intro='<p><strong>Lyžařské a snowboardové oblečení</strong> má držet teplo, odvádět pot a nepustit dovnitř vodu. Pomáhá vrstvení: <a href="/lyzarske-termopradlo/">termoprádlo</a> na tělo, lehká izolace uprostřed '
          'a <a href="/lyzarske-bundy/">bunda</a> s <a href="/lyzarske-kalhoty/">kalhotami</a> navrch. Děti často nosí <a href="/lyzarske-kombinezy/">kombinézu</a>, dospělí na rozdíl od nich dvoudílný komplet. K tomu patří '
          '<a href="/lyzarske-rukavice/">rukavice</a>, <a href="/lyzarske-ponozky/">ponožky</a> a <a href="/lyzarske-cepice-a-nakrcniky/">čepice a nákrčníky</a>.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů a výběr zúžíte podle pohlaví, velikosti, značky a vodního sloupce.</p>',
    guide='<h2>Jak vybrat lyžařské oblečení</h2>'
          '<p>Většina chyb vzniká tím, že se kupuje jen bunda a pod ní se nosí bavlněné tričko. Kdo se potí v mokrém, zmrzne dřív než ten, kdo má správnou spodní vrstvu.</p>'
          '<h3>Parametry, které stojí za pozornost</h3>'
          + T(['Parametr', 'Co znamená', 'Orientačně'], [['Vodní sloupec', 'odolnost proti mokru', '5 000 mm suchý sníh, 10 000 mm běžně, 20 000 mm mokro'], ['Prodyšnost', 'odvod vlhkosti zevnitř', 'vyšší hodnota při aktivní jízdě'], ['Zateplení', 'izolační vrstva', 'tenká pro aktivní jízdu, silnější pro vleky a mráz'], ['Sníh. zástěra, kapuce', 'ochrana před sněhem a větrem', 'důležité pro snowboard a freeride']]) +
          '<h3>Střih a velikost</h3>'
          '<p>Bunda má být tak velká, aby se pod ni vešla střední vrstva a nesvírala v ramenou. Kalhoty se vybírají podle pasu a délky nohavic, u snowboardu bývají volnější. Dětem pomáhá nastavitelný pas a nohavice, vydrží víc sezón.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Největší výběr nabízejí {B(("rossignol", "Rossignol"), ("dare2b", "Dare 2b"), ("trespass", "Trespass"), ("helly-hansen", "Helly Hansen"), ("kilpi", "Kilpi"), ("protest", "Protest"), ("picture", "Picture"), ("loap", "Loap"))}. '
          'Některé jsou silné v lyžování, jiné ve snowboardu a streetovém stylu, takže se dívejte na účel.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš těsná bunda. Pod ní nezbývá místo pro vrstvu a omezuje pohyb.</li>'
          '<li>Rukavice bez možnosti utáhnout manžetu. Dovnitř se dostane sníh.</li>'
          '<li>Dětský komplet o dvě čísla větší. Zadrhává se a dítě se v něm špatně hýbe.</li></ul>'
          '<h3>Péče</h3>'
          '<p>Membránové oblečení perte na 30 °C bez aviváže, která zalepuje póry. Impregnaci obnovte sprejem nebo praním s impregnačním přípravkem.</p>',
    faq=[('Jak vybrat lyžařskou bundu?', 'Podle vodního sloupce, zateplení a střihu. Pod bundu musí zbýt místo na střední vrstvu, ale nesmí být příliš volná.'),
         ('Jaký vodní sloupec na lyže?', 'Pro suchý sníh stačí kolem 5 000 mm, běžně se volí 10 000 mm, do mokrého počasí 20 000 mm a víc.'),
         ('Jak se obléknout na lyže?', 'Termoprádlo, fleece nebo lehká izolace a bunda s membránou. Bavlna na tělo nepatří.'),
         ('Kombinéza, nebo dvoudílný komplet?', 'Kombinéza je teplejší a nenechá sníh pod bundu, dvoudílný komplet je praktičtější pro dospělé.'),
         ('Jak prát lyžařské oblečení?', 'Na 30 °C bez aviváže, podle štítku. Impregnaci obnovte sprejem nebo přípravkem do pračky.'),
         ('Jaké oblečení pro děti?', 'Nepromokavý komplet nebo kombinéza s nastavitelným pasem a nohavicemi. Pod to funkční prádlo a fleece.')],
)

NEW['lyzarske-bundy'] = dict(short=True,
    title='Lyžařské bundy – pánské, dámské, dětské | Sporteka',
    desc='Lyžařské a snowboardové bundy: pánské, dámské a dětské. Porovnejte ceny, vodní sloupec a velikosti skladem v českých obchodech.',
    intro='<p><strong>Lyžařská bunda</strong> musí hřát, nepropustit vodu a zároveň prodýchávat. Rozhoduje vodní sloupec, zateplení a střih. Pro sjezdovku se hodí zateplená bunda s kapucí a sněžnou zástěrou, '
          'na <a href="/bezecke-lyzovani/">běžky</a> tenčí bunda do větru, na skialpinismus lehká izolační vrstva. Další bundy do města najdete mezi <a href="/zimni-bundy/">zimními bundami</a>.</p>'
          '<p>Na Sportece porovnáte ceny lyžařských bund z českých obchodů a vidíte velikosti, které jsou skladem. Hledejte podle pohlaví, značky a vodního sloupce.</p>',
    guide='<h2>Jak vybrat lyžařskou bundu</h2>'
          '<p>Bunda je nejviditelnější a často nejdražší kus oblečení. Při výběru sledujte pět věcí a nenechte se zlákat jen barvou.</p>'
          '<h3>Vodní sloupec a prodyšnost</h3>'
          + T(['Vodní sloupec', 'Pro koho'], [['5 000 mm', 'suchý sníh, rekreační lyžování'], ['10 000 mm', 'běžné podmínky, většina lyžařů'], ['15 000–20 000 mm a více', 'mokrý sníh, freeride, snowboard']]) +
          '<h3>Zateplení</h3>'
          '<ul><li><strong>Zateplená bunda:</strong> hřeje i při vleku, vhodná pro mráz.</li>'
          '<li><strong>Bunda bez zateplení (shell):</strong> volíte teplo podle střední vrstvy, univerzální na celou sezónu.</li>'
          '<li><strong>Softshell:</strong> pružný a prodyšný, na aktivní jízdu a běžky.</li></ul>'
          '<h3>Funkce, které se hodí</h3>'
          '<p>Sněhová zástěra, kapuce na helmu, větrací zipy v podpaží, kapsa na skipas a utahování manžet. Větrání pomůže při stoupání nebo na slunci.</p>'
          '<h3>Střih a velikost</h3>'
          '<p>Bunda má sedět tak, aby pod ni šla fleecová vrstva. Rukávy zasahují přes zápěstí a po zvednutí rukou nesmí odhalit záda. Pánské a dámské střihy se liší, dětské se vybírají podle výšky.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Nabídku tvoří {B(("rossignol", "Rossignol"), ("dare2b", "Dare 2b"), ("trespass", "Trespass"), ("helly-hansen", "Helly Hansen"), ("kilpi", "Kilpi"), ("protest", "Protest"), ("siroko", "Siroko"), ("picture", "Picture"), ("loap", "Loap"))}.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Nízký vodní sloupec do mokrého počasí. Bunda začne propouštět na rukávech a ramenou.</li>'
          '<li>Příliš těsný střih. Bunda se stáhne a omezuje pohyb při jízdě.</li>'
          '<li>Dětská bunda o dvě čísla větší. Zachytává se o hole a lyže.</li></ul>'
          '<h3>Péče</h3>'
          '<p>Perte bez aviváže, na 30 °C. Po několika prání obnovte impregnaci sprejem. Před uskladněním bundu vysušte a uložte volně.</p>',
    faq=[('Jaká lyžařská bunda je nejlepší?', 'Taková, která odpovídá vašim podmínkám: pro většinu lyžařů stačí vodní sloupec 10 000 mm, zateplení podle teploty a střih s místem pro fleece.'),
         ('Jaký vodní sloupec má mít lyžařská bunda?', 'Pro suchý sníh kolem 5 000 mm, běžně 10 000 mm, do mokrého počasí 15 000–20 000 mm a víc.'),
         ('Zateplená bunda, nebo shell?', 'Zateplená je pohodlná a hřeje bez dalších vrstev, shell nabízí flexibilitu podle počasí.'),
         ('Jak vybrat dámskou lyžařskou bundu?', 'Dámský střih je užší v pase a boky, hledejte kapuci na helmu a sněhovou zástěru.'),
         ('Jakou bundu pro dítě?', 'Nepromokavou, s nastavitelnými manžetami a reflexními prvky. Vybírejte podle výšky, ne s velkou rezervou.'),
         ('Jak prát lyžařskou bundu?', 'Na 30 °C bez aviváže. Impregnaci obnovte sprejem, ať voda dál stéká po povrchu.')],
)

NEW['lyzarske-kalhoty'] = dict(short=True,
    title='Lyžařské kalhoty – pánské, dámské, dětské | Sporteka',
    desc='Lyžařské a snowboardové kalhoty: pánské, dámské i dětské, s membránou i zateplené. Porovnejte ceny a velikosti v českých obchodech.',
    intro='<p><strong>Lyžařské kalhoty</strong> chrání před sněhem, větrem a mokrem. Vybírejte podle vodního sloupce, zateplení a střihu. Pro sjezdovku se hodí zateplené kalhoty s lyžařskou manžetou, '
          'pro snowboard volnější střih, pro <a href="/bezecke-lyzovani/">běžky</a> pružné kalhoty do větru. K nim patří <a href="/lyzarske-bundy/">bunda</a> a <a href="/lyzarske-termopradlo/">termoprádlo</a>.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů a výběr zúžíte podle velikosti, značky a ceny.</p>',
    guide='<h2>Jak vybrat lyžařské kalhoty</h2>'
          '<p>Kalhoty zatíží kolena a zadek nejvíc, takže záleží na odolnosti a vodním sloupci. Pro běžnou jízdu stačí 10 000 mm, při pádech do mokrého sněhu 15 000 mm a víc.</p>'
          '<h3>Typy</h3>'
          '<ul><li><strong>Zateplené:</strong> do mrazu a na vlek, ale hřejí i při chůzi.</li>'
          '<li><strong>Shell bez zateplení:</strong> kombinujete je s teplým prádlem, vhodné na celou sezónu.</li>'
          '<li><strong>Kalhoty s náprsenkou (bib):</strong> chrání záda a nedovolí sníh pod bundu.</li></ul>'
          '<h3>Střih a funkce</h3>'
          '<p>Lyže vyžadují přiléhavější střih, snowboard volnější a pevnější koleno. Dobré kalhoty mají zesílené nohavice, sněhovou manžetu, větrací zipy a nastavitelný pas.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Nabídku tvoří {B(("rossignol", "Rossignol"), ("kilpi", "Kilpi"), ("dare2b", "Dare 2b"), ("helly-hansen", "Helly Hansen"), ("northfinder", "Northfinder"), ("protest", "Protest"), ("cmp", "CMP"), ("siroko", "Siroko"), ("loap", "Loap"))}.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš dlouhé nohavice, které se zadírají do lyžáků.</li><li>Kalhoty bez zesílení na kolenou a lemu, rychle se rozedřou.</li></ul>'
          '<p>Perte je na 30 °C a obnovujte impregnaci. Dětské kalhoty kupujte podle výšky, s nastavitelným pasem.</p>',
    faq=[('Jaké lyžařské kalhoty vybrat?', 'Podle vodního sloupce a zateplení. Pro většinu lyžařů stačí 10 000 mm.'),
         ('Zateplené, nebo ne?', 'Zateplené hřejí i bez vrstvy pod nimi, bez zateplení jsou univerzálnější a kombinují se s prádlem.'),
         ('Co jsou kalhoty s náprsenkou?', 'Jsou to kalhoty se zvýšeným pasem a ramínky, které chrání záda a brání sněhu pod bundou.'),
         ('Jaký střih na snowboard?', 'Volnější a s pevným kolenem. Přiléhavé střihy se hodí hlavně na lyže.'),
         ('Jak vybrat velikost dětských kalhot?', 'Podle výšky a pasu, s nastavitelným pasem a nohavicí vydrží víc sezón.'),
         ('Jak prát lyžařské kalhoty?', 'Na 30 °C bez aviváže, impregnaci obnovte sprejem.')],
)

NEW['lyzarske-rukavice'] = dict(short=True,
    title='Lyžařské rukavice a palčáky | Porovnání cen',
    desc='Lyžařské a snowboardové rukavice a palčáky: pánské, dámské a dětské. Porovnejte ceny a velikosti v českých obchodech.',
    intro='<p><strong>Lyžařské rukavice</strong> jsou nejdůležitější doplněk proti omrzlinám. Prstové rukavice jsou obratnější, <strong>palčáky</strong> teplejší, protože se prsty ohřívají navzájem. '
          'Rozhodujte podle teploty, intenzity jízdy a toho, jestli potřebujete ovládat telefon nebo zip.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů. K rukavicím se hodí <a href="/lyzarske-ponozky/">lyžařské ponožky</a> a <a href="/lyzarske-cepice-a-nakrcniky/">čepice a nákrčníky</a>. Jiné rukavice najdete v kategorii <a href="/sportovni-rukavice/">sportovní rukavice</a>.</p>',
    guide='<h2>Jak vybrat lyžařské rukavice</h2>'
          '<p>Při výběru hledejte membránu proti vodě, izolaci proti mrazu a pevnou dlaň, která při pádu chrání ruku.</p>'
          '<h3>Prstové, nebo palčáky</h3>'
          '<ul><li><strong>Prstové:</strong> přesnější úchop hole, zipu a telefonu.</li>'
          '<li><strong>Palčáky:</strong> teplejší, doporučují se do velkých mrazů a pro děti.</li>'
          '<li><strong>3v1:</strong> vnitřní fleecová rukavice a vnější shell, praktické na celou sezónu.</li></ul>'
          '<h3>Velikost</h3>'
          + T(['Obvod dlaně', 'Velikost'], [['18–20 cm', 'S'], ['20–22 cm', 'M'], ['22–24 cm', 'L'], ['24–26 cm', 'XL']]) +
          '<p>Obvod měřte pod prsty. Rukavice nesmí stahovat a prsty se mají dotýkat konců.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("viking", "Viking"), ("rossignol", "Rossignol"), ("ziener", "Ziener"), ("reusch", "Reusch"), ("reima", "Reima"), ("swix", "Swix"), ("dynafit", "Dynafit"))}.</p>'
          '<p>Mokré rukavice sušte při pokojové teplotě, ne na topení, které poškozuje membránu. Pro děti vezměte náhradní pár.</p>',
    faq=[('Palčáky, nebo prstové rukavice na lyže?', 'Palčáky jsou teplejší, prstové obratnější. Pro velké mrazy a děti se hodí palčáky.'),
         ('Jak vybrat velikost rukavic?', 'Změřte obvod dlaně pod prsty a porovnejte s tabulkou výrobce.'),
         ('Jsou lyžařské rukavice nepromokavé?', 'Většina má membránu. Při dlouhém pobytu ve sněhu zkontrolujte popis a vodní odolnost.'),
         ('Jak sušit rukavice?', 'Při pokojové teplotě, ideálně na větraném místě. Topení a sušička materiál poškozují.'),
         ('Jaké rukavice pro děti?', 'Palčáky s nastavitelnou manžetou a se šňůrkou, nebo prstové s pevným úchopem.'),
         ('Co jsou rukavice 3v1?', 'Skládají se z vnější nepromokavé vrstvy a vnitřní fleecové rukavice. Dají se nosit zvlášť nebo spolu.')],
)

NEW['sjezdove-lyze'] = dict(short=True,
    title='Sjezdové lyže – komplety, dětské, pánské | Sporteka',
    desc='Sjezdové lyže s vázáním i bez: pánské, dámské a dětské. Porovnejte ceny, délky a profil lyží v českých obchodech.',
    intro='<p><strong>Sjezdové lyže</strong> se vybírají podle úrovně, stylu a hmotnosti lyžaře. Pro rekreační lyžování na upravených sjezdovkách se hodí <strong>carvingové</strong> lyže, '
          'pro jízdu mimo sjezdovku širší <strong>freeridové</strong> a pro jednoduchý začátek <a href="/lyze-komplety/">komplety lyží s vázáním</a>. Děti si vyberou z <a href="/detske-lyze/">dětských lyží</a>.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů a výběr zúžíte podle délky, typu a značky. K lyžím patří <a href="/lyzarske-boty/">boty</a>, <a href="/lyzarske-hole/">hole</a> a <a href="/lyzarske-helmy/">helma</a>.</p>',
    guide='<h2>Jak vybrat sjezdové lyže</h2>'
          '<p>Správně zvolená lyže se vybírá podle tří věcí: kde jezdíte, jak dobře lyžujete a kolik vážíte. Nejdražší lyže pro špatného lyžaře nejsou lepší než střední lyže odpovídající jeho úrovni.</p>'
          '<h3>Typ lyží</h3>'
          '<ul><li><strong>Carving:</strong> užší střed, krátký rádius, na upravené sjezdovky.</li>'
          '<li><strong>All-mountain:</strong> univerzální, zvládnou sjezdovku i sníh mimo ni.</li>'
          '<li><strong>Freeride:</strong> široké lyže na prašan a neupravený terén.</li>'
          '<li><strong>Závodní (SL, GS):</strong> tuhé a agresivní pro zkušené lyžaře.</li></ul>'
          '<h3>Délka lyží</h3>'
          + T(['Úroveň', 'Orientační délka'], [['Začátečník', 'od brady po nos'], ['Středně pokročilý', 'od nosu po čelo'], ['Pokročilý', 'zhruba k výšce hlavy'], ['Dítě', 'od ramen po bradu']]) +
          '<p>Přesnou délku určuje výrobce podle hmotnosti. Ženy a lehčí lyžaři volí kratší a měkčí lyže.</p>'
          '<h3>Vázání a komplety</h3>'
          '<p>Komplet už má namontované vázání, takže ušetříte čas a vyhnete se kombinaci, která nepasuje k botám. Vázání musí odpovídat normě bot a nastavuje se podle hmotnosti a úrovně v servisu.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Nabídku tvoří {B(("rossignol", "Rossignol"), ("elan", "Elan"), ("fischer", "Fischer"), ("head", "Head"), ("atomic", "Atomic"), ("blizzard", "Blizzard"), ("salomon", "Salomon"), ("stockli", "Stöckli"))}.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš dlouhé a tuhé lyže pro začátečníka. Hůř se zatáčí.</li>'
          '<li>Nezkontrolované vázání. Před sezónou ho nechte seřídit.</li>'
          '<li>Zapomenuté ošetření. Skluznici je dobré před sezónou navoskovat.</li></ul>',
    faq=[('Jak vybrat délku sjezdových lyží?', 'Podle výšky, hmotnosti a úrovně. Začátečníci volí kratší lyže zhruba po bradu až nos, pokročilí delší.'),
         ('Jaké lyže pro začátečníka?', 'Kratší, měkčí carvingové lyže, ideálně jako komplet s vázáním.'),
         ('Carving, nebo all-mountain?', 'Carving je ideální na upravené sjezdovky, all-mountain se hodí tam, kde lyžujete i mimo upravenou trasu.'),
         ('Jaké lyže pro děti?', 'Dětské lyže s měkčím flexem a jednoduchým vázáním. Vybírejte podle výšky dítěte.'),
         ('Co je komplet lyže s vázáním?', 'Je to lyže s namontovaným vázáním, připravená k jízdě. Seřízení provede servis podle bot.'),
         ('Jak pečovat o lyže?', 'Po sezóně očistit, navoskovat skluznici, ošetřit hrany a uložit na suchém místě.')],
)

NEW['lyzarske-boty'] = dict(short=True,
    title='Lyžařské boty – pánské, dámské, dětské | Sporteka',
    desc='Lyžařské boty pro sjezdové lyžování: pánské, dámské a dětské. Porovnejte ceny, velikost Mondopoint a flex v českých obchodech.',
    intro='<p><strong>Lyžařské boty</strong> rozhodují o tom, jak se vám bude lyžovat. Špatně padnoucí bota bolí a lyže se hůř ovládá, správná naopak přenáší pohyb z nohy na lyži. '
          'Velikost se udává v <strong>Mondopointu</strong> (délka chodidla v cm) a tuhost číslem flexu. Začátečníci a ženy volí měkčí flex, zkušení lyžaři tužší.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů. K botám se hodí <a href="/lyzarske-ponozky/">lyžařské ponožky</a>, <a href="/sjezdove-lyze/">lyže</a> a <a href="/lyzarske-helmy/">helma</a>.</p>',
    guide='<h2>Jak vybrat lyžařské boty</h2>'
          '<p>Boty se nekupují podle čísla běžné obuvi. Změřte si chodidlo a řiďte se Mondopointem, ideálně nechte botu zkontrolovat v servisu.</p>'
          '<h3>Velikost a tvar</h3>'
          + T(['Délka chodidla', 'Mondopoint'], [['25,0 cm', '25'], ['26,0 cm', '26'], ['27,0 cm', '27'], ['28,0 cm', '28']]) +
          '<p>Bota má na patě pevně držet a prsty se jen lehce dotýkat špičky. Šířku skeletu (last) udává výrobce, běžné jsou 98 až 106 mm.</p>'
          '<h3>Flex</h3>'
          '<ul><li><strong>60–80:</strong> začátečníci a děti.</li><li><strong>90–110:</strong> středně pokročilí.</li><li><strong>120 a více:</strong> zkušení lyžaři, tuhá bota.</li></ul>'
          '<h3>Zapínání a výbava</h3>'
          '<p>Přezky jsou standard, BOA systém se utahuje kolečkem. Komfort přidává termoformovaná vložka a režim chůze.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("rossignol", "Rossignol"), ("k2", "K2"), ("head", "Head"), ("fischer", "Fischer"), ("nordica", "Nordica"), ("atomic", "Atomic"), ("salomon", "Salomon"), ("tecnica", "Tecnica"), ("dalbello", "Dalbello"))}.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš velká bota. Noha se hýbe a lyže se hůř ovládá.</li><li>Příliš těsná bota. Tlačí a mrzne v ní.</li></ul>',
    faq=[('Jak vybrat velikost lyžařských bot?', 'Podle délky chodidla v Mondopointu. Bota má držet patu a prsty se jen lehce dotýkají špičky.'),
         ('Co je flex lyžařských bot?', 'Tuhost boty. Nižší hodnota je pro začátečníky a děti, vyšší pro pokročilé.'),
         ('Mohu koupit lyžáky online?', 'Ano, pokud známe přesný Mondopoint a tvar nohy. Při váhání je vhodné botu zkusit v servisu.'),
         ('Jaká šířka boty (last)?', 'Podle šířky chodidla, běžně 98 až 106 mm. Širší noha vyžaduje širší last.'),
         ('Jaké lyžáky pro dítě?', 'Měkčí flex a přezky, které dítě ovládne samo. Velikost nechte raději přesnou než velkou.'),
         ('Jak pečovat o lyžařské boty?', 'Po sezóně vysušit, vyjmout vložky a uložit zapnuté na suchém místě.')],
)

NEW['lyzarske-helmy'] = dict(short=True,
    title='Lyžařské helmy – dětské, pánské, dámské | Sporteka',
    desc='Lyžařské helmy: dětské, dámské i pánské, s MIPS a ventilací. Porovnejte ceny a velikosti skladem v českých obchodech.',
    intro='<p><strong>Lyžařská helma</strong> chrání hlavu při pádu i při střetu. Vybírejte podle <strong>obvodu hlavy</strong>, certifikace a toho, zda se hodí k brýlím. U dětí je helma povinná a měla by sedět přesně, ne s rezervou na vyrůstání.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů. K helmě patří <a href="/lyzarske-bryle/">lyžařské brýle</a> a <a href="/lyzarske-cepice-a-nakrcniky/">čepice a nákrčníky</a>.</p>',
    guide='<h2>Jak vybrat lyžařskou helmu</h2>'
          '<p>Helma musí sedět pevně, ale netlačit. Při předklonu nesmí sjet přes oči a pásek pod bradou se dá utáhnout na dva prsty.</p>'
          '<h3>Velikost podle obvodu hlavy</h3>'
          + T(['Obvod hlavy', 'Velikost'], [['52–55 cm', 'S'], ['55–58 cm', 'M'], ['58–61 cm', 'L'], ['61–64 cm', 'XL']]) +
          '<h3>Technologie</h3>'
          '<ul><li><strong>MIPS:</strong> vrstva, která snižuje rotační síly při nárazu.</li><li><strong>Ventilace:</strong> nastavitelná, hodí se na jaro.</li><li><strong>Audio a kamera:</strong> držáky a možnost sluchátek.</li></ul>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("alpina", "Alpina"), ("uvex", "Uvex"), ("relax", "Relax"), ("smith", "Smith"), ("rossignol", "Rossignol"), ("poc", "POC"), ("head", "Head"), ("salomon", "Salomon"))}.</p>'
          '<p>Po silnějším nárazu helmu vyměňte, i když vypadá v pořádku, a po deseti letech používání ji také nahraďte novou.</p>',
    faq=[('Jak vybrat velikost lyžařské helmy?', 'Podle obvodu hlavy v centimetrech, naměřeného nad obočím. Helma má sedět pevně, ale netlačit.'),
         ('Je lyžařská helma povinná?', 'Pro děti je povinná, pro dospělé ji silně doporučujeme na každém svahu.'),
         ('Co je MIPS?', 'Je to technologie, která snižuje rotační síly při šikmém nárazu. Sníží riziko poranění mozku.'),
         ('Jak často měnit helmu?', 'Po nárazu a po několika letech používání, výrobci obvykle uvádějí pět až deset let.'),
         ('Hodí se helma i na snowboard?', 'Ano, většina lyžařských helem je určena i pro snowboard.'),
         ('Jaká helma pro dítě?', 'Dětská helma s nastavitelným obvodem, přesně padnoucí. Neberte ji větší s rezervou.')],
)

NEW['lyzarske-bryle'] = dict(short=True,
    title='Lyžařské brýle – dětské, dámské, pánské | Sporteka',
    desc='Lyžařské a snowboardové brýle s fotochromatickými i výměnnými zorníky. Porovnejte ceny a dostupnost v českých obchodech.',
    intro='<p><strong>Lyžařské brýle</strong> chrání oči před sluncem, větrem a odleskem sněhu. Rozhoduje kategorie zorníku (světlost), tvar a kompatibilita s helmou. '
          'Světlejší zorník se hodí do mlhy, tmavý na slunce. Dobré brýle nemlží a nejsou příliš těsné.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů a k brýlím vyberete <a href="/lyzarske-helmy/">helmu</a> a <a href="/lyzarske-cepice-a-nakrcniky/">kuklu</a>.</p>',
    guide='<h2>Jak vybrat lyžařské brýle</h2>'
          '<p>Brýle mají pevně sedět na obličeji a navazovat na okraj helmy bez mezery. Při zkoušení je vždy nasaďte s helmou.</p>'
          '<h3>Kategorie zorníku</h3>'
          + T(['Kategorie', 'Podmínky'], [['1', 'mlha, zataženo, večer'], ['2', 'proměnlivé počasí'], ['3', 'slunce, běžná sjezdovka'], ['4', 'vysoké hory, ledovec']]) +
          '<h3>Zorníky a technologie</h3>'
          '<ul><li><strong>Fotochromatické:</strong> mění propustnost podle světla.</li><li><strong>Výměnné:</strong> druhý zorník do mlhy.</li><li><strong>Dvojité s antifogem:</strong> méně mlžení.</li></ul>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("alpina", "Alpina"), ("uvex", "Uvex"), ("rossignol", "Rossignol"), ("relax", "Relax"), ("smith", "Smith"), ("salomon", "Salomon"), ("meatfly", "Meatfly"))}.</p>'
          '<p>Brýle neutírejte suchým hadrem, poškrábete zorník. Používejte měkké pouzdro a osušte je volně na vzduchu.</p>',
    faq=[('Jaké lyžařské brýle vybrat?', 'Podle kategorie zorníku a kompatibility s helmou. Pro proměnlivé počasí fotochromatické nebo výměnné zorníky.'),
         ('Co znamená kategorie zorníku?', 'Číslo od 0 do 4 udává, kolik světla zorník propustí. Vyšší číslo znamená tmavší zorník na slunce.'),
         ('Jak zabránit mlžení brýlí?', 'Nezvedat je na čelo, dopřát jim větrání a vybrat model s antifogem a dvojitým zorníkem.'),
         ('Hodí se lyžařské brýle i na snowboard?', 'Ano, brýle jsou určené pro oba sporty.'),
         ('Jaké brýle pro dítě?', 'Dětský střih s měkkým rámem a UV ochranou, s nastavitelným popruhem.'),
         ('Jak čistit zorník?', 'Měkkou látkou, bez tření, a nechat uschnout na vzduchu.')],
)

NEW['snowboarding'] = dict(short=True,
    title='Snowboarding – snowboardy, boty, vázání | Sporteka',
    desc='Snowboardy, boty, vázání, helmy a oblečení. Porovnejte ceny a velikosti v českých obchodech a vyberte výbavu podle stylu jízdy.',
    intro='<p><strong>Snowboarding</strong> vyžaduje trojici, která musí ladit: <a href="/snowboardy/">snowboard</a>, <a href="/snowboardove-boty/">boty</a> a <a href="/snowboardova-vazani/">vázání</a>. '
          'Rozhoduje váha jezdce, styl jízdy (freestyle, freeride, all-mountain) a velikost nohy. K desce patří helma, brýle, rukavice a <a href="/snowboardove-chranice/">chrániče</a>.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů a snowboardy hledáte podle délky, typu a značky. Pro oblečení vyberte <a href="/lyzarske-obleceni/">lyžařské a snowboardové oblečení</a>.</p>',
    guide='<h2>Jak vybrat snowboard</h2>'
          '<p>Správný snowboard se liší podle stylu a váhy jezdce. Zkušení jezdci volí tužší a kratší desky podle disciplíny, začátečníci měkčí a odpouštějící.</p>'
          '<h3>Délka podle váhy</h3>'
          + T(['Hmotnost', 'Orientační délka'], [['50–60 kg', '140–148 cm'], ['60–70 kg', '148–154 cm'], ['70–80 kg', '154–159 cm'], ['80–90 kg', '158–163 cm'], ['nad 90 kg', '160 cm a více']]) +
          '<h3>Typ snowboardu</h3>'
          '<ul><li><strong>All-mountain:</strong> univerzální, hodí se začátečníkům.</li><li><strong>Freestyle:</strong> kratší, měkčí, na parky a triky.</li><li><strong>Freeride:</strong> delší, tužší, na prašan a neupravený terén.</li></ul>'
          '<h3>Boty a vázání</h3>'
          '<p>Boty vyberte podle velikosti nohy a tuhosti. Vázání musí sedět na desku a na botu, kontrolujte velikost a rozteč šroubů.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("raven", "Raven"), ("gravity", "Gravity"), ("burton", "Burton"), ("nitro", "Nitro"), ("head", "Head"), ("hatchey", "Hatchey"), ("ride", "Ride"), ("beany", "Beany"))}.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Příliš dlouhý snowboard pro začátečníka, hůř se ovládá.</li><li>Boty o číslo větší, noha se v nich hýbe.</li></ul>'
          '<h3>Péče</h3>'
          '<p>Po sezóně očistěte skluznici, navoskujte a uložte na suchém místě. Hrany ošetřete proti rzi.</p>',
    faq=[('Jak vybrat snowboard?', 'Podle hmotnosti, výšky a stylu jízdy. Začátečníci volí all-mountain deskou střední délky.'),
         ('Jak dlouhý snowboard?', 'Od brady po nos při postavení na špičku, přesné hodnoty udává výrobce podle hmotnosti.'),
         ('Co je freestyle snowboard?', 'Je to kratší a měkčí deska pro parky, skoky a triky.'),
         ('Jaké vázání na snowboard?', 'Podle velikosti boty a typu snowboardu. Zkontrolujte rozteč šroubů.'),
         ('Jaké boty na snowboard?', 'S měkčím až středním flexem pro začátečníky, přesně padnoucí.'),
         ('Jak pečovat o snowboard?', 'Očistit, navoskovat skluznici a ošetřit hrany po sezóně.')],
)

NEW['bezecke-lyzovani'] = dict(short=True,
    title='Běžecké lyžování – běžky, boty, hole, vosky | Sporteka',
    desc='Běžky, boty, vázání, hole a vosky na běžecké lyžování. Porovnejte ceny a délky lyží v českých obchodech.',
    intro='<p><strong>Běžecké lyžování</strong> je dostupný zimní sport, na který stačí lyže, boty, vázání a hole. Základní volba je mezi <strong>klasickou technikou</strong> (stopa) a <strong>bruslením</strong> (upravená trať). '
          'Pro rekreační jízdu na výlety se hodí kombinované lyže. Každá technika má jinou délku lyží i boty.</p>'
          '<p>Na Sportece najdete <a href="/bezecke-lyze/">běžecké lyže</a>, <a href="/bezecke-boty/">boty na běžky</a>, <a href="/bezecke-vazani/">vázání</a>, <a href="/lyzarske-hole/">hole</a> a <a href="/lyzarske-vosky/">vosky</a>.</p>',
    guide='<h2>Jak se vybavit na běžky</h2>'
          '<p>Nejdřív zvolte techniku. Klasika se jezdí ve stopě a hodí se začátečníkům, bruslení vyžaduje upravenou plochu a kondici. Boty a vázání musí být ze stejného systému.</p>'
          '<h3>Klasika, bruslení, kombi</h3>'
          + T(['Technika', 'Lyže', 'Boty'], [['Klasika', 'delší, s záběrovou zónou (šupiny, vosk)', 'nižší, pružné'], ['Bruslení', 'kratší, tužší', 'vyšší s oporou kotníku'], ['Kombi', 'univerzální', 'střední']]) +
          '<h3>Délka lyží</h3>'
          '<p>Klasické lyže jsou zhruba o 10 až 20 cm delší než výška, bruslařské o 10 až 15 cm kratší, přesnější hodnoty udává tabulka podle hmotnosti. Hole sahají u klasiky po rameno, u bruslení po ústa.</p>'
          '<h3>Vázání</h3>'
          '<p>Nejčastější jsou systémy NNN (NIS) a SNS. Bota musí odpovídat systému vázání, jinak nepasuje.</p>'
          '<h3>Vosky</h3>'
          '<p>Klasika bez šupin potřebuje stoupací vosk podle teploty, skluzný vosk zlepšuje klouzání. Rekreační jezdci si vystačí s lyžemi se šupinami.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("swix", "Swix"), ("fischer", "Fischer"), ("rossignol", "Rossignol"), ("alpina", "Alpina"), ("madshus", "Madshus"), ("vauhti", "Vauhti"), ("peltonen", "Peltonen"))}.</p>',
    faq=[('Jaké běžky pro začátečníka?', 'Lyže se šupinami pro klasiku s měkčím skluzem, které nevyžadují mazání.'),
         ('Jak dlouhé běžky?', 'U klasiky o 10 až 20 cm delší než výška, u bruslení o 10 až 15 cm kratší.'),
         ('Co jsou systémy NNN a SNS?', 'Dva různé systémy vázání na běžky. Boty se musí k vázání hodit.'),
         ('Klasika, nebo bruslení?', 'Klasika je pro začátečníky a stopy, bruslení pro rychlejší jízdu na upravených tratích.'),
         ('Jak často mazat běžky?', 'Podle typu. Šupinaté lyže nepotřebují mazání, hladké se mažou podle teploty.'),
         ('Jaké hole na běžky?', 'U klasiky po rameno, u bruslení po ústa. Lehčí karbonové jsou dražší.')],
)

NEW['bezecke-lyze'] = dict(short=True,
    title='Běžecké lyže – klasika, bruslení, kombi | Sporteka',
    desc='Běžecké lyže na klasiku, bruslení i kombi: pánské, dámské a dětské. Porovnejte ceny a délky lyží v českých obchodech.',
    intro='<p><strong>Běžecké lyže</strong> se dělí podle techniky: klasika, bruslení a kombi. Klasické mají záběrovou zónu a hodí se do stopy, bruslařské jsou kratší a tužší na upravenou trať. '
          'Rekreační jezdci často volí lyže se šupinami, které se nemažou stoupacím voskem.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů. K lyžím vyberte <a href="/bezecke-boty/">boty</a>, <a href="/bezecke-vazani/">vázání</a> a <a href="/lyzarske-vosky/">vosky</a>.</p>',
    guide='<h2>Jak vybrat běžecké lyže</h2>'
          '<p>Vybírejte podle techniky, hmotnosti a podmínek. Hmotnost jezdce určuje tuhost lyží a délku.</p>'
          '<h3>Typy lyží</h3>'
          '<ul><li><strong>Klasika (stopa):</strong> záběrová zóna, delší lyže.</li><li><strong>Bruslení:</strong> hladká skluznice, kratší a tužší.</li><li><strong>Kombi:</strong> kompromis pro rekreační jízdu.</li><li><strong>Turistické:</strong> širší, stabilní, na neupravené trasy.</li></ul>'
          '<h3>Šupiny, nebo vosk</h3>'
          '<p>Šupiny zajišťují záběr bez mazání a jsou praktické pro rekreační jezdce. Vosk nabízí lepší klouzání, ale vyžaduje znalost teplot.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("fischer", "Fischer"), ("rossignol", "Rossignol"), ("madshus", "Madshus"), ("peltonen", "Peltonen"), ("alpina", "Alpina"))}.</p>',
    faq=[('Jaké běžecké lyže vybrat?', 'Pro rekreaci kombinované nebo klasické lyže se šupinami. Podle hmotnosti zvolte tuhost.'),
         ('Jak dlouhé běžky?', 'Klasika o 10 až 20 cm delší než výška, bruslení o 10 až 15 cm kratší.'),
         ('Co jsou šupinaté lyže?', 'Mají v záběrové zóně šupiny, které zaberou bez stoupacího vosku.'),
         ('Jak často mazat?', 'Šupiny mazat nemusíte, hladké se mažou podle teploty a vlhkosti sněhu.'),
         ('Lze jezdit klasiku na bruslařských lyžích?', 'Ne, nemají záběrovou zónu. Jsou určené jen na bruslení.'),
         ('Jaké lyže pro děti?', 'Krátké lyže se šupinami a jednoduchým vázáním, podle výšky dítěte.')],
)

NEW['skialpinismus'] = dict(short=True,
    title='Skialpinismus – lyže, boty, vázání, pásy | Sporteka',
    desc='Skialpinistické lyže, boty, vázání, stoupací pásy a oblečení. Porovnejte ceny a hmotnost výbavy v českých obchodech.',
    intro='<p><strong>Skialpinismus</strong> je výstup na lyžích s pásy a sjezd zpět. Výbava musí být lehká, ale spolehlivá: <a href="/skialpove-lyze/">lyže</a>, <a href="/skialpove-boty/">boty</a> s režimem chůze, '
          '<a href="/skialpove-vazani/">vázání</a> a <a href="/skialpove-pasy/">stoupací pásy</a>. Ke skialpu patří také znalost lavinové problematiky a lavinová výbava.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů. Pro oblečení otevřete <a href="/lyzarske-obleceni/">lyžařské oblečení</a>.</p>',
    guide='<h2>Jak se vybavit na skialpinismus</h2>'
          '<p>Skialp je kompromis mezi váhou a výkonem při sjezdu. Čím lehčí výbava, tím snáze se stoupá, ale tím víc musí jezdec umět.</p>'
          '<h3>Základní výbava</h3>'
          '<ul><li><strong>Lyže:</strong> lehčí než sjezdové, šířka podle snow podmínek.</li><li><strong>Vázání:</strong> pin (tech) vázání jsou lehká, rámová pohodlnější.</li><li><strong>Boty:</strong> s režimem chůze a nižší váhou.</li><li><strong>Pásy:</strong> přilepené na skluznici proti sjíždění dozadu.</li></ul>'
          '<h3>Lavinová výbava</h3>'
          '<p>Při pohybu mimo sjezdovky se používá lavinový vyhledávač, sonda a lopata. Samotné vybavení nestačí, je potřeba absolvovat kurz a sledovat lavinovou předpověď.</p>'
          '<h3>Oblečení</h3>'
          '<p>Při výstupu se zpotíte, takže vrstvy musí rychle odvádět vlhkost. Na vrchol patří izolační bunda a čepice.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("dynafit", "Dynafit"), ("northfinder", "Northfinder"), ("silvini", "Silvini"), ("tenson", "Tenson"), ("simond", "Simond"), ("karpos", "Karpos"), ("camp", "Camp"), ("pomoca", "Pomoca"))}.</p>',
    faq=[('Co potřebuji na skialpinismus?', 'Skialpové lyže, boty, vázání, stoupací pásy, hole a lavinovou výbavu. Dále helmu a teplé oblečení.'),
         ('Jaké vázání na skialp?', 'Pin (tech) vázání jsou lehká, rámová vázání jsou pohodlnější při sjezdu.'),
         ('Jak vybrat skialpové boty?', 'Podle velikosti a hmotnosti, s funkčním režimem chůze.'),
         ('Co je lavinová výbava?', 'Lavinový vyhledávač, sonda a lopata. Vždy se používají společně s kurzem.'),
         ('Jaká délka skialpových lyží?', 'Obvykle od brady po čelo, lehčí lyže bývají o něco delší.'),
         ('Jaké pásy na skialp?', 'Podle šířky lyží, s kvalitním lepidlem a možností jejich uložení.')],
)
