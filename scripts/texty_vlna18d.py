"""sporteka.cz — wave 18d (4. 11. 2026): long texts (>= 1650 words) for plaste-a-duse, stolni-tenis, kombinezy, kempingove-nadobi.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ plaste-a-duse
NEW['plaste-a-duse'] = dict(long=True,
    title='Pláště a duše na kolo: rozměry, ventilky, výběr',
    desc='Pláště a duše na kolo: jak přečíst rozměr, vybrat ventilek, drátovou či skládací patku, bezdušové pláště a opravy defektu. Srovnání českých obchodů.',
    intro='<p>Plášť a duše jsou jediné části kola, které se dotýkají země, a proto na nich závisí přilnavost, valivý odpor, komfort i počet defektů. V kategorii <strong>pláště a duše</strong> najdete '
          'pláště na silniční, gravelová, trekingová, horská i dětská kola, bezdušové varianty, běžné i odlehčené duše a další drobnosti kolem nich. Nabídka je velká a na první pohled se mnohé kusy podobají, '
          'rozdíl ale dělá šířka, směs gumy, vzorek, typ patky a ventilek.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů u stejného zboží, takže u konkrétního rozměru rychle uvidíte, kdo ho má skladem. Kategorie je součástí oddílu <a href="/cyklo-dily/">díly a pláště</a> a v bezprostřední blízkosti '
          'leží <a href="/cyklo-kola-a-rafky/">zapletená kola a ráfky</a>, <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a> i <a href="/cyklo-udrzba/">údržba kola</a>. Níže vysvětlíme čtení rozměrů, výběr podle terénu a opravu defektu.</p>',
    guide='<h2>Rozměr pláště: jak ho přečíst</h2>'
          '<p>Na boku každého pláště je vyražený rozměr a bez něj se při nákupu nevyhnete chybě. Najdete tam obvykle dva zápisy. První je starší palcový, například 29 x 2,35, kde první číslo značí přibližný vnější průměr kola a druhé šířku pláště v palcích. '
          'Druhý zápis je norma ETRTO, například 60-622. První číslo je šířka v milimetrech a druhé je vnitřní průměr, tedy průměr ráfku, na který plášť dosedá. Právě ten druhý údaj musí sedět přesně, šířka se může v mezích ráfku lišit.</p>'
          + T(['Označení kola', 'Průměr ráfku ETRTO', 'Kde se používá'], [
              ['29 palců a 700C', '622 mm', 'horská kola větších velikostí, gravel, silnice, trekink, městská kola'],
              ['27,5 palce', '584 mm', 'horská kola menších rámů a část enduro modelů'],
              ['26 palců', '559 mm', 'starší horská kola, některá dětská a městská kola'],
              ['24 a 20 palců', '507 a 406 mm', 'dětská kola a skládací kola'],
              ['16 a 12 palců', '305 a 203 mm', 'nejmenší dětská kola a odrážedla']]) +
          '<p>Pozor na to, že 29 palců a 700C mají stejný průměr ráfku, ale liší se zvyklostmi: silniční a trekingové pláště se zapisují francouzským způsobem v milimetrech a horské v palcích. Při nákupu proto porovnávejte vždy číslo 622 a nehledejte jen „29“. '
          'Sedí-li průměr, zbývá ověřit šířku. Výrobce ráfku uvádí, jak úzký a jak široký plášť ráfek unese. Příliš úzký plášť na širokém ráfku se tvaruje špatně a příliš široký na úzkém může být nestabilní.</p>'
          '<h2>Typy plášťů podle použití</h2>'
          '<p>Pláště se dělí hlavně podle terénu. Hladký nebo jemně vzorkovaný plášť se na silnici valí lehce, kdežto agresivní kostky v blátě zabírají a na asfaltu hučí a brzdí. Dobrý výběr je vždy kompromis podle toho, kde jezdíte nejčastěji.</p>'
          + T(['Typ pláště', 'Šířka a vzorek', 'Hlavní přednost', 'Na co si dát pozor'], [
              ['Silniční', 'úzký, hladký nebo jemný', 'nízký valivý odpor, nízká hmotnost', 'méně komfortu a menší rezerva na štěrku'],
              ['Gravel', 'střední šířka, jemné kostky uprostřed', 'univerzální na asfalt i šotolinu', 'ověřte, kolik místa je v rámu a vidlici'],
              ['Trekingový a městský', 'střední šířka, často s ochranou proti defektu', 'odolnost a komfort na všem', 'vyšší hmotnost'],
              ['Horský XC', 'širší, nižší kostky', 'rychlost na suchu a mírném terénu', 'horší záběr v bahně'],
              ['Horský trail a enduro', 'široký, vysoké kostky', 'přilnavost a stabilita ve sjezdech', 'těžší a pomalejší do kopce'],
              ['Dětský', 'úzký i široký, často drátová patka', 'odolnost, nízká cena výroby', 'přesný rozměr je u malých kol zásadní']]) +
          '<p>Lehčí plášť stačí v soutěžním nasazení, kde se počítají sekundy, kdežto pro denní dojíždění vyhrává odolnost. Silnější bočnice a výztuž pod běhounem snižují riziko proděravění i řezu, za cenu vyšší hmotnosti. Pokud jezdíte po městských cestách s úlomky skla, trocha navíc v hmotnosti se vyplatí.</p>'
          '<h2>Drátová a skládací patka</h2>'
          '<p>Patka je okraj pláště, kterým se plášť zachytí v ráfku. Drátová patka je z ocelového drátu, je pevná, tvarově stálá a levnější na výrobu, ale plášť je těžší a nelze ho složit. Skládací patka je z kevlaru nebo podobného vlákna, plášť je lehčí, dá se složit do batohu jako náhradní a většinou se lépe tvaruje. '
          'Pro běžné použití stačí drát, pro závodní nebo výpravné jízdy se vyplatí skládací varianta.</p>'
          '<h2>Duše: ventilky a materiál</h2>'
          '<p>Správná duše musí sedět rozměrem a ventilkem. Rozměr duše je uveden jako rozmezí šířek, například 28/37-622, což znamená, že se hodí do plášťů o šířce 28 až 37 mm na ráfku 622. Nejčastější ventilky jsou tři.</p>'
          '<ul><li><strong>Galusák (Presta, francouzský):</strong> tenký, s maticí na špičce, běžný u silničních a lepších horských kol; vejde se i do užšího otvoru v ráfku.</li>'
          '<li><strong>Autoventilek (Schrader):</strong> širší, stejný jako u aut, snadno se huštuje na čerpací stanici, běžný na levnějších a dětských kolech.</li>'
          '<li><strong>Dunlop:</strong> starší typ používaný převážně na městských a historických kolech, dá se použít i s některými pumpami po nasazení adaptéru.</li></ul>'
          '<p>Důležitá je i délka ventilku. U hlubokých ráfků a aerodynamických kol potřebujete delší ventilek, jinak se pumpa nepřipojí. Ventilek musí vyčnívat dost, aby šel nasadit hlavu pumpy. Označení FV 48 nebo FV 60 u duší značí galusák a délku v milimetrech.</p>'
          '<p>Většina duší je z butylu, který dobře drží vzduch, a vyplatí se i levnější kusy do každodenní jízdy. Lehké duše z TPU jsou tenčí, skladné a lehké, jenže dražší a citlivější na špatnou montáž. Hodí se tam, kde záleží na hmotnosti a na objemu náhradní duše v kapse, například ' + B(('maxxis', 'Maxxis'), ('kenda', 'Kenda'), ('cst', 'Cst')) + ' nabízejí běžné butylové i speciálnější modely.</p>'
          '<h2>Bezdušové pláště</h2>'
          '<p>Bezdušová soustava, často zvaná tubeless, nemá duši. Plášť s vhodným ráfkem a ventilkem drží vzduch sám a do jeho vnitřku se přidává tekuté těsnicí mléko, které menší průpichy zalepí. Přináší nižší hmotnost, možnost jet na nižším tlaku s lepším záběrem a méně defektů pro trní a drobné ostré předměty. '
          'Naproti tomu vyžaduje kompatibilní ráfek, pásku v ráfku, ventilek a v pravidelných intervalech obnovu těsnicí tekutiny, protože zasychá. Montáž bývá poprvé náročnější a vyžaduje silnější pumpu nebo kompresor. Pokud bezdušový systém neznáte, vezměte si s sebou k prvním výletům náhradní duši. '
          'Tuto skupinu mají například ' + B(('tufo', 'Tufo'), ('hutchinson', 'Hutchinson'), ('challenge', 'Challenge'), ('wtb', 'WTB')) + '.</p>'
          '<h2>Správný tlak</h2>'
          '<p>Tlak je nejlevnější způsob, jak změnit chování kola. Výrobce uvádí rozmezí na boku pláště a překročit ho se nedoporučuje. Vyšší tlak znamená nižší valivý odpor na hladké silnici, ale tvrdší jízdu a menší záběr. Nižší tlak zlepšuje přilnavost a tlumení terénních nerovností, ovšem zvyšuje riziko, že se duše zaškřípne mezi ráfek a překážku. '
          'Těžší jezdci potřebují tlak vyšší, lehčí nižší a širší plášť unese menší tlak než úzký. Tlak kontrolujte aspoň jednou za dva týdny, protože duše vzduch pomalu ztrácí i bez defektu.</p>'
          '<h2>Výměna a oprava defektu</h2>'
          '<p>Při defektu postupujte klidně a po pořádku. Potřebujete montpáky, pumpu a náhradní duši nebo záplatu. Nářadí najdete v kategorii <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a> a sady do kapsy v sekci <a href="/cyklo-prislusenstvi/">příslušenství</a>.</p>'
          '<ol><li>Vyjměte kolo, u zadního pusťte řetěz na nejmenší kolečko a u kotoučové brzdy nesahejte na kotouč.</li>'
          '<li>Vypusťte zbytek vzduchu, zasuňte montpák pod patku a plášť z jedné strany vyhákněte.</li>'
          '<li>Vyndejte duši a pečlivě prohlédněte vnitřek pláště prsty, hledejte trn, drátek nebo sklo.</li>'
          '<li>Zkontrolujte pásku v ráfku, jestli nezakrývá všechny otvory pro paprsky.</li>'
          '<li>Vložte mírně nafouknutou duši, zasuňte plášť zpátky do ráfku a dejte pozor, ať duše není skřípnutá pod patkou.</li>'
          '<li>Nahustěte na doporučený tlak a zkontrolujte, že je plášť rovnoměrně usazený podle vyražené linky.</li></ol>'
          '<p>Záplatu použijte jen na malé průpichy, u hlubokého řezu duše nebo prasknutého ventilku je výměna spolehlivější. Doma ji můžete zalepit sadou se samolepicími záplatami a před každým lepením povrch očistit a obrousit.</p>'
          '<h2>Směr otáčení a montáž</h2>'
          '<p>Většina plášťů má na boku šipku, která určuje směr otáčení. Při obrácené montáži plášť funguje, ale ztrácí část záběru a odvádí bahno méně účinně. Orientaci u předního a zadního kola uvádí výrobce a bývá odlišná, proto se vždy řiďte symboly na boku a pokyny k danému modelu.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Záměna průměru ráfku, například 584 místo 622. Takový plášť na ráfek prostě nenasadíte.</li>'
          '<li>Koupě příliš široké gumy, která se neprotáhne rámem nebo se dotýká blatníku. Zkontrolujte i <a href="/cyklo-blatniky/">blatníky</a>, pokud je používáte.</li>'
          '<li>Nesprávný ventilek, který se nevejde do otvoru v ráfku nebo je příliš krátký.</li>'
          '<li>Opomenutí pásky v ráfku, kvůli níž duši brzy proděraví hlava paprsku.</li>'
          '<li>Přehuštění nebo podhuštění. Tlak vždy držte v rozmezí na boku pláště.</li>'
          '<li>Výměna jen jednoho pláště na kole, které už je opotřebované. Přední i zadní by měly mít podobnou kvalitu.</li></ul>'
          '<h2>Kdy plášť vyměnit</h2>'
          '<p>Plášť přestává plnit funkci, když je střed běhounu ohlazený, objevují se trhliny v bočnici, látka prosvítá skrz gumu nebo se vyboulí. Zadní plášť se obvykle opotřebuje dřív než přední. Staré pláště tvrdnou i bez ježdění, protože guma stárne vlivem světla a kyslíku, proto je dobré kontrolovat i stejně staré kusy z příručního skladu. '
          'Při výměně pláště zvažte i stav <a href="/cyklo-brzdy/">brzd</a>, <a href="/cyklo-pohon/">pohonu</a> a ráfku, protože se opotřebení často sčítá.</p>'
          '<h2>Pro koho které pláště</h2>'
          '<p>Rekreační jezdec na asfaltu vystačí s odolným trekingovým plástěm střední šířky, který neřeší jemné rozdíly. Závodník na silnici ocení lehký plášť s měkkou směsí a pevnou patkou a dojíždějící cyklista chce spíš ochranu proti defektům než hmotnost. '
          'Rodiče malých dětí vybírají přesný rozměr a pevnou drátovou patku, jelikož dětská kola jsou citlivá na velikost, a v kategorii <a href="/detska-kola/">dětská kola</a> si ověří rozměr ráfku. Pokud potřebujete i osvětlení pro zimní dojíždění, hledejte v sekci <a href="/cyklo-svetla/">světla</a>, a pokud vozíte batoh, užitečné jsou <a href="/cyklo-tasky-a-nosice/">brašny a nosiče</a>.</p>'
          '<h2>Jak na Sportece porovnat nabídky</h2>'
          '<p>Rozměry vyhledávejte podle čísla ETRTO a šířky. U stejného typu se nejlevnější kus obchodu může lišit jen balením nebo barvou bočnice, kdežto rozdíly ve směsi a ve výztuži jsou často vidět až po prostudování popisu. Sledujte i dostupnost: nejčastější velikosti, například 622 s šířkou 37 až 50 mm, jsou skladem častěji než specifické rozměry. '
          'Uložte si oblíbené kusy a vracejte se k nim po sezóně, kdy obchody dopřejí slevy a doplňují sklady.</p>'
          '<p>Samozřejmě stojí za to chránit i nové vybavení. Pláště skladujte vleže v suchu, mimo zdroje ozonu jako elektromotory, a mimo přímé slunce. Duše uchovávejte lehce poprášené, aby se k sobě nelepily, a do montáže je nehustěte.</p>',
    faq=[('Jak poznám, jaký rozměr pláště potřebuji?', 'Podívejte se na bok stávajícího pláště, kde je vyražený rozměr, například 40-622 nebo 29 x 2,25. Rozhodující je druhé číslo normy ETRTO, tedy průměr ráfku, který musí souhlasit přesně. Šířku můžete měnit v rozsahu, který povoluje ráfek a rám.'),
         ('Mohu na stejný ráfek dát širší plášť?', 'Ano, ale v rozmezí, které doporučuje výrobce ráfku, a jen pokud se plášť vejde do rámu, vidlice a případně blatníků. Širší guma bývá komfortnější a přilnavější, ale těžší a o něco pomalejší na asfaltu.'),
         ('Čím se liší galusák od autoventilku?', 'Galusák je tenčí, má maticí zajištěnou špičku a hodí se i na tlak vyšší u silničních kol. Autoventilek je širší, shodný s ventilem u auta a snadno se huštuje na čerpací stanici. Musí odpovídat otvoru v ráfku, širší ventilek se do úzkého otvoru nevejde.'),
         ('Jak dlouho vydrží plášť na kole?', 'Záleží na terénu, hmotnosti jezdce, tlaku a kvalitě gumy. Měřítkem není počet kilometrů, ale stav: ohlazený střed, praskliny v bočnici, prosvítající vlákna nebo vyboulení znamenají, že je čas na výměnu. Zadní plášť se opotřebovává rychleji než přední.'),
         ('Stojí za to přejít na bezdušové pláště?', 'Pokud máte kompatibilní ráfky a ochotu občas doplnit těsnicí tekutinu, ano, snižují hmotnost a umožňují nižší tlak. Pro nenáročného jezdce, který nechce nic řešit, je klasická duše jednodušší a spolehlivá. Při prvních výjezdech si vezměte náhradní duši.'),
         ('Kolik vzduchu mám do pláště dát?', 'Držte se rozmezí vytištěného na boku pláště. Nižší tlak dává lepší záběr a komfort, vyšší menší valivý odpor na hladkém povrchu. Těžší jezdec a užší plášť potřebují tlak vyšší, lehčí jezdec a široký plášť nižší. Kontrolujte ho pravidelně, protože se postupně snižuje.'),
         ('Proč mi duše stále praská ve stejném místě?', 'Často je příčinou chybějící nebo posunutá páska v ráfku, ostrý předmět zapíchnutý v plášti nebo špatně usazená patka. Prohlédněte vnitřek pláště prsty a zkontrolujte pásku. Pomůže také správný tlak a ověření, zda ventilek není skřípnutý v otvoru ráfku.'),
         ('Jak správně vyměním plášť bez poškození duše?', 'Duši nechte mírně nafouknutou, aby netvořila záhyby, a před nasazením pláště ji zasuňte celou dovnitř ráfku. Montpák zasouvejte opatrně pod patku a netlačte jím na duši. Pak zkontrolujte, že se nikde nepřiskřípla pod patkou, a nahustěte postupně.'),
         ('Mohu opravovat duši záplatou, nebo ji radši vyměnit?', 'Malý průpich se spolehlivě záplatuje, pokud povrch očistíte a obrousíte a lepidlo necháte zaschnout. Při větším řezu, poškození u ventilku nebo mnoha děrách je jistější duši vyměnit. Na cestu vozte aspoň jednu náhradní duši a sadu záplat.'),
         ('Jak skladovat náhradní duše a pláště?', 'V suchu, chladu a mimo přímé slunce. Pláště nechte vleže bez zlomení, duše uložte lehce poprášené mastkem v obalu. Vyhněte se blízkosti elektromotorů a zdrojů ozonu, které urychlují stárnutí pryže.')])

# ------------------------------------------------------------------ stolni-tenis
NEW['stolni-tenis'] = dict(long=True,
    title='Stolní tenis: stoly, pálky, míčky a síťky',
    desc='Stolní tenis a pingpong: stoly na doma i ven, pálky, potahy, míčky, síťky, boty a pouzdra. Jak vybrat pro děti, rekreaci i klub a porovnat obchody.',
    intro='<p>Stolní tenis je rychlý míčový sport, který se vejde do garáže, na chodbu školy i na zahradu. Kategorie <strong>stolní tenis</strong> sdružuje stoly pro halu i venkovní provoz, hotové pálky i dřevo s potahy zvlášť, míčky, síťky, '
          'pouzdra, boty a drobné doplňky. Pro začátečníka je to přehled, kde se rychle ztratí, protože pálka za pár stovek vypadá téměř stejně jako sportovní model, a přitom se chová úplně jinak.</p>'
          '<p>Sporteka srovnává nabídky českých obchodů u stejných kusů, takže vidíte, kdo má stůl nebo míčky skladem. Stolní tenis patří mezi <a href="/micove-sporty/">míčové a raketové sporty</a>, vedle <a href="/tenis/">tenisu</a>, '
          '<a href="/badminton/">badmintonu</a> a <a href="/squash/">squashe</a>. Dále se dozvíte, jak vybrat stůl podle místa, pálku podle herního stylu a jak se starat o potahy, aby vydržely.</p>',
    guide='<h2>Co v kategorii najdete</h2>'
          '<p>Vybavení pro stolní tenis se dá rozdělit do několika skupin. Každá má jiná kritéria a nákupní chyby se liší.</p>'
          + T(['Skupina', 'K čemu slouží', 'Na co se zaměřit'], [
              ['Stoly vnitřní', 'hra v místnosti, hale nebo garáži', 'tloušťka desky, stabilita nohou, způsob skládání'],
              ['Stoly venkovní', 'zahrada, školní dvůr, terasa', 'odolnost desky proti vlhkosti, ochrana konstrukce proti korozi'],
              ['Pálky hotové', 'rekreace, děti, začátečníci', 'rukojeť, tloušťka houby, označení určení'],
              ['Dřevo a potahy zvlášť', 'pokročilí a soutěžní hráči', 'rychlost dřeva, tvrdost potahu, povrch'],
              ['Míčky', 'trénink i zápasy', 'materiál, jakost, balení'],
              ['Síťky a držáky', 'rozdělení stolu', 'upevnění na hranu, napínání, výška'],
              ['Pouzdra a tašky', 'přenos a ochrana pálek', 'tvrdost obalu, počet pálek, prostor na míčky'],
              ['Boty a oblečení', 'pohodlí při trénincích', 'lehká podrážka, dobrý úchop, prodyšnost']]) +
          '<h2>Stůl: místo, rozměr a konstrukce</h2>'
          '<p>Oficiální stůl má rozměry 274 × 152,5 cm a výška desky je 76 cm. Takový stůl potřebuje kolem sebe dost místa, aby šlo hrát i z hloubky, zhruba čtyři až pět metrů na délku a dva až tři na šířku. Pokud tolik prostoru nemáte, existují kratší stoly a hobby varianty, které jsou menší nebo se dají přeložit do poloviny a hrát na polovině jako proti zdi. '
          'Rozměr ovlivní i to, jestli stůl vůbec projde dveřmi nebo schodištěm, proto si před koupí změřte cestu od auta po místo hry.</p>'
          '<p>Konstrukce dělí stoly na skládací pojízdné a pevné. Skládací stůl se dá zavřít, dvě poloviny se postaví na kolečka a odvezou. U hodnotnějších modelů se zamykají nohy a kolečka brzdí, aby stůl při hře nejezdil. U levných kusů zkontrolujte, zda se po rozložení obě poloviny drží v jedné rovině, jinak míček nelétá předvídatelně.</p>'
          '<h3>Tloušťka a povrch desky</h3>'
          '<p>Deska se vyrábí z dřevotřísky nebo MDF a její tloušťka obvykle bývá 12, 16, 19, 22 nebo 25 mm. Tenčí deska vyhovuje občasné domácí hře, silnější drží rovinu a míček se odráží stabilněji. Povrch je tmavý, nejčastěji zelený nebo modrý, matný, aby neoslňoval. '
          'Na odrazu míčku se podílí i kvalita laku. Hrana desky má mít bílé čáry šířky 2 cm, na středu je dělicí čára pro čtyřhru.</p>'
          '<h3>Venkovní stoly</h3>'
          '<p>Venkovní stůl vydrží déšť a slunce lépe než vnitřní, protože deska bývá ze speciálního kompozitního materiálu, hliníku nebo silné vrstvy s vodou odolným povrchem a rám je ošetřen proti rezivění. I tak je dobré stůl přikrýt obalem, když se nepoužívá. '
          'Vítr je u venkovní hry hlavním nepřítelem, proto stůl postavte do závětří, třeba ke zdi nebo živému plotu. Pro zahrady a hřiště se osvědčují stoly značek ' + B(('cornilleau', 'Cornilleau'), ('donic', 'Donic'), ('sponeta', 'Sponeta')) + '.</p>'
          '<h2>Pálka: jak se skládá</h2>'
          '<p>Pálka se skládá ze dřeva, které je základem, a dvou potahů. Dřevo, nazývané též blade, udává rychlost a pocit. Rychlé dřevo víc odpružuje a míček vyletí rychleji, pomalé dřevo odpouští chyby a dává větší kontrolu. Dřevo bývá několikavrstvé, dvě až sedm vrstev, a může obsahovat karbonové či podobné vložky. '
          'Potahy se skládají z gumy a pod ní z houby. Tloušťka houby ovlivňuje rychlost a rotaci míčku. Povrch gumy bývá čepičkami ven nebo dovnitř a výsledek je jiný záběr.</p>'
          + T(['Typ potahu', 'Vlastnosti', 'Pro koho'], [
              ['Hladký s čepičkami uvnitř', 'dobrá rotace a rychlost', 'většina hráčů, útok i obrana'],
              ['Čepičky ven, krátké', 'rychlý, špatně čitelný pro soupeře', 'hráči, kteří chtějí rychle útočit z blízka'],
              ['Čepičky ven, dlouhé', 'mění rotaci míčku', 'obrana a speciální styly'],
              ['Antispin', 'tlumí rotaci', 'nejde na útok, hodí se na zvláštní styly']]) +
          '<p>Pro rekreační hru stačí hotová pálka s již nalepenými potahy. Pro děti a začátečníky vybírejte lehčí, s kratší rukojetí a s méně agresivní houbou, aby se dítě učilo správný pohyb a nezvykalo si na špatné úderové návyky. Pokročilý hráč si dřevo a potahy kupuje zvlášť a lepí si je podle potřeby. '
          'Pálky s různým určením najdete u značek ' + B(('butterfly', 'Butterfly'), ('donic', 'Donic'), ('joola', 'Joola'), ('stiga', 'Stiga'), ('giant-dragon', 'Giant Dragon')) + '.</p>'
          '<h3>Držení pálky</h3>'
          '<p>Většina hráčů drží pálku způsobem zvaným shakehand, jako při podání ruky, kdy ukazováček leží na jedné straně a ostatní prsty obejímají rukojeť. Druhý styl, penhold, drží pálku jako pero. Tvar rukojeti se podle toho liší: rovná, anatomická, kónická nebo krátká. Rukojeť by měla pohodlně sedět v dlani, nezačne-li po půlhodině hry tlačit, je vybraná dobře. '
          'Bez ohledu na držení si před koupí vyberte pálku, kterou si vezmete do ruky a zamáváte s ní.</p>'
          '<h2>Míčky: materiál a jakost</h2>'
          '<p>Standardní míček má průměr 40 mm a hmotnost 2,7 g. Dnes se vyrábějí z plastu a mají na povrchu označení 40+. Hvězdičky ukazují jakost: tři hvězdičky se používají v soutěžích, jednohvězdičkové a bez označení jsou tréninkové a rekreační. '
          'Rozdíl je v kulatosti a rovnoměrné tloušťce stěny. Pro domácí hru stačí obyčejné míčky, pro klubové tréninky se hodí kvalitnější. Míček, který se nepravidelně odráží nebo je zdeformovaný, vyřaďte. Bílé a oranžové míčky se liší jen barvou, výběr závisí na kontrastu s okolím a s deskou stolu.</p>'
          '<p>V balení po šesti nebo dvanácti kusech najdete zpravidla míčky jedné značky. Velký balík na trénink je praktický, protože míčky se ztrácejí pod stoly. Nepouštějte míčky na nerovný a tvrdý povrch a nešlapejte na ně. Do aut je nenechávejte na slunci, deformují se teplem.</p>'
          '<h2>Síťka a příslušenství</h2>'
          '<p>Síť má výšku 15,25 cm od desky a přečnívá přes okraj stolu. Hobby síťky se upevňují svorkou na hranu, ta lépe drží u silnější desky. Pevnější sady mají šroubový držák a síť se dá napnout stavěcí maticí. Povolená síť se prověšuje uprostřed a míček pak létá jinak, takže ji před hrou zkontrolujte. '
          'Sady ' + B(('stiga', 'Stiga'), ('donic-schildkrot', 'Donic Schildkröt'), ('joola', 'Joola')) + ' i dalších značek nabízejí síťky s různým způsobem upevnění.</p>'
          '<p>K sadě patří kryt na stůl, který chrání desku před prachem a deštěm, a stojan na pálky. Užitečný je i robot, který vystřeluje míčky v pravidelných intervalech a umožní sólový trénink. Ten je vhodný na zlepšování techniky, ale nenahrazuje hru proti člověku. Mezi další pomůcky patří ručník na osušení rukou, protože pot na dlani snižuje stabilitu držení.</p>'
          '<h2>Boty a oblečení</h2>'
          '<p>Stolní tenis vyžaduje rychlé krátké kroky a změny směru, proto se používají boty s tenkou lehkou podrážkou z gumy, která dobře drží na hale. Běžecká obuv s tlustou podrážkou bývá pro tento sport příliš vysoká a nestabilní. '
          'Boty s protiskluzovou gumou jsou lepší než ploché tenisky. K oblečení patří prodyšné <a href="/sportovni-tricka/">sportovní tričko</a> a <a href="/sportovni-kratasy/">kraťasy</a>. Oblečení nesmí mít stejnou barvu jako míček, aby ho soupeř viděl. Pro všechny sporty najdete základ v kategorii <a href="/sportovni-obleceni/">sportovní oblečení</a>.</p>'
          '<h2>Péče o pálku a potahy</h2>'
          '<p>Potahy je třeba udržovat čisté. Prach z desky se zachytává na gumě a snižuje záběr, takže po hře potah opatrně otřete vlhkým hadříkem nebo speciálním čističem. Na ochranu povrchu se prodává fólie, kterou se přelepí potah na dobu mezi hrami. Pálku uchovávejte v pouzdře, mimo slunce a vlhko. '
          'Nikdy nenechávejte pálku v zimě v autě, guma tuhne a houba může popraskat. Při nalepení nových potahů dodržujte pokyny výrobce lepidla a větrejte místnost. Opotřebovaný potah, na kterém míček klouže, vyměňte. Výměna je rychlá a levná.</p>'
          '<h2>Výběr podle věku a úrovně</h2>'
          '<ul><li><strong>Děti do osmi let:</strong> nižší stůl nebo bedna pod nohy, lehká pálka s kratší rukojetí a více míčků, aby hra neztrácela tempo.</li>'
          '<li><strong>Rodina a hobby:</strong> skládací stůl s kolečky, dvě až čtyři hotové pálky, pytlík míčků a síťka, kterou lze rychle sundat.</li>'
          '<li><strong>Škola a klub:</strong> pevná konstrukce, silná deska, kvalitní míčky a odolné potahy.</li>'
          '<li><strong>Soutěžní hráč:</strong> vlastní skladba dřeva a potahů, sada náhradních potahů a pouzdro.</li>'
          '<li><strong>Zahrada a chata:</strong> venkovní stůl s krytem, odolné síťky a míčky do větru.</li></ul>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Příliš malý prostor kolem stolu. Hra se pak omezuje jen na krátké výměny.</li>'
          '<li>Pálka kupovaná jen podle ceny nebo obrázku. Podívejte se na popis určení.</li>'
          '<li>Použití pálky pro děti u dospělého, nebo naopak.</li>'
          '<li>Opomenutí krytu u venkovního stolu a hra za mokra.</li>'
          '<li>Nesprávné skladování míčků v teple.</li></ul>'
          '<h2>Na co navazuje</h2>'
          '<p>Kdo chce vyzkoušet jiný sport s raketou, pokračuje na <a href="/badminton/">badmintonu</a> nebo <a href="/padel/">padelu</a>, kde je potřeba kondice i koordinace. Vícemístné hry s míčem najdete v kategorii <a href="/volejbal/">volejbal</a>. '
          'Přenášení vybavení vám usnadní <a href="/sportovni-tasky/">sportovní tašky</a> a pro odpočinkové hry na zahradě slouží kategorie <a href="/hry-na-zahradu/">hry na zahradu a pláž</a> a obecně <a href="/volny-cas/">hry a volný čas</a>.</p>'
          '<h2>Jak na Sportece porovnat nabídky</h2>'
          '<p>U stolů se vyplatí porovnat nejen konečnou cenu, ale také dopravu, protože jde o objemný kus. Sledujte rozměry balení a to, jestli se stůl dodává smontovaný. U pálek hledejte přesný název modelu a u potahů tloušťku houby, jinak porovnáváte různé výrobky. '
          'U míčků ověřte počet kusů v balení, protože se cena za kus může lišit. Uložte si sledované položky a vracejte se k nim před sezónou, kdy se zásoby doplňují.</p>',
    faq=[('Jaký stůl na stolní tenis vybrat do bytu nebo garáže?', 'Vnitřní skládací stůl s kolečky a deskou silnou aspoň 16 mm. Před koupí změřte prostor, protože okolo stolu potřebujete několik metrů volného místa. Pokud ho nemáte, hledejte kratší hobby model nebo možnost hry proti přeložené polovině.'),
         ('Jak velký je oficiální stůl a síť?', 'Oficiální stůl má rozměry 274 × 152,5 cm a výšku desky 76 cm. Síť je 15,25 cm vysoká a přesahuje okraje stolu. Hobby stoly mohou být menší, ale síť by měla mít stejnou výšku, aby hra odpovídala pravidlům.'),
         ('Čím se liší hotová pálka od vlastní skladby?', 'Hotová pálka má dřevo a potahy sestavené výrobcem, hodí se pro rekreaci a děti. Při vlastní skladbě si zvlášť vybíráte dřevo, potahy a tloušťku houby podle stylu hry. Je to dražší a vyžaduje znalosti, ale umožňuje přesné ladění.'),
         ('Jak poznám dobrou pálku pro začátečníka?', 'Je lehká, dobře sedí v ruce, má středně tvrdé potahy a menší rychlost, takže hráč drží míček pod kontrolou. Pálky s extrémní rychlostí nebo specifickými potahy jsou na začátek nevhodné, protože zvyšují množství chyb.'),
         ('Co znamenají hvězdičky na míčcích?', 'Hvězdičky označují jakost. Tři hvězdičky mají nejpřesnější kulatost a rovnoměrnou stěnu a používají se v soutěžích, míčky bez hvězdiček či s jednou hvězdičkou jsou určeny pro trénink a rekreační hru. Standardní průměr je 40 mm.'),
         ('Jak často mám měnit potahy na pálce?', 'Když začnou klouzat, ztrácejí záběr nebo mají viditelné poškození. U hobby hráčů to bývá po delší době, u soutěžních po několika měsících tréninku. Pomáhá čištění a ochranná fólie, která prodlouží životnost.'),
         ('Může venkovní stůl zůstat venku celoročně?', 'Venkovní modely snesou déšť lépe než vnitřní, ale i ony vydrží déle s krytem. Mráz, vlhkost a slunce urychlují stárnutí povrchu a rámu. Pokud stůl nepoužíváte přes zimu, uložte ho do suchého prostoru.'),
         ('Jaké boty se hodí na stolní tenis?', 'Lehké boty s tenkou protiskluzovou podrážkou, které dobře drží na hale a umožňují rychlé krátké kroky. Běžecká obuv s vysokou měkkou podrážkou je nestabilní. Pro občasnou hru stačí i sálová obuv.'),
         ('Jak vyčistit pálku bez poškození?', 'Potah otřete jemně navlhčeným hadříkem nebo speciálním čističem a nechte zaschnout. Nepoužívejte agresivní chemii ani abrazivní houbičky. Po čištění přelepte potah ochrannou fólií a uložte pálku do pouzdra.'),
         ('Kolik míčků na trénink potřebuji?', 'Na rodinnou hru stačí šest až dvanáct kusů. Na intenzivní trénink nebo robot se hodí větší balení, třeba několik desítek. Míčky se ztrácí pod nábytkem a lámou, proto je lepší mít zásobu.')])

# ------------------------------------------------------------------ kombinezy
NEW['kombinezy'] = dict(long=True,
    title='Kombinézy a overaly: dětské, zimní, neopren',
    desc='Kombinézy a overaly: dětské zimní a do deště, rybářské termo obleky, neoprenové a triatlonové i volnočasové overaly. Velikosti, materiály a péče.',
    intro='<p>Jednodílný oblek má jednu velkou výhodu: nikde nefouká, nikam nenatéká a nic se nesesune. Kategorie <strong>kombinézy a overaly</strong> proto spojuje zboží velmi rozdílné povahy. Najdete tu zimní kombinézy pro děti, nepromokavé overaly do deště, '
          'zateplené rybářské obleky, neoprenové a triatlonové kombinézy pro vodu i volnočasové dámské overaly. Pro každého je důležité něco jiného: dítě potřebuje teplo a volnost pohybu, rybář izolaci, plavec hydrodynamiku.</p>'
          '<p>Sporteka porovnává nabídky českých obchodů u stejných kusů a pomáhá najít velikost i barvu skladem. Kategorie je součástí oddílu <a href="/sportovni-obleceni/">sportovní oblečení</a>. '
          'Pro lyžování existuje samostatná sekce <a href="/lyzarske-kombinezy/">lyžařské kombinézy</a>, k vodě patří <a href="/neopreny/">neopreny</a> a pro závodní plavce <a href="/triatlon/">triatlon</a>. Níže poradíme, jak obleky rozlišit a vybrat.</p>',
    guide='<h2>Druhy kombinéz a overalů</h2>'
          '<p>Slovo kombinéza se používá pro velmi odlišné produkty. Aby se dalo vybírat, je dobré znát hlavní skupiny a vědět, co od nich očekávat.</p>'
          + T(['Skupina', 'K čemu se hodí', 'Typické znaky'], [
              ['Dětská zimní kombinéza', 'hra ve sněhu, saně, lyžování, pobyt venku v zimě', 'zateplení, odolný povrch, zesílená kolena, odepínací kapuce'],
              ['Nepromokavý dětský overal', 'déšť, bláto, hřiště, školka v přírodě', 'zalepené švy, prodyšná membrána, gumové manžety'],
              ['Zateplený rybářský oblek', 'dlouhý pobyt u vody v chladu', 'plovoucí nebo izolační vrstva, kapsy, reflexní prvky'],
              ['Neoprenová kombinéza', 'plavání, surf, paddleboard, kitesurfing', 'tloušťka neoprenu, zip vzadu nebo vpředu, těsné manžety'],
              ['Triatlonový overal', 'závodní plavání, kolo, běh', 'tenká tkanina, vložka, rychleschnoucí materiál'],
              ['Pracovní a pilotní overal', 'dílna, outdoor, historický styl', 'pevný materiál, kapsy, bavlna nebo směs'],
              ['Módní overal', 'volný čas, léto, město', 'viskóza, bavlna, sametový povrch, různé délky nohavic']]) +
          '<p>Při nákupu si nejprve položte otázku, kde se oblek použije. Zimní kombinéza se do vody nehodí a neopren nezahřeje na horské túře. Ať tedy vybíráte cokoli, začněte účelem.</p>'
          '<h2>Dětské zimní kombinézy</h2>'
          '<p>Zimní kombinéza je nejčastějším důvodem, proč lidé tuto kategorii navštěvují. Pro menší děti je výhodná, protože se do ní oblékne celé tělo najednou, zip vede od kotníku po krk a nikde nefouká. Když dítě padne do sněhu, nesvlékne se mu bunda a nezůstane odkrytá záda. '
          'Starší děti, které se samy převlékají a chodí na toaletu, ocení spíš oddělenou bundu a <a href="/lyzarske-kalhoty/">lyžařské kalhoty</a>, protože jim to zjednoduší život.</p>'
          '<p>Důležité parametry zimní kombinézy jsou následující.</p>'
          '<ul><li><strong>Zateplení:</strong> syntetická vata drží teplo i po provlhnutí a snadno se pere. Silnější vrstva je do mrazu, tenčí na jaro a podzim.</li>'
          '<li><strong>Povrch:</strong> nepromokavý a větruodolný materiál, zesílená kolena a zadek proti opotřebení při sáňkování.</li>'
          '<li><strong>Zip:</strong> dlouhý, s krytem proti pronikání vody a s překrytou bradou, aby nedřel.</li>'
          '<li><strong>Kapuce:</strong> odepínací, aby se nezachytila a aby šla sundat v autě.</li>'
          '<li><strong>Manžety:</strong> pružné nebo stavitelné, někdy s palčáky přes ruku a návleky na botách.</li>'
          '<li><strong>Reflexní prvky:</strong> pro viditelnost za šera.</li></ul>'
          '<p>Značky, které jsou v kategorii nejlépe zastoupené, jsou například ' + B(('reima', 'Reima'), ('didriksons', 'Didriksons'), ('dare2b', 'Dare2b'), ('trespass', 'Trespass'), ('columbia', 'Columbia')) + '. Nabídku najdete zvlášť pro miminka, předškoláky a větší děti.</p>'
          '<h3>Velikost a růst</h3>'
          '<p>Dětské velikosti se obvykle označují výškou těla, například 98 nebo 110 cm, a ne věkem. Změřte dítě bez bot, pak vezměte velikost, která odpovídá nebo je o jednu větší. Příliš velká kombinéza brání pohybu a nepřiléhá k tělu, takže se zbytečně ochlazuje, příliš malá omezuje pohyb a tlačí v rozkroku. '
          'Vyzkoušejte, že dítě v kombinéze dokáže dřepnout, zvednout ruce nad hlavu a ohnout se. Některé modely mají prodloužitelné nohavice a rukávy, které s dítětem vydrží déle než jednu sezónu.</p>'
          '<h2>Nepromokavé overaly do deště</h2>'
          '<p>Dětský overal do deště je z lehkého polyuretanu, PVC nebo membrány a nemá zateplení. Švy jsou zalepené a overal se obléká přes oblečení podle počasí. Je ideální pro hřiště, výlety do přírody a lesní školky, jelikož děti v něm mohou skákat do louží a ušpinit se, aniž by to vadilo. '
          'Vodotěsnost se udává v mm vodního sloupce, ale to je údaj výrobce a skutečnou odolnost ovlivňují švy a zipy. Overal z PU nebo PVC nedýchá, na rozdíl od modelů s membránou, proto při pohybu uvnitř vzniká pot. Hodí se tedy spíš na kratší pobyty, dlouhé aktivní dny se lépe zvládnou v prodyšnějších vrstvách.</p>'
          '<h2>Rybářské a zimní obleky pro dospělé</h2>'
          '<p>Rybáři trávívají hodiny na místě v chladu a vlhku, takže tepelná izolace je pro ně podstatná. Zateplený oblek v jednom kuse brání proniknutí chladu v pase, kde se u dvoudílných souprav často objevuje škvíra. ' + B(('westin', 'Westin')) + ' patří k výrobcům, kteří nabízejí zimní termo obleky pro rybářský pobyt. '
          'Některé obleky mají plovoucí vlastnosti, což se hodí na loďce, ale nenahrazují záchrannou vestu. Při koupi sledujte velikost podle výšky a obvodu hrudníku, počítejte s teplým spodním oblečením a ujistěte se, že kapsy jsou dostatečně velké i na rukavice.</p>'
          '<p>Další rybářské a venkovní oblečení najdete v sekci <a href="/rybarske-obleceni/">rybářské oblečení</a>. Pro vrstvení pod oblek je vhodné <a href="/termopradlo/">funkční a termo prádlo</a>, které odvádí pot od těla.</p>'
          '<h2>Neoprenové a triatlonové kombinézy</h2>'
          '<p>Neoprenový oblek chrání před chladem tím, že mezi tělo a vodu vloží tenkou vrstvu vody, kterou tělo ohřeje. Proto musí obleku těsně sedět, ale nesmí omezovat dýchání. Kombinézy se dělí na krátké, které končí u kolen a ramen, a dlouhé. Tloušťka se udává v milimetrech a obvykle se pohybuje od jednoho do pěti. '
          'Tlustší neopren je teplejší, ale méně pružný. Triatlonové obleky se vyrábějí tenčí, s větší pružností v ramenou a hladkým povrchem, který zkracuje čas při převlékání. Zone3 patří mezi značky, které se těmto oblekům věnují, a v kategorii najdete i neoprenové modely.</p>'
          '<p>Víc pro plavce najdete v kategoriích <a href="/neopreny/">neopreny</a>, <a href="/plavky/">plavky</a> a <a href="/vodni-sporty/">vodní sporty</a>. Po každém použití neopren opláchněte sladkou vodou, nechte uschnout ve stínu zavěšený za ramena a nepoužívejte sušičku.</p>'
          '<h2>Volnočasové a módní overaly</h2>'
          '<p>Dámské overaly z viskózy, bavlny nebo sametu jsou oblečení pro léto, dovolenou i večer. Od sportovního oblečení se liší tím, že se u nich neřeší odvod potu ani pružnost, ale střih a pohodlí. Při výběru sledujte délku trupu, protože u jednodílného kusu se nedá vyměnit horní a spodní část. '
          'Pokud máte dlouhý trup, hledejte větší velikost nebo pružný materiál, pokud kratší, vybírejte modely s páskem v pase. Hodí se i pro cestování, protože nezmačkané viskózové kusy zabírají málo místa. Doplnit je můžete <a href="/sportovni-bundy/">sportovní bundou</a> nebo <a href="/leginy/">legíny</a> pod kratšími modely.</p>'
          '<h2>Materiály a jejich vlastnosti</h2>'
          + T(['Materiál', 'Výhody', 'Nevýhody'], [
              ['Polyesterová tkanina s membránou', 'voděodolná, prodyšná', 'vyžaduje péči, aby si membrána udržela funkci'],
              ['Nylon s impregnací', 'lehký, odolný proti odření', 'impregnace časem slábne'],
              ['Syntetická vata', 'teplo i při provlhnutí', 'objemná'],
              ['Fleece', 'hřeje a dýchá', 'nezastaví vítr'],
              ['Neopren', 'izolace ve vodě', 'těžko se obléká a suší'],
              ['Bavlna a viskóza', 'příjemná na dotek, prodyšná', 'pomalu schnou, nehřejí při navlhnutí']]) +
          '<p>Vrstvy se v zimě kombinují: spodní funkční, střední fleece a svrchní nepromokavá. Kombinéza často nahrazuje střední i svrchní vrstvu, a proto spodní vrstva rozhoduje o tom, zda dítě nezmrzne. Bavlněné tričko pod kombinézou není vhodné, vlhne a ochlazuje, vyberte syntetické nebo vlněné.</p>'
          '<h2>Péče o kombinézy</h2>'
          '<p>Postupujte podle štítku, ale některá obecná pravidla platí vždy. Před praním zapněte všechny zipy a suché zipy, odstraňte nečistoty z kapes. Nepoužívejte aviváž, protože zalepuje póry membrány a snižuje její funkčnost. Teplota praní je u zateplených a membránových kusů obvykle nižší, zhruba do 30 stupňů, a používá se jemný prací prostředek bez změkčovadel. '
          'Po vyprání je vhodné obnovit impregnaci, pokud voda přestala perlit na povrchu. Sušte v rozvěšeném stavu při pokojové teplotě, vatu občas protřepejte, aby se nesrážela. Neoprenové obleky nikdy nežehlete a nesušte na radiátoru.</p>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Koupě „na vyrůstání“ o dvě velikosti víc, kdy dítě tone v nohavicích a studí ho.</li>'
          '<li>Opomenutí spodní vrstvy. Nejlepší kombinéza nehřeje, pokud pod ní dítě nemá funkční prádlo.</li>'
          '<li>Použití do vody modelu, který není určen k namáčení.</li>'
          '<li>Ignorování velikostní tabulky značky. Reima, Didriksons i Columbia mají mírně odlišný střih.</li>'
          '<li>Nákup až v sezóně, kdy se vyprodají nejčastější velikosti.</li>'
          '<li>Nevyzkoušení zipu a kapuce před koupí. U malých dětí musí jít zip ovládat jednou rukou.</li></ul>'
          '<h2>Pro koho jednotlivé typy</h2>'
          '<p>Rodiny s malými dětmi vyhledávají zimní kombinézy a dešťové overaly, protože zjednodušují každé oblékání. Rybáři a lidé pracující venku hledají zateplené obleky. Vodní sportovci řeší neopren podle teploty vody a typu aktivity. Milovníci módy vybírají overaly podle střihu a materiálu. '
          'Pokud se chystáte na hory, projděte si i <a href="/lyzarske-obleceni/">lyžařské oblečení</a>, <a href="/detske-lyze/">dětské lyže</a> a <a href="/snowboarding/">snowboarding</a>. Pro chladné procházky přijdou vhod <a href="/zimni-bundy/">zimní bundy</a> a <a href="/soupravy/">soupravy a komplety</a>.</p>'
          '<h2>Kdy nakupovat</h2>'
          '<p>Zimní dětské kombinézy se vyprodávají na začátku sezóny, kdy jsou nejoblíbenější velikosti rychle pryč. Slevy přicházejí v únoru a březnu, ale na sklad se dostane jen to, co zbylo. Jarní a dešťové overaly jsou na trhu od března a letní módní kusy od dubna. '
          'Neopreny se kupují na jaře před sezónou. Na Sportece sledujte nabídky několika obchodů najednou a kontrolujte, zda je skladem přesně ta velikost, kterou potřebujete.</p>',
    faq=[('Je lepší kombinéza, nebo bunda a kalhoty pro dítě?', 'Kombinéza je jednodušší a nikde nefouká, hodí se pro malé děti. Starší děti, které si samy chodí na toaletu, ocení oddělené kusy, protože jsou praktičtější. Rozhodněte podle věku a toho, jak se dítě obléká.'),
         ('Jakou velikost dětské kombinézy koupit?', 'Změřte výšku dítěte bez bot a porovnejte s tabulkou výrobce. Ideální je velikost, která odpovídá, nebo je o jednu větší. Kombinéza o hodně větší nehřeje a překáží, malá tlačí a omezuje pohyb.'),
         ('Jak poznám, že je kombinéza dostatečně teplá?', 'Podívejte se na typ a množství zateplení a na to, do jaké teploty ji výrobce doporučuje. Syntetická vata zahřeje i vlhká. Skutečný pocit ale závisí na spodním prádle a pohybu dítěte, proto pod ni dejte funkční vrstvu.'),
         ('Jak prát zateplenou kombinézu?', 'Podle štítku, obvykle na jemném programu při nízké teplotě s tekutým pracím prostředkem bez aviváže. Zapněte zipy, vypněte nadměrné ždímání a sušte rozvěšenou. Vatu občas protřepejte, aby se nesrážela do hrudek.'),
         ('Hodí se nepromokavý overal na celodenní pobyt venku?', 'Na krátké pobyty ano. Při dlouhém pohybu se v něm vytváří pot, pokud nemá prodyšnou membránu. Pro celé dny je lepší kombinovat prodyšnou svrchní vrstvu s teplým spodním prádlem.'),
         ('Jak vybrat neoprenovou kombinézu?', 'Podle teploty vody, sportu a tloušťky neoprenu. Oblek musí těsně přiléhat, ale nesmí omezovat dýchání ani pohyb ramen. Pro plavání se hodí tenčí a pružnější, pro surf nebo studenou vodu tlustší. Vyzkoušejte ho oblečený jen ve spodním prádle nebo plavkách.'),
         ('Čím se liší triatlonový overal od neoprenu?', 'Triatlonový overal je tenká pružná kombinéza s vložkou, kterou lze použít při plavání, jízdě na kole i běhu. Neopren je silnější a určený k plavání ve studené vodě. Pro závod se často kombinují, tri overal se nosí pod neoprenem.'),
         ('Mohu zimní overal použít i na lyže?', 'Ano, pokud je nepromokavý, zateplený a má zesílená místa na kolenou. Specializované lyžařské kombinézy mají ještě sněhové manžety a kapsy na skipass. Širší výběr najdete v kategorii lyžařské kombinézy.'),
         ('Jak se starat o neopren?', 'Po každém použití ho opláchněte sladkou vodou, sušte rozvěšený ve stínu a vyvarujte se přímého slunce a topení. Nesušte v sušičce a neskládejte do ostrých záhybů. Při dlouhém skladování ho zavěste na širokém ramínku.'),
         ('Kdy je nejlepší doba na koupi dětských zimních kombinéz?', 'Na začátku podzimu, kdy je výběr největší. Slevy přicházejí později v zimě, ale oblíbené velikosti bývají vyprodané. Pokud nespěcháte, sledujte nabídky několika obchodů a koupi načasujte podle dostupnosti.')])

# ------------------------------------------------------------------ kempingove-nadobi
NEW['kempingove-nadobi'] = dict(long=True,
    title='Kempingové nádobí a příbory: hrnce, hrnky, sady',
    desc='Kempingové nádobí a příbory: sady hrnců, hrnky, misky, spork, skládací silikon, hliník, nerez i titan. Jak vybrat na túru, kemp i auto a pečovat o ně.',
    intro='<p>Dobré jídlo na cestách začíná u správných nádob. Kategorie <strong>kempingové nádobí a příbory</strong> nabízí sady hrnců a pánviček, hrnky a termohrnky, misky a talíře, lžíce, vidličky a spork, skládací nádoby ze silikonu i další drobnosti, '
          'které z kempu dělají domov. Něco jiného potřebuje turista s batohem na týden, něco jiného rodina s autem plným věcí a rybář na břehu. Vybrat se proto dá hlavně podle hmotnosti, materiálu a velikosti sady.</p>'
          '<p>Sporteka srovnává nabídky českých obchodů a u stejné sady ukáže, kde je skladem. Kategorie navazuje na <a href="/vareni-v-prirode/">vaření v přírodě</a> a doplňují ji <a href="/varice-a-kartuse/">vařiče a kartuše</a>. '
          'Celý oddíl najdete v kategorii <a href="/kemping/">kemping</a>. Níže vysvětlíme materiály, velikosti, kompatibilitu s vařičem i péči, aby vám nádobí vydrželo mnoho výprav.</p>',
    guide='<h2>Co všechno do nádobí patří</h2>'
          '<p>Kempingové nádobí není jen hrnec. Skládá se z několika skupin a každá slouží jinému účelu. Před nákupem si rozmyslete, co skutečně vaříte, a vybírejte podle toho.</p>'
          + T(['Skupina', 'K čemu slouží', 'Na co se zaměřit'], [
              ['Sady hrnců a pánviček', 'vaření pro jednoho až několik lidí', 'objem, vnořitelnost, rukojeti, víko'],
              ['Konvice a rychlovarné hrnce', 'ohřev vody na kávu, čaj a instantní jídla', 'tvar dna, přenos tepla, zobáček'],
              ['Hrnky a termohrnky', 'pití za tepla i za studena', 'izolace, víčko, objem'],
              ['Misky a talíře', 'servírování a jídlo', 'hloubka, hmotnost, stohovatelnost'],
              ['Příbory a spork', 'jedení', 'délka, materiál, skládání'],
              ['Skládací nádoby', 'úspora místa v batohu', 'odolnost vůči teplu, způsob uzavření'],
              ['Pomůcky', 'sítka, naběračky, škrabky, utěrky', 'hmotnost a odolnost'],
              ['Nádoby na vodu a jídlo', 'skladování a přenos', 'těsnost, snadné mytí']]) +
          '<h2>Materiály: hliník, nerez, titan, plast</h2>'
          '<p>Nejdůležitější rozhodnutí je materiál. Každý má své přednosti a slabiny a nejlepší volba závisí na tom, jak často a jak daleko se vydáváte.</p>'
          + T(['Materiál', 'Výhody', 'Nevýhody', 'Vhodné použití'], [
              ['Hliník', 'lehký, rychle ohřívá, dostupný', 'snadno se připaluje, může se promáčknout', 'turistika, rychlý ohřev vody'],
              ['Eloxovaný hliník', 'tvrdší povrch, lépe se čistí', 'nenechte škrábat', 'sady na túry a do kempu'],
              ['Nerez', 'odolný, nerezaví, vydrží roky', 'těžší, pomaleji vede teplo', 'autokemping, rodina, vaření na ohni'],
              ['Titan', 'velmi lehký a pevný', 'teplo se rozvádí nerovnoměrně, vaření vyžaduje pozornost', 'ultralehká turistika, ohřev vody'],
              ['Plast a kompozit', 'lehký, nepálí do rukou', 'nesmí na plamen, může zapáchat', 'misky, hrnky, příbory'],
              ['Silikon', 'skládací, malý objem', 'méně tuhý, nesnese přímý plamen', 'úspora místa, ohřev nad vařičem s ochranným dnem']]) +
          '<p>Hliník se hodí tam, kde záleží na hmotnosti a rychlém ohřevu, ale vyžaduje opatrnost při vaření hustých jídel. Nerez je spolehlivější do rodinného kempu a na ohniště, protože snese silnější zacházení. '
          'Titan je ideální na ohřev vody a instantní jídla. Pokud vaříte složitější jídla, vyberte nádobu s vícevrstvým dnem, která rozvádí teplo rovnoměrně. Mezi výrobce, kteří nabízejí různé materiály, patří ' + B(('sea-to-summit', 'Sea to Summit'), ('gsi-outdoors', 'GSI Outdoors'), ('primus', 'Primus'), ('fire-maple', 'Fire-maple'), ('kupilka', 'Kupilka')) + '.</p>'
          '<h2>Velikost sady podle počtu lidí</h2>'
          '<p>Základní pravidlo zní: na osobu počítejte půl litru až litr objemu hrnce na vaření, podle toho, zda vaříte hustá jídla, nebo jen ohříváte vodu. Samotář si vystačí s hrnkem a hrncem o objemu zhruba jeden litr, dvě osoby s dvou až třílitrovým hrncem a rodina potřebuje několik nádob najednou.</p>'
          + T(['Počet lidí', 'Doporučené složení'], [
              ['1 osoba', 'hrnec nebo hrnek s víkem, lžíce nebo spork, miska'],
              ['2 osoby', 'sada hrnec a pánev, dva hrnky, dvě misky, příbory'],
              ['3 až 4 osoby', 'větší hrnec, pánev, konvice, talíře, příbory pro každého'],
              ['Skupina nebo rodina v autě', 'několik hrnců, pánev, gril, prkénko, nůž, nádoba na mytí']]) +
          '<p>Na pěší túru se hodí vnořitelné sady, kde se menší nádoby ukládají do větších a vejde se do nich i kartuše s vařičem. Tím se šetří místo. V autokempu se místa nemusíte bát, preferujte větší rovnější nádoby se silným dnem a pevnými rukojeťmi.</p>'
          '<h2>Kompatibilita s vařičem</h2>'
          '<p>Nádobí musí odpovídat zdroji tepla. Plynový vařič na kartuši potřebuje stabilní hrnec o průměru, který se na jeho trysky vejde, a příliš široký hrnec se převrhne. Některé nádoby mají na dně žebra, takzvaný výměník tepla, který zvyšuje účinnost a šetří plyn, ale hodí se jen k určitým vařičům. '
          'Jak vybrat vařič, zjistíte v kategorii <a href="/varice-a-kartuse/">vařiče a kartuše</a>. Pokud vaříte na ohni, vybírejte nerez nebo pevné nádoby bez plastových částí. Plastové rukojeti a silikonové obaly nesmí zasáhnout plamen. Pro vaření na kamnech či grilu se hodí litinové nádoby, ty jsou těžké a ukládají se do auta.</p>'
          '<h2>Příbory a spork</h2>'
          '<p>Mezi příbory pro turisty se osvědčila kombinace lžíce a vidličky v jednom, zvaná spork. Je lehká a vejde se do každé kapsy. ' + B(('light-my-fire', 'Light my fire')) + ' je jeden z nejznámějších výrobců sporků, a v nabídce najdete i další varianty. '
          'Pro delší pobyty se hodí příbory z nerezu s pevnou rukojetí. Dlouhá lžíce umožní jíst přímo z pytlíku s instantním jídlem. Nůž nahradí outdoorový multifunkční nástroj z kategorie <a href="/outdoorove-noze-a-multitoola/">outdoorové nože a multitoola</a>, pokud jej legálně používáte. U plastových příborů sledujte materiál určený pro styk s potravinami.</p>'
          '<h2>Hrnky a termohrnky</h2>'
          '<p>Hrnek na túře slouží ke všemu: k pití čaje, polévky i jako miska. Kovový hrnek je odolný a dá se ohřát přímo na plameni, ale okraj se rychle rozpálí a pálí do rtů. Plastový je teplejší na dotek, ale nesnese plamen. Termohrnek udrží teplotu déle a hodí se do auta i na ranní pohyb. '
          'Dvouvrstvé nerezové hrnky se nepálí, ale váží víc. Termohrnek se sítkem na čaj, jako najdete v nabídce, se hodí pro milovníky čaje na cestách. Další nádoby na pití najdete v kategorii <a href="/lahve-a-termosky/">láhve a termosky</a>.</p>'
          '<h2>Skládací nádobí</h2>'
          '<p>Skládací misky, hrnce a hrnky z potravinářského silikonu s pevným okrajem se po vyprázdnění složí do plochého disku. Pro lehké batohy a kolo jsou úsporné. Je dobré vědět, že silikon nesmí na přímý plamen a při ohřevu vody se obvykle používá jen s tuhým kovovým dnem. '
          'Skládací nádoby jsou méně tuhé než pevné a při míchání se mohou prohýbat. Uložení se zjednoduší, ale mytí vyžaduje trochu péče, aby se v záhybech nezachytila špína.</p>'
          '<h2>Hygiena a mytí v přírodě</h2>'
          '<p>Nádobí v přírodě se myje jinak než doma. Vodu na mytí nelijte přímo do potoka. Odneste ji alespoň několik desítek metrů od zdroje, použijte jen malé množství biologicky odbouratelného prostředku a zbytky jídla seberte. Mastné nádoby nejdřív vytřete papírem nebo trávou. '
          'Houbička s drsnou stranou a malý kus utěrky se vejdou do každé sady. Po umytí nádobí důkladně osušte, vlhké nádobí v batohu zapáchá. Pokud kempujete delší dobu, vezměte skládací dřez nebo vědro.</p>'
          '<h2>Péče a čištění</h2>'
          '<ul><li><strong>Hliník:</strong> myjte jemnou houbou, nepoužívejte drátěnky a agresivní chemii, která může povrch poškodit. Připálené zbytky namočte do vody a odstraňte.</li>'
          '<li><strong>Nerez:</strong> snese běžné čisticí prostředky, ale stopy po pálení pomáhá odstranit jemná soda nebo ocet.</li>'
          '<li><strong>Nepřilnavý povrch:</strong> nepoužívejte kovové nástroje, vařte na nižší teplotě a umývejte jemně.</li>'
          '<li><strong>Plast:</strong> nenechávejte u ohně, pozor na barvení od jídla jako je kari nebo rajčata.</li>'
          '<li><strong>Dřevokompozit:</strong> nenechte dlouho ve vodě, osušte a občas namažte potravinářským olejem, pokud to doporučuje výrobce.</li></ul>'
          '<p>Hrnce při ukládání vložte do látkového sáčku, aby se navzájem neškrábaly a nešpinily batoh. Víčka a rukojeti pravidelně kontrolujte, zda se nepovolují.</p>'
          '<h2>Bezpečnost při vaření</h2>'
          '<p>Vařič a horká nádoba jsou nejčastější příčinou popálenin. Vařte na rovném stabilním podkladu a mimo stan nebo jeho přístřešek. Prázdný hrnec na plameni nenechávejte, přehřátí poškodí povrch i rukojeti. '
          'Pro přenos horkých nádob používejte rukavice nebo chňapku, protože kovové rukojeti hřejí. Děti vařit nenechávejte bez dozoru. Pokyny k obsluze plynového vařiče dodržujte vždy podle návodu výrobce a nikdy nepoužívejte nádobu, která je viditelně poškozená.</p>'
          '<h2>Výběr podle způsobu cestování</h2>'
          '<ul><li><strong>Pěší túra a trek:</strong> lehká vnořitelná sada z hliníku nebo titanu, hrnek, spork a malá miska. Doplňte <a href="/turisticke-batohy/">turistickým batohem</a> a <a href="/outdoorova-strava/">outdoorovou stravou</a>.</li>'
          '<li><strong>Kolo a motocykl:</strong> skládací silikon a kompaktní sady, aby se nic nehrnulo z brašen.</li>'
          '<li><strong>Autokemping:</strong> nerezové nebo smaltované nádobí, plnohodnotné příbory a nábytek z kategorie <a href="/kempingovy-nabytek/">kempingový nábytek</a>.</li>'
          '<li><strong>Rodinný výlet:</strong> pevné plastové misky a hrnky, které děti neroztlučou, ve velkém množství a v dobře stohovatelném provedení.</li>'
          '<li><strong>Rybolov a bivak:</strong> nerezová konvice nebo hrnec s uchem na zavěšení nad oheň, doplněné o <a href="/rybareni/">vybavení k rybaření</a>.</li></ul>'
          '<h2>Časté chyby při nákupu</h2>'
          '<ul><li>Příliš velká sada pro jednoho člověka, která zbytečně zatěžuje batoh.</li>'
          '<li>Nerespektování vařiče: hrnec s širokým dnem na úzkém vařiči je nestabilní.</li>'
          '<li>Plastový hrnek na plameni. Taková nádoba se zdeformuje a může uvolnit zápach.</li>'
          '<li>Opomenutí víka. Víko zkracuje dobu varu a šetří palivo.</li>'
          '<li>Koupě podle vzhledu bez ohledu na materiál. Hliník a nerez se v praxi chovají odlišně.</li>'
          '<li>Zapomenutí na čištění a sušení, nádobí pak zapáchá a koroduje.</li></ul>'
          '<h2>Na co navazuje</h2>'
          '<p>Ke kempingovému nádobí se hodí zázemí v podobě stanu a spacáku. Hledejte v kategoriích <a href="/stany/">stany</a> a <a href="/spaci-pytle/">spací pytle</a>, doplňky najdete u <a href="/kempingove-doplnky/">kempingových doplňků</a> a drobnosti u <a href="/outdoor-doplnky/">outdoorových doplňků</a>. '
          'Celý přehled outdoorového vybavení shrnuje kategorie <a href="/outdoor/">outdoor</a>.</p>'
          '<h2>Jak porovnat nabídky na Sportece</h2>'
          '<p>Při srovnávání hledejte přesný název sady a počet kusů v balení, protože levnější nabídka může obsahovat méně součástí. U objemu sledujte údaj v litrech, u hmotnosti gramy. Značky a materiály se opakují v několika obchodech, proto je dobré porovnat i poštovné a dostupnost. '
          'Před sezónou se doplňují sklady a bývají časté slevy na starší série, výběr je ale největší na jaře.</p>',
    faq=[('Z čeho je nejlepší kempingové nádobí?', 'Záleží na použití. Hliník je lehký a levný, nerez odolný a vhodný pro rodinný kemp, titan nejlehčí pro turisty. Plast se hodí na misky a hrnky, ne na plamen. Pro běžné turistické použití je rozumným kompromisem eloxovaný hliník.'),
         ('Jak velký hrnec potřebuji?', 'Počítejte přibližně půl litru až litr na osobu podle jídla. Pro jednoho stačí zhruba jednolitrový hrnec, pro dva dvou- až třílitrový. Pokud jen ohříváte vodu na instantní jídla, vystačíte s menším objemem.'),
         ('Mohu vařit v silikonovém skládacím hrnci?', 'Silikon nesmí na přímý plamen. Některé sady mají kovové dno pro ohřev vody, vždy se řiďte návodem výrobce, jinak hrozí poškození nádoby i popálení.'),
         ('Co je spork a proč se hodí na túru?', 'Spork je kombinace lžíce a vidličky v jednom kusu. Zabírá málo místa, váží málo a stačí na většinu jídel. Delší model se hodí pro jídlo z pytlíku s instantními pokrmy.'),
         ('Jak čistit připálené jídlo z hliníkového hrnce?', 'Namočte nádobu na pár minut do teplé vody a pak zbytky odstraňte měkkou houbou. Vyhněte se drátěnkám a agresivním přípravkům, které poškodí povrch. U eloxovaného hliníku šetřete zvlášť.'),
         ('Hodí se nádobí z kempu do myčky?', 'U nerezových kusů většinou ano, ale zkontrolujte pokyny výrobce. Hliník v myčce tmavne a eloxovaný povrch se poškozuje, plast se může deformovat a dřevokompozit v ní nepatří. Šetrnější je ruční mytí.'),
         ('Jak zabalit nádobí, aby nehrčelo v batohu?', 'Použijte vnořitelnou sadu a uvnitř uložte menší předměty, třeba kartuši, hrnek a sirky. Mezi nádoby vložte utěrku, která tlumí zvuk a chrání povrch. Sadu uložte do látkového sáčku.'),
         ('Je titanové nádobí dobré i na vaření?', 'Je velmi lehké a pevné, ale špatně rozvádí teplo, takže se jídlo snadno připálí. Nejvíc se hodí na ohřev vody a instantní jídla. Na složitější vaření je lepší hliník s vícevrstvým dnem nebo nerez.'),
         ('Jak se myje nádobí v přírodě?', 'Nejdřív setřete zbytky jídla papírem, vodu s malým množstvím biologicky odbouratelného prostředku odneste daleko od potoka a vylijte na zem. Nádobí osušte, aby nezapáchalo. Hygienu doplňte čistou vodou na opláchnutí.'),
         ('Jaké nádobí vybrat pro rodinu v autokempu?', 'Pevné nerezové nebo smaltované hrnce, plastové misky a hrnky, které děti nerozbijí, a příbory pro každého člena. Doplňte konvici, prkénko, nůž a nádobu na mytí. Na hmotnost se nemusíte dívat, důležitá je odolnost a počet kusů.')])
