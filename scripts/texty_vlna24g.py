"""sporteka.cz — wave 24g (5. 11. 2026): long texts for jezdecka-obuv, jezdecke-helmy, cyklo-sedacky-a-voziky, bezecke-vazani.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ jezdecka-obuv
NEW['jezdecka-obuv'] = dict(long=True,
    title='Jezdecká obuv a chapsy: boty, minichapsy, výběr',
    desc='Jezdecké boty, minichapsy a chapsy pro děti i dospělé. Jak vybrat výšku, materiál, zip a velikost lýtka a porovnat nabídky českých obchodů.',
    intro='<p>Jezdecká obuv má dvě úlohy. Chrání nohu před šlápnutím koně a drží ji ve správné poloze ve třmenu, takže noha nemůže projet třmenem. Proto má jezdecká bota výraznou patku, hladkou podešev a pevnou špičku. V nabídce Sporteky porovnáte vysoké jezdecké boty, kotníčkové boty a minichapsy, tedy nízké kožené nebo textilní návleky, které se nosí přes boty. Všechny nabídky pocházejí z českých obchodů a my je řadíme tak, abyste rychle našli svou velikost i pro děti.</p>'
          '<p>Na výběr jsou značky ' + B(('fouganza', 'Fouganza'), ('dublin', 'Dublin'), ('horze', 'Horze'), ('lexhis', 'Lexhis'), ('sergio-grasso', 'Sergio Grasso'), ('hkm', 'HKM'), ('covalliero', 'Covalliero')) +
          '. Ke kompletní výbavě se hodí <a href="/jezdecke-kalhoty/">jezdecké kalhoty</a>, <a href="/jezdecke-helmy/">jezdecké helmy</a>, <a href="/jezdecke-obleceni/">jezdecké oblečení</a>, <a href="/jezdecke-doplnky/">jezdecké doplňky</a> a celá sekce <a href="/jezdectvi/">jezdectví</a>.</p>',
    guide='<h2>Jaké druhy jezdecké obuvi existují</h2>'
          '<p>Základní volba je mezi vysokou botou a kombinací nízké boty s chapsy. Obě varianty plní stejný účel, liší se pohodlím, cenou za pár, rychlostí obouvání a také tím, jak dobře sednou na lýtko. Pro rekreační jezdce a děti, kterým rychle roste noha, bývá praktičtější druhá možnost.</p>'
          + T(['Typ', 'Charakteristika', 'Hodí se pro'], [
              ['Vysoké jezdecké boty', 'sahají pod koleno, zip nebo šněrování, tuhá patka', 'pravidelný trénink, drezuru, skoky a závody'],
              ['Kotníčkové jezdecké boty', 'nízké, s elastickými vsadkami nebo šněrováním', 'kombinace s chapsy, ježdění ve stáji, začátečníky'],
              ['Chapsy a minichapsy', 'návlek na lýtko přes kotníčkovou botu, zip nebo suchý zip', 'děti, rekreační a školní jezdectví'],
              ['Dětské jezdecké boty', 'menší velikosti, jednodušší zapínání', 'jezdecké kroužky a první sezónu v sedle'],
              ['Zimní jezdecké boty', 'podšívka, silnější podešev, často vyšší lýtko', 'venkovní ježdění v chladném počasí']
           ]) +
          '<h2>Boty, nebo chapsy?</h2>'
          '<p>Vysoká bota drží lýtko jako celek, takže jezdec nepotřebuje žádný další díl. Sedí pevně, vypadá jednotně a při soutěžích nebývá výhrada k vzhledu. Nevýhodou je, že musí přesně sedět na obvod lýtka i délku nohy, a dokud se kůže nerozchodí, bývá tuhá. Kombinace kotníčkové boty s chapsy je volnější. Obuv a návleky se dají vyměňovat samostatně, takže když dítěti naroste lýtko, koupíte jen chapsy. Také se lépe nosí mimo sedlo, protože kotníčková bota je pohodlnější při chůzi ve stáji.</p>'
          '<p>Minichapsy jsou nižší než klasické chapsy a sahají zhruba do poloviny lýtka. Hodí se k jezdeckým rajtkám a nosí se s nimi kotníčková bota. Vyberte je, pokud jezdíte jen občas a nechcete investovat do vysokých bot.</p>'
          '<h2>Jak vybrat velikost a obvod lýtka</h2>'
          '<p>U vysokých bot rozhodují tři míry. Velikost chodidla, výška lýtka od paty po záhyb pod kolenem a obvod lýtka v nejširším místě. Změřte je ráno, kdy je noha nejmenší, a pak odpoledne, kdy otéká. U bot, které se zapínají zipem, ověřte, zda se zip zavře i přes silnější jezdeckou ponožku, a u pružných vsadek, zda nesvírají cévy.</p>'
          '<ul><li><strong>Výška lýtka:</strong> bota nesmí tlačit do záhybu kolena, když pokrčíte nohu ve třmenu.</li>'
          '<li><strong>Obvod lýtka:</strong> příliš úzká bota se dře o kalhoty, příliš široká se krabatí a špatně drží.</li>'
          '<li><strong>Velikost chodidla:</strong> špička má mít malou rezervu, ale patka nesmí v botě sjíždět.</li>'
          '<li><strong>Šířka nártu:</strong> u kotníčkových bot je důležitá, protože nárt se v sedle tlačí na třmen.</li></ul>'
          '<p>Chapsy se vybírají hlavně podle obvodu lýtka a výšky. Návlek by měl obepnout lýtko bez záhybů a nesmí se při chůzi posouvat. Pokud je velikostní tabulka u nabídky, měřte podle ní a ne podle čísla na tenisce.</p>'
          '<h2>Materiál, podešev a konstrukce</h2>'
          '<p>Nejčastějším materiálem je kůže a syntetická kůže. Kožené boty se po rozchození přizpůsobí noze, lépe dýchají a při správné péči vydrží mnoho sezón. Syntetické a textilní modely jsou lehčí, rychleji schnou a nevadí jim občasné promoknutí, ale špatně se přizpůsobí noze. Minichapsy se vyrábí z kůže, mikrovlákna i z perforovaného materiálu, který odvádí teplo v létě.</p>'
          '<p>Podešev jezdecké boty je hladká a má jasně oddělenou patku. Patka musí být alespoň tak vysoká, aby noha nemohla projet třmenem. Podrážka se nesmí podobat treku s hlubokým vzorem, protože hluboký vzor se zasekne ve třmenu. To je největší bezpečnostní riziko u nevhodné obuvi, a proto na koni nenoste turistické boty ani tenisky.</p>'
          '<h3>Zapínání</h3>'
          '<p>Zip na zadní nebo vnitřní straně se obouvá nejrychleji. Elastická vložka v zadní části, tzv. pružný klín, usnadní zapnutí u lýtka s větším obvodem. Šněrování dovolí přesné nastavení, ale zabere víc času. U chapsů se používá zip, přezky nebo suchý zip. Dětem se hodí jednodušší zapínání, aby se obouvaly bez pomoci.</p>'
          '<h2>Výběr podle disciplíny</h2>'
          '<p>Pro drezuru jsou ideální vyšší, tuhé boty bez vzorů, které vizuálně prodlužují nohu a drží ji v klidné poloze. Při skocích se hodí pružnější vsadky v oblasti kotníku, protože jezdec skáče s kratšími třmeny a více ohýbá kotník. Pro vyjížďky do terénu zvolte pevnou patku a dobře přiléhající chapsy nebo vysokou botu. V západním stylu se nosí jiné boty s vyšší patkou, ty se v nabídce vyskytují jen sporadicky.</p>'
          '<p>Při práci v zemi, třeba čištění koně a práci ve stáji, chrání nohy pevná špička a nepromokavý materiál. Jezdecká obuv není vhodná pro lyžování či turistiku, ale jako stájová bota obstojí dobře.</p>'
          '<h2>Péče o jezdeckou obuv</h2>'
          '<p>Kožené boty po ježdění otřete vlhkým hadrem, odstraňte hlínu a pot a nechte je schnout při pokojové teplotě, nikdy na topení. Jakmile kůže zbělá nebo zešedne, použijte krém nebo balzám na kůži a nechte jej vsáknout. Pak botu vyleštěte kartáčem. Do bot vložte napínáky, aby neztratily tvar.</p>'
          '<ul><li>Zip občas potřete vhodným mazivem nebo svíčkou, aby se nezasekával.</li>'
          '<li>Chapsy po ježdění rozepněte a nechte vyvětrat. Vlhkost uvnitř urychluje stárnutí materiálu.</li>'
          '<li>Boty, které jste použili v dešti, vycpěte novinami, ale papír po hodině vyměňte.</li>'
          '<li>Jednou za sezónu zkontrolujte švy a patku. Uvolněná patka je znamením, že je čas na opravu u obuvníka.</li></ul>'
          '<h2>Rozchození a první týdny s novou botou</h2>'
          '<p>Nová kožená bota je zpočátku tužší, než se čekalo, hlavně v kotníku a na zadní straně lýtka. První dny ji nosit doma několik hodin, pak na krátkém ježdění a až potom na celý trénink. Pomáhá tenká jezdecká ponožka bez švů, protože šev tře o kůži a vytvoří puchýř. Pokud bota tlačí na jednom místě, nepoužívejte silný tlak. Obuvník ji umí lokálně roztáhnout, a to je lepší než šít novou.</p>'
          '<p>Chapsy se rozchází rychleji než vysoké boty, ale i ony se musí usadit. Při prvním ježdění zkontrolujte, zda se spodní hrana neopírá o kotník a zda zip nedře o kalhoty. Návlek má sedět tak, aby se při pokrčeném kolenu nevytvářel tlak v záhybu.</p>'
          '<h2>Co nosit pod botu a kolem ní</h2>'
          '<p>Jezdecká ponožka má být vyšší než bota, aby se okraj nedotýkal kůže, a dobře odvádět vlhkost. Bavlněné silné ponožky se zapaří a zvětší objem v botě, takže se bota zapíná obtížněji. V zimě je lepší vrstva termoprádla a tenká vlněná ponožka než jedna silná. Teplé ponožky najdete také mezi <a href="/lyzarske-ponozky/">lyžařskými ponožkami</a>, ale pozor na tloušťku. Jezdecké kalhoty mají mít spodní okraj hladký, aby netlačil pod chapsem. Pro dětské kroužky je praktická jednoduchá kombinace pružných kalhot a nízké boty s minichapsy.</p>'
          '<h2>Jezdecká obuv pro děti</h2>'
          '<p>Děti rostou rychle a velikost se může měnit několikrát za sezónu. Nejpraktičtější je koupit boty, které sedí hned, a ne o dvě čísla větší. Chapsy a minichapsy mají nastavitelný obvod, takže prodlouží životnost. Pro děti je důležité jednoduché zapínání, protože malé ruce nezvládnou složitý zip. Zkontrolujte, zda je podešev dostatečně hladká a zda patka nemá příliš nízký sklon. Pro zimní tréninky venku vybírejte boty s podšívkou, ale tak, aby se vešla jedna tenká ponožka. Pokud dítě jezdí jen sporadicky, může se vyplatit půjčit boty od kroužku a až po několika měsících koupit vlastní.</p>'
          '<h2>Jak poznat, že je čas boty vyměnit</h2>'
          '<ul><li>Podešev je vyšoupaná a ztratila hladký profil, takže noha ve třmenu drží nebezpečně nebo naopak sklouzává.</li>'
          '<li>Patka se viklá, odlepuje se nebo je výrazně seřezaná na jedné straně.</li>'
          '<li>Kůže praská v ohybech a už ji nespraví ani krém.</li>'
          '<li>Zip se nedá bezpečně zavřít nebo se sám otevírá při chůzi.</li>'
          '<li>Dítěti bota tlačí na špičku nebo ve výšce lýtka.</li></ul>'
          '<p>Lehčí opotřebení spraví obuvník. Výměna podrážky u vysokých bot je často levnější než nákup nových, ale jen pokud je svršek v dobrém stavu.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Koupě na vyrůstání:</strong> příliš velká bota ve třmenu sjíždí a hrozí, že noha prokluzuje.</li>'
          '<li><strong>Špatné měření lýtka:</strong> boty, které sedí na chodidlo, ale nezapnou se přes lýtko, jsou nejčastější důvod vrácení.</li>'
          '<li><strong>Záměna sportovní obuvi za jezdeckou:</strong> v nabídkách se ojediněle objevují sportovní boty s podobným názvem, ale s jiným určením. Vždy zkontrolujte popis a podešev.</li>'
          '<li><strong>Nošení chapsů bez kvalitních kotníčkových bot:</strong> měkká bota bez patky nenahradí jezdeckou obuv.</li>'
          '<li><strong>Zanedbání rozchození:</strong> nové vysoké boty nenoste první den celý den. Rozchoďte je krátkými procházkami.</li></ul>'
          '<h2>Kde to nejlépe využít a jak nakupovat</h2>'
          '<p>Pro děti, které s jezdectvím teprve začínají, zvolte jednoduché kotníčkové boty a minichapsy, protože výdaje jsou nízké a nohy rostou. Pro pravidelné jezdce stojí za zvážení kvalitní kožené vysoké boty. Na Sportece porovnáte obchody podle dostupnosti velikostí a doby dodání. Před objednávkou zkontrolujte, jak obchod řeší výměnu, protože vysoké boty se často vyměňují kvůli lýtku.</p>'
          '<p>K botám doplňte <a href="/jezdecke-kalhoty/">jezdecké kalhoty</a> se správnou délkou a vybavení pro koně z kategorie <a href="/vybaveni-pro-kone/">vybavení pro koně</a>. Pokud začínáte, nezapomeňte na <a href="/jezdecke-helmy/">jezdeckou helmu</a>, která je důležitější než jakýkoli módní doplněk.</p>',
    faq=[('Jaký je rozdíl mezi jezdeckými botami a chapsy?', 'Jezdecká bota je vysoká a drží lýtko sama. Chapsy jsou návlek na lýtko, který se nosí přes kotníčkovou botu. Chapsy jsou levnější a snadno se vyměňují, vysoká bota sedí pevněji.'),
         ('Mohu jezdit v tenisce nebo turistické botě?', 'Nedoporučuje se. Hluboký vzor podrážky se může zachytit ve třmenu a chybí podpatěnka. Pro jízdu volte obuv s hladkou podešví a výraznou patkou.'),
         ('Jak změřit obvod lýtka?', 'Měřicí páskou v nejširším místě lýtka, vsedě s pokrčeným kolenem a ve stejných kalhotách, které budete nosit na koni. Hodnotu porovnejte s tabulkou výrobce.'),
         ('Jsou minichapsy vhodné pro děti?', 'Ano, pro rekreační a výukové jezdectví jsou praktické. Kotníčková bota s patkou doplněná minichapsy dobře chrání lýtko a dá se snadno vyměnit, když dítě vyroste.'),
         ('Kožené, nebo syntetické boty?', 'Kůže se přizpůsobí noze a vydrží déle, ale vyžaduje péči. Syntetika je lehčí, rychleji schne a hodí se na začátky nebo pro děti.'),
         ('Jak často mám boty mazat?', 'Po každém větším zamoknutí a jinak podle stavu kůže, zhruba jednou za několik týdnů. Povrch nesmí být vysušený ani zešedlý.'),
         ('Jak vyčistit pot z jezdeckých bot?', 'Po ježdění boty vyvětrejte, vložte do nich napínáky a nechte je schnout při pokojové teplotě. Zápach omezí také vyměnitelné vložky.'),
         ('Co dělat, když zip vázne?', 'Očistěte zip kartáčkem a potřete ho voskem nebo svíčkou. Pokud je zip prasklý, nechte jej vyměnit v opravně obuvi, ne ho přetahujte silou.'),
         ('Hodí se jezdecké boty i na chození po stáji?', 'Kotníčkové boty ano, vysoké boty jsou na delší chůzi tužší. Pro práci ve stáji se hodí nepromokavý materiál a pevná špička, která chrání při šlápnutí koně.'),
         ('Na co si dát pozor při nákupu online?', 'Na velikostní tabulku, obvod lýtka a podmínky výměny. Zkontrolujte také, zda nabídka obsahuje opravdu jezdeckou obuv, ne sportovní botu s podobným názvem.')],
)

# ------------------------------------------------------------------ jezdecke-helmy
NEW['jezdecke-helmy'] = dict(long=True,
    title='Jezdecké helmy a přilby: velikost, typy, výběr',
    desc='Jezdecké helmy a přilby pro děti i dospělé. Jak vybrat velikost, ventilaci a typ podle disciplíny a porovnat nabídky českých obchodů.',
    intro='<p>Jezdecká helma chrání hlavu při pádu z koně, k němuž dochází z výšky a často velkou rychlostí. Pro bezpečí musí helma přesně sedět, mít pevný podbradní pásek a nesmí být poškozená. Sporteka porovnává nabídku českých obchodů u přileb pro děti, dospělé, rekreační jezdce i závodníky, od jednoduchých modelů s kšiltem po lakované a sametové varianty. Každá nabídka ukazuje velikost a dostupnost, takže si snadno vyberete model, který skutečně můžete mít doma za pár dní.</p>'
          '<p>Najdete zde značky ' + B(('fouganza', 'Fouganza'), ('br', 'BR'), ('gpa', 'GPA'), ('qhp', 'QHP'), ('tattini', 'Tattini'), ('antares', 'Antares'), ('covalliero', 'Covalliero'), ('usg', 'USG'), ('kep', 'KEP')) +
          '. K helmě se hodí <a href="/jezdecka-obuv/">jezdecká obuv</a>, <a href="/jezdecke-kalhoty/">jezdecké kalhoty</a>, <a href="/jezdecke-obleceni/">oblečení</a>, <a href="/jezdecke-doplnky/">doplňky</a> a celá sekce <a href="/jezdectvi/">jezdectví</a>.</p>',
    guide='<h2>Jaké typy jezdeckých přileb existují</h2>'
          '<p>Přilby se liší kšiltem, ventilací, povrchem a konstrukcí. Pro rekreační ježdění nebo kroužek stačí jednoduchá přilba s regulací obvodu. Závodníci často volí lakovanou nebo sametovou přilbu, která odpovídá pravidlům disciplíny a lépe vypadá.</p>'
          + T(['Typ', 'Charakteristika', 'Hodí se pro'], [
              ['Rekreační přilba', 'plastová skořepina, ventilační otvory, regulace obvodu', 'začátečníky a vyjížďky'],
              ['Dětská přilba', 'menší velikosti, někdy s nastavitelným kolečkem', 'děti, které rychle rostou'],
              ['Přilba s kšiltem', 'pevný nebo odnímatelný kšilt, často v klasickém tvaru', 'drezuru a skoky'],
              ['Lakovaná přilba', 'lesklý nebo matný povrch, často s ozdobnými lištami', 'závody a soutěžní vystoupení'],
              ['Sametová přilba', 'potah z textilu, tradiční vzhled', 'trénink a drezuru'],
              ['Přilba s ventilací', 'velké průduchy, otvory v horní části', 'léto a intenzivnější ježdění']
           ]) +
          '<h2>Jak změřit velikost hlavy</h2>'
          '<p>Správná velikost je důležitější než značka. Změřte obvod hlavy měkkým krejčovským metrem asi 1 cm nad obočím a nad ušima, nejširším místem, a nechejte pásku vodorovně. Změřte dvakrát a použijte větší hodnotu. Pak ji porovnejte s tabulkou výrobce, protože značky se liší.</p>'
          '<ul><li><strong>Přilba sedí rovně:</strong> okraj je zhruba o prst nad obočím, ne na čele ani v týlu.</li>'
          '<li><strong>Po zapnutí nehybná:</strong> při zakývání hlavou se nepohybuje nezávisle na pokožce.</li>'
          '<li><strong>Pásek pod bradou:</strong> těsně přilehlý, ale nedusí. Mezi bradou a páskem projde jeden prst.</li>'
          '<li><strong>Bez bolesti:</strong> po deseti minutách nosit bez tlaku na čelo či spánky.</li></ul>'
          '<p>U dětí nikdy nekupujte helmu o číslo větší na vyrůstání. Velká přilba při pádu sklouzne a nechrání. Regulační kolečko vzadu pomůže jen s drobnou změnou obvodu.</p>'
          '<h2>Konstrukce a bezpečnost</h2>'
          '<p>Přilba se skládá z tvrdé skořepiny, vnitřní pěnové vrstvy pohlcující náraz, vložky pro pohodlí a pásků. Skořepina rozloží sílu nárazu a pěna ho utlumí. Po silném úderu je pěna poškozená, i když to není zvenku vidět, proto helmu po pádu na tvrdý povrch vyměňte. Totéž platí pro prasklinu nebo uvolněný pásek.</p>'
          '<p>Při nákupu hledejte údaje o certifikaci podle norem, například EN 1384, PAS 015, VG1 nebo ASTM/SEI, které výrobce uvádí v popisu nebo na štítku v přilbě. Značení by mělo být jasně čitelné a soutěžní řády mnohdy určují, jaké certifikace přilby musí mít. Údaje si ověřte u organizátora, kterému chcete ježdění přizpůsobit.</p>'
          '<h3>Ventilace a vložka</h3>'
          '<p>Přilby s více otvory lépe odvádějí teplo, což ocení jezdci v letních měsících a při náročnějším tréninku. Vyjímatelná vložka se dá vyprat a prodloužit tak životnost přilby. Měkká a savá vložka je pohodlnější u dětí, které přilbu nosí celé hodiny.</p>'
          '<h2>Výběr podle disciplíny</h2>'
          '<p>V drezuře převládají klasické přilby s tradičním vzhledem, v soutěžích často s jemným zdobením. Při skocích jsou důležité kšilt a lehkost, protože jezdec se v sedle naklání dopředu. Pro vyjížďky a terén se hodí přilba s dobrou ventilací a upevněním. Při práci s mladými koňmi a na zemi doporučujeme také nosit přilbu, i když člověk na koni nesedí, protože kopnutí do hlavy je reálné riziko.</p>'
          '<p>Pro děti na kroužku většinou postačí robustní jednoduchý model s regulací. Dospělí, kteří jezdí často, ocení lehčí konstrukci a lepší ventilaci. Pokud v zimě jezdíte, zkontrolujte, zda se pod helmu vejde tenká čepice nebo čelenka, aniž by se změnil obvod.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Přilbu čistěte jemným mýdlem a vodou, nepoužívejte rozpouštědla, která poškodí pěnu a lak. Nesušte ji u topení ani v autě za sluncem. Skladujte ji v látkovém obalu v suchu, nikdy ne mezi těžkými věcmi, kde se může promáčknout. Neodkládejte ji na plot nebo na sedlo, kde by mohla spadnout.</p>'
          '<ul><li>Pásek a spona se kontrolují před každým použitím.</li>'
          '<li>Vložku sundejte a vyperte podle návodu.</li>'
          '<li>Po pádu, který přilba zachytila, ji vyřaďte.</li>'
          '<li>Starší přilby měňte i bez pádu, protože materiály stárnou. Doporučenou dobu výměny uvádí výrobce.</li></ul>'
          '<h2>Jak helmu správně nasadit a nastavit</h2>'
          '<p>Přilbu nasazujte rovně na hlavu, ne nakloněnou dozadu. Nejdřív nastavte obvod kolečkem v týlu nebo jiným systémem tak, aby přilba pevně obepínala hlavu. Pak upravte pásky u uší, aby tvořily trojúhelník pod ušním lalůčkem. Pásek pod bradou zapněte a utáhněte. Pak přilbu zkuste zatlačit dopředu i dozadu. Pokud se hýbe kůže na čele společně s přilbou, sedí dobře. Pokud přilba klouže, je velká nebo špatně nastavená.</p>'
          '<p>Vlasy mají být sepnuty tak, aby netvořily hrbol, který přilbu zvedá. Dlouhé vlasy se hodí do nízkého drdolu nebo copu. Silná gumička vzadu změní sedění, proto zkoušejte přilbu přesně s účesem, který budete mít na koni.</p>'
          '<h2>Přilba, nebo bezpečnostní vesta</h2>'
          '<p>Helma chrání hlavu a nedá se nahradit ničím jiným. Bezpečnostní vesta chrání trup a patří do skokové a terénní jízdy, ale s přilbou nesouvisí. U hlavy nemá smysl šetřit, protože zranění hlavy má nejvážnější následky. Dospělí i děti by měli nosit přilbu při každém nasednutí, při lonžování i při práci s neznámým koněm. Rekreační jezdec nemá smysl vystavovat se riziku jen kvůli tomu, že jede „jen krokem“. K pádu může dojít i v kroku.</p>'
          '<h2>Přilba pro začátečníka a pro pokročilého</h2>'
          '<p>Začátečník potřebuje jednoduchou přilbu, která dobře sedí a dá se snadno nastavit. Nepotřebuje zdobení, lak ani exkluzivní materiály. Pokud je začátek na kroužku, ověřte u trenéra, zda půjčují přilby, a rozhodněte, zda koupit vlastní. Vlastní přilba má hygienickou výhodu a sedí na vaši hlavu. Pokročilí jezdci ocení lehčí hmotnost, lepší ventilaci a vyměnitelnou vložku. Při soutěžích se používají přilby v předepsaných barvách, nejčastěji černé nebo tmavě modré, a s malým počtem ozdob.</p>'
          '<h2>Vzhled a doplňky</h2>'
          '<p>Přilba přichází s různými povrchy a barvami, od černé po světlé odstíny. Tmavá se v létě více zahřívá, světlá rychle špiní. Ozdobné pásky a kamínky jsou jen estetické a nemají vliv na ochranu. Přídavný kryt do deště, textilní potah a odnímatelný kšilt prodlužují využití přilby. Pokud potah nasazujete, ověřte, že nezakrývá ventilační otvory a nemění obvod.</p>'
          '<ul><li>Potah lze prát, snadno se vymění a chrání lak před poškrábáním.</li>'
          '<li>Taška na přilbu chrání před nárazy při převozu.</li>'
          '<li>Čelenka nebo tenká čepice pod přilbu pomůže v zimě, ale musí být velmi tenká.</li></ul>'
          '<h2>Přilba a hlavy dětí a mládeže</h2>'
          '<p>Hlava dítěte roste nerovnoměrně, proto zkontrolujte velikost přilby alespoň jednou za sezónu. Pokud přilba tlačí, vyměňte ji. Děti mají často tendenci přilbu povolit nebo si ji sundávat, proto je potřeba je naučit zapínání pásku jako automatický krok. Rodiče by měli pásek kontrolovat před každým nasednutím. Hravé vzory a barvy děti přilákají k tomu, aby ji nosily rády, a to je pro bezpečnost víc než cokoliv jiného.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Použitá přilba:</strong> neznáte její historii, a proto ji nekupujte z druhé ruky.</li>'
          '<li><strong>Cyklistická přilba místo jezdecké:</strong> chrání jinak a nemá tvar pro pády z koně.</li>'
          '<li><strong>Příliš volný pásek:</strong> přilba se při pádu může sklouznout z hlavy.</li>'
          '<li><strong>Výběr podle vzhledu:</strong> barva je až poslední kritérium, nejdřív sedí velikost.</li>'
          '<li><strong>Nošení pod kapucí či silnou čepicí:</strong> změní obvod a sedí hůř.</li></ul>'
          '<h2>Jak nakupovat</h2>'
          '<p>Na Sportece porovnáte nabídku českých obchodů podle velikosti a dostupnosti. Přilbu objednávejte jen v obchodě, který přijímá výměny, protože tvar hlavy se liší a nejlépe ho poznáte až na hlavě. Kdo řeší kompletní vybavení, najde i <a href="/jezdecka-obuv/">jezdeckou obuv</a>, <a href="/jezdecke-doplnky/">doplňky</a> a <a href="/vybaveni-pro-kone/">vybavení pro koně</a>. Pro méně zkušené jezdce je vhodné vybrat přilbu spolu s trenérem nebo v kamenné prodejně.</p>',
    faq=[('Jak poznám správnou velikost jezdecké helmy?', 'Změřte obvod hlavy nad obočím a nad ušima a porovnejte s tabulkou výrobce. Helma sedí rovně, nehýbe se po zapnutí a nic netlačí.'),
         ('Mám použít cyklistickou přilbu na koně?', 'Nedoporučuje se. Jezdecká přilba je navržena pro pády z výšky a chrání zadní část hlavy jinak než cyklistická.'),
         ('Kdy helmu vyměnit?', 'Po silnějším nárazu, při prasklině nebo poškozeném pásku. Také po době, kterou doporučuje výrobce, protože materiály stárnou.'),
         ('Mohu koupit použitou přilbu?', 'Nedoporučujeme, protože nevíte, zda nebyla nárazem poškozena. Poškození pěny není vidět zvenčí.'),
         ('Jak vybrat helmu pro dítě?', 'Podle změřeného obvodu hlavy, ne na vyrůstání. Regulační kolečko pomůže s drobnou změnou, ale velká helma by při pádu sklouzla.'),
         ('Jak čistit helmu?', 'Jemným mýdlem a vodou, vložku vyperte podle návodu. Nepoužívejte rozpouštědla a nesušte u topení.'),
         ('Je lakovaná přilba bezpečnější než sametová?', 'Bezpečnost určuje konstrukce a certifikace, ne povrch. Lak a samet jsou hlavně otázka vzhledu a soutěžních zvyklostí.'),
         ('Musí mít helma kšilt?', 'Ne vždy. Kšilt chrání před sluncem a je tradiční v drezuře a skocích, ale rekreační modely mohou být i bez něj.'),
         ('Co s přilbou v zimě?', 'Pod přilbu se vejde jen tenká čepice či čelenka. Pokud potřebujete více, nekupujte větší helmu, ale zvolte tenčí čepici nebo čelenku, aby helma dobře seděla.'),
         ('Jak přilbu skladovat?', 'Suchá, ve vzdušném obalu, mimo slunce a mimo těžké věci. Nenechávejte ji v rozpáleném autě.')],
)

# ------------------------------------------------------------------ cyklo-sedacky-a-voziky
NEW['cyklo-sedacky-a-voziky'] = dict(long=True,
    title='Dětské sedačky a vozíky za kolo: jak vybrat',
    desc='Dětské sedačky na kolo, cyklovozíky a přívěsy za kolo. Jak vybrat přední či zadní sedačku, vozík pro 1–2 děti nebo psa a porovnat obchody.',
    intro='<p>Dětská sedačka na kolo nebo vozík za kolo umožní vyrazit s dítětem na výlet i každodenní cestu. Správný výběr závisí na věku, hmotnosti dítěte, typu kola a tom, kam jezdíte. Sedačka je lehčí a obratnější, vozík pojme více dětí, zavazadla a často i dítě v chladném počasí. Sporteka porovnává nabídky českých obchodů u předních a zadních sedaček, vozíků pro děti i psy, přívěsů s jedním kolem a také náhradních dílů, jako jsou oje, kola a konektory.</p>'
          '<p>V nabídce jsou značky ' + B(('polisport', 'Polisport'), ('acra-sport', 'ACRA Sport'), ('bellelli', 'Bellelli'), ('thule', 'Thule'), ('hamax', 'Hamax'), ('bobike', 'Bobike'), ('yepp', 'Yepp'), ('topeak', 'Topeak')) +
          '. K tomu se hodí <a href="/detske-cyklohelmy/">dětské cyklohelmy</a>, <a href="/cyklisticke-helmy/">cyklistické helmy</a>, <a href="/cyklo-svetla/">světla</a>, <a href="/cyklo-zvonky-a-zrcatka/">zvonky a zrcátka</a> a <a href="/cyklo-prislusenstvi/">příslušenství</a>.</p>',
    guide='<h2>Sedačka, nebo vozík</h2>'
          '<p>Sedačka se upevní na kolo, takže dítě sedí poblíž rodiče a vidí dopředu. Vozík se táhne za kolem a je stabilní i při zastavení, jelikož má vlastní dvě kola. Rozhodují věk dítěte, počet dětí a místo, kde jezdíte.</p>'
          + T(['Řešení', 'Výhody', 'Omezení'], [
              ['Přední sedačka', 'dítě je blízko, vidí dopředu, vhodná pro menší děti', 'omezená hmotnost, ovlivňuje řízení a koleno'],
              ['Zadní sedačka na nosič', 'větší nosnost, déle vydrží s dítětem', 'dítě je za vámi, nosič musí sedět'],
              ['Zadní sedačka na rámu', 'nepotřebuje nosič, často odnímatelná', 'nesedí na každý rám'],
              ['Vozík pro děti', 'chrání před deštěm, pojme zavazadla a druhé dítě', 'širší, těžší, potřebuje místo na uskladnění'],
              ['Přívěs s jedním kolem', 'úzký, obratný, často pro zavazadla', 'dítě se většinou nepřepravuje'],
              ['Vozík pro psa', 'chráněný prostor, reflexní prvky', 'nosnost určuje výrobce']
           ]) +
          '<h2>Jaké sedačky v nabídce najdete</h2>'
          '<p>Přední sedačky se montují mezi sedlo a řídítka. Mají nižší nosnost, ale dítě vás vidí a vy ho. Zadní sedačky se montují na nosič nebo přímo na sedlovou trubku a vydrží déle, protože unesou těžší dítě. Některé modely mají odklápěcí upevnění, které dovolí sedačku z kola rychle sundat a nechat na kole jen úchyt.</p>'
          '<ul><li><strong>Polohování opěrky:</strong> pomáhá, když dítě během jízdy usne.</li>'
          '<li><strong>Nastavitelné stupačky:</strong> musí mít popruh, který zajistí nohy, aby se nedostaly do paprsků.</li>'
          '<li><strong>Pětibodový pás:</strong> bezpečně drží dítě v sedačce.</li>'
          '<li><strong>Chránič paprsků:</strong> obvykle součást sedačky nebo doplněk, a jeho přítomnost kontrolujte.</li></ul>'
          '<h2>Jak zjistit, zda sedačka sedne na vaše kolo</h2>'
          '<p>Nejčastější problém je kompatibilita. Zadní sedačky na rám se hodí jen pro kola s vhodným tvarem sedlové trubky a bez kolíku tlumiče. Karbonové rámy jsou citlivé na sevření a výrobce rámu obvykle upozorní, zda je upevnění dovoleno. Sedačky na nosič vyžadují pevný nosič se správnou nosností. Elektrokola mají někdy jiné rozměry rámu a baterii pod sedlem.</p>'
          '<p>Před nákupem zkontrolujte průměr sedlové trubky, délku nosiče, volné místo mezi řídítky a sedlem a zda sedačka nebrání brzdovým lankům. Pokud si nejste jistí, poraďte se v cykloservisu.</p>'
          '<h3>Věk a hmotnost dítěte</h3>'
          '<p>Dítě by mělo samo sedět, držet hlavu a nosit přilbu. To nastává zpravidla až po prvním roce života. Horní limit určuje nosnost sedačky uvedená výrobcem a nikdy ji nepřekračujte. Pokud dítě vyroste, přejděte na zadní sedačku s vyšší nosností nebo vozík.</p>'
          '<h2>Vozíky za kolo: co sledovat</h2>'
          '<p>Vozík musí mít spolehlivé spojení s kolem, pevný rám, bezpečnostní pásy a reflexní prvky. Dobrý vozík se skládá, aby se vešel do auta i sklepa. Jednomístné modely jsou menší a lehčí, dvoumístné pojmou sourozence. Některé vozíky se po přemontování stanou kočárkem nebo běžeckým kočárkem, což se hodí rodinám, které chtějí jedno zařízení na více účelů.</p>'
          '<ul><li><strong>Vlajka a světla:</strong> vozík je nízký a v provozu hůře viditelný, takže vlajka a světla jsou nutnost.</li>'
          '<li><strong>Rozvor kol a stabilita:</strong> širší kola jsou stabilnější v zatáčkách.</li>'
          '<li><strong>Odpružení:</strong> pomáhá při jízdě po nerovnostech a dětem se lépe spí.</li>'
          '<li><strong>Ochrana proti počasí:</strong> průhledný kryt, moskytiéra a stínění.</li>'
          '<li><strong>Vnitřní prostor:</strong> dítě v přilbě potřebuje hlavu s dostatečnou výškou nad opěrkou.</li></ul>'
          '<h2>Přívěsy pro zavazadla a vozíky pro psy</h2>'
          '<p>Přívěs s jedním kolem se hodí pro náklad, tedy zavazadla, stan nebo nákup. Často se připojuje k ose zadního kola a po kolejích sleduje stopu kola. Nenahrazuje dětský vozík, protože nemá pásy ani ochranu pro dítě. Vozík pro psa je prostorná kabina s pevným dnem, větráním a reflexními prvky. U vozíků pro psy sledujte nosnost uvedenou výrobcem, pevné uchycení vodítka uvnitř a snadný nástup.</p>'
          '<p>Náhradní díly, jako oje, kola, konektory a nárazníky, jsou v kategorii také. Slouží k opravě, když se poškodí tažná tyč nebo ztratí spojka, a ušetří vás výměny celého vozíku. Při koupi dílu vždy ověřte, pro který model je určen.</p>'
          '<h2>Bezpečnost za jízdy</h2>'
          '<ul><li>Dítě musí mít vlastní helmu, která mu přesně sedí. Pomůže <a href="/detske-cyklohelmy/">kategorie dětských cyklohelem</a>.</li>'
          '<li>Při nasazení sedačky se změní těžiště kola. Začněte na rovné cestě bez provozu a zkuste rozjezd, brzdění a zatáčky.</li>'
          '<li>Kolo s dítětem nikdy nenechávejte bez dozoru, protože se může převrhnout.</li>'
          '<li>Se sedačkou i vozíkem jezdíte pomaleji, s delší brzdnou dráhou. Zkontrolujte <a href="/cyklo-brzdy/">brzdy</a> a plášť.</li>'
          '<li>Vozík v provozu označte vlajkou a světly, dobré světlo najdete v kategorii <a href="/cyklo-svetla/">světla</a>.</li></ul>'
          '<h2>Údržba a skladování</h2>'
          '<p>Sedačky otírejte vlhkým hadříkem, textilní potahy lze prát podle návodu. Pravidelně kontrolujte šrouby, pásy a upevnění, protože vibrace je povolují. Vozík po dešti osušte, zkontrolujte tlak v kolech a promažte spojku. Skládací vozík skladujte v suchu a uzavřený. Kovové díly lehce naolejujte, abyste předešli korozi. Šroubovací pomůcky najdete v kategorii <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>.</p>'
          '<h2>Jak se jezdí s dítětem na kole</h2>'
          '<p>Kolo se sedačkou nebo s vozíkem se chová jinak. Je těžší, hůř se udržuje rovnováha při stání a delší je i brzdná dráha. Při nasedání držte kolo pevně a dítě usazujte až po stabilním postavení, nejlépe s pomocí druhé osoby. Zpočátku jezděte pomalu, zkuste prudší zatáčky a brzdění na prázdném prostranství. V zatáčkách se vyhýbejte prudkému naklonění. Vozík sleduje stopu kola po vnitřní straně zatáčky, proto zatáčejte o něco šířeji.</p>'
          '<p>Při rozjezdu do kopce se vyplatí nižší převod. S dítětem v sedačce raději volte cesty bez provozu, cyklostezky a zpevněné polní cesty. Nejezděte po kluzkých či mokrých dlažbách, kde hrozí smyk. Po dešti zkontrolujte, zda se do vozíku nenahromadila voda.</p>'
          '<h2>Oblečení a pohodlí dítěte</h2>'
          '<p>Dítě v sedačce nebo vozíku se nehýbe, takže mu je rychle chladno. Oblékejte je o vrstvu víc než sebe. Důležité jsou rukavice a čepice pod přilbu v chladném počasí. Naopak v létě pomáhá sluneční brýle, stínění a pití. U delších výletů dělejte přestávky, aby si dítě mohlo protáhnout nohy. Spící dítě v sedačce potřebuje vyšší opěrku nebo podepřenou hlavu, aby mu hlava nepadala. Ve vozíku pomáhá polstrování a odpružení.</p>'
          '<h2>Elektrokola a těžší jezdci</h2>'
          '<p>U elektrokol je důležité ověřit, zda výrobce rámu povoluje montáž sedačky nebo tažení vozíku. Některé modely nemají vhodný nosič nebo mají baterii na nosiči, takže se sedačka namontovat nedá. Pohon pomůže s rozjezdem a do kopce, ale brzdy zůstávají stejně důležité. Celková hmotnost kola, jezdce, dítěte a nákladu nesmí překročit limit výrobce kola. U těžších jezdců zkontrolujte nosnost nosiče a sedlovky.</p>'
          '<h2>Jak vybrat podle místa užití</h2>'
          '<ul><li><strong>Město:</strong> sedačka nebo úzký vozík, který se vejde do výtahu či chodby, a dobré osvětlení.</li>'
          '<li><strong>Cyklostezky a víkendové výlety:</strong> vozík s odpružením a prostorem na zavazadla.</li>'
          '<li><strong>Terén:</strong> větší kola a odpružení, jinak se dítě bude třást.</li>'
          '<li><strong>Dojíždění do školky:</strong> sedačka s rychlým snímáním a pevným pásem.</li>'
          '<li><strong>Rodina s dvěma dětmi:</strong> dvoumístný vozík nebo kombinace sedačky a vozíku podle věku dětí.</li></ul>'
          '<p>Pokud kolo používáte na delší trasy, hodí se i <a href="/cyklo-nosice-na-auto/">nosič na auto</a> a <a href="/cyklo-tasky-a-nosice/">tašky na kolo</a> pro zavazadla. Na hlídání kola při zastávce použijte <a href="/cyklo-zamky/">zámek</a>.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li><strong>Špatná kompatibilita:</strong> sedačka nebo vozík nesedí na kolo, jehož rám je nestandardní.</li>'
          '<li><strong>Brzké nasazení:</strong> dítě, které ještě nesedí samo, nepatří do sedačky.</li>'
          '<li><strong>Chybějící helma:</strong> i při krátké cestě.</li>'
          '<li><strong>Přetížení:</strong> zavazadla a dítě společně nesmí překročit nosnost.</li>'
          '<li><strong>Nezajištěné nohy:</strong> bez popruhu mohou zajet do paprsků.</li></ul>'
          '<h2>Jak nakupovat</h2>'
          '<p>Na Sportece porovnáte nabídky českých obchodů a zkontrolujete dostupnost. Před objednávkou si ověřte rozměry kola, nosnost, věk dítěte a to, jak se sedačka nebo vozík skládá. U dílů pro vozíky vždy kontrolujte shodu modelu. Pro vozík vyberte <a href="/cyklo-nosice-na-auto/">nosič na auto</a>, pokud chcete vyjet dál, a doplňte <a href="/cyklo-zamky/">zámek</a> a <a href="/cyklo-tasky-a-nosice/">tašky</a>.</p>',
    faq=[('Od kolika let může dítě jezdit v sedačce?', 'Dítě musí samo sedět, držet hlavu a nosit přilbu. To bývá obvykle po prvním roce. Konkrétní věk a hmotnost uvádí výrobce sedačky.'),
         ('Přední, nebo zadní sedačka?', 'Přední je pro menší děti, dítě je blízko a vidí dopředu. Zadní unese větší dítě, ale vyžaduje nosič nebo vhodný rám.'),
         ('Hodí se sedačka na karbonový rám?', 'Pouze pokud to výrobce rámu dovoluje, protože sevření může karbon poškodit. Bezpečnější je nosič nebo vozík.'),
         ('Mám pořídit vozík, nebo sedačku?', 'Sedačka je lehčí a obratnější. Vozík pojme více dětí, zavazadla a chrání před počasím, ale zabere víc místa.'),
         ('Musí mít dítě ve vozíku helmu?', 'Doporučujeme ji, protože vozík se může převrhnout. U některých vozíků je nutné ověřit, zda je uvnitř dost místa pro hlavu v helmě.'),
         ('Jak připojit vozík ke kolu?', 'Pomocí oje, která se připevní k ose zadního kola nebo k rámu. Dodržujte postup výrobce a přidejte bezpečnostní pojistku.'),
         ('Mohu v přívěsu vozit psa?', 'Ano, jestliže je vozík určen pro psy a pes nepřekračuje nosnost. Zkontrolujte větrání a bezpečné uchycení vodítka.'),
         ('Jak často kontrolovat šrouby a pásy?', 'Před každou delší jízdou. Vibrace a změny teploty uvolňují šrouby, a pásy mohou s časem ztrácet pevnost.'),
         ('Jsou náhradní díly univerzální?', 'Ne. Oje, kola a konektory se liší podle modelu, proto vždy ověřte shodu s názvem vozíku.'),
         ('Jak sedačku uskladnit?', 'Sejměte ji z kola, očistěte a uložte v suchu. Sluneční záření a mráz zkracují životnost plastu a textilu.')],
)

# ------------------------------------------------------------------ bezecke-vazani
NEW['bezecke-vazani'] = dict(long=True,
    title='Vázání na běžky: NNN, SNS, Prolink, výběr',
    desc='Vázání na běžecké lyže systémů NNN, NIS, SNS a Prolink. Jak vybrat podle bot a stylu, ověřit montáž a porovnat nabídky českých obchodů.',
    intro='<p>Vázání je spojení mezi botou a lyží a rozhoduje, jestli běžecká lyže poslechne každý pohyb nohy. Musí odpovídat systému bot, stylu jízdy a typu lyže. Nejčastěji se setkáte se systémy NNN, SNS a Prolink, často v kombinaci s montážní deskou NIS. Sporteka porovnává nabídky českých obchodů u vázání pro klasiku, bruslení, kombi, dětské a juniorské vázání i vázání na kolečkové lyže a pro terénní běžky. U každé nabídky uvádíme systém, takže se nespletete.</p>'
          '<p>V nabídce jsou značky ' + B(('rottefella', 'Rottefella'), ('salomon', 'Salomon'), ('fischer', 'Fischer'), ('kastle', 'Kästle'), ('rossignol', 'Rossignol'), ('kubisport', 'Kubisport'), ('skol', 'Skol')) +
          '. Pro kompletní výbavu hledejte také <a href="/bezecke-boty/">běžecké boty</a>, <a href="/bezecke-lyze/">běžecké lyže</a>, <a href="/lyzarske-hole/">lyžařské hole</a>, <a href="/lyzarske-vosky/">vosky</a>, <a href="/lyzarske-ponozky/">lyžařské ponožky</a> a <a href="/bezecke-lyzovani/">celé běžecké lyžování</a>.</p>',
    guide='<h2>Co všechno patří do kategorie vázání</h2>'
          '<p>Kromě klasických vázání na lyže najdete v nabídce také sady pro montáž, díly pro desky NIS, vázání pro kolečkové lyže a občas kompletní běžky s vázáním od výrobce. Kategorii proto prohlížejte podle názvu a systému, nikoli jen podle značky.</p>'
          + T(['Systém', 'Charakteristika', 'Poznámka'], [
              ['NNN', 'systém Rottefella s drážkami v podrážce boty a příčnou tyčí', 'velmi rozšířený, vyráběn více značkami'],
              ['NIS', 'montážní deska na lyži s lištami pro vázání', 'umožňuje posun vázání a výměnu'],
              ['SNS', 'starší systém Salomon s kolejnicí podél boty', 'vyžaduje boty SNS'],
              ['Prolink', 'novější systém Salomon, také s deskou', 'boty Prolink a vázání musí být kompatibilní'],
              ['Rollerski', 'vázání pro kolečkové lyže', 'stejný systém jako na zimních lyžích'],
              ['Terénní vázání', 'robustní a širší pro turistické běžky', 'pro vyšší a širší boty']
           ]) +
          '<h2>Jak vybrat správný systém</h2>'
          '<p>Nejdůležitější pravidlo zní: nejdříve boty, potom vázání. Bota určuje systém, protože podrážka a přední část mají přesně daný tvar. Systémy NNN a Prolink jsou navzájem kompatibilní, ale starší SNS je samostatný systém a s nimi se nemíchá. Pokud boty ještě nemáte, vybírejte spolu s vázáním a lyžemi podle toho, co nabízí obchod a co používají lidé kolem vás, protože nejsnáze se půjčuje, vyměňuje a servisuje oblíbený systém.</p>'
          '<p>Při koupi vázání zkontrolujte tři věci. Za prvé označení systému na botě, za druhé typ montáže na lyžích, tedy zda je na lyži deska NIS, nebo jde o holou lyži. Za třetí styl, kterému bota odpovídá, tedy klasika, bruslení nebo kombi.</p>'
          '<h3>Klasika, bruslení, kombi</h3>'
          '<p>Při klasickém stylu se noha pohybuje v dlouhém kroku a pata se zdvihá, takže vázání je pružnější. Bruslení vyžaduje tužší spojení a stabilnější patu, protože lyže se odráží do stran. Kombi vázání se snaží obojí spojit, hodí se rekreačním běžcům, kteří střídají styly. Závodníci obvykle používají specializovaná vázání a lyže pro daný styl.</p>'
          '<h3>Pružina a nastavení</h3>'
          '<p>Některá vázání pro klasiku mají pružinu s nastavením tuhosti nebo výměnnými prvky. Tvrdší pružina dává přesnější odraz, měkčí pohodlnější chůzi. Pro začátečníky a rekreační jezdce se hodí střední nastavení. Pružina sama o sobě nevadí, ale musí být nastavena na hmotnost běžce.</p>'
          '<h2>Montáž a deska NIS</h2>'
          '<p>Lyže bez desky se vrtají a vázání se montuje šrouby. Lyže s deskou NIS mají lištu, do které se vázání zasune nebo přišroubuje, takže se dá posunout dopředu či dozadu a doladit podle bot. Pozici vázání určuje výrobce lyže. Obvykle je vyznačena na bocích. Špatně posazené vázání změní vyvážení, takže lyže špatně klouže nebo nedrží stopu.</p>'
          '<ul><li>Vrtání si nechte u servisu, protože chybný otvor se opraví jen obtížně.</li>'
          '<li>Při montáži používejte správný šroubovák a návod výrobce.</li>'
          '<li>Po prvních kilometrech zkontrolujte dotažení šroubů.</li>'
          '<li>Při výměně vázání ověřte, že otvory v lyži odpovídají novému modelu.</li></ul>'
          '<h2>Dětské a juniorské vázání</h2>'
          '<p>Děti rostou a dětské boty se mění často, proto si pořiďte vázání, které se dá přenést na další lyže. Juniorská vázání mají jednodušší nastavení a bývají lehčí. Dětské boty mají často shodný systém s dospělými, ale menší velikosti. Při výběru dbejte, aby bota správně zacvakla a zároveň se dítěti snadno vyvlékala. Kompletní běžky pro děti obvykle už vázání obsahují a je výhodné je koupit jako sadu.</p>'
          '<h2>Vázání na kolečkové lyže a terén</h2>'
          '<p>Kolečkové lyže slouží k tréninku v létě a využívají stejné systémy jako zimní lyže, proto lze často použít stejné boty. Vázání pro kolečkové lyže je vyrobeno pro styl klasika nebo bruslení a není záměnné. Pro terénní a turistické běžky se používají robustnější vázání, která drží vyšší a širší boty. Pokud lyžujete mimo stopu, zvolte odolnější verzi a ověřte, že se hodí k obuvi.</p>'
          '<h2>Péče a servis</h2>'
          '<p>Vázání po sezóně očistěte od soli a písku. Lehce promažte pohyblivé části a zkontrolujte, zda není prasklá plastová část. Mechanismus zámku udržujte čistý, protože zamrzlý sníh může bránit zacvaknutí. Boty před nasazením oklepejte, aby se led nenahromadil v drážce.</p>'
          '<ul><li>Pravidelně kontrolujte šrouby, protože vibrace je povolují.</li>'
          '<li>Při přepravě lyže chraňte před poškozením vázání, použijte obal.</li>'
          '<li>Pokud se bota nezacvakává, vyčistěte drážku a zkontrolujte, zda není vázání ohnuté.</li>'
          '<li>Starší vázání zkontrolujte u servisu před sezónou.</li></ul>'
          '<h2>Jak se vázání liší podle úrovně běžce</h2>'
          '<p>Rekreační běžec potřebuje spolehlivé vázání, které se snadno zapíná a nevyžaduje časté seřizování. Pro něj jsou vhodná vázání střední třídy se základní pružinou. Sportovní běžec, který jezdí pravidelně a trénuje techniku, ocení vázání s lepším přenosem síly, nižší hmotností a jemným nastavením. Závodník vybírá podle disciplíny a podmínek, dokonce podle tvrdosti sněhu. Rozdíly se projeví hlavně v hmotnosti, tuhosti a v přesnosti vedení boty.</p>'
          '<p>Pokud začínáte, nehoňte se za závodními díly. Přínos je vidět až při dobré technice a vyšší rychlosti, zatímco na rekreačním tempu rozhoduje hlavně správné nastavení a bota, která pohodlně sedí.</p>'
          '<h2>Jak zjistit systém boty</h2>'
          '<p>Systém boty najdete na podrážce, v prostoru pod špičkou, nebo v popisu produktu. U bot NNN je na špičce příčná tyč a po jejím okraji vedou dvě drážky. U SNS je hlubší jedna střední drážka s tyčí. U Prolinku je tvar jiný, a proto se označení uvádí výslovně. Pokud označení nevidíte, zeptejte se prodejce nebo si vyhledejte model boty u výrobce. Nikdy nespoléhejte na to, že boty stejné značky mají stejný systém, protože výrobci často nabízejí oba.</p>'
          '<h2>Jak nastavit polohu vázání</h2>'
          '<p>Správná poloha vázání zajistí, že váha je rozložena mezi přední a zadní část lyže. Výrobce lyží udává referenční bod, který obvykle odpovídá těžišti lyže, a vázání se montuje podle délky boty. Posun na desce NIS umožňuje jemné doladění. Při posunu dopředu lyže více zatěžuje špičku, což zlepšuje vedení, ale zhoršuje stopu při klouzání. Posun dozadu dává lepší záběr, ale zhoršuje stabilitu. Experimentujte po malých krocích, nejlépe po milimetrech.</p>'
          '<h2>Skladování a sezónní kontrola</h2>'
          '<p>Po sezóně lyže s vázáním osušte a uložte v suchu a chladu, mimo slunce a topení. Vázání nechte uzavřené, aby se zámek nenamáhal. Před další sezónou zkontrolujte pružiny, plastové části a šrouby. Pokud se objeví trhlina, vázání vyměňte, protože prasklý díl může při zátěži selhat. Zámek lehce promažte silikonovým sprejem určeným pro plasty, ale přebytek odstraňte, aby se v něm nezachytávala špína.</p>'
          '<ul><li>Před sezónou zkuste zacvaknout botu na sucho a ověřte hlasité cvaknutí.</li>'
          '<li>Zkontrolujte, zda se vázání při zdvihnutí paty pohybuje plynule.</li>'
          '<li>Díly vázání nikdy neohýbejte silou, aby se nezměnila geometrie.</li></ul>'
          '<h2>Vázání a související výbava</h2>'
          '<p>Vázání je jen jeden díl systému. Stejně důležité jsou boty, lyže a hole. <a href="/bezecke-boty/">Běžecké boty</a> musí odpovídat systému a stylu, <a href="/bezecke-lyze/">lyže</a> určují délku, tuhost a typ skluznice. <a href="/lyzarske-hole/">Hole</a> by měly sahat zhruba k podpaží pro klasiku a k ústům nebo bradě pro bruslení. <a href="/lyzarske-vosky/">Vosky</a> upravují skluz i stoupání a bez nich lyže bez šupin neposlouchají. Teplé a prodyšné <a href="/lyzarske-rukavice/">rukavice</a> a <a href="/lyzarske-ponozky/">ponožky</a> dotvářejí pohodlí. Celý výběr najdete v sekci <a href="/bezecke-lyzovani/">běžecké lyžování</a>.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li><strong>Záměna systémů:</strong> vázání NNN nesedí na boty SNS a naopak.</li>'
          '<li><strong>Nejasnost u Prolinku:</strong> ověřte kompatibilitu u výrobce, než koupíte.</li>'
          '<li><strong>Špatný styl:</strong> vázání pro klasiku nenahradí bruslařské a naopak.</li>'
          '<li><strong>Montáž bez nářadí:</strong> improvizace často končí poškozením lyže.</li>'
          '<li><strong>Zanedbání čištění:</strong> led v zámku brání zacvaknutí.</li></ul>'
          '<h2>Jak nakupovat</h2>'
          '<p>Na Sportece porovnáte nabídky českých obchodů a vyfiltrujete systém, který potřebujete. Před objednávkou si zapište označení na botě, typ desky na lyžích a styl jízdy. Při nejistotě kontaktujte obchod. Vázání nekupujte podle fotky, ale podle popisu systému. K vázání nezapomeňte na <a href="/lyzarske-vosky/">vosky</a>, <a href="/lyzarske-hole/">hole</a> a <a href="/lyzarske-rukavice/">rukavice</a>.</p>',
    faq=[('Jak poznám, jaké vázání potřebuji?', 'Podle označení na botě. SNS se nedá zaměnit s NNN, zatímco NNN a Prolink jsou navzájem kompatibilní. Vázání musí odpovídat systému boty.'),
         ('Mohu kombinovat NNN a SNS?', 'Ne. Jde o dva různé systémy a bota funguje jen s vázáním stejného systému.'),
         ('Co je deska NIS?', 'Montážní deska na lyži s lištami, do kterých se vázání zasune nebo přišroubuje. Umožňuje posun vázání i výměnu bez nového vrtání.'),
         ('Je vázání na klasiku jiné než na bruslení?', 'Ano. Klasika vyžaduje pružnější vázání se zdvihem paty, bruslení tužší a stabilnější. Kombi vázání se snaží spojit obojí.'),
         ('Kdy použít vázání na kolečkové lyže?', 'Při letním tréninku. Vázání má stejný systém jako zimní, ale je určeno pro konkrétní kolečkovou lyži.'),
         ('Mohu vázání namontovat sám?', 'Na lyži s deskou NIS je to snadnější. U vrtaných lyží doporučujeme servis, protože špatný otvor poškodí lyži.'),
         ('Jak často kontrolovat šrouby?', 'Po prvních kilometrech a pak před každou sezónou. Vibrace a změny teploty je mohou povolit.'),
         ('Hodí se dětské vázání pro další lyže?', 'Často ano, když je systém stejný. Při koupi ověřte, zda bude odpovídat budoucím botám.'),
         ('Proč se bota nezacvakává?', 'Nejčastěji kvůli ledu či nečistotě v drážce nebo poškozenému zámku. Očistěte oboje a zkontrolujte tvar vázání.'),
         ('Mám volit vázání podle značky lyží?', 'Rozhodující je systém bot a desky na lyžích. Značka je druhotná, když se systémy shodují.')],
)

# ------------------------------------------------------------------ additional FAQ
NEW['jezdecke-helmy']['faq'] += [
    ('Jak poznám, že je přilba poškozená?', 'Hledejte praskliny ve skořepině, promáčklá místa, uvolněný nebo roztřepený pásek a poškozenou sponu. Skryté poškození pěny uvnitř zvenčí nevidíte, proto přilbu po silnějším nárazu raději vyřaďte, i když vypadá celá. Totéž platí, pokud vám přilba spadla z velké výšky na tvrdý povrch.'),
    ('Můžu přilbu půjčit kamarádce nebo sourozenci?', 'Z hygienických i bezpečnostních důvodů je lepší mít vlastní. Každá hlava má jiný tvar a přilba se postupně přizpůsobí vložkou a pěnou konkrétnímu uživateli. Půjčená přilba může sedět hůře a nechrání tak, jak má. V kroužcích bývají půjčovací přilby, ty se ale pravidelně kontrolují a čistí.'),
    ('Musím nosit helmu i při práci na zemi?', 'Doporučuje se při lonžování, vodění mladých nebo neznámých koní a všude tam, kde hrozí kopnutí či uskočení. Zranění hlavy se stávají i mimo sedlo, a proto stojí za to nosit přilbu při jakékoli práci s koněm, kdy nemáte plnou kontrolu nad jeho reakcí.')]
NEW['cyklo-sedacky-a-voziky']['faq'] += [
    ('Jak dlouho může dítě bezpečně jet na jeden zátah?', 'Záleží na věku, počasí a tom, zda dítě spí. U menších dětí se doporučují krátké úseky s přestávkami, aby si protáhly nohy a napily se. Při chladu nebo horku zkraťte etapy. Pokud je dítě nespokojené, zastavte a zkontrolujte, zda ho nic netlačí a není mu zima.'),
    ('Dá se vozík použít jako kočárek?', 'Některé modely mají sadu pro přestavbu na kočárek nebo běžecký kočárek, obvykle s předním kolem a madlem. Vždy ověřte v popisu výrobce, zda daný model tuto funkci má, protože běžný cyklovozík bez přestavby jako kočárek nefunguje bezpečně a pohodlně.')]
NEW['bezecke-vazani']['faq'] += [
    ('Kolik lyží se hodí na jedno vázání?', 'Samotné vázání se při přemontování dá použít na další lyže, ale jen pokud máte kompatibilní montáž a uchycení. Lyže s deskou NIS usnadňují výměnu, u vrtaných lyží je každé přemontování zásahem do materiálu a otvory se nedají znovu použít donekonečna. Rozhodněte se podle toho, kolik párů lyží plánujete.'),
    ('Jak poznám opotřebené vázání?', 'Typickým znakem je volný zámek, který se při běhu uvolňuje, prasklé plastové díly, ohnutý kov nebo ztuhlá pružina, která se nevrací do původní polohy. Pokud se bota po zacvaknutí viditelně hýbe do stran nebo se rozepíná sama, nechte vázání zkontrolovat a podle potřeby vyměňte.')]

# ------------------------------------------------------------------ additional guide paragraphs
NEW['jezdecka-obuv']['guide'] += ('<h2>Související výbava</h2>'
    '<p>K obuvi patří celek, který společně tvoří bezpečné a pohodlné ježdění. <a href="/jezdecke-kalhoty/">Jezdecké kalhoty</a> se zesílením na vnitřní straně chrání před odíráním, <a href="/jezdecke-obleceni/">jezdecké oblečení</a> a vrstvy podle počasí drží teplo. <a href="/jezdecke-doplnky/">Doplňky</a> jako rukavice a pláštěnky řeší detaily a <a href="/vybaveni-pro-kone/">vybavení pro koně</a> doplňuje péči o zvíře. Pokud sháníte dárek pro začínajícího jezdce, kombinujte obuv s <a href="/jezdecke-helmy/">helmou</a>, a to vždy podle změřených velikostí.</p>')
NEW['jezdecke-helmy']['guide'] += ('<h2>Související výbava a nákup</h2>'
    '<p>Helma je jen jeden díl výbavy. K ní patří <a href="/jezdecke-kalhoty/">jezdecké kalhoty</a>, <a href="/jezdecke-obleceni/">oblečení</a> s vrstvením do zimy, <a href="/jezdecke-doplnky/">doplňky</a> a vybavení pro koně z kategorie <a href="/vybaveni-pro-kone/">vybavení pro koně</a>. Pokud nakupujete pro dítě, počítejte s tím, že přilbu je potřeba zkontrolovat každou sezónu. U všech nabídek sledujte, zda obchod uvádí přesné rozměry přilby, váhu a možnost výměny velikosti, protože tvar hlavy se liší a jedna značka může sedět výrazně jinak než jiná.</p>')
NEW['cyklo-sedacky-a-voziky']['guide'] += ('<h2>Dobrá příprava před první jízdou</h2>'
    '<p>Před první vyjížďkou si doma nasaďte sedačku a vyzkoušejte všechny pásy, nastavení stupaček a sundání z kola. U vozíku si vyzkoušejte skládání, připojení oje a zajištění pojistky. Posaďte dítě a zkontrolujte, zda pásy sedí těsně a dítě ve vozíku nebo sedačce pohodlně sedí s přilbou. Pak naplánujte krátkou trasu po rovině a postupně prodlužujte vzdálenost. Mít po ruce základní nářadí, náhradní duši a lékárničku je u rodinných výletů vždy dobrý nápad.</p>')
NEW['bezecke-vazani']['guide'] += ('<h2>Kdy se obrátit na servis</h2>'
    '<p>Do servisu patří vrtání nových otvorů, výměna vázání na lyžích bez desky, kontrola geometrie po pádu a diagnostika, když se bota sama uvolňuje. Servis také poradí s nastavením polohy podle hmotnosti a stylu jízdy. Pokud vázání kupujete jako náhradu, vezměte s sebou boty a lyže, aby technik ověřil kompatibilitu. Takový krok ušetří nepříjemné překvapení uprostřed sezóny.</p>')
