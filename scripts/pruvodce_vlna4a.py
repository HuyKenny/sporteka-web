"""Guides wave 4a (2026-11-18): jak-opravit-zip, co-je-modal, nubuk, jak-prat-perovou-bundu.

Demand (CZ / month): jak opravit zip 600, co je modal 700 + co je to modal 250, nubuk 600, jak prát péřovou bundu.

Sources used for the facts:
- Zips: Treeline Review "How to Fix Zippers on Outdoor Gear" (diagnosis, cleaning, lubricating with wax, compressing a
  loose slider with needle-nose pliers, slider replacement: remove stop, slide on, crimp new stop; exact model number
  on the slider; tent zips risky to DIY); Rab "Zip care and repair" (do not force a jammed zip, check the back of the
  slider, coil zip: remove top stop, YKK VISLON: remove top tooth, slide the new slider on from the top, fit new top
  stop); Sailrite / Trivantage / Wawak zipper guides (size number = approx. width of the closed chain in mm, YKK codes
  C/CN coil, VS Vislon moulded plastic, M metal; measure the chain if the marking does not match); iFixit zipper
  guides (a crushed coil or torn tape is fixed only by replacing the whole zipper); skrblik.cz and blesk.cz Czech
  how-tos (pliers, dose the force, graphite pencil on teeth, re-threading a slider that fell off).
- Modal: Regulation (EU) No 1007/2011, Annex I no. 22 (modal = regenerated cellulose fibre obtained by a modified
  viscose process having a high breaking force and high wet modulus; only Annex I names may be used on labels);
  Wikipedia "Rayon" (Modal is spun from beech cellulose, HWM rayon, stronger when wet, keeps shape, can be machine
  washed, pills less than cotton, often blended with cotton or elastane; Modal is a Lenzing trademark); Wikipedia
  "Lyocell" (NMMO direct solvent, solvent largely recovered, Tencel brand owned by Lenzing); alpinetrek.co.uk and
  goodonyou.eco (modal exclusively from beech, viscose from various woods; Lenzing sources beech from FSC/PEFC forests).
- Nubuck: Keen "Shoe care tips: nubuck and suede" (soft brush along the nap, suede/pencil eraser, dab not scrub,
  test vinegar/alcohol, water damages the nap, proofing spray); Meindl UK care page (clean with water and brush after
  walks, dry airy away from sun and heat, newspaper then remove it, shoe trees, nubuck/suede: brush to raise the nap,
  Conditioner & Proofer may darken slightly, Wetproof on slightly damp boots before first wear, renew when water stops
  beading); LOWA boot care (air dry, no direct heat, leather may shrink or crack); samuelhubbard.com, snakehive.co.uk
  (nubuck = outer grain side buffed, suede = inner/split side, nubuck more durable).
- Down: Rab "How to wash a down jacket" (rinse empty machine first, close zips, inside out, one item, non-bio or
  down-specific detergent, cool long gentle cycle, thorough rinse, spin, support wet jacket, tumble dry low-mid heat,
  shake every 20-30 min, tennis or dryer balls, 3-5 hours, air for a couple of days, wash about once a season or when
  dirty/flat, store uncompressed); Rab "How to wash a sleeping bag" (no fabric softener, never dry clean or iron the
  bag, store uncompressed in a cool dry place); Patagonia product care via search snippets (front loader preferred,
  top loader on delicate/hand-wash, cold to low temperature, down wash, low or no heat, 2-3 clean tennis balls or a
  heavy cotton towel, several cycles); Nikwax Down Wash Direct retailer instructions (clean detergent drawer, slow
  spin, wet down is heavy and fast spin can break baffles, multiple spins, low heat only if the label allows).
Left out because not verified: when Modal was invented, exact wet-strength percentages of modal vs viscose,
absorbency numbers vs cotton, water-use claims, specific temperatures for Down Wash Direct, a fixed drying time for
wet boots, a rule that nubuck can never be washed in a machine (left as "most manufacturers do not allow it").
"""
from texty_vlna1a import T

GUIDES = {}

# ---------------------------------------------------------------- jak-opravit-zip
ZIP_TYPES = T(['Typ zipu', 'Jak ho poznáte', 'Kde ho najdete', 'Co jde opravit doma'], [
    ['Spirálový (coil, nylonový)', 'Zoubky tvoří souvislá spirála přišitá k pásku', 'Bundy, spacáky, stany, kapsy batohů', 'Stažení jezdce, výměna jezdce i zarážky'],
    ['Plastový lisovaný (u YKK Vislon)', 'Samostatné plastové zuby nalisované na pásek', 'Zimní a lyžařské bundy, mikiny, batohy', 'Stažení a výměna jezdce; vylomený zub už ne'],
    ['Kovový', 'Samostatné kovové zuby, zip je tužší', 'Džíny, kožené bundy, pracovní oděvy', 'Stažení jezdce, výměna zarážky; chybějící zub ne'],
    ['Voděodolný', 'Spirála zakrytá pogumovanou vrstvou', 'Nepromokavé bundy a kalhoty, kapsy', 'Jezdec ano, celý zip raději v opravně'],
])

