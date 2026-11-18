"""sporteka.cz — brand page texts wave 236: burton, jack-wolfskin, lowa, klimatex.
General facts only, no prices or counts; assortment taken from the live catalogue copy (18. 11. 2026).

Sources (checked 18. 11. 2026):
- Burton: en.wikipedia.org/wiki/Burton_Snowboards (1977 Jake Burton Carpenter, Londonderry VT, HQ Burlington, private,
  Jake died 20. 11. 2019, Donna Carpenter CEO 2015, Channel on 2008 models, EST, Anon, Analog);
  burton.com blog: Step On EST overview (Step On launched 2017, heel clip + two toe hooks, Step On EST needs Step On boots
  and The Channel), EST vs Re:Flex guides (Re:Flex fits 2x4, 4x4, 3D and Channel), rocker snowboard guide (Camber,
  Flying V, Flat Top, PurePop Camber, Directional Flat Top); [ak] = Alaska, 1997, Craig Kelly (burton.com blog, auski.com.au).
- Jack Wolfskin: en.wikipedia.org/wiki/Jack_Wolfskin (1981, Ulrich Dausien, trademark of Sine in Frankfurt am Main,
  HQ Idstein, paw logo, Johnson Outdoors 1991, Bain 2002, Quadriga + Barclays PE 2005, Blackstone 2011, creditors 2017,
  Callaway 2019); jack-wolfskin.com press release "Anta Sports completes acquisition of Jack Wolfskin" (2025),
  textileworld.com (sale closed 2025); highsnobiety.com/p/jack-wolfskin-history (Yukon trip, name, Texapore).
- Lowa: lowa.com/stories/corporate/history (1923 Lorenz Wagner, Jetzendorf; Sepp Lederer 1953–1988; Tecnica Group 1992;
  Werner Riethmann 1992–2023, Renegade developed in his era); lowa.com production locations (Europe, Vietnam, China);
  lowa.com lexicon (TF = task force, occupational footwear); retailer pages on Renegade GTX / LL (nubuck, Gore-Tex vs
  leather lining, Monowrap PU frame, Vibram sole).
- Klimatex: mediaguru.cz 2020/05 "Sportisimo koupilo českou značku Klimatex" (Karel Bastl 2007, roots in the 1970s at
  Výzkumný ústav pletařský with polypropylene fibre, nine patents, 80 % stake bought by Sportisimo, part of production
  in Czechia); snowboard-online.eu Lynx Klimafeel page (polypropylene inside, modal outside, made in Czechia).
Left out (not verified): Renegade launch year (1998 only in one source), Lowa factory town, Klimatex seat, exact
composition of ThermoCool Soft / Thermolight / No-Wind fabrics, Step On boot compatibility tables, Burton wide-board
boot-size threshold, current owner shares after 2020 at Klimatex."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ burton
NEW['burton'] = dict(
    title='Burton: snowboardy, vázání Step On, boty a oblečení',
    desc='Burton v katalogu: snowboardy Custom a Process, vázání Re:Flex, EST a Step On, boty BOA, bundy Gore-Tex, termoprádlo, batohy. Jak vybrat a srovnat nabídky.',
    intro='<p>Burton je americká snowboardová firma z Vermontu, kterou v roce 1977 založil Jake Burton Carpenter. Pro mnoho jezdců je to první jméno, které si se snowboardingem spojí, a značka dodnes pokrývá celou výbavu od prkna po rukavice. '
          'V katalogu najdete <a href="/snowboardy/">snowboardy</a>, vázání, boty, svrchní oblečení do sněhu, termoprádlo, čepice, batohy a vaky na prkno. Velkou část tvoří dětské velikosti, od batolat po teenagery. '
          'Sporteka.cz u každého produktu ukazuje nabídky českých e-shopů vedle sebe, takže hned vidíte, kde je konkrétní délka prkna nebo velikost bot skladem. Nakupujete pak přímo v obchodě, který si vyberete. '
          'Níže vysvětlujeme rozdíly mezi systémy vázání Re:Flex, EST a Step On, profily prken, značení oblečení a postup, jak porovnat nabídky na stejný model z různých sezón.</p>',
    guide='<h2>Od garáže ve Vermontu k celosvětové značce</h2>'
          '<p>Jake Burton Carpenter vyrobil první prkna ručně v roce 1977 v garáži v Londonderry ve státě Vermont. O rok později se firma přestěhovala do Manchesteru a dnes sídlí v Burlingtonu. Burton je soukromá firma v rukou rodiny Carpenterových. Zakladatel zemřel v listopadu 2019, na vedení firmy se dlouhodobě podílí jeho manželka Donna Carpenter. Ke skupině patří také značka Anon, která dělá snowboardové brýle a helmy, a v minulosti i další značky prken a oblečení.</p>'
          '<p>Burton ovlivnil i technické standardy. Montážní systém The Channel, tedy drážku ve středu prkna místo pevných děr, firma uvedla na modelech pro rok 2008. Na něj navazuje vázání EST. V roce 2017 přišel systém Step On, u kterého se bota do vázání zacvakne bez pásků.</p>'
          '<h2>Co v nabídce převažuje</h2>'
          '<p>Nejpočetnější skupinu tvoří snowboardové vybavení: prkna, <a href="/snowboardova-vazani/">vázání na snowboard</a> a <a href="/snowboardove-boty/">snowboardové boty</a>. Velký podíl má <a href="/termopradlo/">termoprádlo</a> Lightweight, Midweight a Heavyweight, lyžařské a snowboardové rukavice, <a href="/cepice-a-celenky/">čepice</a> a nákrčníky. Ze svrchního oblečení obchody vedou bundy, kalhoty s laclem i kombinézy, často s membránou Gore-Tex. Další větší skupinou jsou <a href="/mestske-batohy/">městské batohy</a> Kilo, Prospect, Annex nebo Day Hiker, fleecové a bavlněné mikiny a vaky na prkno Gig a Wheelie Gig, které najdete mezi <a href="/lyzarske-vaky-a-tasky/">vaky a taškami na lyže</a>.</p>'
          + T(['Řada', 'Typ', 'Pro koho'], [
              ['Custom, Custom X', 'všestranné a tvrdší snowboardy s kamberem', 'pokročilí jezdci na sjezdovce i mimo ni'],
              ['Process, Yeasayer', 'freestylová a všestranná prkna, Yeasayer v dámské verzi', 'park, sjezdovka, učení triků'],
              ['Family Tree', 'směrová prkna do prašanu a terénu', 'zkušení jezdci mimo upravené tratě'],
              ['Grom, Smalls, Zipline', 'dětská prkna, vázání a boty', 'děti od prvních krůčků na sněhu'],
              ['Freestyle, Mission, Cartel, Lexa, Citizen', 'klasická vázání s pásky Re:Flex', 'od začátečníků po náročné jezdce'],
              ['Ruler, Photon, Felix, Limelight, Ritual', 'snowboardové boty s BOA nebo pro Step On', 'pánské a dámské modely různé tuhosti']]) +
          '<h2>Re:Flex, EST a Step On: jaké vázání na jaké prkno</h2>'
          '<p>Než koupíte vázání, zjistěte, jaký montážní systém má vaše prkno. Re:Flex je univerzální. Kotouč s otvory pasuje na vzory 2x4, 4x4, na starší 3D od Burtonu i na The Channel. Pokud máte prkno jiné značky, je Re:Flex nejjistější volba. EST se šroubuje po stranách do drážky a funguje jen na prknech s The Channel. Výhodou je méně materiálu pod chodidlem, lepší cit pro prkno a jemné nastavení postoje.</p>'
          '<p>Step On je systém bez pásků. Bota má na patě a ve špičce kovové úchyty, vázání ji zachytí jednou sponou na patě a dvěma háčky u špičky. Nastoupíte, zatlačíte patu a pak přenesete váhu dopředu, dokud neuslyšíte cvaknutí. Vázání Step On potřebuje boty Step On a obráceně, klasickou botu do něj nedáte. Step On se vyrábí s montáží Re:Flex i EST, takže i tady musíte ověřit prkno. Hodí se tomu, kdo nechce na kopci sedat do sněhu kvůli páskům, často jde o rodiče s dětmi nebo jezdce na vlecích.</p>'
          '<h2>Profily prken a délka</h2>'
          '<p>Profil určuje, jak se prkno chová. Camber je klasický oblouk mezi vázáními, který drží hranu a dává odraz, ale odpouští méně chyb. Flying V kombinuje rocker mezi nohama s kousky camberu pod vázáním, prkno se snáz točí a méně chytá hrany. Flat Top je rovný mezi nohama a nabízí stabilitu bez nervozity. PurePop Camber přidává k camberu ploché zóny ve špičce a patce, které přidávají hravost. Směrové varianty mají zvednutou špičku a lépe plavou v prašanu.</p>'
          '<p>Délku volte hlavně podle hmotnosti, výrobce u každé délky uvádí doporučený rozsah. Kratší prkno se snáz točí a hodí se do parku a začátečníkům, delší je stabilnější ve vyšší rychlosti a v hlubokém sněhu. Písmeno W za délkou, například 159W, znamená široké prkno pro jezdce s velkou botou, aby špička ani pata nepřečnívaly přes hranu.</p>'
          '<h2>Snowboardové boty</h2>'
          '<p>Boty Burton se liší způsobem utahování a tuhostí. BOA má kolečko a ocelové lanko, utáhnete ho i v rukavicích. Některé modely mají dvě kolečka zvlášť pro horní a dolní část boty. Klasické tkaničky dovolí nejjemnější nastavení, ale zabírají víc času. Boty pro Step On mají na podrážce úchyty a nelze je dát do běžného vázání. Velikost se uvádí v amerických číslech, proto si vždy otevřete tabulku a změřte délku chodidla. Snowboardová bota má po utažení pevně držet patu, prsty se smí lehce dotýkat špičky. Po několika dnech ježdění se vložka sedne.</p>'
          '<h2>Oblečení: Gore-Tex, 2L, 3L a [ak]</h2>'
          '<p>Většina bund a kalhot nese v názvu 2L nebo 3L. U dvouvrstvé konstrukce je membrána nalepená na vrchní látku a uvnitř visí samostatná podšívka. Třívrstvý materiál má podšívku zalaminovanou, je lehčí a odolnější, ale tužší na omak. Insulated označuje zateplenou verzi, Stretch pružný materiál a Bib kalhoty s laclem, které v prašanu nepustí sníh k zádům. Nejtechničtější řada se jmenuje [ak]. Vznikla koncem 90. let na popud jezdce Craiga Kellyho pro freeride na Aljašce a dodnes je určená do terénu a do špatného počasí. Pod <a href="/snowboardove-bundy/">snowboardové bundy</a> se vyplatí obléct vrstvu termoprádla nebo fleece.</p>'
          '<ul><li>Lightweight: tenká první vrstva na jaro a do teplejších dnů.</li>'
          '<li>Midweight: univerzální tloušťka na běžnou zimu.</li>'
          '<li>Heavyweight: silná vrstva na mrazy a pomalé ježdění s dětmi.</li></ul>'
          '<h2>Dětská výbava</h2>'
          '<p>Dětské velikosti jsou u Burtonu rozdělené na Toddler pro nejmenší a Kid pro starší děti. Dětská prkna Grom, vázání Smalls a boty Zipline nebo Grom jsou měkčí, aby je dítě dokázalo ovládnout. Kombinézy One Piece a zateplené kalhoty s laclem drží sníh mimo oblečení. Dětem kupujte prkno odpovídající jejich současné váze. Příliš dlouhé prkno na „dvě sezóny“ učení výrazně zkomplikuje.</p>'
          '<h2>Batohy a vaky na prkno</h2>'
          '<p>Batohy Burton se dělí na městské a horské. Městské modely mají přihrádku na notebook a hodí se do školy i do práce. Horské batohy, například Day Hiker, mají popruhy na připevnění prkna a vejdou se do nich rukavice, svačina a náhradní vrstva. Na cestu autem nebo letadlem slouží vaky Gig a verze s kolečky, do kterých se vejde prkno s namontovaným vázáním, boty i oblečení.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Vázání EST koupené na prkno bez drážky The Channel.</li>'
          '<li>Boty Step On k běžnému vázání s pásky, nebo opačně.</li>'
          '<li>Příliš tvrdé prkno s camberem pro úplného začátečníka.</li>'
          '<li>Velikost vázání nevybraná podle velikosti boty. Vázání S, M a L má každé jiný rozsah.</li>'
          '<li>Úzké prkno pro velkou nohu, kdy špička bot zadrhává o sníh.</li></ul>'
          '<h2>Péče o prkno a oblečení</h2>'
          '<ul><li>Skluznici pravidelně voskujte a před sezónou nechte zkontrolovat hrany.</li>'
          '<li>Šrouby vázání po prvních jízdách dotáhněte, časem se mohou povolit.</li>'
          '<li>Boty sušte s vyjmutou vložkou při pokojové teplotě.</li>'
          '<li>Bundy s membránou perte v tekutém prostředku bez aviváže a po vyprání obnovte <a href="/impregnace/">impregnací</a> povrchovou úpravu proti vodě.</li></ul>'
          '<h2>Jak porovnat nabídky</h2>'
          '<p>Burton každý rok mění grafiky a řada modelů se prodává ve více sezónách souběžně. Porovnávejte proto přesný název, délku prkna, šířku, montážní systém vázání a u oblečení střih a pohlaví. Starší ročník bývá levnější a technicky se často neliší. Pokud nakupujete komplet, ověřte, že prkno, vázání a boty spolu fungují, nebo se podívejte na hotové <a href="/snowboardove-sety/">snowboardové sety</a>. Výběr prken jiných značek najdete i na stránce <a href="/head-snowboard/">snowboardy Head</a>. Pro srovnání stojí za pohled také '
          + B(('roxy', 'Roxy'), ('o-neill', 'O’Neill'), ('horsefeathers', 'Horsefeathers'), ('quiksilver', 'Quiksilver')) + '.</p>',
    faq=[
        ('Odkud pochází značka Burton?',
         'Z amerického Vermontu. Firmu založil v roce 1977 Jake Burton Carpenter, první prkna vyráběl v garáži v Londonderry. Dnes sídlí v Burlingtonu a patří rodině zakladatele.'),
        ('Jaký je rozdíl mezi vázáním Re:Flex a EST?',
         'Re:Flex má kotouč, který pasuje na většinu prken včetně vzorů 4x4, 2x4 a The Channel. EST se montuje jen do drážky The Channel a dává lepší cit pro prkno.'),
        ('Jak funguje Step On?',
         'Bota se do vázání zacvakne bez pásků: jedna spona drží patu a dva háčky špičku. Potřebujete k tomu boty Step On, s běžnými botami vázání nefunguje.'),
        ('Pasuje vázání Burton na snowboard jiné značky?',
         'Většinou ano, pokud zvolíte montáž Re:Flex. EST a Step On EST vyžadují drážku The Channel, kterou mají hlavně prkna Burton.'),
        ('Co znamená W za délkou snowboardu?',
         'Široké prkno, například 159W. Je určené jezdcům s větší botou, aby špička a pata nepřečnívaly přes hranu a nezadrhávaly v oblouku.'),
        ('Jaký je rozdíl mezi Camber a Flying V?',
         'Camber má oblouk mezi vázáními, drží hranu a dává odraz. Flying V má mezi nohama rocker a pod vázáními camber, takže se snáz točí a méně chytá hrany.'),
        ('Co znamená [ak] u oblečení Burton?',
         'Nejtechničtější řadu svrchního oblečení. Jméno odkazuje na Aljašku a řada je určená do terénu a do špatného počasí, často s materiály Gore-Tex.'),
        ('Jaké termoprádlo Burton zvolit?',
         'Lightweight na jaro a teplejší dny, Midweight na běžnou zimu a Heavyweight do mrazů. Pod bundou funguje lépe než bavlněné tričko.'),
        ('Kdy jsou snowboardy Burton nejlevnější?',
         'Obvykle na konci zimy a na jaře, kdy obchody doprodávají ročník. Starší kolekce se často liší hlavně grafikou, proto porovnejte oba roky.'),
        ('Prodává sporteka.cz výrobky Burton přímo?',
         'Ne. Sporteka porovnává nabídky českých e-shopů a odkazuje na ně. Objednávku, montáž vázání i reklamaci řešíte s obchodem, který si vyberete.'),
    ],
)

# ------------------------------------------------------------------ jack-wolfskin
NEW['jack-wolfskin'] = dict(
    title='Jack Wolfskin: bundy, trekové boty a fleecové mikiny',
    desc='Jack Wolfskin v katalogu: bundy Texapore, péřové a 3v1, fleece Taunus, trekové boty Everquest, Wild Hike a Refugio i batohy. Jak vybrat a srovnat nabídky.',
    intro='<p>Jack Wolfskin je německá outdoorová značka s tlapkou v logu. Vznikla v roce 1981 ve Frankfurtu nad Mohanem a dnes sídlí v hesenském Idsteinu. Od roku 2025 patří čínské sportovní skupině ANTA Sports. '
          'V katalogu převažuje obuv: trekové a trailové boty, zimní boty a nízká vycházková obuv. Velký podíl mají také bundy na jaro i zimu, <a href="/fleecove-mikiny/">fleecové mikiny</a>, trička, kalhoty, čepice a batohy. '
          'Sporteka.cz u každého produktu ukazuje nabídky českých e-shopů vedle sebe, takže snadno najdete obchod, kde je vaše velikost a barva skladem. Nákup pak dokončíte přímo v e-shopu, který si zvolíte. '
          'Níže najdete stručnou historii značky, vysvětlení značení Texapore, přehled řad obuvi a bund a rady, jak porovnat stejný model u různých prodejců.</p>',
    guide='<h2>Historie a vlastníci</h2>'
          '<p>Značku založil Ulrich Dausien, který ve Frankfurtu provozoval obchod s outdoorovým vybavením Sine. Podle firemní legendy dostal nápad na jméno u táboráku na cestě po Yukonu, kde slyšel vytí vlků, a Jack odkazuje na spisovatele Jacka Londona, který o tom kraji psal. Jack Wolfskin se rychle rozrostl a v roce 1991 ho koupila americká skupina Johnson Outdoors.</p>'
          '<p>Další roky byly bohaté na změny majitelů. Firmu postupně vlastnily investiční fondy, mezi nimi Bain Capital, Quadriga Capital s Barclays Private Equity a od roku 2011 Blackstone. Po restrukturalizaci dluhů v roce 2017 přešla na věřitele, v roce 2019 ji koupila americká golfová firma Callaway. V roce 2025 Jack Wolfskin převzala ANTA Sports, jeden z největších čínských výrobců sportovního zboží. Sídlo firmy zůstává v Idsteinu.</p>'
          '<h2>Co v nabídce převažuje</h2>'
          '<p>Nejpočetnější je obuv. Obchody pod značkou vedou <a href="/nizke-trekove-boty/">nízké trekové boty</a>, <a href="/vysoke-trekove-boty/">vysoké trekové boty</a>, lehké trailové modely, <a href="/zimni-obuv/">zimní obuv</a> a sandály. Druhou velkou skupinou jsou přechodové, nepromokavé, zimní a lyžařské bundy, dále fleecové mikiny, trička, šortky, outdoorové kalhoty a sukně. Menší část tvoří batohy, tašky přes rameno, merino ponožky, rukavice, čepice, stany a prostředky na praní a impregnaci.</p>'
          + T(['Řada', 'Typ', 'Na co'], [
              ['Everquest', 'kotníkové a vysoké boty, často zateplené', 'zima, mokro, delší túry'],
              ['Wild Hike, Refugio, Vojo', 'trekové boty v nízké i kotníkové verzi', 'běžná turistika po značených cestách'],
              ['Dromoventure, Terraventure', 'lehké boty na kratší výlety a do města', 'výlety, cestování'],
              ['Spirit, Cyrox', 'lehká vycházková obuv s úpletem nebo vlnou', 'město, nenáročné procházky'],
              ['Taunus', 'fleecové mikiny na zip i polozip', 'střední vrstva pod bundu'],
              ['Routeburn, Flowline, Icecape', 'zateplené, lyžařské a péřové bundy a kalhoty', 'zima, hory, lyže']]) +
          '<h2>Co znamená Texapore</h2>'
          '<p>Texapore je vlastní označení nepromokavé a prodyšné technologie Jack Wolfskin. U obuvi znamená membránu uvnitř boty, u oblečení nepromokavý materiál s podlepenými švy. Slovo v názvu tak rychle napoví, že model zvládne déšť nebo mokrou trávu. Membrána ale nefunguje zázračně: v horku bota hřeje víc než verze bez ní a pokud voda nateče horem přes kotník, ven už neodteče. Na letní výlety za sucha je proto často příjemnější obuv bez membrány nebo sandály.</p>'
          '<p>U bund se setkáte s údaji 2L a 3L. Dvouvrstvá bunda má volnou podšívku a je měkčí, třívrstvá je lehčí a odolnější vůči oděru batohem. Ins nebo In v názvu znamená zateplení, Down péřovou výplň. Bundy 3v1 se skládají z nepromokavé svrchní vrstvy a vnitřní fleecové nebo zateplené bundy, které nosíte spolu nebo každou zvlášť. Hodí se tomu, kdo chce jednu bundu na podzim, zimu i jaro.</p>'
          '<h2>Jak vybrat trekové boty</h2>'
          '<p>Nejdřív rozhodněte výšku. Low je nízká bota na upravené cesty a lehčí náklad, Mid sahá ke kotníku a lépe chrání před kamením a vodou, High je vysoká zimní bota. Pro turistiku s větším batohem nebo v kamenitém terénu volte Mid. Velikost zkoušejte odpoledne, kdy je noha nejvíc oteklá, a s ponožkami, ve kterých chodíte. Před palcem nechte zhruba centimetr místa, aby prsty při sestupu nenarážely do špičky.</p>'
          '<ol><li>Určete terén a roční období.</li>'
          '<li>Vyberte výšku Low, Mid nebo High.</li>'
          '<li>Rozhodněte, zda potřebujete membránu Texapore.</li>'
          '<li>Porovnejte velikostní tabulku, dámské a pánské modely mají jiné kopyto.</li></ol>'
          '<p>Pro srovnání s jinými výrobci se podívejte na výběr <a href="/damske-trekove-boty/">dámských trekových bot</a> a pro nejmenší na <a href="/detske-trekove-boty/">dětské trekové boty</a>, kde Jack Wolfskin nabízí i zimní řadu Polar Bear.</p>'
          '<h2>Bundy, fleece a vrstvení</h2>'
          '<p>Oblékání do hor stojí na třech vrstvách. První odvádí pot, druhá hřeje a třetí chrání před větrem a deštěm. U Jack Wolfskin je typickou střední vrstvou fleece Taunus, který se vyrábí v plném zipu, polozipu i v dětských velikostech. Na přechodné období poslouží <a href="/softshellove-kalhoty/">softshellové kalhoty</a> a lehké bundy. Do zimy jsou tu zateplené a <a href="/perove-bundy/">péřové bundy</a>, pro sjezdovky lyžařské kalhoty a soupravy Flowline. Městské péřové kabáty, například Marienplatz, jsou delší a zakryjí i stehna. Hledáte-li membránovou bundu, podívejte se i na výběr <a href="/nepromokave-bundy/">nepromokavých bund</a>.</p>'
          '<h2>Na sjezdovku</h2>'
          '<p>Lyžařská řada zahrnuje zateplené bundy a kalhoty Flowline, které se prodávají i jako souprava, a péřové bundy Icecape. U <a href="/lyzarske-kalhoty/">lyžařských kalhot</a> sledujte, zda mají sněhové návleky přes boty, zesílené vnitřní strany nohavic proti hranám lyží a nastavitelný pas. U bundy se hodí sněžný pás, kapuce přes helmu a kapsa na skipas na rukávu. Výbava se liší model od modelu, proto si ji ověřte v popisu nabídky. Pod lyžařskou bundu patří funkční první vrstva a tenký fleece, bavlna na svahu rychle navlhne a začne studit. Kalhoty volte tak, aby se v nich dalo pohodlně dřepnout i s chrániči kolen.</p>'
          '<h2>Letní obuv a sandály</h2>'
          '<p>Na léto nabízí Jack Wolfskin turistické <a href="/sandaly/">sandály</a> s nastavitelnými pásky a tvarovanou stélkou, a to pro dospělé i děti. Hodí se k vodě, na kempování a na kratší výlety po zpevněných cestách. Do kamenitého terénu nebo s těžším batohem ale sandál nenahradí uzavřenou botu, protože nechrání prsty a kotník. Lehké nízké boty bez membrány, například řady Spirit, jsou vzdušnější než modely Texapore a na teplé dny ve městě nebo na nenáročné procházky stačí.</p>'
          '<h2>Batohy, stany a doplňky</h2>'
          '<p>Kromě oblečení a obuvi vedou obchody pod značkou také <a href="/turisticke-batohy/">turistické batohy</a> na jednodenní i delší výlety, městské batohy a tašky přes rameno. U turistického batohu sledujte objem, nastavitelnou délku zad a bederní pás, který přenese váhu na boky. Na denní túru obvykle stačí menší objem, na vícedenní přechod s noclehem potřebujete výrazně větší batoh. V nabídce se objevují i stany a kempingové vybavení, merino ponožky, rukavice, čepice s logem tlapky a prací a impregnační prostředky na membránové oblečení.</p>'
          '<h2>Dětská kolekce</h2>'
          '<p>Dětské oblečení a obuv mají u Jack Wolfskin v názvu obvykle písmeno K. Najdete zde fleecové mikiny, nepromokavé kalhoty do deště, zimní bundy, čepice s bambulí, sandály a zimní boty. Dětské boty Polar Bear mají membránu Texapore a zapínání na suchý zip, které děti zvládnou samy. U dětí kupujte obuv s rezervou kolem jednoho centimetru, větší bota se na noze kroutí a dítě v ní zakopává. Oblečení do deště vybírejte s možností obléct pod něj mikinu.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Bota s membránou na horké letní dny, kdy se noha zbytečně potí.</li>'
          '<li>Nízká obuv do kamenitého terénu s těžkým batohem.</li>'
          '<li>Bunda koupená těsně, bez místa na fleece pod ní.</li>'
          '<li>Praní membránové bundy s aviváží, která ucpe póry.</li>'
          '<li>Zimní bota vybraná bez ohledu na silnější ponožku.</li></ul>'
          '<h2>Péče o obuv a oblečení</h2>'
          '<ul><li>Boty po túře očistěte kartáčem a sušte volně při pokojové teplotě, ne na topení.</li>'
          '<li>Kožené části ošetřujte přípravkem určeným pro daný typ kůže.</li>'
          '<li>Bundy perte podle štítku, v tekutém prostředku a bez aviváže.</li>'
          '<li>Když voda přestane po povrchu perlit, obnovte ji <a href="/impregnace/">impregnací</a>.</li>'
          '<li>Péřové bundy skladujte volně zavěšené, ne dlouhodobě stlačené v obalu.</li></ul>'
          '<h2>Jak porovnat nabídky</h2>'
          '<p>Stejný model Jack Wolfskin prodává mnoho obchodů a název se může lišit pořadím slov nebo překladem. U bot proto porovnávejte název řady, výšku Low, Mid nebo High, označení Texapore a velikost. U bund hlídejte střih, pohlaví, zateplení a kolekci. Starší barvy a sezóny se doprodávají za nižší ceny a technicky se často neliší. Pro srovnání stojí za pohled značky '
          + B(('the-north-face', 'The North Face'), ('columbia', 'Columbia'), ('northfinder', 'Northfinder'), ('lowa', 'Lowa')) + '.</p>',
    faq=[
        ('Odkud pochází Jack Wolfskin?',
         'Z Německa. Značku založil Ulrich Dausien v roce 1981 ve Frankfurtu nad Mohanem, dnes firma sídlí v Idsteinu v Hesensku.'),
        ('Komu patří Jack Wolfskin?',
         'Od roku 2025 čínské skupině ANTA Sports, která ji koupila od americké firmy Callaway. Před tím značku vlastnily investiční fondy a věřitelé.'),
        ('Co znamená Texapore?',
         'Vlastní nepromokavou a prodyšnou technologii Jack Wolfskin. U bot jde o membránu uvnitř, u bund o nepromokavý materiál s podlepenými švy.'),
        ('Jsou boty Jack Wolfskin s Texapore nepromokavé?',
         'Ano, membrána brání průniku vody. Pokud ale voda nateče horem přes okraj boty, ven už neodteče, a v horku se v botě noha víc potí.'),
        ('Jaký je rozdíl mezi Low, Mid a High?',
         'Low je nízká bota na upravené cesty, Mid sahá ke kotníku a lépe chrání v terénu, High je vysoká bota hlavně do zimy a sněhu.'),
        ('Co je bunda 3v1?',
         'Souprava svrchní nepromokavé bundy a vnitřní fleecové nebo zateplené bundy. Nosíte je spolu v zimě, nebo každou zvlášť na jaře a na podzim.'),
        ('Jakou velikost bot Jack Wolfskin zvolit?',
         'Změřte délku chodidla a porovnejte ji s tabulkou výrobce. Před palcem nechte asi centimetr místa a boty zkoušejte s turistickými ponožkami.'),
        ('Jak prát bundu s membránou?',
         'Podle štítku, obvykle na nízkou teplotu v tekutém prostředku bez aviváže. Pak bundu nechte uschnout a obnovte impregnaci povrchu.'),
        ('Kdy jsou výrobky Jack Wolfskin levnější?',
         'Obvykle na konci sezóny, kdy obchody doprodávají starší barvy a kolekce. Bundy bývají levnější na jaře, letní obuv na podzim.'),
        ('Prodává sporteka.cz zboží Jack Wolfskin přímo?',
         'Ne. Sporteka porovnává nabídky českých obchodů a odkazuje na ně. Nákup, výměnu velikosti i reklamaci řešíte s e-shopem, který si vyberete.'),
    ],
)

# ------------------------------------------------------------------ lowa
NEW['lowa'] = dict(
    title='Lowa: trekové boty Renegade, Innox a dětské Maddox',
    desc='Lowa v katalogu: trekové boty Renegade, Innox, Ranger a Sirkos, dámské Ws, dětské Maddox a Milo, tkaničky i vložky. Jak vybrat a srovnat nabídky.',
    intro='<p>Lowa je bavorský výrobce turistické a horské obuvi z Jetzendorfu severně od Mnichova, jehož historie sahá do roku 1923. Od roku 1992 patří italské skupině Tecnica Group. Nejznámějším modelem je kotníková bota Renegade, kterou mnoho turistů zná i z výprav po Česku a Alpách. '
          'V katalogu jsou pod značkou téměř výhradně boty: <a href="/trekova-obuv/">treková obuv</a> nízká i kotníková, lehčí trailové a vycházkové modely, zimní boty, dětská obuv a několik profesních modelů. Doplňují je originální tkaničky, vložky a impregnace. '
          'Sporteka.cz u každého páru ukazuje nabídky českých e-shopů vedle sebe, takže zjistíte, kde je vaše číslo skladem. Nákup pak dokončíte v obchodě, který si vyberete. '
          'Níže vysvětlujeme značení modelů, rozdíl mezi verzemi GTX a LL a postup při výběru velikosti.</p>',
    guide='<h2>Ševcovská dílna z Bavorska</h2>'
          '<p>V roce 1923 převzal Lorenz Wagner ševcovskou dílnu v Jetzendorfu. Jméno Lowa vzniklo ze začátečních slabik jeho jména a příjmení, tedy LOrenz WAgner. V těžkých letech po válce a v padesátých letech vedli firmu jeho dcera Berti a její manžel Sepp Lederer, který byl ředitelem v letech 1953 až 1988. V roce 1992 firmu koupila italská skupina Tecnica Group, kam patří také lyžařské boty Tecnica a lyže Blizzard. Za éry ředitele Wernera Riethmanna, který Lowu vedl od roku 1992 do roku 2023, vznikl model Renegade a značka se rozšířila do mnoha zemí. Jetzendorf zůstal domovským sídlem.</p>'
          '<p>Výrobce uvádí, že boty vyrábí v Evropě, Vietnamu a Číně. Konkrétní místo výroby najdete na štítku boty, stejně jako materiál svršku a typ podšívky.</p>'
          '<h2>Co v nabídce převažuje</h2>'
          '<p>Nejvíc je trekové obuvi, a to <a href="/nizke-trekove-boty/">nízkých trekových bot</a> i <a href="/vysoke-trekove-boty/">vysokých trekových bot</a> s membránou Gore-Tex. Velkou skupinu tvoří lehčí modely, které obchody řadí mezi <a href="/trailove-boty/">trailové boty</a> nebo tenisky, například Innox, Merger, Fusion nebo Citux. Dále jsou tu dětské boty Maddox, Milo a Callisto, zimní a zateplené verze, několik skialpových bot a profesní řady. Doplňky tvoří tkaničky v různých délkách, <a href="/vlozky-do-bot/">vložky do bot</a> a impregnace.</p>'
          + T(['Řada', 'Typ', 'Na co'], [
              ['Renegade', 'kotníková i nízká bota se semišovým svrškem', 'turistika, delší výlety, lehčí batoh'],
              ['Innox, Innovo, Merger', 'lehké nízké a kotníkové boty', 'rychlá turistika, cestování'],
              ['Ranger, Trek, Renetrek', 'pevnější vysoké boty', 'těžší batoh, kamenitý terén'],
              ['Sirkos, Barina, Calceta', 'všestranné boty na denní túry', 'značené cesty, kopce'],
              ['Delago, Zirrox', 'nástupové boty s lepší přilnavostí', 'cesta pod skály, ferraty'],
              ['Maddox, Milo, Callisto', 'dětská treková a zimní obuv', 'děti na výletech']]) +
          '<h2>Renegade: co znamená GTX, LL a Evo</h2>'
          '<p>Renegade je kotníková bota se svrškem z broušené kůže, podrážkou Vibram a rámem Monowrap. Monowrap je pevný polyuretanový rám, který obepíná botu v oblasti mezipodešve, zpevňuje patu a podpírá klenbu. Díky tomu bota drží stabilitu, ale není tak tuhá jako vysokohorská obuv. Verze GTX má membránu Gore-Tex a je nepromokavá. Verze LL má místo membrány koženou podšívku, je vzdušnější a hodí se do suchého a teplého počasí. Evo označuje novější provedení modelu. Mid znamená výšku ke kotníku, Lo nízkou verzi, Hi vyšší botu.</p>'
          '<h2>Značení modelů Lowa</h2>'
          '<ul><li>GTX: membrána Gore-Tex, bota je nepromokavá.</li>'
          '<li>LL: kožená podšívka bez membrány, do sucha a tepla.</li>'
          '<li>Ws nebo Lady: dámský model s užším kopytem.</li>'
          '<li>Jr: dětská a juniorská obuv.</li>'
          '<li>Warm nebo Ice: zateplené zimní provedení.</li>'
          '<li>Wide: širší střih pro objemnější nohu, jen u vybraných modelů.</li>'
          '<li>TF: profesní řada Task Force s certifikací pro pracovní použití.</li></ul>'
          '<p>Profesní modely, například Zephyr TF nebo Renegade Work, jsou určené pro pracovní a služební použití a mají vlastní certifikaci jako osobní ochranné prostředky. Pokud boty potřebujete do práce, ověřte v popisu, kterou normu splňují.</p>'
          '<h2>Jak vybrat velikost a střih</h2>'
          '<p>Lowa uvádí velikosti v britském i evropském číslování, proto si vždy otevřete tabulku výrobce. Boty zkoušejte odpoledne a se stejnými ponožkami, jaké nosíte na túry, ideálně <a href="/merino-ponozky/">merino ponožkami</a>. Pata nesmí v botě klouzat a před palcem má zůstat zhruba centimetr místa. Při sestupu se noha posouvá dopředu, a pokud prsty narážejí do špičky, je bota malá. Pánské modely jsou širší, dámské Ws mají užší patu a nižší nárt. Pokud máte širší nohu, hledejte verzi Wide.</p>'
          '<p>Nové boty rozchoďte na kratších výletech, než s nimi vyrazíte na vícedenní trasu. Lehké modely jako Innox jsou pohodlné hned, kožené Renegade nebo Ranger se do nohy usadí po několika dnech chůze. Pro srovnání se podívejte i na výběr <a href="/trekove-boty-panske/">pánských trekových bot</a> a <a href="/damske-trekove-boty/">dámských trekových bot</a> jiných výrobců.</p>'
          '<h2>Kotníková, nebo nízká bota</h2>'
          '<p>Kotníková bota Mid lépe drží patu, chrání kotník před narážením o kameny a do bláta nebo mokré trávy pustí vodu později. Hodí se na vícedenní túry, do hor, na kamenité stezky a tomu, kdo nese větší batoh nebo má slabší kotníky. Nízká bota Lo je lehčí a ohebnější, v teple se v ní noha méně potí a na upravených cestách se chodí příjemněji. Řada modelů Lowa se vyrábí v obou výškách se stejnou podrážkou i svrškem, takže si snadno vyberete podle toho, kde chodíte nejčastěji.</p>'
          '<h2>Lehké boty a obuv do města</h2>'
          '<p>Kromě klasických kožených bot vyrábí Lowa i lehčí modely se syntetickým svrškem. Innox a Merger jsou určené na rychlou turistiku a cestování, Amplux na svižnou chůzi po zpevněných cestách. Fusion a Citux jsou spíš vycházkové boty, které obchody často řadí mezi tenisky. Lehká bota se méně unaví a nevyžaduje rozchození, ale vydrží kratší dobu než kožená a v kamenitém terénu chrání nohu méně. Pokud chodíte hlavně po značených cestách do kopců bez těžkého batohu, lehký model bohatě stačí.</p>'
          '<h2>Zimní a dětské boty</h2>'
          '<p>Na zimu jsou určené zateplené verze, například Renegade Warm nebo Renegade Evo Ice, které mají vrstvu izolace a podrážku do chladu. Hodí se na zimní vycházky a na túry po zasněžených cestách, nejsou to ale boty na mačky do vysokých hor. Pro ty jsou určené tužší horolezecké modely. Dětské boty Maddox, Milo a Callisto jsou postavené podobně jako dospělé, jen jsou měkčí a mají zapínání, které dítě zvládne samo. U dětí ověřujte velikost každou sezónu, noha roste rychle a malá bota na túře rychle otlačí prsty. Další výběr najdete na stránce <a href="/detske-trekove-boty/">dětské trekové boty</a>.</p>'
          '<h2>Tkaničky, vložky a skialpové boty</h2>'
          '<p>Originální tkaničky Lowa se prodávají v různých délkách podle výšky boty, takže při výměně zjistěte délku té původní. Vložky do bot nahradí opotřebovanou stélku nebo zlepší oporu klenby. Při výměně vyjměte původní stélku a novou zkuste nejdřív položit vedle ní, aby měla stejnou délku i tvar. Pokud vložku zastřihujete, berte méně a zkoušejte postupně. V nabídce se objevuje i několik skialpových bot Struktura. U nich si v popisu nabídky ověřte velikost skeletu v mondopointu a kompatibilitu s vaším vázáním.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Bota s membránou na letní pochody v horku, kde by stačila verze LL.</li>'
          '<li>Lehká nízká bota pro vícedenní trek s těžkým batohem.</li>'
          '<li>Velikost vybraná podle čísla z jiné značky, bez tabulky.</li>'
          '<li>Dětská bota „na růst“, ve které noha klouže a dítě zakopává.</li>'
          '<li>Zkoušení bot s tenkou ponožkou, kterou na túru nevezmete.</li></ul>'
          '<h2>Péče o boty Lowa</h2>'
          '<ul><li>Po túře boty očistěte kartáčem a vlažnou vodou, bláto na kůži nenechávejte zaschnout.</li>'
          '<li>Sušte je s vyjmutou vložkou a povolenými tkaničkami při pokojové teplotě, ne u kamen ani na topení.</li>'
          '<li>Kůži ošetřete přípravkem pro broušenou kůži, u membránových bot volte prostředky, které neucpou póry.</li>'
          '<li>Obnovte vodoodpudivost <a href="/impregnace/">impregnací</a>, výrobce nabízí vlastní sprej Water Stop.</li>'
          '<li>Opotřebovanou podrážku lze u řady modelů vyměnit v obuvnickém servisu.</li></ul>'
          '<h2>Jak porovnat nabídky</h2>'
          '<p>Lowa mění modely pomalu a stejná bota se prodává několik let. Mezi nabídkami se liší hlavně barva, provedení GTX nebo LL, generace Evo a dámská či pánská verze. Porovnávejte proto celý název a ověřte, že velikost je uvedená ve stejném číslování. Kožené boty mají dlouhou životnost, takže se vyplatí vybírat podle střihu, ne podle barvy. Na ferraty a nástupy pod skály se hodí <a href="/via-ferrata/">vybavení na via ferraty</a> a k dlouhým túrám <a href="/trekove-hole/">trekové hole</a>. Pro srovnání stojí za pohled boty značek '
          + B(('salewa', 'Salewa'), ('la-sportiva', 'La Sportiva'), ('merrell', 'Merrell'), ('jack-wolfskin', 'Jack Wolfskin')) + '.</p>',
    faq=[
        ('Odkud pochází značka Lowa?',
         'Z Bavorska. Lorenz Wagner převzal ševcovskou dílnu v Jetzendorfu v roce 1923 a jméno Lowa vzniklo ze začátků jeho jména a příjmení.'),
        ('Komu patří Lowa?',
         'Od roku 1992 italské skupině Tecnica Group. Sídlo a vývoj zůstaly v Jetzendorfu u Mnichova.'),
        ('Kde se boty Lowa vyrábějí?',
         'Výrobce uvádí výrobu v Evropě, Vietnamu a Číně. Zemi výroby konkrétního páru najdete na štítku.'),
        ('Jaký je rozdíl mezi Renegade GTX a Renegade LL?',
         'GTX má membránu Gore-Tex a je nepromokavá. LL má koženou podšívku bez membrány, je vzdušnější a hodí se do suchého a teplého počasí.'),
        ('Co je Monowrap?',
         'Pevný polyuretanový rám v mezipodešvi, který zpevňuje patu a podpírá klenbu. Najdete ho například u modelu Renegade.'),
        ('Co znamená Ws u bot Lowa?',
         'Dámský model. Mívá užší patu a nižší nárt než pánská verze. Jr označuje dětské a juniorské boty.'),
        ('Co znamená TF u bot Lowa?',
         'Profesní řadu Task Force pro pracovní a služební použití. Tyto modely mají certifikaci jako osobní ochranné prostředky.'),
        ('Jakou velikost bot Lowa zvolit?',
         'Podle tabulky výrobce, kde je britské i evropské číslování. Před palcem nechte asi centimetr místa a zkoušejte s turistickými ponožkami.'),
        ('Jak se starat o boty Lowa?',
         'Po túře je očistěte, sušte při pokojové teplotě s vyjmutou vložkou a kůži ošetřete přípravkem pro daný typ. Pak obnovte impregnaci.'),
        ('Prodává sporteka.cz boty Lowa přímo?',
         'Ne. Sporteka porovnává nabídky českých e-shopů a odkazuje na ně. Objednávku, výměnu velikosti i reklamaci řešíte s obchodem, který si vyberete.'),
    ],
)

# ------------------------------------------------------------------ klimatex
NEW['klimatex'] = dict(
    title='Klimatex: české funkční prádlo, trička a cyklo oblečení',
    desc='Klimatex v katalogu: funkční trička KlimaFeel, termoprádlo, merino, spodní prádlo, cyklodresy, cyklošortky, mikiny a ponožky. Jak vybrat a srovnat nabídky.',
    intro='<p>Klimatex je česká značka funkčního prádla a sportovního oblečení, kterou v roce 2007 založil Karel Bastl. Její kořeny ale sahají do 70. let, kdy se v tehdejším Výzkumném ústavu pletařském začalo s polypropylenovým vláknem pro funkční oblečení. Od roku 2020 má ve firmě většinový podíl obchodní řetězec Sportisimo. '
          'V katalogu najdete hlavně <a href="/funkcni-tricka/">funkční trička</a>, termoprádlo, sportovní spodní prádlo, mikiny a legíny. Velkou skupinu tvoří cyklistické oblečení, dále čepice, ponožky, bundy a doplňky. '
          'Sporteka.cz u každého produktu ukazuje nabídky českých e-shopů vedle sebe, takže snadno porovnáte, kde je vaše velikost a barva skladem. Nákup pak dokončíte v obchodě, který si vyberete. '
          'Níže vysvětlujeme materiály, jak volit první vrstvu podle aktivity a na co si dát pozor při praní.</p>',
    guide='<h2>Česká značka s dlouhou tradicí materiálu</h2>'
          '<p>Polypropylen je syntetické vlákno, které samo téměř nesaje vodu. Pot proto prochází látkou ven a kůže zůstává sušší než v bavlně. Na této myšlence Klimatex stavěl od začátku. Podle údajů z roku 2020 měla značka devět patentů, vlastní prodejny, nové kolekce dvakrát ročně a část výroby v Česku. V květnu 2020 koupil 80procentní podíl ve firmě Sportisimo, takže Klimatex najdete i v jeho prodejnách, ale prodávají ho také další obchody.</p>'
          '<h2>Co v nabídce převažuje</h2>'
          '<p>Nejpočetnější jsou funkční trička s krátkým i dlouhým rukávem, následuje <a href="/termopradlo/">termoprádlo</a> a <a href="/sportovni-spodni-pradlo/">sportovní spodní prádlo</a>: boxerky, kalhotky, brazilky, sportovní topy a termo spodky. Velkou část tvoří mikiny, <a href="/leginy/">legíny</a> a cyklistické oblečení, tedy dresy, MTB trička, cyklošortky, cykloprádlo a rukavice. Menší skupiny jsou čepice a čelenky, ponožky včetně kompresních podkolenek, merino trička a čepice, bundy, vesty, outdoorové kalhoty, cyklistické batohy, lahve a rychleschnoucí ručníky.</p>'
          + T(['Označení', 'Co to je', 'Kdy se hodí'], [
              ['KlimaFeel', 'látka s polypropylenem uvnitř a modalem zvenku', 'každodenní sport, příjemná na omak'],
              ['ThermoCool Soft', 'funkční materiál z vláken Thermocool', 'běh, kolo, aktivita ve středních teplotách'],
              ['Seamless', 'bezešvé pletení', 'první vrstva, kde vadí švy'],
              ['Merino, Merino blend', 'čistá merino vlna nebo směs s funkčním vláknem', 'túry, vícedenní nošení'],
              ['No-Wind', 'větruodolné provedení', 'běh a kolo v chladném větru'],
              ['Waterproof', 'nepromokavé bundy s membránou', 'déšť, outdoor']]) +
          '<h2>Jak vybrat první vrstvu</h2>'
          '<p>První vrstva má odvádět pot a nehřát víc, než je potřeba. Při intenzivním sportu, jako je běh, kolo nebo běžky, volte tenké syntetické tričko, které rychle schne. Pro pomalejší aktivity, túry a cestování je příjemnější merino, které méně zapáchá a hřeje i lehce vlhké. Směs merina s funkčním vláknem kombinuje obojí a je odolnější než čistá vlna. KlimaFeel je měkčí a na dotek připomíná bavlnu, proto se hodí i na nošení mimo sport.</p>'
          '<p>Funkční prádlo musí přiléhat k tělu, jinak pot neodvádí. Pokud jste mezi dvěma velikostmi, volte spíš menší, u volnějších triček pro posilovnu pak větší. Termo trička a spodky noste pod mikinou a bundou, ne samostatně v mrazu. Na lyže a do hor se podívejte i na výběr <a href="/termopradlo-panske/">pánského termoprádla</a> a <a href="/termopradlo-damske/">dámského termoprádla</a>.</p>'
          '<ol><li>Určete aktivitu a teplotu, ve které budete sportovat.</li>'
          '<li>Vyberte materiál: syntetika na výkon, merino na pomalejší pohyb.</li>'
          '<li>Zvolte přiléhavý střih a délku rukávu.</li>'
          '<li>Doplňte střední vrstvu, například funkční mikinu, a větruodolnou bundu.</li></ol>'
          '<h2>Cyklistické oblečení</h2>'
          '<p>Klimatex nabízí silniční dresy, volnější MTB trička s krátkým i dlouhým rukávem, elastické cyklošortky, 3/4 cyklolegíny a cykloprádlo, které se nosí pod volné kraťasy. Zda mají kalhoty cyklistickou vložku a jakou, ověřte v popisu konkrétního modelu. Dres s kapsami na zádech se hodí na silnici, volné triko do terénu. Doplnit můžete <a href="/cyklisticke-rukavice/">cyklistické rukavice</a>, menší cyklistické batohy a <a href="/cyklo-lahve-a-drzaky/">cyklistické lahve</a>. Pod cyklošortky s vložkou se spodní prádlo nenosí, jinak se tvoří otlaky.</p>'
          '<h2>Spodní prádlo, ponožky a kompresní podkolenky</h2>'
          '<p>Sportovní <a href="/boxerky/">boxerky</a> a kalhotky z funkčního materiálu se nehrnou a rychle schnou. U ponožek najdete nízké běžecké, trekové i kompresní podkolenky. Kompresní ponožky se prodávají jako sportovní doplněk, který lidé nosí třeba po výkonu nebo na dlouhé cestě. Nejde o zdravotnický prostředek ani léčbu. Pokud máte potíže s žilami, otoky nebo jinou zdravotní komplikaci, poraďte se o kompresi s lékařem.</p>'
          '<h2>Vrstvení podle teploty</h2>'
          '<ul><li>Teplo nad 15 °C: tenké funkční triko, případně lehká větrovka.</li>'
          '<li>Mezi 5 a 15 °C: triko s dlouhým rukávem, tenká mikina nebo vesta.</li>'
          '<li>Kolem nuly: termo triko, funkční mikina a větruodolná vrstva.</li>'
          '<li>Mráz: silnější termoprádlo nebo merino, fleece, zateplená bunda, čepice a rukavice.</li></ul>'
          '<p>Hranice berte orientačně. Záleží na intenzitě pohybu, větru, vlhkosti i na tom, jak snadno je vám zima. Při běhu se oblékejte tak, aby vám bylo na startu lehce chladno, po pár minutách se zahřejete. Při pomalé chůzi nebo na lyžích s dětmi naopak potřebujete o vrstvu víc.</p>'
          '<h2>Merino od Klimatexu</h2>'
          '<p>Kromě syntetiky prodává Klimatex <a href="/merino-tricka/">merino trička</a>, merino spodní prádlo, ponožky a čepice. Některé modely jsou z čisté merino vlny, jiné ze směsi merina a syntetického vlákna, která je pevnější a rychleji schne. Merino méně zapáchá, proto se hodí na vícedenní túry nebo na cesty, kde nemáte možnost prádlo prát. Je ale choulostivější na oděr, například pod popruhy batohu, a dražší než syntetika. Složení každého modelu najdete v popisu produktu. Merino pere většina lidí méně často, stačí ho po nošení nechat vyvětrat. Když už ho perete, volte program na vlnu a prostředek bez enzymů, které vlnu poškozují.</p>'
          '<h2>Mikiny, bundy a vesty</h2>'
          '<p>Jako druhou vrstvu nabízí Klimatex <a href="/funkcni-mikiny/">funkční mikiny</a> z tenkého úpletu, mikrofleece a hybridní mikiny, které mají na hrudi větruodolný panel a na rukávech a zádech pružnou látku. Takové kombinace se hodí na běh, skialpy nebo kolo, kde se člověk zahřeje a nepotřebuje plnou bundu. Ze svrchních vrstev najdete <a href="/softshellove-bundy/">softshellové bundy</a>, lehké sbalitelné bundy, větruodolné bundy No-Wind, nepromokavé bundy s membránou a sbalitelné péřové bundy. Vesty zahřejí trup a nechají volné ruce, na kole i při běhu proto dobře poslouží v chladném ránu.</p>'
          '<h2>Běh, fitness a volný čas</h2>'
          '<p>Pro běh jsou určené legíny v celé délce i ve 3/4 délce, krátké legíny, šortky, běžecké sukně a lehké bundy. Do posilovny a na jógu se hodí volnější trička, tílka a sportovní topy. Některá trička a šaty jsou střižená tak, aby se daly nosit i mimo sport, typicky z měkčího materiálu KlimaFeel. U legín na běh v zimě sledujte, zda jsou zateplené nebo větruodolné, protože tenké legíny v mrazu a větru nestačí. Na výlety se hodí rychleschnoucí ručníky, které se sbalí do malého obalu.</p>'
          '<h2>Dětské oblečení a doplňky</h2>'
          '<p>Dětské funkční prádlo prodává Klimatex často jako termoset, tedy tričko a spodky v jednom balení. Hodí se pod lyžařskou kombinézu nebo na běžky. Další výběr najdete na stránce <a href="/detske-termopradlo/">dětské termoprádlo</a>. Dětem kupujte prádlo v aktuální velikosti, volné prádlo pot neodvede a dítěti bude zima. Pro dospělé i děti jsou v nabídce pletené a funkční <a href="/cepice-a-celenky/">čepice a čelenky</a>, merino čepice, rukavice a ponožky.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Bavlněné tričko pod funkční bundu. Nasákne potem a začne studit.</li>'
          '<li>Funkční triko o dvě čísla větší, které na těle volně visí.</li>'
          '<li>Příliš teplé termoprádlo na běh nebo kolo za mírného počasí.</li>'
          '<li>Spodní prádlo pod cyklošortkami s vložkou.</li>'
          '<li>Merino na rychlé intervaly v létě, kdy schne pomaleji.</li></ul>'
          '<h2>Praní a péče</h2>'
          '<ul><li>Funkční prádlo perte obvykle na nízkou teplotu, nejčastěji do 40 °C, a vždy se řiďte štítkem.</li>'
          '<li>Nepoužívejte aviváž, zanáší vlákna a zhoršuje odvod potu.</li>'
          '<li>Polypropylen nesušte v sušičce ani nežehlete, vlákno je citlivé na teplo.</li>'
          '<li>Merino perte na vlnu nebo ručně a sušte rozložené naplocho.</li>'
          '<li>Pokud prádlo začne zapáchat, pomůže prací prostředek na sportovní oblečení.</li></ul>'
          '<h2>Jak porovnat nabídky</h2>'
          '<p>Klimatex pojmenovává modely jmény, například Lynx, Arvid nebo Wooly. Některé existují ve dvou verzích lišících se číslicí za jménem, třeba Mauna a Mauna1, proto si ověřte, kterou z nich obchod nabízí. Porovnávejte celé jméno, materiál, pohlaví a barvu. Kolekce se obměňují dvakrát ročně a starší barvy obchody doprodávají. Pro srovnání stojí za pohled funkční prádlo značek '
          + B(('sensor', 'Sensor'), ('craft', 'Craft'), ('progress', 'Progress'), ('icebreaker', 'Icebreaker')) + '.</p>',
    faq=[
        ('Je Klimatex česká značka?',
         'Ano. Klimatex založil Karel Bastl v roce 2007, tradice polypropylenového funkčního prádla ale sahá do 70. let a Výzkumného ústavu pletařského.'),
        ('Komu patří Klimatex?',
         'V roce 2020 koupil 80procentní podíl ve firmě obchodní řetězec Sportisimo. Výrobky Klimatex ale prodávají i další obchody.'),
        ('Vyrábí se Klimatex v Česku?',
         'Podle údajů z roku 2020 probíhala v Česku část výroby. Zemi výroby konkrétního kusu najdete na štítku nebo v popisu produktu.'),
        ('Co je KlimaFeel?',
         'Materiál s polypropylenem na vnitřní straně, který odvádí pot, a modalem zvenku, který je měkký na omak. Hodí se na sport i každodenní nošení.'),
        ('Jaký je rozdíl mezi syntetickým a merino prádlem Klimatex?',
         'Syntetika rychleji schne a hodí se na intenzivní sport. Merino méně zapáchá a hřeje i vlhké, proto je lepší na túry a vícedenní nošení.'),
        ('Jakou velikost funkčního prádla zvolit?',
         'Funkční prádlo má přiléhat k tělu, jinak pot neodvádí. Pokud jste mezi dvěma velikostmi, volte spíš menší a vždy se řiďte tabulkou.'),
        ('Jak prát funkční prádlo Klimatex?',
         'Podle štítku, obvykle na nízkou teplotu a bez aviváže. Polypropylen nesušte v sušičce ani nežehlete, merino perte na vlnu.'),
        ('Jsou kompresní podkolenky Klimatex zdravotnický prostředek?',
         'Ne, jde o sportovní doplněk. Pokud máte potíže s žilami nebo otoky, poraďte se o vhodné kompresi s lékařem.'),
        ('Nosí se pod cyklošortky s vložkou spodní prádlo?',
         'Ne. Vložka je určená na holou kůži, spodní prádlo by tvořilo švy a otlaky. Cykloprádlo s vložkou se nosí místo spodního prádla.'),
        ('Prodává sporteka.cz oblečení Klimatex přímo?',
         'Ne. Sporteka porovnává nabídky českých obchodů a odkazuje na ně. Nákup, výměnu velikosti i reklamaci řešíte s e-shopem, který si vyberete.'),
    ],
)
