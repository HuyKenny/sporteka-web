"""sporteka.cz — texts of wave 3 (3. 11. 2026): nutrition, racket and ball sports, darts, golf, backpacks, jackets, gloves.
Same rules as texty_vlna1a.py; every entry is short=True (intro ≥ 50 words, guide ≥ 220). Brands come from the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

NEW['proteiny'] = dict(short=True,
    title='Proteiny – syrovátkový, kaseinový, rostlinný | Sporteka',
    desc='Proteiny a proteinové prášky: syrovátkový, kaseinový a rostlinný protein. Porovnejte ceny za 1 kg a příchutě v českých obchodech se sportovní výživou.',
    intro='<p><strong>Protein</strong> je doplněk stravy, který pomáhá dosáhnout denní dávky bílkovin, pokud ji nezvládáte z jídla. Nejčastější je <strong>syrovátkový</strong> (rychle se vstřebává), '
          '<strong>kaseinový</strong> (pomalu, vhodný na večer) a <strong>rostlinný</strong> (hrachový, sójový, rýžový). Dvě stejně velká balení se mohou lišit obsahem bílkovin i cenou za dávku, proto porovnávejte cenu za 1 kg čistého proteinu.</p>'
          '<p>Na Sportece vidíte ceny z českých obchodů vedle sebe. K proteinu se hodí <a href="/kreatin/">kreatin</a>, <a href="/aminokyseliny-bcaa/">aminokyseliny</a> a <a href="/proteinove-tycinky-a-snacky/">proteinové tyčinky</a>.</p>',
    guide='<h2>Jak vybrat protein</h2>'
          '<p>Protein nenahrazuje stravu, jen ji doplňuje. Nejdřív zvažte, kolik bílkovin přijmete z jídla, teprve potom kolik chybí. Obecně se pro aktivní lidi uvádí rozmezí zhruba 1,4 až 2,0 g bílkovin na kilogram hmotnosti, přesnou potřebu ale určí lékař nebo dietolog.</p>'
          '<h3>Druhy proteinu</h3>'
          + T(['Typ', 'Vstřebávání', 'Pro koho'], [['Syrovátkový koncentrát (WPC)', 'rychlé', 'běžné doplnění po tréninku, nižší cena'], ['Syrovátkový izolát (WPI)', 'rychlé', 'vyšší podíl bílkovin, méně laktózy'], ['Kasein', 'pomalé', 'večer, delší pocit nasycení'], ['Rostlinný (hrách, rýže, soja)', 'střední', 'vegani a lidé s intolerancí mléka']]) +
          '<h3>Na co se dívat na etiketě</h3>'
          '<ul><li><strong>Obsah bílkovin v 100 g:</strong> u kvalitního syrovátkového proteinu bývá přes 70 %.</li>'
          '<li><strong>Velikost dávky:</strong> srovnávejte cenu za dávku, ne za balení.</li>'
          '<li><strong>Cukr a sladidla:</strong> příchuť často přidává sladidla, bez příchuti jsou čistší.</li>'
          '<li><strong>Alergeny:</strong> mléko, sója a lepek, hlídejte při intoleranci.</li></ul>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Největší výběr nabízejí {B(("gymbeam", "GymBeam"), ("myprotein", "Myprotein"), ("extrifit", "Extrifit"), ("amix", "Amix"), ("biotech-usa", "BioTech USA"), ("nutrend", "Nutrend"), ("scitec-nutrition", "Scitec Nutrition"), ("weider", "Weider"))}.</p>'
          '<h3>Jak a kdy ho používat</h3>'
          '<p>Nejčastěji po tréninku nebo jako doplnění snídaně či svačiny. Rozmíchává se ve vodě nebo mléce, lze ho přidat do ovesné kaše či smoothie. Dodržujte dávkování na obalu a skladujte v suchu.</p>',
    faq=[('Který protein je nejlepší pro začátek?', 'Syrovátkový koncentrát v oblíbené příchuti. Je cenově dostupný a dobře se rozmíchává.'),
         ('Kolik proteinu denně?', 'Záleží na hmotnosti a aktivitě. Pro sportovce se běžně uvádí 1,4 až 2,0 g na kilogram, konkrétní potřebu poraďte s odborníkem.'),
         ('Jaký protein pro vegany?', 'Rostlinný protein z hrachu, rýže nebo sóji. Kombinace více zdrojů dává plnější profil aminokyselin.'),
         ('Kdy pít protein?', 'Nejčastěji po tréninku nebo kdykoli během dne, kdy chybí bílkoviny. Kasein se hodí na večer.'),
         ('Čím se liší koncentrát od izolátu?', 'Izolát má vyšší podíl bílkovin a méně laktózy a tuku, koncentrát je levnější.'),
         ('Jak porovnat ceny proteinů?', 'Podle ceny za 1 kg čistého proteinu, tedy ceny za kilogram vynásobené podílem bílkovin v prášku.')],
)

NEW['kreatin'] = dict(short=True,
    title='Kreatin – monohydrát, kapsle, prášek | Porovnání cen',
    desc='Kreatin monohydrát v prášku i kapslích. Porovnejte ceny za dávku a čistotu v českých obchodech se sportovní výživou.',
    intro='<p><strong>Kreatin</strong> patří k nejlépe prozkoumaným doplňkům pro sportovce. Nejčastější formou je <strong>kreatin monohydrát</strong>, který se prodává v prášku nebo v kapslích. '
          'Pro běžné používání stačí obvykle několik gramů denně a rozhodující je spíš pravidelnost než druh. Dražší „speciální formy“ nemusí nabízet znatelnou výhodu.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů a vedle kreatinu najdete <a href="/proteiny/">proteiny</a>, <a href="/aminokyseliny-bcaa/">aminokyseliny</a> a <a href="/spalovace-tuku/">spalovače tuků</a>.</p>',
    guide='<h2>Jak vybrat kreatin</h2>'
          '<p>Při výběru dávejte přednost osvědčenému monohydrátu a ověřené čistotě. U doplňků stravy platí, že si dávkování ověříte na obalu a při zdravotních potížích, užívání léků nebo těhotenství se poradíte s lékařem.</p>'
          '<h3>Formy kreatinu</h3>'
          '<ul><li><strong>Monohydrát:</strong> nejčastější a nejlevnější forma, základ většiny studií.</li>'
          '<li><strong>Mikronizovaný monohydrát:</strong> jemnější zrno, lépe se rozpouští.</li>'
          '<li><strong>Kapsle a tablety:</strong> pohodlné, dražší na gram.</li>'
          '<li><strong>Jiné formy (HCl, ethylester a další):</strong> bývají dražší a výhodu je potřeba posuzovat opatrně.</li></ul>'
          '<h3>Dávkování a pitný režim</h3>'
          '<p>Obvykle se uvádí dávka několik gramů denně, buď bez nasycovací fáze, nebo s ní. Přesné dávkování najdete na obalu. Během užívání se doporučuje dostatečný příjem tekutin.</p>'
          '<h3>Na co se dívat</h3>'
          '<ul><li>Cena za dávku, ne za balení.</li><li>Čistý složení bez zbytečných přísad.</li><li>Certifikace a kvalita výrobce.</li></ul>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Kreatin nabízejí {B(("gymbeam", "GymBeam"), ("amix", "Amix"), ("masmusculo", "Mas Musculo"), ("allnutrition", "AllNutrition"), ("biotech-usa", "BioTech USA"), ("myprotein", "Myprotein"), ("weider", "Weider"), ("ostrovit", "OstroVit"))}.</p>',
    faq=[('Který kreatin je nejlepší?', 'Nejčastěji doporučovaný je kreatin monohydrát. Je nejlevnější a nejvíce prozkoumaný.'),
         ('Kolik kreatinu denně?', 'Obvykle několik gramů denně podle návodu na obalu. Nezvyšujte dávku bez doporučení odborníka.'),
         ('Je lepší prášek, nebo kapsle?', 'Prášek je levnější za dávku, kapsle pohodlnější. Účinná látka je stejná.'),
         ('Musí se pít víc vody?', 'Ano, při užívání se doporučuje dostatečný pitný režim.'),
         ('Kdy brát kreatin?', 'Čas není rozhodující, důležité je užívat ho pravidelně každý den.'),
         ('Hodí se kreatin pro ženy?', 'Není vázaný na pohlaví. Pokud máte zdravotní potíže, poraďte se s lékařem.')],
)

NEW['golfove-doplnky'] = dict(short=True,
    title='Golfové doplňky – rukavice, čepice, míčky | Sporteka',
    desc='Golfové doplňky: rukavice, čepice, dalekohledy, ručníky a další vybavení na hřiště. Porovnejte ceny v českých obchodech.',
    intro='<p><strong>Golfové doplňky</strong> doplňují základní vybavení, tedy hole, míčky a tašku. Patří sem rukavice, čepice a kšiltovky, ručníky, tee, značkovače a pomůcky na čištění holí. '
          'Vybírejte podle hřiště a počasí: v létě ochranu před sluncem, na jaře a na podzim něco proti chladu a dešti.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů. K doplňkům se hodí <a href="/golfove-hole/">golfové hole</a>, <a href="/golfove-micky/">míčky</a>, <a href="/golfove-tasky-a-voziky/">tašky a vozíky</a> a <a href="/golfove-obleceni-a-obuv/">oblečení a obuv</a>.</p>',
    guide='<h2>Co se hodí na golfové hřiště</h2>'
          '<p>Doplňky nejsou povinné, ale kolo golfu trvá několik hodin a drobnosti rozhodnou o pohodlí. Vyberte si ty, které použijete při každé hře.</p>'
          '<h3>Rukavice</h3>'
          '<p>Golfová rukavice se nosí na jedné ruce, praváci na levé. Má držet přesně na dlani a nesmí se na prstech krčit. Kožené jsou jemnější a drží lépe, syntetické odolnější a levnější.</p>'
          '<h3>Čepice a ochrana před počasím</h3>'
          '<ul><li><strong>Kšiltovka:</strong> chrání oči a obličej před sluncem.</li>'
          '<li><strong>Čepice a čelenka:</strong> v chladném počasí.</li>'
          '<li><strong>Pláštěnka a deštník:</strong> přijdou vhod v nestálém počasí.</li></ul>'
          '<h3>Drobné pomůcky</h3>'
          '<p>Tee, značkovače, nástroje na opravu důlků po dopadu míčku a ručník na čištění holí. Dalekohledy a laserové měřiče vzdálenosti pomáhají při výběru hole.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("inesis", "Inesis"), ("new-era", "New Era"), ("under-armour", "Under Armour"), ("nike", "Nike"), ("adidas", "Adidas"))} a další. Pro začátečníky stačí základní doplňky, výbavu je možné rozšiřovat postupně.</p>',
    faq=[('Na kterou ruku se nosí golfová rukavice?', 'Praváci na levou, leváci na pravou. Rukavice se nosí na ruce, která vede hůl nahoře.'),
         ('Jaké doplňky potřebuje začátečník?', 'Rukavici, kšiltovku, tee, značkovač a ručník. Ostatní lze dokoupit podle potřeby.'),
         ('Kožená, nebo syntetická rukavice?', 'Kožená lépe drží a je jemnější, syntetická odolnější a levnější.'),
         ('Jak vyčistit golfové hole?', 'Vlhkým ručníkem a kartáčem po každém kole. Hlavy holí můžete namočit do vlažné vody s jarem.'),
         ('Potřebuji dalekohled na golf?', 'Není nutný, ale měřič vzdálenosti usnadňuje výběr hole. Pro turnaje ověřte pravidla.'),
         ('Kde najdu golfové oblečení?', 'V kategorii golfové oblečení a obuv, která je součástí golfu.')],
)

NEW['sipky'] = dict(short=True,
    title='Šipky – terče, šipky, doplňky | Porovnání cen',
    desc='Šipky, terče a doplňky: steel i soft šipky, sisalové terče, letky a pouzdra. Porovnejte ceny a dostupnost v českých obchodech.',
    intro='<p><strong>Šipky</strong> se dělí na <strong>steel</strong> (kovový hrot, klasický terč ze sisalu) a <strong>soft</strong> (plastový hrot, elektronický terč). Ke hře potřebujete šipky, terč a vhodné osvětlení. '
          'Důležitá je hmotnost šipky, tvar těla (barrel), letky a stonek. Pro začátek stačí vyvážená šipka střední hmotnosti.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů. Vyberte <a href="/sipkove-terce/">šipkové terče</a> nebo <a href="/sipkove-doplnky/">šipkové doplňky</a> jako letky, stonky a pouzdra.</p>',
    guide='<h2>Jak vybrat šipky</h2>'
          '<p>Správné šipky vám sednou do ruky. Hmotnost a tvar těla ovlivní, jak šipku držíte a jak letí.</p>'
          '<h3>Steel, nebo soft</h3>'
          + T(['Typ', 'Hrot', 'Terč'], [['Steel', 'kovový', 'sisalový (borstle)'], ['Soft', 'plastový', 'elektronický']]) +
          '<h3>Hmotnost a tvar</h3>'
          '<p>Hmotnost šipek se udává v gramech, běžné jsou 18 až 26 g u steel šipek, soft bývají lehčí. Lehčí šipky mají rychlejší dráhu, těžší stabilnější. Tvar těla a rýhování ovlivňují úchop.</p>'
          '<h3>Letky a stonky</h3>'
          '<ul><li><strong>Letky:</strong> stabilizují let, větší letka dává stabilitu, menší rychlost.</li>'
          '<li><strong>Stonky:</strong> krátké pro rychlejší šipky, dlouhé pro vyšší stabilitu.</li></ul>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("harrows", "Harrows"), ("mission", "Mission"), ("bull-s", "Bull\'s"), ("winmau", "Winmau"), ("target-darts", "Target Darts"), ("unicorn", "Unicorn"), ("shot", "Shot"))} a další.</p>'
          '<p>Terč věšte tak, aby střed byl ve výšce 173 cm od podlahy a čára hodu vzdálená 237 cm.</p>',
    faq=[('Jaké šipky pro začátečníka?', 'Steel šipky o hmotnosti kolem 22 až 24 g a sisalový terč. Nebo soft šipky s elektronickým terčem.'),
         ('Jak vysoko věšet šipkový terč?', 'Střed terče ve výšce 173 cm, čára hodu ve vzdálenosti 237 cm od terče.'),
         ('Čím se liší steel a soft?', 'Steel mají kovový hrot a sisalový terč, soft plastový hrot a elektronický terč.'),
         ('Jak vybrat letky?', 'Větší letky dávají stabilitu, menší rychlost. Začátečníkům se hodí standardní tvar.'),
         ('Jak pečovat o sisalový terč?', 'Pravidelně ho otáčejte, aby se opotřebení rovnoměrně rozložilo. Skladujte v suchu.'),
         ('Jak často měnit hroty?', 'Podle opotřebení. Ztupené hroty se lehce odrážejí od terče.')],
)

NEW['florbal'] = dict(short=True,
    title='Florbal – hole, míčky, brány a výbava | Sporteka',
    desc='Florbalové vybavení: hole, čepele, míčky, brány a chrániče. Porovnejte ceny a dostupnost v českých obchodech.',
    intro='<p><strong>Florbal</strong> je rychlý halový sport, ve kterém si vystačíte s holí, míčkem a sálovou obuví. Florbalová hůl se vybírá podle délky a ohebnosti, čepel podle zahnutí a materiálu. '
          'Děti začínají kratšími holemi s nízkou tuhostí. Brankáři mají vlastní výbavu.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů a vyberete konkrétní <a href="/florbalove-hole/">florbalové hole</a>. Do haly se hodí <a href="/salova-obuv/">sálová obuv</a> a vhodné <a href="/sportovni-tricka/">sportovní trička</a>.</p>',
    guide='<h2>Jak vybrat florbalovou výbavu</h2>'
          '<p>Florbal se hraje v hale a hůl je hlavním nástrojem hráče. Správná délka a tuhost pomáhají při střelbě i vedení míčku.</p>'
          '<h3>Délka hole</h3>'
          '<p>Hůl by měla sahat zhruba k pupku nebo k bedrům, podle stylu hry. Kratší hůl dává lepší ovládání míčku, delší dosah a sílu střely.</p>'
          + T(['Výška hráče', 'Orientační délka hole'], [['do 130 cm', '70–80 cm'], ['130–150 cm', '80–90 cm'], ['150–170 cm', '90–100 cm'], ['nad 170 cm', '100–105 cm']]) +
          '<h3>Tuhost (flex)</h3>'
          '<p>Udává se číslem, například 27, 29 nebo 32. Nižší číslo znamená měkčí hůl, která se lépe ohýbá, vyšší tužší. Děti a lehčí hráči volí měkčí, silnější hráči tužší.</p>'
          '<h3>Čepel a míčky</h3>'
          '<ul><li><strong>Čepel:</strong> může být rovná nebo zahnutá, tvrdší nebo měkčí.</li>'
          '<li><strong>Míček:</strong> do soutěží se používají certifikované míčky, na trénink stačí běžné.</li></ul>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Nabídka obsahuje značky {B(("salming", "Salming"), ("winnwell", "Winnwell"), ("bauer", "Bauer"), ("unihoc", "Unihoc"), ("freez", "Freez"), ("fat-pipe", "Fat Pipe"), ("tempish", "Tempish"), ("kubisport", "Kubisport"))}.</p>',
    faq=[('Jak dlouhá má být florbalová hůl?', 'Obvykle po pupek nebo bedra. Kratší dává lepší ovládání, delší dosah.'),
         ('Jaký flex florbalové hole zvolit?', 'Děti a lehčí hráči měkčí, silnější a zkušenější tužší. Běžné hodnoty jsou 27 až 32.'),
         ('Co potřebuji na začátek s florbalem?', 'Hůl, míček, sálovou obuv a sportovní oblečení. Dětem doporučujeme i chrániče.'),
         ('Jaká obuv do haly?', 'Sálová obuv s nešpinící podrážkou. Nepoužívejte běžecké boty s hrubou podrážkou.'),
         ('Jak vybrat hůl pro dítě?', 'Podle výšky dítěte, ne na vyrůstání. Dítě s příliš dlouhou holí hůře ovládá míček.'),
         ('Jak často měnit čepel?', 'Podle opotřebení, při praskání nebo ztrátě tvaru.')],
)

NEW['padel'] = dict(short=True,
    title='Padel – rakety, míče a vybavení | Porovnání cen',
    desc='Padelové rakety, míče a obuv. Porovnejte ceny, váhu a tvar rakety pro začátečníky i pokročilé v českých obchodech.',
    intro='<p><strong>Padel</strong> je rychle rostoucí raketový sport. Hraje se ve čtyřech na menším kurtu se stěnami. Padelová raketa nemá strunění, ale perforovaný povrch a pěnové jádro. '
          'Tvar rakety určuje, jestli bude více kontroly (kulatá), nebo síly (diamant). Pro začátečníky je nejlepší kulatý nebo slzový tvar.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů. Pro další raketové sporty se podívejte na <a href="/tenis/">tenis</a>, <a href="/badminton/">badminton</a> nebo <a href="/squash/">squash</a>.</p>',
    guide='<h2>Jak vybrat padelovou raketu</h2>'
          '<p>Správná raketa závisí na úrovni, stylu hry a síle ruky. Při výběru sledujte tvar, váhu a vyvážení.</p>'
          '<h3>Tvar rakety</h3>'
          + T(['Tvar', 'Charakter', 'Pro koho'], [['Kulatý', 'kontrola, velké sweet spot', 'začátečníci'], ['Slza', 'univerzální', 'střední úroveň'], ['Diamant', 'síla, menší sweet spot', 'pokročilí útoční hráči']]) +
          '<h3>Váha a vyvážení</h3>'
          '<p>Rakety váží obvykle 355 až 375 g. Lehčí se lépe ovládají a méně zatěžují zápěstí, těžší dávají sílu. Vyvážení v hlavě znamená větší sílu, v rukojeti lepší manévrovatelnost.</p>'
          '<h3>Materiál</h3>'
          '<ul><li><strong>Karbon:</strong> tuhý a výkonný, dražší.</li>'
          '<li><strong>Sklolaminát:</strong> měkčí, odpouští chyby, vhodný pro začátečníky.</li></ul>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("bullpadel", "Bullpadel"), ("kuikma", "Kuikma"), ("asics", "Asics"), ("head", "Head"), ("wilson", "Wilson"), ("dunlop", "Dunlop"), ("adidas", "Adidas"), ("babolat", "Babolat"))}.</p>'
          '<p>Na kurt patří obuv s podrážkou do písku nebo umělé trávy, běžecké boty se nehodí.</p>',
    faq=[('Jakou raketu pro začátečníka?', 'Kulatý tvar a sklolaminátový povrch. Má větší sweet spot a odpouští chyby.'),
         ('Jaká váha padelové rakety?', 'Obvykle 355 až 375 g. Lehčí je vhodnější pro začátek a ženy.'),
         ('Čím se padel liší od tenisu?', 'Hraje se ve čtyřech, na menším kurtu se stěnami, s raketou bez strun.'),
         ('Jaká obuv na padel?', 'Obuv určená pro padel s podrážkou pro písek nebo umělou trávu.'),
         ('Jak často měnit míče?', 'Podle opotřebení, ztrácejí tlak. U pravidelné hry zhruba každých několik zápasů.'),
         ('Hodí se padelová raketa pro děti?', 'Ano, jsou dětské verze s nižší hmotností a kratší rukojetí.')],
)

NEW['badminton'] = dict(short=True,
    title='Badminton – rakety, košíky a výbava | Sporteka',
    desc='Badmintonové rakety, košíky, sítě a obuv. Porovnejte ceny a váhu rakety pro rekreační hráče i závodníky v českých obchodech.',
    intro='<p><strong>Badminton</strong> je rychlá hra, ve které záleží na lehké raketě a dobré obuvi. Rekreační hráči si vystačí s cenově dostupnou raketou s ocelovým nebo hliníkovým rámem, '
          'zkušenější sáhnou po karbonové raketě. Důležité jsou váha, vyvážení a tuhost násady.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů. Další raketové sporty najdete v kategoriích <a href="/tenis/">tenis</a>, <a href="/squash/">squash</a> a <a href="/padel/">padel</a>.</p>',
    guide='<h2>Jak vybrat badmintonovou raketu</h2>'
          '<p>Badmintonová raketa je lehká, běžně 80 až 95 g. Při výběru zvažte váhu, vyvážení a tuhost.</p>'
          '<h3>Vyvážení</h3>'
          + T(['Vyvážení', 'Charakter'], [['Do hlavy', 'síla úderu, útočná hra'], ['Vyvážená', 'univerzální'], ['Do rukojeti', 'rychlost a obrana']]) +
          '<h3>Tuhost násady</h3>'
          '<p>Měkčí násada se lépe ohýbá a pomáhá začátečníkům s výkonem, tužší dává přesnost a vyžaduje techniku.</p>'
          '<h3>Košíky a sítě</h3>'
          '<ul><li><strong>Peříčkové košíky:</strong> na soutěže a klubovou hru, rychle se opotřebují.</li>'
          '<li><strong>Plastové košíky:</strong> odolnější, vhodné na venkovní hru a trénink.</li></ul>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Nabídka obsahuje {B(("yonex", "Yonex"), ("kuikma", "Kuikma"), ("babolat", "Babolat"), ("victor", "Victor"), ("nils", "Nils"), ("talbot-torro", "Talbot Torro"))}.</p>'
          '<p>Do haly patří sálová obuv s dobrou přilnavostí, která chrání kotníky při rychlých změnách směru.</p>',
    faq=[('Jakou badmintonovou raketu pro začátečníka?', 'Lehkou raketu s vyváženým vyvážením a měkčí násadou, cenově dostupnou.'),
         ('Jaká váha badmintonové rakety?', 'Obvykle 80 až 95 g. Údaj bývá označen 3U, 4U nebo 5U.'),
         ('Peříčkové, nebo plastové košíky?', 'Peříčkové pro soutěže, plastové pro rekreaci a venku.'),
         ('Hodí se badminton na zahradu?', 'Ano, s plastovými košíky a pevnou sítí. Vítr ale ovlivňuje let.'),
         ('Jak často měnit strunění?', 'Podle intenzity hry, rekreační hráči zhruba jednou ročně.'),
         ('Jaká obuv na badminton?', 'Sálová obuv s dobrou přilnavostí a oporou kotníku.')],
)

NEW['mestske-batohy'] = dict(short=True,
    title='Městské batohy – na notebook, do práce | Sporteka',
    desc='Městské batohy na notebook, do školy i do práce. Porovnejte ceny, objem a kapsy v českých obchodech.',
    intro='<p><strong>Městský batoh</strong> je každodenní společník do práce, školy i na výlet. Typický objem se pohybuje kolem 15 až 30 litrů, důležitá je vyztužená kapsa na notebook, pohodlné popruhy a zádová část. '
          'Dobrý městský batoh unese váhu, nepromokne a zůstane stylový.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů. Na túry zvolte <a href="/turisticke-batohy/">turistické batohy</a>, pro děti <a href="/skolni-batohy/">školní batohy</a>.</p>',
    guide='<h2>Jak vybrat městský batoh</h2>'
          '<p>Rozhoduje, co v něm nosíte. Notebook potřebuje polstrovanou kapsu, věci na cestu větší objem.</p>'
          '<h3>Objem</h3>'
          + T(['Použití', 'Objem'], [['Základní věci', '10–20 l'], ['Práce a notebook', '20–30 l'], ['Cestování', '30–40 l']]) +
          '<h3>Funkce</h3>'
          '<ul><li><strong>Kapsa na notebook:</strong> zkontrolujte maximální velikost displeje.</li>'
          '<li><strong>Nepromokavost:</strong> voděodolný materiál nebo pláštěnka.</li>'
          '<li><strong>Zádová část:</strong> vzdušná chrání před pocením.</li>'
          '<li><strong>Zabezpečení:</strong> skrytá kapsa na doklady.</li></ul>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("fjallraven", "Fjällräven"), ("deuter", "Deuter"), ("adidas", "Adidas"), ("vans", "Vans"), ("the-north-face", "The North Face"), ("nike", "Nike"), ("jansport", "JanSport"))}.</p>',
    faq=[('Kolik litrů má mít městský batoh?', 'Pro práci a notebook 20 až 30 litrů, na každodenní drobnosti stačí 15.'),
         ('Jaký batoh na notebook 15,6 palce?', 'S polstrovanou kapsou o odpovídajícím rozměru. Rozměry ověřte v popisu.'),
         ('Je městský batoh nepromokavý?', 'Záleží na materiálu. Hledejte označení voděodolný, nebo použijte pláštěnku.'),
         ('Jak vyčistit batoh?', 'Ručně vlažnou vodou a jemným mýdlem, bez pračky.'),
         ('Hodí se do letadla?', 'Pokud odpovídá limitům příručního zavazadla dopravce, ano. Ověřte rozměry.'),
         ('Jak ho správně nastavit?', 'Popruhy utáhněte tak, aby batoh přiléhal k zádům a nevisel.')],
)

NEW['softshellove-bundy'] = dict(short=True,
    title='Softshellové bundy – pánské, dámské | Porovnání cen',
    desc='Softshellové bundy do větru a lehkého deště: pánské, dámské a dětské. Porovnejte ceny a velikosti v českých obchodech.',
    intro='<p><strong>Softshellová bunda</strong> je univerzální vrstva do jara a podzimu. Chrání před větrem, snese lehký déšť a zároveň dobře prodýchává. '
          'Na rozdíl od <a href="/nepromokave-bundy/">nepromokavých bund</a> není určena na vytrvalý déšť, na rozdíl od <a href="/zimni-bundy/">zimních bund</a> nehřeje v mrazu.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů a vybíráte podle značky, velikosti a ceny. Další bundy najdete v kategorii <a href="/sportovni-bundy/">sportovní bundy</a>.</p>',
    guide='<h2>Jak vybrat softshellovou bundu</h2>'
          '<p>Softshell je kompromis mezi pohodlím a ochranou. Vyberte ho na aktivity, kdy se hodně pohybujete.</p>'
          '<h3>Vrstvy a funkce</h3>'
          '<ul><li><strong>Bez podšívky:</strong> lehká, prodyšná, na jaro a podzim.</li>'
          '<li><strong>S fleecovou podšívkou:</strong> teplejší, na chladnější dny.</li>'
          '<li><strong>S membránou:</strong> lepší odolnost proti vodě, nižší prodyšnost.</li></ul>'
          '<h3>Na co se dívat</h3>'
          '<p>Kapuce (pevná nebo odnímatelná), kapsy na zip, nastavitelné manžety a spodní lem. Prodyšnost a odolnost proti vodě se udávají v hodnotách, orientujte se podle účelu.</p>'
          '<h3>Velikost</h3>'
          '<p>Bunda má přiléhat, ale nesmí omezovat pohyb. Pod softshell se vejde tenká vrstva, silnější mikinu už ne.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("trespass", "Trespass"), ("regatta", "Regatta"), ("kilpi", "Kilpi"), ("loap", "Loap"), ("haglofs", "Haglöfs"), ("northfinder", "Northfinder"), ("helly-hansen", "Helly Hansen"), ("hannah", "Hannah"))}.</p>'
          '<p>Praní provádějte podle návodu, bez aviváže, která zhoršuje prodyšnost.</p>',
    faq=[('Co je softshell?', 'Pružný, větruodolný a prodyšný materiál, který snese lehký déšť. Hodí se na jaro a podzim.'),
         ('Je softshell nepromokavý?', 'Je odolný proti lehkému dešti. Na vytrvalý déšť je lepší nepromokavá bunda.'),
         ('Jak prát softshell?', 'Při 30 °C, bez aviváže, podle štítku. Impregnaci můžete obnovit sprejem.'),
         ('Hodí se softshell do zimy?', 'Jen s teplou vrstvou pod ním nebo s fleecovou podšívkou.'),
         ('Jakou velikost zvolit?', 'Podle tabulky výrobce, bunda má přiléhat, ale nesmí omezovat pohyb.'),
         ('Jak se liší od zimní bundy?', 'Je lehčí a pružnější, ale nehřeje tolik.')],
)

NEW['sportovni-rukavice'] = dict(short=True,
    title='Sportovní rukavice – zimní, běžecké, lyžařské | Sporteka',
    desc='Sportovní rukavice na běh, lyže, kolo i zimní sporty. Porovnejte ceny a velikosti v českých obchodech.',
    intro='<p><strong>Sportovní rukavice</strong> se vybírají podle sportu. Běžecké jsou tenké a lehké, lyžařské teplé a voděodolné, cyklistické mají polstrování dlaně. '
          'Správná velikost je důležitá, protože příliš těsné omezují pohyb a příliš volné nedrží.</p>'
          '<p>Na Sportece porovnáte ceny z českých obchodů. Pro kolo vyberte <a href="/cyklisticke-rukavice/">cyklistické rukavice</a>, pro boxerské sporty <a href="/boxerske-rukavice/">boxerské</a>, na zimu doplňte <a href="/cepice-a-celenky/">čepice a čelenky</a>.</p>',
    guide='<h2>Jak vybrat sportovní rukavice</h2>'
          '<p>Pro zimní sporty se rozhoduje mezi prstovými rukavicemi a palčáky. Palčáky jsou teplejší, prstové obratnější.</p>'
          '<h3>Typy podle sportu</h3>'
          '<ul><li><strong>Běžecké:</strong> lehké, tenké, často s úpravou na dotykový displej.</li>'
          '<li><strong>Lyžařské a snowboardové:</strong> izolované, voděodolné, s vyztuženou dlaní.</li>'
          '<li><strong>Cyklistické:</strong> polstrování dlaně, prodyšný hřbet.</li>'
          '<li><strong>Trekové:</strong> odolné a větruodolné.</li></ul>'
          '<h3>Velikost</h3>'
          + T(['Obvod dlaně', 'Velikost'], [['18–20 cm', 'S'], ['20–22 cm', 'M'], ['22–24 cm', 'L'], ['24–26 cm', 'XL']]) +
          '<p>Obvod měřte kolem dlaně pod prsty. Hodnoty jsou orientační.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>V nabídce jsou {B(("viking", "Viking"), ("rossignol", "Rossignol"), ("ziener", "Ziener"), ("reusch", "Reusch"), ("force", "Force"), ("reima", "Reima"), ("swix", "Swix"), ("dynafit", "Dynafit"))}.</p>',
    faq=[('Jaké rukavice na běhání?', 'Lehké a prodyšné. Při chladu vybírejte tenké fleecové, případně s ochranou před větrem.'),
         ('Palčáky, nebo prstové rukavice?', 'Palčáky jsou teplejší, prstové obratnější. Na lyže vhodné obojí.'),
         ('Jak vybrat velikost rukavic?', 'Změřte obvod dlaně pod prsty a porovnejte s tabulkou výrobce.'),
         ('Jak prát rukavice?', 'Podle štítku, nejlépe ručně vlažnou vodou. Nesušte na topení.'),
         ('Jsou rukavice voděodolné?', 'Záleží na modelu. Lyžařské rukavice mají membránu, běžecké většinou ne.'),
         ('Hodí se rukavice pro děti?', 'Ano, dětské velikosti se vybírají podle věku a obvodu dlaně.')],
)