GUIDES['jak-opravit-zip'] = dict(
    name='Jak opravit zip',
    h1='Jak opravit zip: zaseknutý jezdec, rozjetý zip, táhlo i zarážka',
    seo_title='Jak opravit zip: rozjetý jezdec, zaseknutí i chybějící zarážka',
    seo_desc='Zip se rozjíždí, zasekává nebo vypadl jezdec? Postup opravy kleštěmi, výměna jezdce a zarážky, rozdíl spirálového a zubového zipu a kdy už nový zip.',
    intro_html=(
        '<p><strong>Jak opravit zip?</strong> Nejčastěji vůbec není rozbitý zip, ale jezdec. Když se zip za jezdcem znovu rozjíždí, jezdec se časem roztáhl a přestal tlačit zoubky k sobě. '
        'Stačí ho vyčistit a malými kleštěmi opatrně stáhnout, aby se mezera mezi jeho horní a spodní destičkou zmenšila. '
        'Když je jezdec prasklý nebo ohnutý, vyměňte ho za nový stejné velikosti, kterou najdete vyraženou na jeho rubu. Celý zip se mění, až když chybí zuby, je rozdrcená spirála nebo roztržený pásek.</p>'
        '<p>V tomto návodu projdeme jednotlivé závady jednu po druhé: zaseknutý jezdec, zip, který se rozjíždí, vypadlý jezdec, chybějící zarážku i ulomené táhlo. '
        'Ukážeme, jak poznat spirálový a zubový zip, jaké nářadí se hodí a v jakých případech je lepší dát bundu, batoh, stan nebo spacák do opravny. '
        'Většinu oprav zvládnete za pár minut doma u stolu.</p>'
        '<p>Sporteka nic neprodává, jen srovnává nabídky českých e-shopů. Pod některými částmi proto uvidíte bundy, batohy, stany nebo spacáky, kdyby už oprava nestála za to.</p>'
    ),
    sections=[
        dict(h2='Nejdřív zjistěte, co přesně nefunguje',
             html=(
                 '<p>Než sáhnete po kleštích, prohlédněte si zip na světle. Podle příznaku se pozná, kterou část opravujete:</p>'
                 '<ul><li><strong>Jezdec jde ztuha nebo se zasekne na jednom místě:</strong> v zipu je nečistota, písek nebo zachycená látka, případně je spirála na krátkém úseku pokřivená.</li>'
                 '<li><strong>Jezdec jede, ale zip se za ním hned rozpojí:</strong> jezdec je roztažený a opotřebený. Tohle je vůbec nejčastější závada.</li>'
                 '<li><strong>Zip se rozpojuje jen v jednom místě:</strong> chybí nebo je ohnutý zub, případně je tam poškozená spirála.</li>'
                 '<li><strong>Jezdec sjel z konce zipu:</strong> chybí zarážka, která ho dřív držela.</li>'
                 '<li><strong>Zůstal vám v ruce kousek kovu:</strong> ulomilo se táhlo, jezdec jako takový může být v pořádku.</li>'
                 '<li><strong>Dělitelný zip bundy nejde začít:</strong> kolík nedosedá do pouzdra, bývá ohnutý nebo se odtrhl od pásku.</li></ul>'
                 '<p>Podle Rab, britského výrobce outdoorového oblečení, se zaseknutý zip nemá nikdy rvát silou. Z drobné závady se tak snadno stane trvalé poškození pásku nebo spirály.</p>'
             )),
        dict(h2='Spirálový, zubový nebo kovový zip: proč na typu záleží',
             html=(
                 '<p>Pro opravu je důležité vědět, jaký zip máte. Liší se tím, jak drží zoubky, a tedy i tím, co se na něm dá spravit.</p>'
                 + ZIP_TYPES +
                 '<p><strong>Velikost zipu</strong> se značí číslem, které zhruba odpovídá šířce zapnutého zipu v milimetrech. U oblečení se nejčastěji potkáte s čísly 3 a 5, na batozích a stanech s 5, 8 nebo 10. '
                 'Číslo bývá vyražené na rubu jezdce, často s písmeny podle typu. U značky YKK znamená C nebo CN spirálový zip, VS lisované plastové zuby Vislon a M kovový zip. '
                 'Když značení chybí nebo nesedí, změřte šířku zapnutého zipu pravítkem. Nový jezdec musí odpovídat typu i velikosti, jinak zoubky nespojí.</p>'
                 '<p>Rozlišujte také <strong>dělitelný zip</strong>, který se dole úplně rozepne (bundy, mikiny), a <strong>nedělitelný zip</strong> s pevným koncem (kapsy, batohy, kalhoty). '
                 'Dvoucestný zip má dva jezdce a jde otevřít odspodu, typicky u delších bund a spacáků. Výběr bund s kvalitními zipy najdete v kategorii <a href="/nepromokave-bundy/">nepromokavé bundy</a>.</p>'
             ), cat='nepromokave-bundy', n=4),
        dict(h2='Zaseknutý jezdec: jak ho uvolnit bez poškození',
             html=(
                 '<ol><li><strong>Zastavte.</strong> Netahejte dál za táhlo. Podívejte se na jezdce z obou stran a zjistěte, co ho blokuje.</li>'
                 '<li><strong>Zachycenou látku</strong> (podšívku, lem kapuce, okraj kapsy) opatrně vytahujte z jezdce opačným směrem, než do něj vjela. Jezdec přitom posouvejte o kousek zpět.</li>'
                 '<li><strong>Písek a prach</strong> vyčistěte starým zubním kartáčkem a vlažnou vodou. Hlavně u stanů a batohů po pobytu u vody je to častá příčina.</li>'
                 '<li><strong>Tuhý zip</strong> promažte. Doma poslouží speciální lubrikant na zipy, na cestě obyčejný vosk ze svíčky nebo jelení lůj. Někteří přejíždějí po zoubcích tuhou z měkké tužky.</li>'
                 '<li><strong>Pokřivenou spirálu</strong> zkuste prsty srovnat zpět. Silně rozdrcená spirála se už opravit nedá.</li></ol>'
                 '<p>Mazivo naneste v malém množství a přebytek setřete, jinak na něj bude chytat další nečistota. Olej ani silikonový sprej na látku nestříkejte, mohl by zanechat skvrny.</p>'
             )),
        dict(h2='Zip se rozjíždí: stažení jezdce kleštěmi krok za krokem',
             html=(
                 '<p>Jezdec funguje jako klín: zezadu do něj vstupují dvě řady zoubků a vepředu je natlačí do sebe. Když se jeho destičky časem rozevřou, zoubky do sebe nezapadnou a zip se otevře hned za jezdcem. Postup opravy:</p>'
                 '<ol><li>Posuňte jezdce úplně dolů, k začátku zipu. U dělitelného zipu ho nechte nasazený na obou stranách.</li>'
                 '<li>Vezměte malé ploché kleště nebo kleště s úzkými čelistmi. Pod čelisti můžete dát kousek látky, aby nepoškrábaly povrch.</li>'
                 '<li>Najděte zadní konec jezdce, kudy vychází už spojený zip. Mezi horní a spodní destičkou je tam vidět mezera.</li>'
                 '<li>Lehce stiskněte destičky k sobě, nejdřív na jedné straně, pak na druhé. Sílu dávkujte po malých krocích.</li>'
                 '<li>Po každém stisku zip zkuste zapnout a rozepnout. Když drží, jste hotovi. Když ne, přidejte trochu tlaku.</li></ol>'
                 '<p>Přitlačíte-li příliš, jezdec se zasekne nebo praskne, hlavně levný jezdec ze slitiny zinku. Pak už ho vymění jen nový. U tenkých plastových jezdců buďte obzvlášť opatrní. '
                 'Pomůže to i u batohu, kde zip povoluje kvůli přeplnění. Než ho opravíte, uberte náklad, jinak se problém brzy vrátí. Batohy s pevnějšími zipy najdete mezi <a href="/turisticke-batohy/">turistickými batohy</a>.</p>'
             ), cat='turisticke-batohy', n=4),
        dict(h2='Vypadlý jezdec a chybějící zarážka',
             html=(
                 '<p>Zarážky jsou malé kovové nebo plastové svorky na koncích zipu. Horní zarážky brání jezdci sjet z pásku, spodní spojuje obě strany nedělitelného zipu. Když jedna chybí, jezdec dřív nebo později vypadne.</p>'
                 '<ol><li>Rozepněte zip úplně a obě poloviny srovnejte vedle sebe tak, aby začátky byly ve stejné výšce.</li>'
                 '<li>Nasuňte jezdce z otevřeného konce na obě řady zoubků naráz. Správně otočený jezdec má stranu se dvěma vstupy pro zoubky natočenou k rozepnutému konci zipu.</li>'
                 '<li>Pomalu jezdce posuňte o pár centimetrů a zkontrolujte, že zoubky za ním do sebe pravidelně zapadají. Když jedna strana „předběhla“, vraťte se a začněte znovu.</li>'
                 '<li>Na konec pásku nasaďte novou zarážku a kleštěmi ji pevně stiskněte. Zarážky se prodávají v sadách na opravu zipů spolu s jezdci.</li></ol>'
                 '<p>Nouzově můžete zarážku nahradit několika pevnými stehy přes pásek na konci zipu, nejlépe silnou nití. Jezdec se o ně zastaví a zip dál slouží, než seženete náhradní díl.</p>'
             )),
        dict(h2='Ulomené táhlo a nefunkční kolík dělitelného zipu',
             html=(
                 '<p>Ulomené táhlo je nejjednodušší oprava. Když na jezdci zůstalo očko, provlékněte jím malý kroužek z klíčenky, kancelářskou sponku na nejbližší cestu nebo kousek šňůry s uzlem. '
                 'V galanterii a v obchodech s outdoorovým vybavením se prodávají i náhradní táhla, která se na očko jen nacvaknou. Šňůrka má výhodu v rukavicích, kde se za ni lépe chytá.</p>'
                 '<p>Když se ulomilo očko přímo na těle jezdce, nové táhlo už nepřipevníte. Jezdec je pak potřeba vyměnit celý, postup najdete v další části.</p>'
                 '<p>U dělitelného zipu bundy se občas ohne nebo odtrhne <strong>kolík</strong>, který se zasouvá do pouzdra pod jezdcem. Ohnutý kolík jde někdy opatrně srovnat kleštěmi. '
                 'Utržený kolík nebo prasklé pouzdro ale většinou znamená výměnu celého zipu. Rab radí zasouvat kolík vždy úplně, až na doraz, a teprve pak táhnout jezdcem. Šikmo zasunutý kolík se ohýbá a pásek se na tom místě třepí.</p>'
             )),
        dict(h2='Výměna jezdce bez vyměnění celého zipu',
             html=(
                 '<p>Pokud je jezdec prasklý, zdeformovaný nebo stažení kleštěmi nepomohlo, vyměňte jen jeho. Pásek se zoubky zůstane. Budete potřebovat jezdce stejného typu i velikosti, kleště a novou zarážku.</p>'
                 '<ol><li>Zjistěte číslo a typ zipu podle značení na rubu jezdce nebo podle šířky zapnutého zipu.</li>'
                 '<li>Kleštěmi opatrně odstraňte horní zarážku na straně, odkud budete jezdce stahovat. Rab uvádí, že u lisovaného zipu Vislon se místo zarážky odstraňuje nejvyšší zub.</li>'
                 '<li>Starého jezdce stáhněte z konce zipu.</li>'
                 '<li>Nového jezdce nasuňte ze stejného konce, správnou stranou nahoru. Táhlo musí být na lícové straně.</li>'
                 '<li>Zip několikrát zapněte a rozepněte, než nasadíte novou zarážku a stisknete ji kleštěmi.</li></ol>'
                 '<p>Na dělitelném zipu bundy se jezdec mění podobně, jen se nasazuje shora na tu polovinu, na které jezdí. U dvoucestného zipu dbejte, aby oba jezdci směřovali proti sobě jako předtím. '
                 'Univerzální „rychlé“ jezdce bez šití sice existují, sedí ale jen na některé zipy. Jistější je originál stejné značky a velikosti.</p>'
             )),
        dict(h2='Kdy vyměnit celý zip a kdy jít do opravny',
             html=(
                 '<p>Nový jezdec nepomůže, když je chyba v pásku nebo v zoubcích. Výměnu celého zipu potřebujete, když:</p>'
                 '<ul><li>chybí jeden nebo více zubů u kovového či plastového zipu,</li>'
                 '<li>je spirála rozdrcená, natavená nebo vytržená z pásku,</li>'
                 '<li>je roztržený pásek, ze kterého se páře šev,</li>'
                 '<li>je utržený kolík nebo prasklé pouzdro dělitelného zipu.</li></ul>'
                 '<p>Výměna celého zipu znamená vypárat starý a našít nový, u bundy často skrz několik vrstev. Kdo šije na stroji, zvládne to u mikiny nebo kapsy. '
                 'U nepromokavé bundy s podlepenými švy, u péřové bundy nebo u vstupu stanu je ale lepší krejčovská dílna nebo servis výrobce. Chybný steh tu propustí vodu nebo peří. '
                 'Řada outdoorových značek opravy nabízí přímo, a u dražší bundy se oprava vyplatí víc než nákup nové.</p>'
                 '<p>Když je bunda už opotřebená i jinde a oprava by stála podobně jako nový kus, srovnejte nabídky v kategoriích <a href="/sportovni-bundy/">sportovní bundy</a> nebo <a href="/softshellove-bundy/">softshellové bundy</a>.</p>'
             ), cat='sportovni-bundy', n=4),
        dict(h2='Zip na bundě, batohu, stanu a spacáku: na co si dát pozor',
             html=(
                 '<ul><li><strong>Bundy:</strong> nejvíc trpí jezdec dělitelného zipu, protože ho denně rozpojujete. Kolík zasouvejte rovně a až na doraz a jezdcem netahejte šikmo do strany, když je bunda na těle napnutá.</li>'
                 '<li><strong>Batohy:</strong> přeplněná kapsa táhne zip do stran a jezdec se rychleji roztáhne. Těžký obsah dávejte do hlavní komory a kapsy nechte pro drobnosti.</li>'
                 '<li><strong>Stany:</strong> písek a jehličí jsou největší nepřítel. Před zavřením vstupu zip oprašte a nikdy ho nezapínejte, když je stanová plachta napnutá do oblouku. Oprava zipu u vchodu stanu je náročná, protože se lehce poškodí tenká látka.</li>'
                 '<li><strong>Spacáky:</strong> zip často chytá látku nebo podšívku. Kvalitnější spacáky mají podél zipu ztužující pásek proti zachycení. Při zapínání přidržujte druhou rukou okraj látky, aby nevjel do jezdce.</li></ul>'
                 '<p>U spacáku a stanu se vyplatí mít v lékárničce na výlety malou sadu na opravu zipů. Nové kusy s pevnými zipy najdete v kategoriích <a href="/stany/">stany</a> a <a href="/spaci-pytle/">spací pytle</a>.</p>'
             ), cat='stany', n=4),
        dict(h2='Nářadí na opravu a péče, aby zip vydržel',
             html=(
                 '<p>Na drobné opravy zipů vám stačí:</p>'
                 '<ul><li>malé ploché nebo úzké kleště,</li>'
                 '<li>sada náhradních jezdců a zarážek ve velikostech, které doma máte (nejčastěji 3, 5 a 8),</li>'
                 '<li>párátko na nitě, silná nit a jehla,</li>'
                 '<li>starý zubní kartáček,</li>'
                 '<li>lubrikant na zipy nebo kousek vosku.</li></ul>'
                 '<p>Prevence je jednoduchá. Před praním zip zapněte, aby se zoubky nezachytily o jiné prádlo a pásek se nekroutil. Po výletě do písku nebo bláta zip opláchněte a vysušte. '
                 'Netahejte za jezdce do strany a nezapínejte přeplněnou kapsu násilím. Voděodolné zipy se zakrytou spirálou jdou tužeji už od výroby, proto je posouvejte pomalu a rovně.</p>'
                 '<p>Péči o nepromokavé oblečení po praní popisuje průvodce <a href="/jak-prat-perovou-bundu/">jak prát péřovou bundu</a>, prostředky na obnovu impregnace najdete v kategorii <a href="/impregnace/">impregnace</a>.</p>'
             )),
    ],
    faq=[
        ('Proč se zip po zapnutí sám rozjíždí?',
         '<p>Ve většině případů je roztažený jezdec, který už netlačí zoubky dost silně k sobě. Pomůže opatrné stažení jeho destiček malými kleštěmi. Když se zip rozjíždí jen na jednom místě, chybí tam zub nebo je poškozená spirála.</p>'),
        ('Jak opravit zip kleštěmi?',
         '<p>Posuňte jezdce na začátek zipu a kleštěmi lehce stiskněte jeho zadní konec, kudy vychází spojený zip. Mačkejte po malých krocích, střídavě na obou stranách, a po každém stisku zip vyzkoušejte. Příliš velká síla jezdce zasekne nebo zlomí.</p>'),
        ('Jak nasadit jezdce zpět na zip?',
         '<p>Rozepněte zip, srovnejte obě poloviny do stejné výšky a nasuňte jezdce z otevřeného konce na obě řady naráz. Pak ho pomalu posuňte a zkontrolujte, že zoubky zapadají. Na konec nasaďte zarážku, aby jezdec znovu nesjel.</p>'),
        ('Jakou velikost jezdce potřebuji?',
         '<p>Stejnou, jakou má původní zip. Číslo bývá vyražené na rubu jezdce, například 5 nebo 8, a zhruba odpovídá šířce zapnutého zipu v milimetrech. Musí sedět i typ: spirálový, lisovaný plastový, nebo kovový.</p>'),
        ('Jak poznám spirálový zip od zubového?',
         '<p>Spirálový zip má zoubky z jedné souvislé nylonové spirály, je ohebný a lehký. Zubový zip má každý zub zvlášť, z plastu nebo kovu. Na rubu jezdce bývá u YKK písmeno C nebo CN pro spirálu, VS pro plast a M pro kov.</p>'),
        ('Co dělat, když se ulomí táhlo zipu?',
         '<p>Pokud zůstalo na jezdci očko, provlékněte jím kroužek, šňůrku nebo nacvakávací náhradní táhlo. Když prasklo samotné očko, je potřeba vyměnit celého jezdce.</p>'),
        ('Čím promazat zasekávající se zip?',
         '<p>Nejlépe lubrikantem určeným na zipy. V nouzi pomůže vosk ze svíčky, jelení lůj nebo tuha z měkké tužky. Použijte malé množství a přebytek setřete, aby se na zip nelepila nečistota.</p>'),
        ('Kdy už se zip nedá opravit?',
         '<p>Když chybí zuby, je rozdrcená spirála, roztržený pásek nebo utržený kolík dělitelného zipu. Pak je potřeba vyměnit celý zip, což u bundy nebo stanu nejlépe zvládne krejčí nebo servis výrobce.</p>'),
        ('Můžu opravit zip na nepromokavé bundě sám?',
         '<p>Výměnu jezdce nebo zarážky ano. Výměnu celého zipu raději ne, protože se musí párat podlepené švy a nový zip znovu utěsnit. To patří do odborné opravny.</p>'),
    ],
    cats=['nepromokave-bundy', 'turisticke-batohy', 'stany', 'spaci-pytle', 'sportovni-bundy'],
    updated='2026-11-18')

