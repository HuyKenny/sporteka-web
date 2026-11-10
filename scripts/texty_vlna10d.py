"""sporteka.cz — wave 10d (4. 11. 2026): next categories without a text. General true facts only, no prices."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}


def _e(slug, title, desc, intro, guide, faq):
    NEW[slug] = dict(short=True, title=title, desc=desc, intro=intro, guide=guide, faq=faq)


_e('muskareni', 'Muškaření – mušky, vlasce, pruty a vázání | Sporteka',
   'Vybavení pro muškaření: mušky, materiály na vázání, šňůry a podvazky. Porovnejte nabídku českých obchodů a vyberte podle lovu.',
   '<p><strong>Muškaření</strong> je lov ryb na umělé mušky, které imitují hmyz a drobné živočichy. Vybavení se liší podle toho, zda lovíte pstruhy v řece, nebo štiky a okouny na jezeře.</p>'
   '<p>Na Sportece najdete mušky a materiály na vázání od značek jako Sybai, Hends, Tommi-Fly, Semperfli, Hanák Competition nebo Veniard.</p>',
   '<h2>Jak začít s muškařením</h2>'
   '<p>Základem je souprava prutu, navijáku a šňůry stejné třídy. Třída se označuje číslem AFTM a určuje hmotnost šňůry, kterou prut unese. Pro pstruhy na menších tocích se běžně používají třídy kolem 3 až 5, pro větší vody a dravce vyšší.</p>'
   '<h3>Typy mušek</h3>'
   + T(['Typ', 'Použití'], [['Suchá muška', 'plave na hladině, imituje dospělý hmyz'], ['Mokrá muška', 'potápí se mírně pod hladinu'], ['Nymfa', 'ke dnu, imituje larvy'], ['Streamer', 'imituje rybku, na dravce a velké pstruhy']]) +
   '<h3>Vázání mušek</h3>'
   '<p>Pokud chcete mušky vázat sami, potřebujete svěrák, háčky, nitě, peří, srst a třpytivé materiály. Vázání je levnější než nákup hotových mušek a dovolí vám napodobit hmyz, který zrovna v revíru líhne.</p>'
   '<h3>Co dalšího se hodí</h3>'
   '<ul><li>Podvazky a návazce odpovídající síle mušky.</li><li>Plováky a olova na nymfy.</li><li>Pinzeta a nůžky v pouzdře na krk.</li><li>Krabičky na mušky.</li></ul>'
   '<h3>Pravidla a ohleduplnost</h3>'
   '<p>Dodržujte řád revíru a mnoho vod vyžaduje použití bezzubého háčku. Ulovenou rybu vracejte šetrně v mokrých rukou. Související kategorie: <a href="/rybareni/">rybaření</a>, <a href="/rybarske-pruty/">rybářské pruty</a> a <a href="/rybarske-navijaky/">navijáky</a>.</p>',
   [('Jak vybrat muškařský prut?', 'Podle třídy a délky. Na menší potok kratší lehčí prut, na větší vodu delší a silnější.'),
    ('Co znamená třída AFTM?', 'Číslo, které odpovídá hmotnosti první části šňůry. Šňůra a prut musí mít stejnou třídu.'),
    ('Jaká je rozdíl mezi suchou a mokrou muškou?', 'Suchá plave na hladině, mokrá se potápí pod hladinu.'),
    ('Můžu vázat mušky sám?', 'Ano, potřebujete svěrák, háčky a materiály. Je to levnější a přesnější podle hmyzu.'),
    ('Potřebuji speciální vlasec?', 'Ano, muškařská šňůra má jinou stavbu než běžný vlasec a nese váhu hodu.'),
    ('Jaké háčky povoluje revír?', 'Řád každého revíru je jiný, často je povinný bezzubý háček.')])

_e('skateboardy', 'Skateboardy a longboardy – kompletní i desky | Sporteka',
   'Skateboardy, longboardy, elektrické boardy, kola a ložiska. Porovnejte ceny z českých obchodů a vyberte board podle stylu jízdy.',
   '<p><strong>Skateboard nebo longboard</strong> se vybírá podle stylu jízdy. Krátká deska je určená na triky a skatepark, delší a pružnější na dojíždění, cruising a sjezdy.</p>'
   '<p>Na Sportece najdete boardy značek Exway, Enuff, Globe, Tempish, Arbor nebo Triple Eight.</p>',
   '<h2>Jak vybrat skateboard nebo longboard</h2>'
   '<p>Pro začátek se vyplatí kompletní board, který má desku, osy, kola a ložiska sestavené. Zkušenější jezdci skládají board podle sebe z jednotlivých dílů.</p>'
   '<h3>Typy boardů</h3>'
   + T(['Typ', 'Pro koho'], [['Street skateboard', 'triky, skatepark, krátká deska'], ['Cruiser', 'rekreace a pohodlné dojíždění'], ['Longboard', 'delší dojezdy, carving, pohodlí'], ['Elektrický board', 'dojíždění a delší vzdálenosti'], ['Dětský skateboard', 'menší rozměry a měkká kola']]) +
   '<h3>Na co se dívat</h3>'
   '<ul><li><strong>Šířka desky:</strong> většinou zhruba 7,5 až 8,5 palce pro street.</li>'
   '<li><strong>Kola:</strong> tvrdší na hladký povrch, měkčí na hrubý asfalt.</li>'
   '<li><strong>Ložiska:</strong> kvalitnější se točí plynuleji.</li>'
   '<li><strong>Osy:</strong> šířka má odpovídat šířce desky.</li></ul>'
   '<h3>Bezpečnost</h3>'
   '<p>Helma a chrániče na zápěstí, lokty a kolena patří k jízdě, hlavně pro začátečníky. Dopřejte si i vhodnou obuv s plochou podrážkou. Chrániče a helmy najdete v kategorii <a href="/chranice-a-helmy/">chrániče a helmy</a>. Jiné kolečkové sporty: <a href="/inline-brusle/">inline brusle</a> a <a href="/kolobezky/">koloběžky</a>.</p>',
   [('Jaký skateboard pro začátečníka?', 'Kompletní board se šířkou desky kolem 8 palců, v ceně s ložisky.'),
    ('Rozdíl mezi skateboardem a longboardem?', 'Longboard je delší a pružnější, hodí se na dojíždění a carving.'),
    ('Jaká kola zvolit?', 'Tvrdší na hladký skatepark, měkčí na asfalt a rekreaci.'),
    ('Potřebuji helmu?', 'Doporučuje se vždy, zvlášť při učení triků.'),
    ('Jak dlouho vydrží deska?', 'Podle intenzity, deska se po pár měsících tvrdého skateboardingu může prolomit.'),
    ('Jsou elektrické boardy povolené na silnici?', 'Pravidla se liší, před jízdou si zjistěte místní předpisy.')])

_e('vysoke-trekove-boty', 'Vysoké trekové boty – pánské a dámské | Sporteka',
   'Vysoké trekové a turistické boty s membránou i bez. Porovnejte ceny českých obchodů a vyberte boty podle terénu a sezóny.',
   '<p><strong>Vysoké trekové boty</strong> chrání kotník a nabízejí oporu v nerovném terénu. Hodí se na vícedenní túry s batohem, do hor i na náročnější pěší cesty.</p>'
   '<p>Na Sportece najdete modely značek Merrell, La Sportiva, Salomon, CMP, Adidas nebo Keen.</p>',
   '<h2>Jak vybrat vysoké trekové boty</h2>'
   '<p>Rozhoduje terén, hmotnost batohu a sezóna. Lehčí boty se hodí na dobře značené cesty, pevnější s tuhou podrážkou na skály a kamenité hřebeny.</p>'
   '<h3>Typy a tuhost</h3>'
   + T(['Typ', 'Použití'], [['Lehké turistické', 'značené cesty, lehký batoh'], ['Trekové', 'víc dní, vyšší zátěž, členitý terén'], ['Horské', 'skály, ferraty, tuhá podrážka'], ['Zimní', 'sníh a mráz, zateplené']]) +
   '<h3>Na co se dívat</h3>'
   '<ul><li><strong>Membrána:</strong> chrání před vodou, ale snižuje prodyšnost v horku.</li>'
   '<li><strong>Podrážka:</strong> kvalitní vzor drží na mokrých kamenech.</li>'
   '<li><strong>Tuhost:</strong> tužší boty unesou těžší batoh, lehčí jsou pohodlnější.</li>'
   '<li><strong>Špička:</strong> zesílená chrání při nárazu do kamenů.</li></ul>'
   '<h3>Velikost a rozchození</h3>'
   '<p>Boty zkoušejte odpoledne a v ponožkách, které na túře použijete. Prsty se při sestupu nesmí dotýkat špičky. Nové boty rozchoďte před delší túrou. Související kategorie: <a href="/trekova-obuv/">trekové boty</a>, <a href="/trekove-hole/">trekové hole</a> a <a href="/turisticke-batohy/">turistické batohy</a>.</p>',
   [('Kdy zvolit vysoké boty?', 'Při těžším batohu, nerovném terénu nebo na vícedenní túře.'),
    ('Je membrána nutná?', 'V mokru ano, v horku může boty přehřívat.'),
    ('Jak boty rozchodit?', 'Několik kratších vycházek před hlavní túrou.'),
    ('Jak boty impregnovat?', 'Speciálním přípravkem podle materiálu, po vyčištění od bláta.'),
    ('Jaká velikost?', 'Odpoledne a s turistickou ponožkou, s malou rezervou ve špičce.'),
    ('Jak dlouho vydrží boty?', 'Záleží na používání, podrážku lze často nechat přepodešvovat.')])

_e('outdoorove-kalhoty', 'Outdoorové kalhoty – turistické, odepínací | Sporteka',
   'Outdoorové a turistické kalhoty pánské i dámské: odepínací, softshellové a letní. Porovnejte ceny českých obchodů.',
   '<p><strong>Outdoorové kalhoty</strong> jsou odolné, rychle schnou a nebrání v pohybu. Hodí se na túry, kempování i každodenní nošení.</p>'
   '<p>Na Sportece najdete modely značek Fjällräven, Viking, Regatta, Northfinder, Dare2b nebo Dynafit.</p>',
   '<h2>Jak vybrat outdoorové kalhoty</h2>'
   '<p>Zvolte podle sezóny a terénu. V létě se hodí lehké rychleschnoucí nebo odepínací, na podzim a jaro pevnější softshell, v zimě zateplené.</p>'
   '<h3>Typy</h3>'
   + T(['Typ', 'Použití'], [['Lehké letní', 'teplo, rychlé schnutí'], ['Odepínací', 'proměnlivé počasí, kalhoty i kraťasy'], ['Softshellové', 'chladno a vítr'], ['Zateplené', 'zima'], ['Nepromokavé', 'ochrana před deštěm']]) +
   '<h3>Na co se dívat</h3>'
   '<ul><li><strong>Střih:</strong> předtvarovaná kolena usnadňují krok.</li>'
   '<li><strong>Kapsy:</strong> zipové na mobil a doklady.</li>'
   '<li><strong>Materiál:</strong> pevný nylon s elastanem nebo odolná bavlněná směs.</li>'
   '<li><strong>Pas:</strong> pružný nebo s páskem pro přizpůsobení.</li></ul>'
   '<h3>Péče</h3>'
   '<p>Perte na 30 až 40 °C bez aviváže. Impregnace odpuzující vodu se časem obnovuje speciálním přípravkem. Související kategorie: <a href="/sportovni-kalhoty/">sportovní kalhoty</a> a <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>.</p>'
   '<h3>Časté chyby</h3>'
   '<ul><li>Bavlněné kalhoty na deštivou túru.</li><li>Příliš těsný střih, který omezuje krok.</li></ul>',
   [('Jaké kalhoty na turistiku?', 'Lehké a pružné, které rychle schnou, v chladu softshellové.'),
    ('K čemu jsou odepínací kalhoty?', 'Odepnete nohavice a z kalhot jsou kraťasy.'),
    ('Jsou nepromokavé kalhoty nutné?', 'Na deštivé dny ano, jinak stačí impregnace softshellu.'),
    ('Jak praní?', 'Šetrně, bez aviváže.'),
    ('Kolik kapes?', 'Alespoň zipové na mobil a klíče.'),
    ('Jak je vybrat velikost?', 'Podle pasu a délky nohavice, s ohledem na vrstvy.')])

_e('inline-brusle', 'Inline brusle – dětské, dámské, pánské | Sporteka',
   'Inline brusle pro děti i dospělé, rekreační, fitness a agresivní. Porovnejte ceny českých obchodů a vyberte brusle podle velikosti a stylu.',
   '<p><strong>Inline brusle</strong> jsou kolečkové brusle s kolečky v jedné řadě. Hodí se na rekreační jízdu, fitness i tréninky, dětské modely mají nastavitelnou velikost.</p>'
   '<p>Na Sportece najdete značky Raven, Powerslide, Fila, Roces, K2 nebo Bauer.</p>',
   '<h2>Jak vybrat inline brusle</h2>'
   '<p>Podle zkušeností a stylu jízdy. Začátečník ocení měkčí botu s dobrou oporou kotníku, zkušenější jezdec tužší s většími koly.</p>'
   '<h3>Typy</h3>'
   + T(['Typ', 'Pro koho'], [['Rekreační', 'začátečníci, pohodlí'], ['Fitness', 'delší vzdálenosti, větší kola'], ['Rychlostní', 'zkušení, velká kola, nízká bota'], ['Agresivní', 'skatepark, triky'], ['Dětské', 'nastavitelná velikost']]) +
   '<h3>Na co se dívat</h3>'
   '<ul><li><strong>Kola:</strong> větší kola jsou rychlejší, menší obratnější.</li>'
   '<li><strong>Ložiska:</strong> vyšší třída se točí plynuleji.</li>'
   '<li><strong>Bota:</strong> musí sedět a podpírat kotník.</li>'
   '<li><strong>Brzda:</strong> patní brzda pro začátečníky.</li></ul>'
   '<h3>Bezpečnost</h3>'
   '<p>Helma a chrániče na zápěstí, kolena a lokty jsou základ. Před jízdou zkontrolujte dotažení šroubů a stav koleček. Chrániče najdete v kategorii <a href="/chranice-a-helmy/">chrániče a helmy</a>. Podobné: <a href="/brusle/">brusle</a> a <a href="/kolobezky-a-brusle/">koloběžky a brusle</a>.</p>',
   [('Jakou velikost inline bruslí?', 'Podle délky chodidla a tabulky výrobce, boty musí sedět pevně.'),
    ('Jaká kola zvolit?', 'Větší kola pro rychlost, menší pro obratnost.'),
    ('Jsou dětské inline brusle nastavitelné?', 'Ano, mnoho modelů roste s nohou.'),
    ('Potřebuji chrániče?', 'Ano, na zápěstí, kolena a lokty, plus helmu.'),
    ('Jak se brzdí?', 'Patní brzdou nebo technikou, kterou se začátečník naučí.'),
    ('Jak brusle udržovat?', 'Čistit ložiska, měnit opotřebená kola a otáčet je.')])

_e('cyklo-tasky-a-nosice', 'Cyklo brašny, nosiče a košíky | Sporteka',
   'Brašny na kolo, nosiče, košíky a tašky na řídítka. Porovnejte ceny českých obchodů a vyberte podle typu kola a nákladu.',
   '<p><strong>Brašny, nosiče a košíky</strong> pomáhají převézt náklad na kole bez batohu na zádech. Hodí se na nákupy, dojíždění i vícedenní cyklotúry.</p>'
   '<p>Na Sportece najdete značky Rockbros, Topeak, Deuter, M-Wave, Ortlieb nebo Basil.</p>',
   '<h2>Jak vybrat brašnu nebo nosič</h2>'
   '<p>Ověřte, zda má vaše kolo oka pro nosič a jaký systém uchycení preferujete. Pak zvolte objem a voděodolnost.</p>'
   '<h3>Typy</h3>'
   + T(['Typ', 'Použití'], [['Zadní nosič', 'základ pro boční brašny'], ['Boční brašny', 'cyklotúry, velký objem'], ['Brašna na rám', 'lehká výbava, bikepacking'], ['Taška na řídítka', 'rychlý přístup k věcem'], ['Košík', 'nákupy a město']]) +
   '<h3>Na co se dívat</h3>'
   '<ul><li><strong>Voděodolnost:</strong> uzavíratelné rolovací brašny jsou nejodolnější.</li>'
   '<li><strong>Uchycení:</strong> rychloupínací systémy usnadňují sundání.</li>'
   '<li><strong>Nosnost nosiče:</strong> uvádí výrobce.</li>'
   '<li><strong>Reflexní prvky:</strong> bezpečnost za šera.</li></ul>'
   '<h3>Jak ložit</h3>'
   '<p>Těžší věci dávejte dolů a ke středu kola, aby se zlepšila stabilita. Nezatěžujte nerovnoměrně jednu stranu. Související: <a href="/cyklo-prislusenstvi/">cyklo příslušenství</a>, <a href="/cyklo-blatniky/">blatníky</a> a <a href="/cyklo-nosice-na-auto/">nosiče na auto</a>.</p>',
   [('Pasuje nosič na každé kolo?', 'Ne, kolo musí mít oka nebo adaptér.'),
    ('Jaká brašna je nepromokavá?', 'Rolovací uzávěr a svařované švy zajistí největší odolnost.'),
    ('Kolik litrů potřebuji?', 'Na dojíždění stačí 15–20 litrů, na túru víc.'),
    ('Co je bikepacking?', 'Cestování s taškami na rámu, řídítkách a sedlovce místo nosičů.'),
    ('Mohu jet s brašnami v terénu?', 'Pevně uchycené ano, ale rámové tašky se hodí víc.'),
    ('Jak brašnu čistit?', 'Vlhkým hadříkem a po dešti vysušit.')])

_e('salova-obuv', 'Sálová a halová obuv – volejbal, florbal | Sporteka',
   'Sálová obuv na florbal, volejbal, házenou a futsal. Porovnejte ceny z českých obchodů a vyberte halovou obuv podle sportu.',
   '<p><strong>Sálová obuv</strong> má světlou nezanechávající stopy podrážku a dobrý grip na palubovce. Hodí se na florbal, volejbal, házenou i hodiny tělocviku.</p>'
   '<p>Na Sportece najdete modely značek Adidas, Asics, Mizuno, Puma, Nike nebo Joma.</p>',
   '<h2>Jak vybrat sálovou obuv</h2>'
   '<p>Hlavní je přilnavost a boční opora. Podrážka z gumy dobře drží, světlá nezanechá šmouhy na podlaze haly.</p>'
   '<h3>Podle sportu</h3>'
   + T(['Sport', 'Důležité'], [['Florbal', 'lehká, dobrý grip'], ['Volejbal', 'tlumení pro skoky'], ['Házená', 'boční stabilita'], ['Futsal', 'ochrana špičky a grip'], ['Tělocvik', 'univerzální a lehká']]) +
   '<h3>Na co se dívat</h3>'
   '<ul><li><strong>Podrážka:</strong> světlá a nešmouhující.</li>'
   '<li><strong>Tlumení:</strong> při skocích chrání klouby.</li>'
   '<li><strong>Prodyšnost:</strong> síťovina odvádí teplo.</li>'
   '<li><strong>Fixace:</strong> pevné šněrování drží nohu.</li></ul>'
   '<h3>Péče</h3>'
   '<p>Obuv noste jen v hale, venku se podrážka znečistí a ztrácí přilnavost. Čistěte ji vlhkým hadříkem. Související: <a href="/florbal/">florbal</a>, <a href="/volejbal/">volejbal</a> a <a href="/hazena/">házená</a>.</p>',
   [('Proč sálová obuv?', 'Díky grip a světlé podrážce nepoškodí palubovku.'),
    ('Mohu je nosit venku?', 'Nedoporučuje se, podrážka se znečistí.'),
    ('Jaká obuv na florbal?', 'Lehká s dobrým gripem a oporou.'),
    ('Jaká obuv na volejbal?', 'S tlumením pro skoky.'),
    ('Jak velikost?', 'Podle chodidla, s lehkou rezervou ve špičce.'),
    ('Jak dlouho vydrží?', 'Při pravidelném používání jednu až dvě sezóny.')])

_e('merino-pradlo', 'Merino spodní prádlo a legíny | Sporteka',
   'Merino spodní prádlo, legíny a termoprádlo. Porovnejte ceny z českých obchodů a vyberte merino podle gramáže a použití.',
   '<p><strong>Merino spodní prádlo</strong> hřeje i vlhké, odvádí pot a dlouho nezapáchá. Hodí se jako první vrstva na lyže, běžky i túry.</p>'
   '<p>Na Sportece najdete značky Icebreaker, Sensor, Smartwool, Lasting, Viking nebo Husky.</p>',
   '<h2>Jak vybrat merino prádlo</h2>'
   '<p>Rozhoduje gramáž, tedy hustota materiálu. Lehká se hodí na aktivní sporty, střední na chladné dny, těžká do mrazu a k odpočinku.</p>'
   '<h3>Gramáž</h3>'
   + T(['Gramáž', 'Použití'], [['Lehká do 150 g/m²', 'běh, kolo, mírné počasí'], ['Střední kolem 200 g/m²', 'turistika, podzim, jaro'], ['Těžká nad 250 g/m²', 'zima, nízká aktivita']]) +
   '<h3>Na co se dívat</h3>'
   '<ul><li><strong>Směsi:</strong> příměs polyamidu zvyšuje odolnost.</li>'
   '<li><strong>Švy:</strong> ploché zmenšují otěry.</li>'
   '<li><strong>Střih:</strong> musí přiléhat k pokožce.</li>'
   '<li><strong>Délka:</strong> delší nohavice a záda chrání před chladem.</li></ul>'
   '<h3>Péče</h3>'
   '<p>Perte šetrně na 30 °C a nesušte v sušičce, aby se vlna nesrážela. Merino stačí praní méně často než syntetika. Související: <a href="/merino/">merino</a>, <a href="/merino-tricka/">merino trička</a>, <a href="/termopradlo/">termoprádlo</a> a <a href="/merino-ponozky/">merino ponožky</a>.</p>',
   [('Proč merino?', 'Reguluje teplotu a dlouho nezapáchá.'),
    ('Škrábe merino?', 'Jemná vlákna ne, kvalitní prádlo je příjemné na kůži.'),
    ('Jaká gramáž?', 'Podle aktivity a teploty, lehká pro pohyb, těžká pro chlad.'),
    ('Jak praní?', 'Na 30 °C, bez aviváže a bez sušičky.'),
    ('Je merino trvanlivé?', 'Směs s polyamidem vydrží déle.'),
    ('Mohu ho nosit celý rok?', 'Lehké ano, jako první vrstvu.')])

_e('sportovni-sukne-a-saty', 'Sportovní sukně a šaty – tenis, golf, fitness | Sporteka',
   'Sportovní sukně a šaty na tenis, golf, běh a fitness. Porovnejte ceny z českých obchodů a vyberte podle sportu a střihu.',
   '<p><strong>Sportovní sukně a šaty</strong> spojují volnost pohybu se stylovým vzhledem. Oblíbené jsou na tenis, golf, padel a lehkou aktivitu v teple.</p>'
   '<p>Na Sportece najdete modely od předních sportovních značek v různých střizích a barvách.</p>',
   '<h2>Jak vybrat sportovní sukni nebo šaty</h2>'
   '<p>Zvolte podle sportu. Na tenis a padel se hodí sukně s vnitřními kraťasy, na běh lehčí střih, na golf delší a elegantnější.</p>'
   '<h3>Typy</h3>'
   + T(['Typ', 'Použití'], [['Tenisová sukně', 'vnitřní kraťasy, kapsa na míček'], ['Golfová sukně', 'delší, dobrý střih'], ['Běžecká sukně', 'lehká, rychle schne'], ['Sportovní šaty', 'tenis, padel, rekreace']]) +
   '<h3>Na co se dívat</h3>'
   '<ul><li><strong>Vnitřní kraťasy:</strong> musí sedět a neposouvat se.</li>'
   '<li><strong>Pas:</strong> široká gumička nevtlačí.</li>'
   '<li><strong>Kapsy:</strong> na míčky a telefon.</li>'
   '<li><strong>Materiál:</strong> pružný, prodyšný, rychleschnoucí.</li></ul>'
   '<h3>Kombinace</h3>'
   '<p>Sukni doplňte tričkem nebo <a href="/tilka/">tílkem</a> a vhodnou obuví, například <a href="/tenisova-obuv/">tenisovou</a>. Související kategorie: <a href="/tenis/">tenis</a> a <a href="/golfove-obleceni-a-obuv/">golfové oblečení</a>.</p>'
   '<h3>Péče</h3>'
   '<p>Perte na 30 °C a sušte na vzduchu, aby se zachovala pružnost materiálu.</p>',
   [('Jaká sukně na tenis?', 'S vnitřními kraťasy a kapsou na míček.'),
    ('Jsou sportovní šaty vhodné na běh?', 'Lehké ano, hlavně se šortkami uvnitř.'),
    ('Jak velikost?', 'Podle tabulky, pas i boky by měly sedět pohodlně.'),
    ('Mohu je nosit i mimo sport?', 'Ano, jako lehké letní oblečení.'),
    ('Jak péče?', 'Šetrné praní a sušení na vzduchu.'),
    ('Jaký materiál?', 'Elastické syntetické vlákno nebo směs.')])

_e('rybarske-navijaky', 'Rybářské navijáky – feeder, přívlač, kapr | Sporteka',
   'Rybářské navijáky na přívlač, feeder, kapry a moře. Porovnejte ceny z českých obchodů a vyberte naviják podle velikosti a převodu.',
   '<p><strong>Rybářský naviják</strong> ukládá vlasec, vyvíjí brzdu a pomáhá při zdolávání ryby. Správná velikost a převod určují, jak pohodlně se s ním loví.</p>'
   '<p>Na Sportece najdete navijáky značek Daiwa, Shimano, Mikado, Delphin, Fox a dalších.</p>',
   '<h2>Jak vybrat naviják</h2>'
   '<p>Velikost navijáku se udává číslem, například 2000 pro lehkou přívlač, 4000 pro feeder a vyšší pro kapry a moře. Menší číslo znamená menší a lehčí naviják.</p>'
   '<h3>Typy</h3>'
   + T(['Typ', 'Použití'], [['Přední brzda', 'univerzální, jemnější nastavení'], ['Zadní brzda', 'jednodušší, rychlé nastavení'], ['Multiplikátor', 'těžká přívlač a moře'], ['Baitrunner', 'kapři a pasivní lov'], ['Muškařský', 'jednoduchý navíjecí mechanizmus']]) +
   '<h3>Na co se dívat</h3>'
   '<ul><li><strong>Brzda:</strong> plynulá je důležitější než maximum.</li>'
   '<li><strong>Převod:</strong> vyšší navine víc vlasce na otáčku.</li>'
   '<li><strong>Ložiska:</strong> ovlivňují plynulost chodu.</li>'
   '<li><strong>Hmotnost:</strong> lehčí méně unaví při dlouhém lovu.</li></ul>'
   '<h3>Péče</h3>'
   '<p>Po lovu naviják opláchněte, hlavně po moři, a občas promažte. Související: <a href="/rybarske-pruty/">rybářské pruty</a>, <a href="/vlasce-a-snury/">vlasce a šňůry</a> a <a href="/rybareni/">rybaření</a>.</p>',
   [('Jaká velikost navijáku?', 'Podle způsobu lovu, 2000 přívlač, 4000 feeder, vyšší kapr.'),
    ('Přední nebo zadní brzda?', 'Přední je jemnější, zadní jednodušší.'),
    ('Co je baitrunner?', 'Systém volného chodu, který pustí vlasec při záběru.'),
    ('Jak naviják mazat?', 'Pravidelně podle návodu, nepřemazávat.'),
    ('Hodí se do slané vody?', 'Jen označené, a vždy opláchnout.'),
    ('Jak naviják spárovat s prutem?', 'Podle hmotnosti a délky prutu.')])

_e('sedla-a-gripy', 'Sedla a gripy na kolo | Sporteka',
   'Cyklo sedla, gripy, omotávky a sedlovky. Porovnejte ceny z českých obchodů a vyberte pohodlné sedlo a gripy podle typu jízdy.',
   '<p><strong>Sedlo a gripy</strong> jsou místa, kde se kolo dotýká těla. Správné sedlo a držadla zlepšují pohodlí a snižují únavu při delších jízdách.</p>'
   '<p>Na Sportece najdete sedla, gripy, omotávky a sedlovky od předních výrobců.</p>',
   '<h2>Jak vybrat sedlo a gripy</h2>'
   '<p>Šířka sedla se odvíjí od vzdálenosti sedacích kůstek. Sportovní jezdci volí užší, rekreační širší s polstrováním.</p>'
   '<h3>Typy</h3>'
   + T(['Typ', 'Použití'], [['Sportovní sedlo', 'užší, lehké, silnice a MTB'], ['Komfortní sedlo', 'širší, polstrované, město'], ['Gripy', 'držadla řídítek, rekreace a MTB'], ['Omotávka', 'silniční kola, tlumení vibrací'], ['Sedlovka', 'upevní sedlo, nastavení výšky']]) +
   '<h3>Na co se dívat</h3>'
   '<ul><li><strong>Šířka:</strong> podle sedacích kůstek.</li>'
   '<li><strong>Polstrování:</strong> měkčí není vždy pohodlnější.</li>'
   '<li><strong>Gripy:</strong> ergonomické snižují tlak na dlaň.</li>'
   '<li><strong>Průměr:</strong> musí odpovídat řídítkům.</li></ul>'
   '<h3>Nastavení</h3>'
   '<p>Výška sedla ovlivňuje účinnost šlapání i zdraví kolen. Při šlapání má být noha v nejnižším bodě lehce pokrčená. Související: <a href="/cyklo-dily/">cyklo díly</a>, <a href="/cyklo-riditka/">řídítka</a> a <a href="/cyklisticke-rukavice/">cyklistické rukavice</a>.</p>',
   [('Jak vybrat sedlo?', 'Podle šířky sedacích kůstek a stylu jízdy.'),
    ('Jsou měkká sedla lepší?', 'Ne vždy, na delší trase pohodlnější bývá pevnější.'),
    ('Jaké gripy?', 'Ergonomické s dobrým povrchem a průměrem podle řídítek.'),
    ('Jak nastavit výšku sedla?', 'Noha má být v nejnižším bodě mírně pokrčená.'),
    ('Kdy měnit omotávku?', 'Když se opotřebuje nebo ztratí přilnavost.'),
    ('Pasují gripy na každé řídítko?', 'Musí odpovídat průměru a typu řídítek.')])

_e('soupravy', 'Sportovní soupravy a komplety | Sporteka',
   'Sportovní soupravy, tepláky s mikinou, dresové komplety a tréninkové sady. Porovnejte ceny českých obchodů.',
   '<p><strong>Sportovní souprava</strong> spojuje bundu nebo mikinu s kalhotami do jednoho kompletu. Hodí se na trénink, zahřátí před zápasem i volný čas.</p>'
   '<p>Na Sportece najdete soupravy značek Adidas, Nike, Peak Mountain, Puma a dalších.</p>',
   '<h2>Jak vybrat soupravu</h2>'
   '<p>Rozhodněte, k čemu ji budete nosit. Týmové a tréninkové soupravy jsou pevnější, volnočasové měkké. Zkontrolujte střih, zda souprava sedí na horní i dolní části.</p>'
   '<h3>Typy</h3>'
   + T(['Typ', 'Použití'], [['Tepláková souprava', 'volný čas, zahřátí'], ['Tréninková souprava', 'trénink, týmy'], ['Dětská souprava', 'škola a hřiště'], ['Bojové sporty', 'kimono a komplety'], ['Fitness komplet', 'top a legíny']]) +
   '<h3>Na co se dívat</h3>'
   '<ul><li><strong>Materiál:</strong> bavlna pro pohodlí, polyester pro sport.</li>'
   '<li><strong>Zip a kapsy:</strong> kvalitní zip vydrží.</li>'
   '<li><strong>Střih:</strong> volnější pro pohyb, slim pro styl.</li>'
   '<li><strong>Velikosti:</strong> horní a dolní díl mohou mít odlišné rozměry.</li></ul>'
   '<h3>Péče</h3>'
   '<p>Perte souprávu obrácenou a bez aviváže u funkčních materiálů. Související: <a href="/teplaky/">tepláky</a>, <a href="/mikiny/">mikiny</a> a <a href="/sportovni-bundy/">sportovní bundy</a>.</p>',
   [('Co obsahuje souprava?', 'Obvykle bundu nebo mikinu a kalhoty, někdy i tričko.'),
    ('Hodí se i na sport?', 'Tréninkové ano, volnočasové spíš na nošení.'),
    ('Mohu velikosti kombinovat?', 'U některých obchodů ano, jinak se prodávají jako celek.'),
    ('Jak péče?', 'Dle štítku, šetrně.'),
    ('Jsou dětské soupravy odolné?', 'Pevný materiál a zesílená kolena vydrží víc.'),
    ('Jaký materiál?', 'Bavlna je pohodlná, polyester lépe odvádí pot.')])

_e('joga-a-pilates', 'Jóga, pilates a meditace – podložky a pomůcky | Sporteka',
   'Vybavení na jógu, pilates a meditaci: podložky, bloky, popruhy, míče a polštáře. Porovnejte ceny českých obchodů.',
   '<p><strong>Jóga, pilates a meditace</strong> vyžadují jen málo vybavení, ale kvalitní podložka a pár pomůcek zlepší pohodlí i bezpečnost cvičení.</p>'
   '<p>Na Sportece najdete vybavení značek Merco, HMS, Sportago, Adidas nebo Insportline.</p>',
   '<h2>Jak vybrat vybavení</h2>'
   '<p>Začněte podložkou. Tloušťka a materiál rozhodují o tlumení a přilnavosti, a podle typu cvičení se doplňuje blokem, popruhem nebo míčem.</p>'
   '<h3>Základní pomůcky</h3>'
   + T(['Pomůcka', 'K čemu'], [['Podložka', 'tlumení a přilnavost'], ['Jógový blok', 'zkrácení vzdálenosti k zemi'], ['Popruh', 'prohloubení strečinku'], ['Pilates míč', 'stabilizace středu těla'], ['Meditační polštář', 'pohodlné sezení']]) +
   '<h3>Na co se dívat</h3>'
   '<ul><li><strong>Tloušťka podložky:</strong> tenčí pro stabilitu, silnější pro tlumení.</li>'
   '<li><strong>Materiál:</strong> přírodní kaučuk, PVC nebo TPE.</li>'
   '<li><strong>Protiskluz:</strong> důležitý u dynamické jógy.</li>'
   '<li><strong>Rozměr:</strong> delší pro vyšší lidi.</li></ul>'
   '<h3>Kategorie</h3>'
   '<p>Podrobnější přehledy: <a href="/joga-a-podlozky/">jóga a podložky</a>, <a href="/jogove-pomucky/">jógové pomůcky</a>, <a href="/pilates-pomucky/">pilates pomůcky</a> a <a href="/meditace/">meditace</a>.</p>'
   '<h3>Péče</h3>'
   '<p>Podložku čistěte vlhkým hadříkem a skladujte srolovanou mimo přímé slunce.</p>',
   [('Jaká podložka na jógu?', 'S dobrou přilnavostí a tloušťkou kolem několika milimetrů.'),
    ('K čemu je jógový blok?', 'Pomáhá v pozicích, kdy dosáhnete na zem hůře.'),
    ('Potřebuji speciální vybavení na pilates?', 'Stačí podložka, ostatní pomůcky jsou volitelné.'),
    ('Jak podložku čistit?', 'Vlhkým hadříkem a jemným mýdlem.'),
    ('Rozdíl mezi jógovou a pilates podložkou?', 'Pilates bývá silnější pro tlumení páteře.'),
    ('Co na meditaci?', 'Pohodlný polštář nebo podložka.')])

_e('ostatni-doplnky-stravy', 'Doplňky stravy – vitaminy, adaptogeny, zdraví | Sporteka',
   'Doplňky stravy pro sportovce a zdraví: houby, omega-3, probiotika a další. Porovnejte ceny z českých obchodů.',
   '<p><strong>Doplňky stravy</strong> doplňují jídelníček tam, kde sportovec nebo aktivní člověk potřebuje víc. Nenahrazují pestrou stravu, ale mohou pomoci při zvýšené zátěži.</p>'
   '<p>Na Sportece najdete doplňky značek GymBeam, MycoMedica, GreenFood Nutrition, VitaHarmony, Viridian nebo OstroVit.</p>',
   '<h2>Jak vybrat doplněk stravy</h2>'
   '<p>Nejdřív zvažte, co vám v jídelníčku chybí. Sledujte složení, dávkování a formu, tedy kapsle, prášek nebo kapky.</p>'
   '<h3>Časté skupiny</h3>'
   + T(['Skupina', 'K čemu se používá'], [['Omega-3', 'doplnění mastných kyselin'], ['Probiotika', 'podpora trávení'], ['Funkční houby', 'tradiční doplněk pro vitalitu'], ['Hořčík a minerály', 'doplnění při zátěži'], ['Adaptogeny', 'tradiční bylinné doplňky']]) +
   '<h3>Na co se dívat</h3>'
   '<ul><li><strong>Složení:</strong> aktivní látka a její množství.</li>'
   '<li><strong>Dávkování:</strong> řiďte se pokyny výrobce.</li>'
   '<li><strong>Čistota:</strong> bez zbytečných přísad.</li>'
   '<li><strong>Původ a certifikace:</strong> uvedeno výrobcem.</li></ul>'
   '<h3>Upozornění</h3>'
   '<p>Doplňky stravy nejsou léky. Při zdravotních potížích, těhotenství nebo užívání léků se poraďte s lékařem. Související: <a href="/vitaminy-a-mineraly/">vitaminy a minerály</a>, <a href="/sportovni-vyziva/">sportovní výživa</a> a <a href="/proteiny/">proteiny</a>.</p>',
   [('Jsou doplňky stravy nutné?', 'Pestrá strava je základ, doplňky mohou pomoci při zvýšených potřebách.'),
    ('Jak vybrat kvalitní doplněk?', 'Podle složení, dávkování a důvěryhodného výrobce.'),
    ('Mohu kombinovat více doplňků?', 'Poraďte se s lékařem, zvlášť při užívání léků.'),
    ('Kdy je užívat?', 'Podle pokynů výrobce, některé s jídlem.'),
    ('Jsou vhodné pro děti?', 'Jen s doporučením lékaře.'),
    ('Mají doplňky vedlejší účinky?', 'Při předávkování mohou, dodržujte doporučenou dávku.')])