# ---------------------------------------------------------------- co-je-modal
MODAL_FIBRES = T(['Vlákno', 'Surovina', 'Jak vzniká', 'V praxi'], [
    ['Viskóza', 'Celulóza z různých dřevin, bambusu apod.', 'Klasický viskózový proces', 'Měkká a levná, za mokra slabší, může se srazit'],
    ['Modal', 'Celulóza, typicky z buku', 'Upravený viskózový proces', 'Pevnější za mokra, drží tvar, jemná na omak'],
    ['Lyocell (TENCEL Lyocell)', 'Celulóza ze dřeva', 'Přímé rozpouštění v rozpouštědle NMMO', 'Pevný, savý, rozpouštědlo se z velké části recykluje'],
    ['Bavlna', 'Přírodní vlákno z bavlníku', 'Sklizeň, čištění a spřádání', 'Prodyšná a savá, pomalu schne, žmolkuje'],
    ['Merino', 'Vlna ovcí merino', 'Stříhání, praní a spřádání', 'Hřeje i vlhká, odolává zápachu'],
    ['Polyester', 'Ropa nebo recyklované PET lahve', 'Syntetické zvlákňování', 'Velmi rychle schne, saje málo vody'],
])

GUIDES['co-je-modal'] = dict(
    name='Co je modal',
    h1='Co je modal: vlákno z bukového dřeva a jak se liší od bavlny',
    seo_title='Co je modal? Vlákno z buku a rozdíl oproti viskóze a bavlně',
    seo_desc='Co je to modal: celulózové vlákno z bukového dřeva. Rozdíl oproti viskóze, lyocellu, bavlně, merinu a polyesteru, kde se hodí a jak modal prát.',
    intro_html=(
        '<p><strong>Co je modal?</strong> Modal je textilní vlákno vyrobené z celulózy, kterou se získává ze dřeva, nejčastěji z buku. Patří mezi takzvaná regenerovaná celulózová vlákna, stejně jako viskóza. '
        'Vyrábí se upraveným viskózovým postupem, díky kterému je pevnější a za mokra drží tvar lépe než běžná viskóza. Není to tedy syntetika z ropy, ale ani čistě přírodní vlákno jako bavlna: surovina je přírodní, vlákno ale vzniká chemickou úpravou v továrně.</p>'
        '<p>Na omak je modal hladký, měkký a splývavý, proto se z něj šije hlavně spodní prádlo, pyžama, trička a ponožky. Často se mísí s bavlnou nebo s elastanem. '
        'Název Modal je původně obchodní značka rakouské firmy Lenzing, dnes se ale používá obecně a evropské nařízení o textilních názvech ho uvádí jako samostatný druh vlákna.</p>'
        '<p>Níže vysvětlujeme, jak se modal vyrábí, čím se liší od viskózy, lyocellu, bavlny, merina a polyesteru, kdy má smysl ve sportovním oblečení a jak se o něj starat.</p>'
    ),
    sections=[
        dict(h2='Z čeho a jak se modal vyrábí',
             html=(
                 '<p>Základem je celulóza, tedy hlavní stavební látka rostlinných buněk. U modalu se získává ze dřeva, typicky z buku. Dřevo se rozemele, z buničiny se oddělí celulóza a ta se chemicky převede do roztoku. '
                 'Roztok se pak protlačuje tryskami do srážecí lázně, kde z něj vznikají jemná vlákna. Ta se natahují, perou, suší a stříhají nebo spřádají do příze.</p>'
                 '<p>Proces vychází z výroby viskózy, je ale upravený, takže výsledné vlákno má uspořádanější molekuly. Evropské nařízení č. 1007/2011 o názvech textilních vláken definuje modal právě takto: '
                 'jde o regenerované celulózové vlákno získané upraveným viskózovým procesem, které má vysokou pevnost v tahu a vysoký modul za mokra. Jednoduše řečeno, mokrý modal se tolik netahá a netrhá.</p>'
                 '<p>Největší a nejznámější výrobce je Lenzing, jehož vlákno se dnes prodává pod značkou TENCEL Modal. Lenzing uvádí, že buk nakupuje z lesů s certifikací FSC nebo PEFC. Modal ale vyrábějí i jiné firmy a na etiketě oblečení pak stojí jen „modal“.</p>'
             )),
        dict(h2='Jaké vlastnosti modal má',
             html=(
                 '<ul><li><strong>Měkkost a hladkost:</strong> vlákna jsou jemná a hladká, látka příjemně klouže po kůži a dobře splývá.</li>'
                 '<li><strong>Savost:</strong> jako všechna celulózová vlákna modal dobře přijímá vlhkost z pokožky. Zároveň ji ale déle drží a schne pomaleji než syntetika.</li>'
                 '<li><strong>Pevnost za mokra:</strong> oproti obyčejné viskóze je mokrý modal výrazně odolnější a méně se deformuje při praní.</li>'
                 '<li><strong>Stálost tvaru:</strong> srazí se méně než viskóza, proto se dá prát v pračce.</li>'
                 '<li><strong>Žmolkování:</strong> podle dostupných zdrojů žmolkuje méně než bavlna.</li>'
                 '<li><strong>Tepelná izolace:</strong> modal skoro nehřeje. Je to lehké, chladivě působící vlákno, ne materiál na zimu.</li></ul>'
                 '<p>Protože čistý modal je dost splývavý a měkký, výrobci ho míchají. Příměs elastanu dodá pružnost, aby prádlo drželo tvar na těle. Směs s bavlnou je pevnější a levnější, s polyesterem rychleji schne.</p>'
             )),
        dict(h2='Modal, viskóza a lyocell: tři vlákna ze dřeva',
             html=(
                 '<p>Viskóza, modal a lyocell vznikají ze stejné suroviny, ale jinou cestou. Proto se na štítku můžete setkat se všemi třemi a rozdíl na první pohled nepoznáte.</p>'
                 + MODAL_FIBRES +
                 '<p><strong>Viskóza</strong> je nejstarší a nejlevnější. Je příjemná, ale za mokra ztrácí pevnost, při praní se může vytahat nebo srazit a starší kusy často vyžadují šetrné praní v ruce. '
                 '<strong>Modal</strong> je její vylepšená verze, odolnější v pračce. <strong>Lyocell</strong>, známý pod značkou TENCEL Lyocell, se vyrábí jiným procesem: celulóza se rozpouští přímo v rozpouštědle NMMO, '
                 'které se z velké části zachytí a použije znovu. Lyocell je pevný a savý, na dotek bývá trochu „broskvový“.</p>'
                 '<p>Pozor na označení „bambus“. Bambus je jen surovina, ze které se celulóza získává. Pokud byla přepracována na vlákno viskózovým procesem, je to podle předpisů viskóza, a na etiketě by tak mělo stát „viskóza“.</p>'
             )),
        dict(h2='Modal versus bavlna',
             html=(
                 '<p>Bavlna je přírodní vlákno, které se jen vyčistí a spřede. Modal má podobný původ v rostlinné celulóze, ale vlákno se vyrábí uměle, takže má rovnoměrnou délku a hladší povrch. V praxi to znamená:</p>'
                 '<ul><li>modal je na omak měkčí a hebčí, bavlna je „sušší“ a matnější,</li>'
                 '<li>modalové tričko lépe splývá, bavlněné drží víc tvar střihu,</li>'
                 '<li>oba materiály sají vlhkost a schnou pomalu, ani jeden se proto nehodí na dlouhý vytrvalostní výkon,</li>'
                 '<li>bavlna snese vyšší teploty praní, modal má raději šetrnější program,</li>'
                 '<li>směs bavlny a modalu bývá kompromis: drží tvar a je jemnější než čistá bavlna.</li></ul>'
                 '<p>Pro běžné nošení, spaní a odpočinek je modal příjemná náhrada bavlny. Na sport, kde se hodně potíte, se ale nehodí o nic lépe než bavlna. Trička pro každý den najdete v kategorii <a href="/sportovni-tricka/">sportovní trička</a>.</p>'
             ), cat='sportovni-tricka', n=4),
        dict(h2='Modal versus merino a polyester ve sportu',
             html=(
                 '<p>Při sportu rozhoduje, jak rychle oblečení odvede pot a jestli hřeje, když je vlhké. Tady modal proti specializovaným materiálům prohrává.</p>'
                 '<ul><li><strong>Polyester</strong> a další syntetika saje velmi málo vody a schne nejrychleji. Proto se z něj šijí <a href="/funkcni-tricka/">funkční trička</a> na běh, kolo nebo do posilovny. Nevýhoda: rychleji začne páchnout.</li>'
                 '<li><strong>Merino</strong> přijme hodně vlhkosti, a přesto hřeje, i když je vlhké. Dobře odolává zápachu, takže se nosí na vícedenní túry. Je ale dražší a choulostivější. Přehled najdete v kategorii <a href="/merino-pradlo/">merino prádlo</a>.</li>'
                 '<li><strong>Modal</strong> vlhkost přijme, ale drží ji a nehřeje. Po doběhnutí v zimě vás mokré modalové tričko spíš ochladí.</li></ul>'
                 '<p>Modal má smysl tam, kde se tolik nepotíte: na jógu, protahování, lehčí procházky, cestování nebo do města. Na intenzivní sport v zimě volte vrstvu ze syntetiky nebo merina, jako je <a href="/termopradlo/">termoprádlo</a>.</p>'
             ), cat='merino-pradlo', n=4),
        dict(h2='Kde se modal hodí: prádlo, pyžama, ponožky',
             html=(
                 '<p>Nejvíc modalu najdete ve výrobcích, které se nosí přímo na těle a kde rozhoduje pohodlí:</p>'
                 '<ul><li><strong>Spodní prádlo:</strong> boxerky, slipy a podprsenky z modalu s elastanem jsou hebké, netlačí a drží tvar. Sportovní varianty bývají ve směsi se syntetikou.</li>'
                 '<li><strong>Pyžama a noční košile:</strong> modal příjemně chladí a splývá, proto je oblíbený na letní spaní.</li>'
                 '<li><strong>Trička a tílka:</strong> volnější střihy na volný čas, často se směsí bavlny.</li>'
                 '<li><strong>Ponožky:</strong> jemné nízké ponožky pro běžné nošení. Na turistiku jsou lepší vlněné nebo syntetické.</li>'
                 '<li><strong>Legíny a oblečení na jógu:</strong> modal s elastanem je měkký, ale méně odolný proti oděru než syntetické legíny.</li></ul>'
                 '<p>Sportovní spodní prádlo z různých materiálů porovnáte v kategorii <a href="/sportovni-spodni-pradlo/">sportovní spodní prádlo</a>, legíny pak mezi <a href="/leginy/">legínami</a>.</p>'
             ), cat='sportovni-spodni-pradlo', n=4),
        dict(h2='Jak modal prát a sušit',
             html=(
                 '<p>Vždy platí údaje na etiketě, protože záleží na směsi a na úpravě látky. Obecně modal snese běžné praní v pračce, je ale lepší ho šetřit:</p>'
                 '<ol><li>Perte na nižší teplotu, typicky 30 °C, u bílého prádla podle štítku i výš.</li>'
                 '<li>Zvolte šetrný program a nízké otáčky ždímání, aby se vlákna nepomačkala a nelámala.</li>'
                 '<li>Použijte jemný prací prostředek. Bělidla vlákno oslabují.</li>'
                 '<li>Trička a prádlo obraťte naruby, sníží se tím odírání povrchu a tvorba žmolků.</li>'
                 '<li>Sušte na sušáku nebo na ramínku. Do sušičky jen tehdy, když to štítek dovoluje, a na nízkou teplotu.</li>'
                 '<li>Žehlete na nižší až střední teplotu, ideálně z rubu.</li></ol>'
                 '<p>Prádlo se směsí elastanu nesnáší vysoké teploty, elastan by ztratil pružnost. Modalové ponožky a prádlo perte s podobně jemnými kusy, ne s ručníky nebo džínami, které je odírají.</p>'
             )),
        dict(h2='Je modal ekologický?',
             html=(
                 '<p>Odpověď není jednoduchá. Modal pochází z obnovitelné suroviny a jako celulózové vlákno se v přírodě rozkládá snáz než polyester. '
                 'Výroba je ale chemicky náročná, protože vychází z viskózového procesu. Hodně záleží na tom, odkud dřevo pochází a jak výrobce nakládá s chemikáliemi a vodou.</p>'
                 '<p>Pokud vás to zajímá, hledejte u výrobku konkrétní značku vlákna, například TENCEL Modal, a certifikace. Samotné slovo „modal“ ani „přírodní vlákno“ na visačce o původu dřeva nic neříká. '
                 'Nejekologičtější je stejně oblečení, které vydrží a nosíte ho dlouho, proto se vyplatí o modal pečovat podle návodu výše.</p>'
             )),
        dict(h2='Na co se dívat při nákupu oblečení z modalu',
             html=(
                 '<ul><li><strong>Složení na štítku:</strong> „modal“ musí být uveden jako název vlákna s procentem. Tričko s 5 % modalu se bude chovat převážně jako bavlna nebo polyester.</li>'
                 '<li><strong>Podíl elastanu:</strong> u prádla a legín pomáhá příměs elastanu, aby výrobek držel tvar a nepovoloval. Čistý modal je splývavý, ale méně pružný.</li>'
                 '<li><strong>Gramáž a hustota:</strong> velmi tenký modal je průsvitný a rychleji se prodře. Podívejte se na fotky látky zblízka a recenze.</li>'
                 '<li><strong>Účel:</strong> na intenzivní sport hledejte syntetiku nebo merino, modal nechte na spaní a volný čas.</li>'
                 '<li><strong>Velikost:</strong> modal dobře splývá a pruží, proto u přiléhavého prádla nekupujte velikost navíc.</li></ul>'
                 '<p>Nabídky stejného výrobku od různých obchodů porovnáte na Sporteka. Jak to děláme, popisuje stránka <a href="/jak-srovnavame/">jak srovnáváme</a>. Pokud se vám prádlo nevešlo, pomůže <a href="/tabulka-velikosti/">tabulka velikostí</a>.</p>'
             )),
    ],
    faq=[
        ('Co je to modal za materiál?',
         '<p>Modal je regenerované celulózové vlákno. Vyrábí se z celulózy ze dřeva, nejčastěji z buku, upraveným viskózovým procesem. Je měkký, hladký a za mokra pevnější než běžná viskóza.</p>'),
        ('Je modal přírodní, nebo umělý materiál?',
         '<p>Je mezi tím. Surovina je přírodní, dřevo, ale vlákno vzniká chemickou úpravou v továrně. Řadí se proto mezi umělá vlákna z přírodních polymerů, ne mezi syntetiku z ropy.</p>'),
        ('Jaký je rozdíl mezi modalem a viskózou?',
         '<p>Oba vznikají z celulózy podobným procesem. Modal má upravenou výrobu, díky níž je pevnější, hlavně za mokra, méně se sráží a lépe snáší praní v pračce. Viskóza bývá levnější a choulostivější.</p>'),
        ('Je modal lepší než bavlna?',
         '<p>Na omak je měkčí a hebčí a lépe splývá. Bavlna snese vyšší teploty a bývá odolnější proti oděru. Na sport, kde se hodně potíte, nejsou ideální ani jeden, oba schnou pomalu.</p>'),
        ('Hodí se modal na sport?',
         '<p>Spíš na lehčí aktivity, jako je jóga, protahování nebo procházky. Na běh, kolo nebo túry v chladu je lepší syntetika nebo merino, protože modal drží vlhkost a nehřeje.</p>'),
        ('Sráží se modal po praní?',
         '<p>Méně než klasická viskóza. Přesto doporučujeme prát podle štítku, obvykle na 30 °C šetrným programem, a do sušičky ho dávat jen tehdy, když to výrobce dovoluje.</p>'),
        ('Co znamená TENCEL Modal?',
         '<p>TENCEL je obchodní značka rakouské firmy Lenzing. TENCEL Modal je její modalové vlákno, TENCEL Lyocell je jiné vlákno vyráběné jiným procesem. Na štítku pak bývá uvedeno „modal“ nebo „lyocell“.</p>'),
        ('Proč je spodní prádlo z modalu tak oblíbené?',
         '<p>Je hebké, hladké a s příměsí elastanu dobře sedí na těle, netlačí a nedře. Příjemně působí i v teple, protože odvádí vlhkost od pokožky.</p>'),
        ('Je modal vhodný pro alergiky?',
         '<p>Modal je hladký a mnoha lidem je na kůži příjemný. Reakce ale může způsobit i barvivo nebo úprava látky. Pokud máte kožní potíže, poraďte se s lékařem a vybírejte podle jeho doporučení.</p>'),
    ],
    cats=['sportovni-spodni-pradlo', 'sportovni-tricka', 'merino-pradlo', 'funkcni-tricka', 'leginy'],
    updated='2026-11-18')

# ---------------------------------------------------------------- nubuk
LEATHERS = T(['Materiál', 'Z jaké strany kůže', 'Povrch', 'Odolnost a péče'], [
    ['Hladká kůže', 'Lícová (vnější) strana, nebroušená', 'Hladký, lesklý nebo matný', 'Nejodolnější, krém nebo vosk'],
    ['Nubuk', 'Lícová strana jemně zbroušená', 'Sametový, krátký jemný vlas', 'Odolný, kartáč a sprej, žádný vosk na hladkou kůži'],
    ['Semiš (velur)', 'Rubová strana nebo štípenka', 'Hrubší a delší vlas', 'Méně odolný, saje vodu, kartáč a sprej'],
])

GUIDES['nubuk'] = dict(
    name='Nubuk',
    h1='Nubuk: co to je, jak se liší od semiše a jak se o něj starat',
    seo_title='Nubuk: co to je a jak se o nubukové boty starat',
    seo_desc='Nubuk je broušená lícová kůže se sametovým povrchem. Rozdíl oproti semiši a hladké kůži, čištění, kartáč, impregnace, sušení mokrých bot a čemu se vyhnout.',
    intro_html=(
        '<p><strong>Nubuk</strong> je pravá kůže, nejčastěji hovězí, jejíž vnější lícová strana se jemně zbrousí. Vznikne tak sametový povrch s velmi krátkým vlasem. '
        'Od semiše se liší tím, že semiš se brousí z vnitřní, rubové strany kůže nebo ze štípenky, takže je měkčí, ale méně odolný. Nubuk si díky lícové vrstvě zachovává pevnost, ale kvůli zbroušenému povrchu potřebuje jinou péči než hladká kůže.</p>'
        '<p>Starat se o něj znamená tři věci: pravidelně ho čistit měkkým kartáčem nebo vodou, impregnovat sprejem určeným pro nubuk a semiš a sušit ho pomalu, nikdy na topení. '
        'Krémy a vosky na hladkou kůži na něj nepatří, slepí vlas a povrch ztmaví. V průvodci najdete postup čištění, sušení mokrých bot i nejčastější chyby, které nubukové boty zničí.</p>'
        '<p>Sporteka srovnává nabídky českých e-shopů, takže pod některými částmi uvidíte nubukové trekové a zimní boty nebo prostředky na impregnaci.</p>'
    ),
    sections=[
        dict(h2='Co je nubuk a jak vzniká',
             html=(
                 '<p>Kůže zvířete má dvě strany. Vnější, lícová strana je hustá a pevná, vnitřní strana je volnější a vláknitá. Silnější kůže se při zpracování často štípe na vrstvy: horní vrstva s lícem a spodní štípenku.</p>'
                 '<p>Nubuk vzniká z lícové vrstvy. Její povrch se po vyčinění jemně přebrousí, takže se z hladké kůže stane matná, sametová plocha s krátkým vlasem. Když po nubuku přejedete prstem, vlas se ohne a materiál změní odstín. '
                 'Podle toho ho snadno poznáte. Protože zůstává zachovaná hustá lícová struktura, je nubuk pevnější a odolnější než semiš.</p>'
                 '<p>Zdroje se rozcházejí v tom, zda nubuk vzniká z celé, nebo jen z horní lícové vrstvy. Pro péči to nehraje roli. Důležité je, že broušený povrch je otevřený, a proto snáz pije vodu, mastnotu i nečistoty.</p>'
             )),
        dict(h2='Nubuk, semiš a hladká kůže v přehledu',
             html=(
                 LEATHERS +
                 '<p><strong>Hladká kůže</strong> má zachovaný přirozený povrch. Snese krémy a vosky, které ji vyživí a zároveň uzavřou. <strong>Semiš</strong>, někdy prodávaný jako velur, má hrubší a delší vlas a je nejměkčí. '
                 'Rychleji ale nasákne a odře se. <strong>Nubuk</strong> je mezi nimi: vypadá podobně jako semiš, ale je hustší a odolnější. Proto se hodně používá na trekové boty, zimní obuv, tenisky a sandály.</p>'
                 '<p>Na nubuk a semiš se používají stejné přípravky. Výrobci je označují jako „nubuck &amp; suede“, česky nubuk a semiš. Pozor u bot kombinovaných: na hladké části kůže použijte krém, na nubukové jen sprej.</p>'
             )),
        dict(h2='Kde se s nubukem setkáte',
             html=(
                 '<ul><li><strong>Trekové boty:</strong> nubuk je klasický materiál svršků pevnějších turistických bot. Často je doplněný membránou, například GORE-TEX, která brání průniku vody dovnitř.</li>'
                 '<li><strong>Zimní obuv:</strong> zateplené kotníkové boty a sněhule s nubukovým svrškem musí odolat soli a mokrému sněhu.</li>'
                 '<li><strong>Tenisky a vycházková obuv:</strong> nubuk dodá teniskám prémiový vzhled, ale bez impregnace se rychle zašpiní.</li>'
                 '<li><strong>Sandály a pantofle:</strong> nubukové pásky jsou měkké, ale nesnášejí časté máčení.</li></ul>'
                 '<p>Trekové boty s nubukovým svrškem porovnáte v kategoriích <a href="/trekova-obuv/">treková obuv</a>, <a href="/vysoke-trekove-boty/">vysoké trekové boty</a> a <a href="/nizke-trekove-boty/">nízké trekové boty</a>. '
                 'Pánské a dámské modely jsou zvlášť na stránkách <a href="/trekove-boty-panske/">pánské trekové boty</a> a <a href="/damske-trekove-boty/">dámské trekové boty</a>.</p>'
             ), cat='trekova-obuv', n=4),
        dict(h2='Běžná péče: kartáč po každém nošení',
             html=(
                 '<p>Nubuk nejlépe ochráníte tím, že nečistota nezůstane v jeho vlasu dlouho. Stačí pár minut po každé túře nebo náročnějším dni:</p>'
                 '<ol><li>Nechte boty oschnout, pokud jsou jen lehce zaprášené nebo od zaschlého bláta.</li>'
                 '<li>Vyklepejte boty o sebe a sundejte hrubé kusy bláta.</li>'
                 '<li>Měkkým kartáčem na nubuk a semiš přejeďte celý svršek. Nejdřív proti směru vlasu, aby se uvolnila špína, pak po směru, aby se povrch sjednotil.</li>'
                 '<li>Zkontrolujte švy a místo napojení svršku na podrážku. Tam se špína drží nejdéle.</li></ol>'
                 '<p>Kartáče se prodávají jako krepové (z pryže), s měkkými syntetickými štětinami nebo kombinované s mosaznými drátky. Pro nubuk volte pryžový nebo měkký kartáč, protože krátký vlas se snadno sedře. '
                 'Mosazné štětiny jsou určené spíš pro hrubší semiš, na nubuk je použijte jen lehce a výjimečně.</p>'
             )),
        dict(h2='Jak vyčistit špinavý nubuk krok za krokem',
             html=(
                 '<p>Hrubou špínu odstraníte vodou. Výrobce trekové obuvi Meindl doporučuje boty po túře omýt větším množstvím vody a kartáčem. Postup:</p>'
                 '<ol><li>Vyndejte tkaničky a vložky.</li>'
                 '<li>Svršek namočte vlažnou vodou a kartáčem nebo houbou vyčistěte celou botu, ne jen skvrnu. Jen tak nevzniknou mapy a ostré okraje mezi mokrým a suchým místem.</li>'
                 '<li>Na silnější špínu použijte čisticí prostředek určený pro nubuk a semiš podle návodu výrobce. Obyčejný saponát může kůži vysušit a ztmavit.</li>'
                 '<li>Opláchněte vodou a přebytečnou vlhkost vysajte ručníkem.</li>'
                 '<li>Boty usušte podle postupu níže a po vyschnutí znovu prokartáčujte.</li></ol>'
                 '<p><strong>Jednotlivé skvrny</strong> zkuste nejdřív vygumovat. Na nubuk a semiš se prodávají speciální gumy, v nouzi poslouží čistá pryžová guma na tužku. Značka Keen u odolných skvrn radí opatrně ťupkat hadříkem s bílým octem nebo lihem, '
                 'ale nejdřív na nenápadném místě. Skvrny nikdy nedrhněte silou, vlas byste vydřeli a vznikla by lesklá ploška.</p>'
             )),
        dict(h2='Impregnace nubuku: čím a kdy',
             html=(
                 '<p>Nubuk bez impregnace vodu rychle přijme, ztmavne a po vyschnutí může ztvrdnout. Impregnace vytvoří ochranu, po které voda steče a nečistota se tolik nezachytí. U bot s membránou chrání svršek, aby nenasákl. Membrána pak lépe odvádí páru.</p>'
                 '<ul><li><strong>Jaký prostředek:</strong> sprej nebo emulze na nubuk a semiš. Vosky a krémy na hladkou kůži nepoužívejte, slepí vlas a změní vzhled.</li>'
                 '<li><strong>Kdy poprvé:</strong> ještě před prvním nošením. Meindl doporučuje nanést impregnaci na nové boty dřív, než vyrazíte ven.</li>'
                 '<li><strong>Na suché, nebo vlhké boty:</strong> podle návodu konkrétního přípravku. Některé (třeba Meindl Wetproof) se nanášejí na mírně vlhké boty, jiné na suché.</li>'
                 '<li><strong>Jak často:</strong> když voda přestane na povrchu tvořit kapky a začne se vsakovat. U trekových bot obvykle po každém důkladném čištění.</li></ul>'
                 '<p>Sprej nanášejte venku nebo u otevřeného okna ze vzdálenosti podle návodu, rovnoměrně po celé botě. Počítejte s tím, že nubuk může po impregnaci mírně ztmavnout. Vyzkoušejte to nejdřív na jazyku boty. '
                 'Přípravky najdete v kategorii <a href="/impregnace/">impregnace</a> a kartáče, gumy a další potřeby mezi <a href="/doplnky-k-obuvi/">doplňky k obuvi</a>.</p>'
             ), cat='impregnace', n=4),
        dict(h2='Jak usušit mokré nubukové boty',
             html=(
                 '<ol><li>Vyndejte vložky a povolte nebo vytáhněte tkaničky, aby se bota otevřela.</li>'
                 '<li>Vycpěte botu zmačkaným papírem, který vlhkost odsaje. Když je papír mokrý, vyměňte ho. Až bota proschne, papír vyndejte.</li>'
                 '<li>Nechte botu sušit při pokojové teplotě na vzdušném místě. Meindl i LOWA varují před sluncem a zdroji tepla.</li>'
                 '<li>Kdo má dřevěné napínáky, vloží je do skoro suché boty, aby si udržela tvar.</li>'
                 '<li>Po úplném vyschnutí boty prokartáčujte a obnovte impregnaci.</li></ol>'
                 '<p>Sušení trvá podle promočení několik hodin až přes noc i déle. Nespěchejte. Kůže sušená na topení, u kamen nebo fénem rychle ztratí vláhu, scvrkne se, ztvrdne a může popraskat. '
                 'Navíc teplo škodí lepeným spojům podrážky. Vyjmuté vložky sušte zvlášť, nové najdete v kategorii <a href="/vlozky-do-bot/">vložky do bot</a>.</p>'
             )),
        dict(h2='Zimní boty z nubuku, sůl a sníh',
             html=(
                 '<p>V zimě nubuk trápí hlavně posypová sůl. Po zaschnutí zanechá bílé mapy a kůži vysušuje. Doma proto boty hned otřete vlhkým hadříkem a nechte je pomalu uschnout. '
                 'Pokud mapy zůstanou, zkuste je setřít hadříkem navlhčeným ve vodě s trochou octa, zase nejdřív na skrytém místě, a po zaschnutí povrch prokartáčujte.</p>'
                 '<p>Zimní boty impregnujte na začátku sezóny a pak průběžně, zvlášť před delší chůzí ve sněhu. Mokrý sníh pronikne do neošetřeného nubuku rychleji než déšť, protože na botě leží dlouho. '
                 'Zateplené modely porovnáte v kategoriích <a href="/zimni-obuv/">zimní obuv</a>, <a href="/panske-zimni-boty/">pánské zimní boty</a> a <a href="/damske-zimni-boty/">dámské zimní boty</a>.</p>'
             ), cat='zimni-obuv', n=4),
        dict(h2='Čemu se u nubuku vyhnout',
             html=(
                 '<ul><li><strong>Pračka:</strong> většina výrobců kožené obuvi praní v pračce nepovoluje. Kůže se zdeformuje a lepené spoje povolí.</li>'
                 '<li><strong>Topení, fén, slunce:</strong> kůže ztvrdne a popraská.</li>'
                 '<li><strong>Vosk a krém na hladkou kůži:</strong> slepí vlas a vytvoří tmavé, lesklé skvrny.</li>'
                 '<li><strong>Drhnutí skvrn:</strong> vydře vlas a zanechá lesklou plošku. Skvrny raději ťupkejte a gumujte.</li>'
                 '<li><strong>Uložení mokrých bot do skříně:</strong> v uzavřeném prostoru začnou plesnivět.</li>'
                 '<li><strong>Neověřené domácí triky:</strong> mléko, olej nebo kávu na nubuk nedávejte, skvrnu spíš rozšíří.</li></ul>'
                 '<p>Když vlas zplihne a povrch zleskne, často pomůže důkladné prokartáčování gumovým kartáčem. Hluboko vydřená místa už opravit nejde, ale prodávají se barevné spreje, které sjednotí odstín.</p>'
             )),
        dict(h2='Jak vybrat nubukové boty',
             html=(
                 '<p>Nubuk se hodí tomu, kdo chce kožené boty s dobrou odolností, ale nevadí mu pravidelná péče. Při výběru se zaměřte na:</p>'
                 '<ul><li><strong>Tloušťku kůže:</strong> u trekových bot se uvádí v milimetrech. Silnější nubuk vydrží víc, ale déle se rozchodí.</li>'
                 '<li><strong>Membránu:</strong> pokud chodíte v mokru, hledejte nubukové boty s membránou. Bez ní promoknou dřív nebo později i po impregnaci.</li>'
                 '<li><strong>Počet švů:</strong> čím méně švů, tím méně míst, kudy proniká voda.</li>'
                 '<li><strong>Barvu:</strong> světlý nubuk je hezký, ale každá skvrna je na něm vidět. Na túry volte tmavší odstíny.</li></ul>'
                 '<p>Na turistiku v létě a lehčí terén se hodí i boty ze syntetiky, které schnou rychleji. Obecné rady k výběru najdete v kategorii <a href="/sportovni-obuv/">sportovní obuv</a>. '
                 'Péči o další materiály oblečení popisují průvodci <a href="/jak-prat-perovou-bundu/">jak prát péřovou bundu</a> a <a href="/co-je-modal/">co je modal</a>.</p>'
             )),
    ],
    faq=[
        ('Co je nubuk?',
         '<p>Nubuk je pravá kůže, obvykle hovězí, jejíž lícová strana je jemně zbroušená. Má sametový povrch s krátkým vlasem a je odolnější než semiš, ale potřebuje jinou péči než hladká kůže.</p>'),
        ('Jaký je rozdíl mezi nubukem a semišem?',
         '<p>Nubuk se brousí z vnější, lícové strany kůže, semiš z vnitřní strany nebo ze štípenky. Nubuk má kratší a jemnější vlas a je pevnější, semiš je měkčí, ale rychleji nasákne a odře se.</p>'),
        ('Čím čistit nubukové boty?',
         '<p>Suchou špínu odstraňte měkkým nebo gumovým kartáčem, skvrny gumou na nubuk. Silnější znečištění omyjte vlažnou vodou a čisticím prostředkem pro nubuk a semiš. Pak botu nechte pomalu uschnout a prokartáčujte.</p>'),
        ('Můžu nubukové boty prát v pračce?',
         '<p>Většina výrobců kožené obuvi to nedoporučuje. Kůže se může zdeformovat a ztvrdnout a lepené spoje podrážky povolí. Čistěte je ručně vodou a kartáčem.</p>'),
        ('Čím impregnovat nubuk?',
         '<p>Sprejem nebo emulzí určenou pro nubuk a semiš. Vosky a krémy na hladkou kůži nepoužívejte. Impregnujte už nové boty před prvním nošením a pak vždy, když voda přestane po povrchu stékat.</p>'),
        ('Jak usušit promočené nubukové boty?',
         '<p>Vyndejte vložky, vycpěte boty papírem a nechte je sušit při pokojové teplotě, mimo topení a slunce. Papír po čase vyměňte a po proschnutí ho vyjměte. Suché boty prokartáčujte a znovu impregnujte.</p>'),
        ('Jak odstranit sůl z nubukových bot?',
         '<p>Otřete boty vlhkým hadříkem co nejdřív po příchodu domů a nechte je uschnout. Odolné bílé mapy zkuste setřít vodou s trochou octa, napřed na skrytém místě, a pak povrch prokartáčujte.</p>'),
        ('Proč nubuk po impregnaci ztmavl?',
         '<p>Některé přípravky povrch mírně ztmaví, výrobci na to upozorňují. Proto je dobré nový sprej vyzkoušet na jazyku boty. Ztmavnutí bývá po úplném vyschnutí a prokartáčování menší.</p>'),
        ('Je nubuk vhodný na turistiku?',
         '<p>Ano, nubuk je jeden z nejčastějších materiálů trekových bot. Je odolný a s membránou a pravidelnou impregnací dobře zvládá mokro. Počítejte ale s tím, že schne pomaleji než syntetika.</p>'),
    ],
    cats=['trekova-obuv', 'zimni-obuv', 'impregnace', 'doplnky-k-obuvi', 'vysoke-trekove-boty', 'tenisky'],
    updated='2026-11-18')

# ---------------------------------------------------------------- jak-prat-perovou-bundu
GUIDES['jak-prat-perovou-bundu'] = dict(
    name='Jak prát péřovou bundu',
    h1='Jak prát péřovou bundu v pračce a správně ji usušit',
    seo_title='Jak prát péřovou bundu: pračka, prací prostředek a sušení',
    seo_desc='Péřovou bundu vyperete v pračce: šetrný program, prostředek na peří, víc máchání, pomalé ždímání a sušička s tenisáky. Postup krok za krokem a chyby.',
    intro_html=(
        '<p><strong>Jak prát péřovou bundu?</strong> V pračce, nejlépe s předním plněním, na šetrný program s nízkou teplotou podle štítku, často 30 °C. Použijte prací prostředek určený na peří, '
        'přidejte máchání navíc, ždímejte nízkými otáčkami a bundu pak hned sušte v sušičce na nízkou teplotu se dvěma až třemi čistými tenisovými míčky. '
        'Sušení trvá několik hodin a skončit má, až když je bunda znovu nadýchaná. Peří se nesmí nechat dlouho mokré, jinak se slepí do chuchvalců a začne zapáchat.</p>'
        '<p>Postup vychází z návodů výrobců outdoorového oblečení, například Rab a Patagonia, a výrobců pracích prostředků na peří. Vždy ale platí štítek vaší bundy. '
        'Pokud výrobce pračku nedovoluje, řiďte se jím. V průvodci najdete přípravu, nastavení pračky, sušení se sušičkou i bez ní, obnovu impregnace a chyby, kterým je lepší se vyhnout.</p>'
        '<p>Stejný postup s malými úpravami platí i pro péřový spacák nebo vestu. Pod jednotlivými částmi uvidíte péřové bundy, prošívané bundy a spacáky z nabídky českých e-shopů.</p>'
    ),
    sections=[
        dict(h2='Než začnete: štítek, kapsy a zipy',
             html=(
                 '<p>Péřová bunda je náročnější na praní ne kvůli látce, ale kvůli náplni. Mokré peří se slepí, ztratí objem a tím i schopnost hřát. Proto se vyplatí pečlivá příprava:</p>'
                 '<ol><li><strong>Přečtěte štítek.</strong> Symbol vaničky s číslem udává nejvyšší teplotu, čárky pod ní šetrný program. Symbol čtverce s kruhem znamená, zda bunda smí do sušičky.</li>'
                 '<li><strong>Zkontrolujte, zda je to opravdu peří.</strong> Prošívané bundy bývají často se syntetickou výplní, ta se pere jinak. Složení výplně najdete na štítku.</li>'
                 '<li><strong>Vyprázdněte kapsy</strong> a vyndejte případný odepínací kožíšek z kapuce.</li>'
                 '<li><strong>Zapněte všechny zipy a suché zipy</strong>, aby se o ně látka netrhala.</li>'
                 '<li><strong>Prohlédněte bundu.</strong> Malé dírky zalepte opravnou páskou nebo zašijte, jinak peří při praní uteče.</li>'
                 '<li><strong>Obraťte bundu naruby</strong>, šetří to vnější látku i její impregnaci.</li></ol>'
             )),
        dict(h2='Jaký prací prostředek na peří',
             html=(
                 '<p>Nejlepší volba je prostředek určený přímo na peří, například Nikwax Down Wash Direct, Toko Down Wash nebo Holmenkol Down Wash. Vyčistí peří, ale nezbaví ho přirozených tuků, '
                 'díky kterým zůstává pružné. Některé z nich zároveň obnovují vodoodpudivou úpravu peří i vnější látky.</p>'
                 '<p>Rab připouští i běžný jemný prací prostředek bez enzymů (takzvaný nebiologický). Nikdy ale nepoužívejte:</p>'
                 '<ul><li><strong>aviváž</strong>, která obalí peří tenkým filmem a sníží jeho schopnost zadržovat teplý vzduch,</li>'
                 '<li><strong>bělidla a odstraňovače skvrn</strong>, které poškozují peří i látku,</li>'
                 '<li><strong>prací prášek</strong>, který se z peří špatně vymáchá,</li>'
                 '<li><strong>velké dávky běžného gelu</strong>, protože zbytky saponátu peří slepují.</li></ul>'
                 '<p>Před praním vyčistěte i dávkovač v pračce a Rab dokonce doporučuje pustit jedno až dvě máchání naprázdno, aby v bubnu nezůstaly zbytky běžného prášku nebo aviváže. '
                 'Prací a impregnační prostředky na peří najdete v kategorii <a href="/impregnace/">impregnace</a>.</p>'
             ), cat='impregnace', n=4),
        dict(h2='Nastavení pračky krok za krokem',
             html=(
                 '<ol><li><strong>Pračka:</strong> nejvhodnější je pračka s předním plněním. Pračka s horním plněním a míchadlem uprostřed bundu víc namáhá. Patagonia ji připouští na program pro ruční nebo jemné praní a Rab doporučuje vložit bundu do síťky.</li>'
                 '<li><strong>Jedna bunda najednou:</strong> peří potřebuje v bubnu místo, aby se rovnoměrně promočilo a vymáchalo.</li>'
                 '<li><strong>Program:</strong> šetrný, jemný nebo program na vlnu, s pomalým pohybem bubnu. Rab doporučuje delší šetrný cyklus.</li>'
                 '<li><strong>Teplota:</strong> nízká, podle štítku. Výrobci uvádějí studenou až chladnou vodu, na štítcích péřových bund se často objevuje 30 °C.</li>'
                 '<li><strong>Dávka prostředku:</strong> podle návodu na lahvi. Více prostředku neznamená lepší vyprání.</li>'
                 '<li><strong>Máchání navíc:</strong> zapněte extra máchání. Zbytky saponátu v peří brání nadýchání.</li>'
                 '<li><strong>Ždímání:</strong> nízké otáčky. Mokré peří je těžké a rychlé točení s velkým množstvím vody může podle výrobců prostředků poškodit vnitřní přepážky. Po vyprání můžete pustit ještě jedno až dvě pomalá odstředění.</li></ol>'
                 '<p>Mokrou bundu z pračky vyndávejte opatrně a podepřete ji celou, třeba ručníkem. Netahejte za rukáv, váha mokrého peří by mohla roztrhnout vnitřní přepážky.</p>'
             )),
        dict(h2='Sušení v sušičce s tenisovými míčky',
             html=(
                 '<p>Sušička je pro péřovou bundu ideální, protože peří během sušení stále rozhýbává. Postup podle návodů výrobců:</p>'
                 '<ol><li>Vložte bundu do sušičky hned po vyprání. Necháte-li ji ležet mokrou, peří se slepí.</li>'
                 '<li>Nastavte nízkou nebo nejvýš střední teplotu. Vysoká teplota může poškodit tenkou vnější látku.</li>'
                 '<li>Přidejte dva až tři čisté tenisové míčky nebo sušicí kuličky. Rozbíjejí chuchvalce peří. Patagonia jako alternativu uvádí velký bavlněný ručník.</li>'
                 '<li>Každých 20 až 30 minut bundu vyndejte, protřepte a prsty rozmělněte hrudky peří v jednotlivých komorách.</li>'
                 '<li>Opakujte cykly, dokud není bunda celá nadýchaná. Rab uvádí obvykle 3 až 5 hodin, u objemnějších kusů i déle.</li></ol>'
                 '<p>Vnější látka uschne dřív než peří uvnitř. Pokud cítíte uvnitř komor hrudky, bunda ještě není suchá. Po sušení ji nechte den nebo dva volně viset v suché místnosti a teprve pak ji uložte. '
                 'Pokud doma sušičku nemáte, hledejte prádelnu se sušičkami. Je to rychlejší a bezpečnější než týden sušení na sušáku.</p>'
             ), cat='perove-bundy', n=4),
        dict(h2='Sušení bez sušičky',
             html=(
                 '<p>I bez sušičky se péřová bunda usuší, jen to trvá déle a vyžaduje trpělivost:</p>'
                 '<ul><li>Bundu položte naplocho na sušák nebo na rošt v teplé, větrané místnosti. Neveste ji na ramínko, mokré peří by steklo do spodní části komor.</li>'
                 '<li>Několikrát denně ji protřepte, otočte a prsty rozbijte hrudky peří. Rab doporučuje při sušení bez sušičky protřepávat často.</li>'
                 '<li>Nepokládejte ji přímo na topení ani do slunce. Mírná teplota z dálky pomůže, horký radiátor může poškodit látku.</li>'
                 '<li>Počítejte s několika dny. Dokud je uvnitř cítit vlhkost, bundu nenoste a neukládejte, jinak může začít zapáchat.</li></ul>'
                 '<p>Když je bunda po usušení na sušáku dál zplihlá, pomůže krátké sušení v sušičce s tenisáky, i když jste ji předtím sušili jinak.</p>'
             )),
        dict(h2='Jak často péřovou bundu prát',
             html=(
                 '<p>Méně, než si myslíte. Každé praní peří trochu namáhá, takže Rab doporučuje prát péřovou bundu zhruba jednou za sezónu, nebo dřív, když je viditelně špinavá nebo peří splasklo a přestává hřát. '
                 'Pot a kožní maz totiž peří postupně slepují a bunda pak hřeje méně, i když vypadá čistě.</p>'
                 '<p>Mezi praními stačí <strong>lokální čištění</strong>. Mastné skvrny na límci, manžetách nebo kolem kapes otřete vlhkým hadříkem s kapkou jemného prostředku a vytřete do sucha. '
                 'Po každém nošení bundu nechte vyvětrat, ne ji hned zavřít do skříně. Pokud nosíte pod bundou vrstvu, která pot zachytí, vydrží bunda čistá déle. Vhodné jsou <a href="/termopradlo/">termoprádlo</a> nebo <a href="/fleecove-mikiny/">fleecové mikiny</a>.</p>'
             )),
        dict(h2='Obnova impregnace po praní',
             html=(
                 '<p>Vnější látka péřových bund má vodoodpudivou úpravu, často označovanou DWR. Díky ní na bundě drobný déšť nebo sníh tvoří kapky a nenasákne. Úprava se nošením a praním opotřebovává. '
                 'Když voda přestane po látce stékat a místo toho ji ztmaví, je čas na obnovu.</p>'
                 '<ul><li><strong>Kombinovaný prostředek:</strong> některé prostředky na praní peří obnovují úpravu zároveň s praním. Stačí jeden cyklus.</li>'
                 '<li><strong>Samostatná impregnace:</strong> po vyprání se do pračky přidá impregnační přípravek pro péřové výrobky, například Nikwax Down Proof, podle jeho návodu.</li>'
                 '<li><strong>Sprej:</strong> na lokální obnovu ramen a kapuce, nanáší se na čistou a vlhkou nebo suchou bundu podle návodu.</li></ul>'
                 '<p>Některé impregnace se podle výrobce aktivují teplem v sušičce na nízkou teplotu, jiné ne. Řiďte se návodem na obalu. Péřová bunda není nepromokavá. Na déšť vezměte přes ni bundu z kategorie <a href="/nepromokave-bundy/">nepromokavé bundy</a>.</p>'
             )),
        dict(h2='Péřový spacák a prošívaná bunda se syntetikou',
             html=(
                 '<p><strong>Péřový spacák</strong> se pere podobně jako bunda, je ale větší a mokrý velmi těžký. Do domácí pračky se vejde jen menší letní spacák. Rab doporučuje prát spacák aspoň jednou ročně, '
                 'když ho používáte často, i častěji. Velké zimní spacáky je lepší svěřit prádelně s velkou pračkou a sušičkou nebo servisu výrobce. Rab uvádí, že spacák se nemá chemicky čistit ani žehlit. '
                 'Uložte ho volně v úložném pytli, nikdy ne stlačený v kompresním obalu. Péřové spacáky porovnáte v kategorii <a href="/perove-spacaky/">péřové spacáky</a>.</p>'
                 '<p><strong>Prošívaná bunda se syntetickou výplní</strong> vypadá stejně jako péřová, ale je jednodušší na údržbu. Snese běžné jemné praní a usuší se rychleji, protože syntetická vlákna se neslepují jako peří. '
                 'I tak se řiďte štítkem a nepoužívejte aviváž. Nabídku najdete v kategorii <a href="/prosivane-bundy/">prošívané bundy</a>, dámské modely na stránce <a href="/damska-prosivana-bunda/">dámská prošívaná bunda</a>.</p>'
             ), cat='prosivane-bundy', n=4),
        dict(h2='Nejčastější chyby při praní péřové bundy',
             html=(
                 '<ul><li><strong>Aviváž a běžný prášek:</strong> peří slepí a bunda pak hřeje méně.</li>'
                 '<li><strong>Vysoké otáčky odstřeďování:</strong> mokré peří je těžké a může roztrhnout přepážky.</li>'
                 '<li><strong>Vyndání ze sušičky moc brzy:</strong> v peří zůstane vlhkost, slepí se do hrudek a začne zapáchat.</li>'
                 '<li><strong>Sušení na ramínku:</strong> peří steče do spodní části komor a už se rovnoměrně nerozloží.</li>'
                 '<li><strong>Chemické čištění:</strong> jen pokud ho štítek výslovně dovoluje. Rozpouštědla mohou peří zbavit přirozených tuků.</li>'
                 '<li><strong>Žehlení:</strong> tenká syntetická látka se může roztavit.</li>'
                 '<li><strong>Dlouhodobé uložení ve stlačeném obalu:</strong> peří ztratí pružnost. Přes léto bundu pověste volně do skříně nebo uložte do velkého prodyšného vaku.</li></ul>'
                 '<p>Pokud bunda po vyprání i důkladném usušení zůstává zplihlá a má hrudky, Rab radí vyprat ji znovu a sušení věnovat víc času. Nové kusy porovnáte v kategorii <a href="/perove-bundy/">péřové bundy</a>, '
                 'pánské a dámské zvlášť na stránkách <a href="/panska-perova-bunda/">pánská péřová bunda</a> a <a href="/perova-bunda-damska/">dámská péřová bunda</a>.</p>'
             )),
    ],
    faq=[
        ('Můžu prát péřovou bundu v pračce?',
         '<p>Ano, většina péřových bund se v pračce prát smí. Řiďte se štítkem, zvolte šetrný program s nízkou teplotou, prostředek na peří, extra máchání a nízké otáčky ždímání.</p>'),
        ('Na kolik stupňů prát péřovou bundu?',
         '<p>Podle štítku, často na 30 °C. Výrobci obecně doporučují studenou až chladnou vodu. Vyšší teplota peří nevyčistí lépe, ale může poškodit látku a impregnaci.</p>'),
        ('Proč dávat do sušičky tenisové míčky?',
         '<p>Míčky během sušení narážejí do bundy a rozbíjejí chuchvalce peří, takže se rovnoměrně rozloží a bunda se nadýchá. Stačí dva až tři čisté míčky, případně sušicí kuličky.</p>'),
        ('Jak dlouho se suší péřová bunda?',
         '<p>V sušičce na nízkou teplotu obvykle tři až pět hodin, podle objemu i déle. Bez sušičky několik dní. Bunda je suchá, až když je celá nadýchaná a v komorách nejsou hrudky.</p>'),
        ('Čím prát péřovou bundu, když nemám speciální prostředek?',
         '<p>Rab připouští jemný prací prostředek bez enzymů v malé dávce. Vyhněte se prášku, aviváži a bělidlům. Speciální prostředek na peří je ale šetrnější a mnohé zároveň obnovují impregnaci.</p>'),
        ('Proč je péřová bunda po vyprání zplihlá a hrudkovitá?',
         '<p>Peří je skoro jistě ještě vlhké nebo v něm zůstal saponát. Pokračujte v sušení s tenisovými míčky a hrudky rozmělňujte prsty. Když to nepomůže, bundu znovu vymáchejte a usušte.</p>'),
        ('Jak často prát péřovou bundu?',
         '<p>Zhruba jednou za sezónu, nebo když je viditelně špinavá či přestává hřát. Mezi praními stačí vyvětrat ji a lokálně otřít skvrny vlhkým hadříkem.</p>'),
        ('Můžu péřovou bundu dát do čistírny?',
         '<p>Jen pokud to štítek výslovně dovoluje. Někteří výrobci chemické čištění nedoporučují, protože rozpouštědla mohou peří zbavit přirozených tuků. Praní ve vodě s prostředkem na peří je obvykle bezpečnější.</p>'),
        ('Jak uložit péřovou bundu přes léto?',
         '<p>Čistou a úplně suchou ji pověste volně do skříně nebo uložte do velkého prodyšného vaku. Ve stlačeném stavu ji nenechávejte celé měsíce, peří by ztratilo pružnost.</p>'),
        ('Je péřová bunda nepromokavá?',
         '<p>Ne. Vnější látka má většinou jen vodoodpudivou úpravu, která zvládne krátký déšť nebo sníh. Při vytrvalém dešti peří promokne, proto přes ni noste nepromokavou bundu.</p>'),
    ],
    cats=['perove-bundy', 'prosivane-bundy', 'impregnace', 'perove-spacaky', 'zimni-bundy'],
    updated='2026-11-18')
