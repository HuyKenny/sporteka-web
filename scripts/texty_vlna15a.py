"""sporteka.cz — wave 15a (4. 11. 2026): long texts (>= 1650 words) for ostatni-doplnky-stravy, muskareni, skateboardy, vysoke-trekove-boty.
General true facts only, no prices, no health claims. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ ostatni-doplnky-stravy
NEW['ostatni-doplnky-stravy'] = dict(long=True,
    title='Doplňky stravy: kapsle, prášky a extrakty | Sporteka',
    desc='Doplňky stravy mimo proteiny a kreatin: extrakty, rostlinné prášky, oleje i kapsle. Jak číst etiketu a kde najdete nabídky obchodů vedle sebe.',
    intro='<p>Do skupiny <strong>dalších doplňků stravy</strong> patří všechno, co se nevešlo mezi proteiny, kreatin nebo vitaminy: rostlinné extrakty, houbové směsi, oleje, prášky z bylin, probiotika, superpotraviny a další specialitky. Je to různorodá sbírka a právě proto se v ní snadno ztratí. Dva produkty s podobným názvem mohou mít zcela odlišné složení, formu i velikost balení.</p>'
          '<p>Na Sportece tu najdete nabídky českých obchodů vedle sebe, takže si porovnáte složení a velikost balení u stejného produktu. Příbuzné skupiny jsou <a href="/vitaminy-a-mineraly/">vitaminy a minerály</a>, <a href="/kolagen-a-klouby/">kolagen a kloubní výživa</a>, <a href="/aminokyseliny-bcaa/">aminokyseliny</a> a <a href="/proteiny/">proteiny</a>. Doplněk stravy nenahrazuje pestrou stravu a před užíváním je rozumné poradit se s lékařem nebo lékárníkem.</p>',
    guide='<h2>Co se pod tímhle označením skrývá</h2>'
          '<p>Doplněk stravy je v právním smyslu potravina, nikoli léčivo. Prodává se v lékovkách, sáčcích, kapslích, tabletách, v prášku i jako tekutina a jeho účelem je doplnit běžnou stravu. Tahle kategorie je záměrně široká. Slouží jako odkladiště pro přípravky, které nemají vlastní podskupinu, a proto v ní vedle sebe leží věci, které spolu nesouvisí.</p>'
          + T(['Typ přípravku', 'Co obvykle obsahuje', 'Na co dát pozor'], [
              ['Rostlinné extrakty', 'sušený výtažek z kořene, listu nebo plodu, často standardizovaný na jednu látku', 'poměr extraktu ke surovině, udávané množství účinné složky'],
              ['Houbové směsi', 'prášek nebo extrakt z plodnic či mycelia', 'zda jde o plodnici, nebo mycelium na zrnu, a původ suroviny'],
              ['Oleje a tuky', 'konopný, lněný, rybí či krillový olej v kapslích nebo lahvičce', 'datum spotřeby, uchování v chladu a tmě, barva a zápach'],
              ['Probiotika', 'kmeny bakterií s udaným počtem kolonií', 'způsob skladování, doba použitelnosti, označení kmenů'],
              ['Superpotraviny', 'sušené bobule, řasy, trávy, semínka v prášku', 'původ, možné nečistoty, chuť a rozpustnost'],
              ['Směsné formule', 'kombinace několika složek v jedné kapsli', 'dávka každé složky zvlášť, ne jen součet']]) +
          '<h2>Jak číst etiketu</h2>'
          '<p>Etiketa je nejlepší zdroj informací a zároveň místo, kde se nejčastěji chybuje. Začněte seznamem složek, který se řadí podle hmotnosti sestupně. Pokud je na prvním místě plnidlo a zajímavá složka až na konci, dostanete jí v jedné dávce jen stopové množství. Tabulka výživových údajů má uvádět obsah v jedné dávce i na sto gramů a je dobré zkontrolovat, kolik kapslí nebo odměrek tvoří doporučenou denní dávku.</p>'
          '<ul><li><strong>Forma látky</strong> se může lišit. Stejný minerál nebo extrakt existuje ve více sloučeninách a jejich podíl účinné složky se liší.</li>'
          '<li><strong>Standardizace</strong> znamená, že výrobce hlídá obsah vybrané látky. Údaj „10:1“ říká, kolik suroviny se spotřebovalo na jednotku extraktu, nikoli kolik účinné složky je uvnitř.</li>'
          '<li><strong>Pomocné látky</strong> jako stearan hořečnatý, oxid křemičitý nebo želatinová kapsle jsou běžné. U veganů a alergiků ale rozhodují.</li>'
          '<li><strong>Alergeny</strong> musí být zvýrazněné. Stopy mléka, sóji nebo lepku bývají v prášcích z vícedruhové výroby.</li>'
          '<li><strong>Šarže a datum spotřeby</strong> se vyplatí zkontrolovat hned po rozbalení, hlavně u olejů a probiotik.</li></ul>'
          '<h2>Formy: kapsle, prášek, tekutina</h2>'
          '<p>Kapsle jsou praktické na cesty a zakryjí nepříjemnou chuť, ale dávkují se po kusech a u vysokých dávek jich musíte spolknout několik. Prášek se dá odměřit přesněji, smíchat do nápoje nebo jogurtu, avšak chuť bývá výrazná, zejména u bylin a řas. Tekuté formy a kapky se rychle dávkují, po otevření se však obvykle kazí dříve. Tablety jsou levnější na výrobu a často obsahují více pojiv. Žádná forma není objektivně nejlepší, záleží na tom, co vám vyhovuje a co budete dodržovat.</p>'
          '<h2>Jak doplňky zapadají do sportovní výživy</h2>'
          '<p>Sportovní výživa má několik pevných skupin a ostatní doplňky jsou jejich okraj. Pro orientaci:</p>'
          '<ul><li>Bílkoviny najdete v kategorii <a href="/proteiny/">proteiny</a>, tabulky a tyčinky v <a href="/proteinove-tycinky-a-snacky/">proteinových tyčinkách a snacích</a>.</li>'
          '<li>Doplňky pro přibírání jsou v kategorii <a href="/gainery/">gainery</a>.</li>'
          '<li>Rozpustné aminokyseliny jsou v <a href="/aminokyseliny-bcaa/">aminokyselinách a BCAA</a> a kreatin má vlastní stránku <a href="/kreatin/">kreatin</a>.</li>'
          '<li>Stimulační směsi před tréninkem jsou ve skupině <a href="/predtreninkove-boostery/">předtréninkové boostery</a> a s nimi souvisejí i <a href="/spalovace-tuku/">spalovače tuku</a>.</li>'
          '<li>Hydratace a rychlá energie na dlouhé výkony patří do <a href="/iontove-napoje/">iontových nápojů</a> a <a href="/energeticke-gely-a-tycinky/">energetických gelů a tyčinek</a>.</li>'
          '<li>Stravu na túry a kempování najdete v <a href="/outdoorova-strava/">outdoorové stravě</a>.</li></ul>'
          '<p>Nadřazená skupina <a href="/sportovni-vyziva/">sportovní výživa</a> shrnuje všechno dohromady a hodí se jako výchozí bod, když si nejste jistí, kam produkt patří.</p>'
          '<h2>Kdy má smysl tuhle kategorii procházet</h2>'
          '<p>Nejčastěji sem míří lidé, kteří hledají konkrétní surovinu, o které slyšeli, nebo přípravek známé značky, který nemá vlastní kategorii. Pokud znáte přesný název, použijte vyhledávání. Pokud jen prozkoumáváte, začněte u značek, jejichž sortiment je široký a dobře popsaný, a čtěte složení, ne marketingové slogany na přední straně obalu.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejpočetnější zastoupení mají ' + B(('gymbeam', 'GymBeam'), ('mycomedica', 'MycoMedica'), ('greenfood-nutrition', 'GreenFood Nutrition'), ('vitaharmony', 'VitaHarmony'), ('viridian', 'Viridian'), ('ostrovit', 'OstroVit'), ('amix', 'Amix'), ('terezia', 'Terezia'), ('blendea', 'Blendea'), ('allnature', 'Allnature'), ('vitar', 'Vitar'), ('hemp-world', 'Hemp World'), ('nutricius', 'Nutricius')) + '. Sportovní značky typu GymBeam, OstroVit a Amix mají široký sortiment v celém oboru. MycoMedica se soustředí na houbové přípravky, Hemp World na konopné produkty a Viridian na doplňky s důrazem na surovinu a čistotu složení. U jedné značky se vyplatí porovnat celou řadu, protože balení a dávkování se mezi výrobky liší.</p>'
          '<h2>Skladování a trvanlivost</h2>'
          '<p>Většina doplňků nesnáší teplo, světlo a vlhkost. Lékovku nechávejte zavřenou, v suchu a mimo dosah dětí. Koupelna je kvůli páře špatné místo. Oleje a probiotika mají někdy nároky na chladnější uchování a výrobce to uvádí na obalu. Silikagelový sáček v lékovce nejezte ani nevyhazujte předčasně, chrání obsah před vlhkostí. Po otevření dodržujte dobu spotřeby uvedenou na etiketě a nepřesypávejte obsah do jiných nádob bez popisu.</p>'
          '<h2>Nejčastější chyby při nákupu</h2>'
          '<ul><li>Řídit se obrázkem a heslem na přední straně místo složením na zadní.</li>'
          '<li>Porovnávat cenu za balení místo ceny za dávku. Balení se stejnou váhou může mít jiný počet dávek.</li>'
          '<li>Kupovat několik různých přípravků najednou, takže se nedá poznat, co vám sedí.</li>'
          '<li>Zapomenout na možné interakce s léky, které již užíváte.</li>'
          '<li>Nenechat si poradit od lékaře nebo lékárníka u těhotenství, kojení, chronických potíží či u dětí.</li>'
          '<li>Brát doplněk jako náhradu stravy místo jejího doplnění.</li></ul>'
          '<h2>Pro koho a pro koho ne</h2>'
          '<p>Doplňky stravy si kupují sportovci, lidé na rostlinné stravě i ti, kdo jen sledují novinky. Nejsou určené jako náhrada léčby a žádný produkt v této kategorii nemá léčit nemoc ani zaručovat výsledek. Dětem, těhotným a kojícím ženám a lidem s pravidelnou medikací se doporučuje konzultace před užíváním čehokoli nového. Jestli si nejste jistí, zeptejte se, a to ještě před nákupem.</p>'
          '<h2>Jak začít s novým přípravkem</h2>'
          '<p>Nezkoušejte víc novinek najednou. Zavádějte jeden přípravek, sledujte, jak se cítíte, a teprve po delší době přidejte další. Vezměte nejnižší doporučenou dávku z etikety a nepřekračujte horní hranici ani tehdy, když máte pocit, že vyšší množství „víc udělá“. U prášků začněte půlkou odměrky, abyste poznali chuť a snášenlivost. Pište si, kdy jste začali a co jste užívali. Poznámky se hodí i pro lékaře, kdybyste se na něco ptali.</p>'
          '<h2>Rostlinná strava a doplňky</h2>'
          '<p>Lidé na vegetariánské nebo veganské stravě často hledají doplňky, které by jinak získali z masa, ryb či mléka. U kapslí proto sledujte, z čeho je obal. Želatina je živočišná, existují ale rostlinné kapsle z celulózy. Stejně tak oleje z řas jsou alternativou k rybím. Pokud vás zajímá konkrétní živina, začněte kategorií <a href="/vitaminy-a-mineraly/">vitaminy a minerály</a>, protože tam je přehlednější výběr podle látky. Tahle skupina je spíš pro specializované suroviny.</p>'
          '<h2>Čistota, původ a ověření</h2>'
          '<p>Seriózní výrobce uvádí zemi původu, název a adresu provozovatele a číslo šarže. Prášky z řas, trav a bobulí mohou kvůli půdě a zpracování obsahovat nežádoucí příměsi, a proto stojí za to dohledat, zda značka zveřejňuje rozbory. Nezávislé testování nebo certifikace (například ekologická) je bonus, ne záruka. Naopak varovným signálem jsou slova jako zázračný, okamžitý nebo bez vedlejších účinků. Takovou řeč si doplněk stravy dovolit nesmí a obchod, který ji používá, nemá důvěru zasluhovat.</p>'
          '<h2>Doplňky a sportovní výkon: realistické očekávání</h2>'
          '<p>Základ tvoří trénink, spánek a jídlo. Doplněk je až kosmetická vrstva nad nimi a nikdy nenahradí chybějící základy. Většina přípravků v téhle kategorii není určená ke zlepšení výkonu v ostrém slova smyslu, spíš si je lidé kupují kvůli pohodlí nebo zvědavosti. Soutěžící sportovci musí navíc kontrolovat složení vůči seznamu zakázaných látek své federace, protože i dobře míněný bylinný přípravek může obsahovat látku, která je v soutěži zakázaná.</p>'
          '<h2>Jak číst srovnání cen u balení</h2>'
          '<p>Produkty stejné značky se prodávají v několika velikostech. Větší balení bývá na dávku levnější, ale vyplatí se jen tehdy, když ho spotřebujete před koncem trvanlivosti. Kapsle s jednou dávkou za den vydrží třicet dní u menšího balení a devadesát u většího. Pokud si přípravek zkoušíte poprvé, vezměte raději malou velikost.</p>'
          '<h2>Jak na Sportece porovnat nabídky</h2>'
          '<p>Najděte produkt, otevřete jeho kartu a podívejte se na seznam obchodů. Porovnávejte současně cenu, velikost balení a dostupnost. Filtrováním podle značky zúžíte výběr a seřazením podle ceny zjistíte, kde je stejné balení nejvýhodnější. Pamatujte, že doprava se mezi obchody liší a že u akčních nabídek se doba spotřeby u některých šarží může blížit konci, takže ji vyžadujte či ověřte před objednávkou.</p>',
    faq=[('Co patří mezi další doplňky stravy?', 'Rostlinné extrakty, houbové směsi, oleje, probiotika, superpotraviny a směsné formule, tedy přípravky, které nemají vlastní podskupinu mezi proteiny, kreatinem nebo vitaminy.'),
         ('Jsou doplňky stravy léky?', 'Ne. Doplněk stravy je potravina určená k doplnění běžné stravy a nemá léčit onemocnění. Při zdravotních potížích se obraťte na lékaře, ne na přípravek z obchodu.'),
         ('Jak poznám kvalitní doplněk?', 'Podívejte se na úplný seznam složek, množství každé látky v dávce, označení šarže a datum spotřeby. Transparentní výrobce uvádí původ suroviny a formu účinné látky.'),
         ('Kapsle, nebo prášek?', 'Kapsle jsou praktické a bez chuti, prášek se dá dávkovat přesněji a míchat do nápojů. Vybírejte podle toho, co budete pravidelně užívat a jak snášíte chuť.'),
         ('Mohu kombinovat více doplňků?', 'Záleží na složení. Některé látky se překrývají a součet dávek by mohl překročit doporučenou hranici. Zkontrolujte etikety a při pochybnostech se zeptejte lékárníka.'),
         ('Co znamená standardizovaný extrakt?', 'Výrobce hlídá obsah vybrané látky v extraktu. Údaj o poměru suroviny a extraktu říká něco jiného než procento účinné složky, proto čtěte obojí.'),
         ('Jak doplňky skladovat?', 'Zavřené, v suchu, chladu a tmě a mimo dosah dětí. Řiďte se pokyny na obalu, hlavně u olejů a probiotik, kde je důležité i datum spotřeby.'),
         ('Mohou doplňky reagovat s léky?', 'Ano, u některých rostlinných látek a minerálů je to možné. Pokud užíváte léky na předpis, poraďte se s lékařem nebo lékárníkem ještě před zahájením užívání.'),
         ('Hodí se doplňky pro děti a těhotné?', 'Tato skupina potřebuje individuální přístup. Bez porady s lékařem nebo pediatrem nic neužívejte, protože dávky a bezpečnost se u nich posuzují jinak.'),
         ('Jak porovnat ceny různých balení?', 'Přepočítejte cenu na jednu dávku. Balení se stejnou hmotností může mít jiný počet dávek podle koncentrace a doporučeného užívání.'),
         ('Kde najdu proteiny a kreatin?', 'Mají vlastní kategorie: proteiny a kreatin. Tahle skupina slouží pro všechno ostatní, co mezi ně nepatří.')])

# ------------------------------------------------------------------ muskareni
NEW['muskareni'] = dict(long=True,
    title='Muškaření: mušky, pruty, šňůry a vázání | Sporteka',
    desc='Vybavení pro muškaření: mušky, muškařské šňůry, návazce, háčky a materiály na vázání. Průvodce pro začátečníky a nabídky obchodů vedle sebe.',
    intro='<p><strong>Muškaření</strong> je rybolov na umělou mušku, která se k rybě dostává na lehké šňůře, ne na závaží. Vlastní hmotnost nese šňůra, a ta zároveň určuje, jak daleko a jak jemně se nástraha uloží na hladinu. Proto se výbava liší od klasického přívlače a dává smysl ji sestavovat jako celek, ne po kusech. Začátečník tak ušetří za zbytečné omyly.</p>'
          '<p>Na Sportece najdete mušky, návazce, háčky, materiály na vázání a další drobnosti z českých obchodů a nabídky porovnáte vedle sebe. Hotovou soupravu doplníte o <a href="/rybarske-pruty/">rybářské pruty</a>, <a href="/rybarske-navijaky/">navijáky</a>, <a href="/vlasce-a-snury/">vlasce a šňůry</a> a <a href="/rybarske-doplnky/">rybářské doplňky</a>. Širší přehled celého oboru najdete v kategorii <a href="/rybareni/">rybaření</a>.</p>',
    guide='<h2>Co potřebujete na první den u vody</h2>'
          '<p>Muškařská souprava má pět článků: prut, naviják, šňůru, návazec a mušku. Každý ovlivňuje ostatní, takže nejdůležitější je, aby k sobě pasovaly. Nejpoužívanější číslování tříd šňůr a prutů, takzvané AFTM, se řídí hmotností prvních několika metrů šňůry. Prut o určité třídě je navržený právě pro šňůru stejné třídy a s jinou se chová hůř.</p>'
          + T(['Část výbavy', 'Úkol', 'Na co si dát pozor'], [
              ['Prut', 'ohýbá se a vystřeluje šňůru', 'třída, délka, akce a počet dílů'],
              ['Naviják', 'drží šňůru a podkladový vlasec, brzdí rybu', 'velikost vůči třídě šňůry, kvalita brzdy a kapacita'],
              ['Šňůra', 'nese mušku a určuje, jak se potápí', 'třída, tvar zúžení a plovoucí nebo tonoucí provedení'],
              ['Návazec', 'jemný přechod ke mušce', 'průměr, délka a materiál'],
              ['Muška', 'nástraha napodobující hmyz či potravu', 'velikost, typ háčku a styl lovu']]) +
          '<h2>Typy mušek a kdy se používají</h2>'
          '<p>Mušky se dělí podle toho, kde ve vodě loví. Přehled základních typů:</p>'
          '<ul><li><strong>Suchá muška</strong> pluje na hladině a napodobuje dospělý hmyz. Je nejviditelnější a pro začátečníky nejpoutavější, protože vidíte záběr.</li>'
          '<li><strong>Nymfa</strong> loví pod hladinou a napodobuje larvy. Bývá zatížená, někdy kuličkou z kovu, aby klesala k dnu.</li>'
          '<li><strong>Mokrá muška</strong> je lehčí než nymfa, pohybuje se těsně pod povrchem a napodobuje uvíznutý nebo tonoucí hmyz.</li>'
          '<li><strong>Streamer</strong> je větší nástraha na dravce, napodobuje drobné ryby a loví se aktivním tahem šňůry.</li>'
          '<li><strong>Technika české nymfy</strong> používá těžké nymfy, které se vedou těsně u dna na krátkou vzdálenost. Vznikla v soutěžním prostředí a dnes ji používají i běžní rybáři.</li></ul>'
          '<h2>Vlastní vázání mušek</h2>'
          '<p>Mnoho muškařů si mušky váže sám, protože to levněji nahradí ztráty a dovolí napodobit právě ten hmyz, který se v řece zrovna vylíhl. Základ tvoří svěrák, nit, háčky a materiály. Svěrák drží háček během vázání a nástroje jako nůžky, pinzeta, jehla na lak a držák cívky nebo vytahovač chmýří práci urychlí. Začátečník potřebuje málo: pár háčků, nit, drátek na zátěž, peří z kohouta, kůži, chlupy a flitry.</p>'
          '<ul><li><strong>Háčky</strong> mají různé tvary (rovné, zahnuté, těžké) a velikosti. Čím vyšší číslo, tím menší háček.</li>'
          '<li><strong>Nitě a drátky</strong> se vybírají podle velikosti mušky a barvy těla.</li>'
          '<li><strong>Peří a srst</strong> slouží na křídla, ocásky a hackle, tedy kolečko jemných vláken kolem těla.</li>'
          '<li><strong>Syntetické materiály</strong> jako pěna, flitry a třpytivé fólie dodávají mušce lesk a plovatelnost.</li>'
          '<li><strong>Pryskyřice a lak</strong> zpevňují hlavičku a zajišťují vázání proti rozmotání.</li></ul>'
          '<h2>Třída prutu a šňůry podle ryby</h2>'
          '<p>Pro malé potoky a pstruhy stačí lehčí třída a kratší prut, který snadno obhodí větve. Větší řeky a pstruhy v otevřené vodě oceníte delší prut a o třídu až dvě silnější. Na štiky a velké dravce se užívají těžší třídy, protože hodíte velkou nástrahu. Pro mořský rybolov a velké ryby je zapotřebí odolnější naviják a korozivzdorné součásti. Začátečník, který chce jednu univerzální sestavu, volí střední třídu a prut kolem středních délek, který zvládne potok i řeku.</p>'
          '<h2>Šňůra a návazec</h2>'
          '<p>Šňůra je nejdůležitější částí soupravy a často se na ní šetří nejvíc. Plovoucí šňůra je univerzální, tonoucí a polotonoucí se hodí do větších hloubek a do proudu. Na konci šňůry je kónický návazec, který se postupně ztenčuje, aby se energie hodu přenášela až k mušce. Posledním dílcem je koncovka z vlasce nebo fluorokarbonu. Návazec se mění často, šňůra vydrží několik sezón, pokud ji čistíte a chráníte před slunečním zářením.</p>'
          '<p>Další materiál pro stavbu návazců najdete v kategorii <a href="/vlasce-a-snury/">vlasců a šňůr</a>, kde jsou i podkladové šňůry a pletené vlasce.</p>'
          '<h2>Oblečení a ochrana</h2>'
          '<p>Lov ve vodě znamená promoklé nohy, a proto se používají brodicí kalhoty (vodníky) s botami, nebo neoprenové varianty do chladných vod. Pro brodění se hodí <a href="/obuv-do-vody/">obuv do vody</a> s protiskluzovou podrážkou, na dlouhé dny pomáhá i <a href="/nepromokave-bundy/">nepromokavá bunda</a> a oblečení v kategorii <a href="/rybarske-obleceni/">rybářské oblečení</a>. Polarizační <a href="/sportovni-bryle/">brýle</a> potlačují odlesky na hladině, takže vidíte pod vodu a chráníte oči před zaseknutým háčkem. Proti hmyzu pomáhá <a href="/hygiena-a-repelenty/">repelent</a>.</p>'
          '<h2>Tašky a drobnosti</h2>'
          '<p>Muškařské kapsy vyžadují organizaci. Krabičky s mušky, vyprošťovák, nůžky, vazelína na šňůru a plovoucí gel zabírají málo místa. Pro přenos se používají <a href="/rybarske-tasky/">rybářské tašky</a>, vesty a hrudní brašny. Podběrák a měřítko jsou součástí běžné výbavy, protože ryby se mají co nejšetrněji pouštět zpět. Pro delší den u vody se hodí i <a href="/bivaky-a-kresla/">bivaky a křesla</a> a pro hlubší vodu <a href="/rybarske-lode-a-elektronika/">rybářské lodě</a>.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Nejvíc zástupců v kategorii mají ' + B(('sybai', 'Sybai'), ('hends', 'Hends'), ('tommi-fly', 'Tommi-Fly'), ('semperfli', 'Semperfli'), ('hanak-competition', 'Hanák Competition'), ('veniard', 'Veniard'), ('vision', 'Vision'), ('azfishing', 'AzFishing'), ('loon', 'Loon'), ('mikado', 'Mikado'), ('stonfo', 'Stonfo'), ('wychwood', 'Wychwood'), ('ahrex', 'Ahrex'), ('greys', 'Greys'), ('whiting-hackles', 'Whiting Hackles')) + '. Hends a Hanák Competition jsou české značky se zaměřením na soutěžní styl, Veniard, Semperfli a Whiting nabízejí materiály na vázání, Ahrex háčky a Stonfo pomůcky a nástroje. U materiálů srovnávejte velikost balení a barvu, kterou na fotografii často posuzujete jen přibližně.</p>'
          '<h2>Čím začít, když jste úplný začátečník</h2>'
          '<p>Nejlepší start není sada za všechny peníze, ale prut střední třídy s kompletním setem, který vám umožní jít k vodě. Pár základních suchých a mokrých mušek, krabička, nůžky a malý podběrák stačí. Zkuste nejdřív zaplatit kurz u zkušeného muškaře, protože správný hod se špatně učí z videí. Hodně pomůže i místní rybářský svaz, který zná revíry a pravidla.</p>'
          '<h2>Péče o výbavu</h2>'
          '<p>Po slané vodě opláchněte všechno sladkou. Šňůru občas umyjte vlažnou vodou s jemným mýdlem, aby se z ní odstranily nečistoty, které zhoršují plavání a klouzání. Prut skládejte opatrně, nespojujte díly násilím a před uložením je osušte. Naviják nechte vyschnout a brzdu na konci sezóny uvolněte, aby se nestlačily kotoučky. Mušky v krabičce vysušte, jinak rezaví háčky a plesniví materiál.</p>'
          '<h2>Nejčastější chyby začátečníků</h2>'
          '<ul><li>Koupit prut a šňůru různých tříd, takže se hod nedaří.</li>'
          '<li>Použít příliš silný návazec, ryba pak muškou pohrdne.</li>'
          '<li>Šetřit na šňůře, i když je to nejdůležitější součást soupravy.</li>'
          '<li>Brodit se bez vhodné obuvi a bez opory na kluzkém dně.</li>'
          '<li>Nezjistit si předem pravidla revíru a povolenku.</li>'
          '<li>Lovit na háček s protihrotem tam, kde řád revíru vyžaduje háček bez něj.</li></ul>'
          '<h2>Roční doba a styl lovu</h2>'
          '<p>Na jaře začínají první líhně hmyzu a lov se soustředí na nymfy a mokré mušky. V létě převládají suché mušky večer a za svítání, kdy se hmyz vznáší nad hladinou. Na podzim se vracejí streamery a těžší nymfy, protože ryby jsou aktivnější před zimou. Zimní lov je pomalý, s drobnými nymfami u dna. Každý styl vyžaduje trochu jiné vybavení, proto se krabička mušek postupně rozrůstá podle sezóny.</p>'
          '<h2>Jak číst vodu</h2>'
          '<p>Ryby stojí tam, kde mají úkryt a přísun potravy: za kameny, pod převisy, na rozhraní rychlého a pomalého proudu. Hodit mušku nad takové místo a nechat ji plynout přirozeně je důležitější než dlouhý hod. Dívejte se na hladinu, zda neuvidíte kroužky po vynořujících se rybách, a zkoumejte, jaký hmyz se vznáší. Podle toho pak vyberete velikost a barvu mušky. Opatrnost patří k věci, protože stín nebo hlasité kroky ryby zaženou.</p>'
          '<h2>Bezpečnost u vody</h2>'
          '<p>Brodění v proudu je nebezpečné, především na kluzkém dně a při zvýšené hladině. Používejte brodicí hůl nebo opřete každý krok, nikdy nebrodte, když voda stoupá, a vždy si dopředu ověřte, kudy se dostanete zpět. Na hlubších místech se doporučuje <a href="/plovaci-vesty/">plovací vesta</a>. Háčky chraňte korkem nebo pěnou a při hodu mějte kolem sebe dost místa, abyste nezasáhli sebe ani ostatní.</p>'
          '<h2>Jak na Sportece porovnat nabídky</h2>'
          '<p>Mušky se prodávají po kusech i po sadách, proto se vyplatí porovnávat cenu za kus. U materiálů zkontrolujte, zda jde o balení pro jednorázové vázání, nebo zásobu na celou sezónu. Filtr podle značky zúží výběr a seřazením podle ceny zjistíte, kde je totéž balení nejlevnější. Přidejte k tomu i poštovné, protože drobné zboží se často vyplatí kombinovat do jedné objednávky u jednoho obchodu.</p>'
          '<p>Pro navazující výbavu se podívejte i do kategorie <a href="/lov-a-priroda/">lov a příroda</a>, kde najdete další outdoorové vybavení.</p>',
    faq=[('Co potřebuje začátečník na muškaření?', 'Prut střední třídy, naviják, šňůru stejné třídy, návazec, pár mušek, nůžky, vyprošťovák a podběrák. Nejdůležitější je, aby prut a šňůra měly shodnou třídu.'),
         ('Jaká třída prutu je univerzální?', 'Pro potoky a menší řeky se obvykle užívá střední lehká třída. Na větší vody a větší ryby se volí silnější třída, pro dravce ještě těžší.'),
         ('Jaký je rozdíl mezi suchou mouchou a nymfou?', 'Suchá muška plave na hladině a napodobuje dospělý hmyz, nymfa loví pod hladinou a napodobuje larvy. Nymfy bývají zatížené, aby klesaly.'),
         ('Co znamená číslo háčku?', 'Čím vyšší číslo, tím menší háček. Velikost se vybírá podle velikosti hmyzu, který mušce odpovídá, a podle ryby, kterou chcete lovit.'),
         ('Proč mám šňůru i návazec?', 'Šňůra nese hmotnost a umožní vrhnout lehkou mušku. Návazec se ztenčuje a přenáší energii hodu jemně k mušce, která pak dopadne přirozeně.'),
         ('Vyplatí se vázat mušky vlastnoručně?', 'Dlouhodobě ano. Ušetříte za ztráty a vytvoříte přesně takové mušky, jaké ryby berou. Začátek vyžaduje svěrák, nit, háčky a pár základních materiálů.'),
         ('Jak se starat o muškařskou šňůru?', 'Čistěte ji vlažnou vodou s jemným mýdlem a chraňte před sluncem a chemikáliemi. Správně ošetřená šňůra se lépe vrhá a vydrží víc sezón.'),
         ('Jaké oblečení je vhodné k vodě?', 'Brodicí kalhoty nebo neopren, obuv s protiskluzovou podrážkou, nepromokavá bunda a polarizační brýle. Na chladné vody se hodí vrstvy z vlny nebo syntetiky.'),
         ('Potřebuji povolenku?', 'Ano, k rybolovu je nutná platná povolenka a členství nebo povolení k revíru; v ČR navíc rybářský lístek. Před výletem si ověřte pravidla, například míru a doby hájení.'),
         ('Musím ryby pouštět zpět?', 'Záleží na revíru a jeho řádu. Muškaři často ryby šetrně pouštějí, k čemuž pomáhá podběrák s jemnou sítí, mokré ruce a háček bez protihrotu.'),
         ('Jak vybrat prut podle délky?', 'Kratší prut se hodí do porostlých potoků, delší do otevřených řek, kde potřebujete větší dosah a lepší kontrolu šňůry nad vodou.')])

# ------------------------------------------------------------------ skateboardy
NEW['skateboardy'] = dict(long=True,
    title='Skateboardy a longboardy: komplety i díly | Sporteka',
    desc='Skateboardy, longboardy, pennyboardy a elektrické boardy. Jak vybrat desku, kola a ložiska, velikost podle věku a nabídky obchodů vedle sebe.',
    intro='<p><strong>Skateboard</strong> je jednoduchá věc na pohled, ale pod deskou se skrývá víc rozhodnutí, než by člověk čekal: šířka desky, tvrdost kol, výška os a ložiska. Jiná sestava se hodí na triky ve skateparku, jiná na dlouhé svezení městem a další na rychlé sjezdy z kopce. Pod stejným názvem se tak prodávají zcela odlišné stroje.</p>'
          '<p>Na Sportece najdete <strong>skateboardy, longboardy, pennyboardy a elektrické boardy</strong> z českých obchodů. Nabídky porovnáte vedle sebe a můžete si vybrat hotový komplet, nebo samostatné díly. K vyjížďkám patří i <a href="/chranice-a-helmy/">chrániče a helmy</a>, pro srovnání dopravy se podívejte také na <a href="/kolobezky/">koloběžky</a> a <a href="/inline-brusle/">inline brusle</a>. Celý obor shrnuje skupina <a href="/kolobezky-a-brusle/">koloběžky, brusle a skateboardy</a>.</p>',
    guide='<h2>Skateboard, longboard, pennyboard: v čem je rozdíl</h2>'
          '<p>Slovo skateboard se používá pro celou skupinu, ale ve skutečnosti se rozlišuje několik typů. Každý má jinou desku, jiná kola a jiný způsob použití. Než vybíráte, rozhodněte, co chcete dělat.</p>'
          + T(['Typ', 'Deska a kola', 'Hodí se na'], [
              ['Klasický skateboard', 'symetrická deska s ohnutými konci, malá tvrdá kola', 'triky, skatepark, schody a zábradlí'],
              ['Longboard', 'delší a širší deska, větší měkčí kola', 'svezení po městě, cestování, sjezdy a carving'],
              ['Pennyboard a malé plastové boardy', 'krátká, lehká plastová deska, měkká kola', 'krátké přesuny, začátečníci a děti'],
              ['Cruiser', 'střední velikost, měkká kola', 'městské svezení, pohodlí a ovladatelnost'],
              ['Elektrický board', 'longboard s motorem a dálkovým ovladačem', 'dojíždění a rychlejší pohyb po rovině'],
              ['Obuv s kolečky', 'běžná bota s kolečkem v patě', 'zábava pro děti, ne náhrada skateboardu']]) +
          '<h2>Velikost desky a šířka</h2>'
          '<p>Šířka desky závisí na typu jízdy a na velikosti chodidel. Užší desky se lépe otáčejí při trikách, širší dávají více stability a hodí se pro vyšší lidi nebo na dlouhé jízdy. Děti začínají na menších deskách, aby dosáhly na všechny části a dobře ovládaly náklon. Výrobci uvádějí šířku v palcích a délku v centimetrech. Důležitý je i rozvor kol, tedy vzdálenost os, která určuje, jak ostře deska zatáčí a jak je stabilní.</p>'
          '<h2>Z čeho se deska skládá</h2>'
          '<ul><li><strong>Deska</strong> je nejčastěji z několika vrstev lisovaného javorového dřeva. Longboardy mohou být také z bambusu, kompozitu nebo plastu.</li>'
          '<li><strong>Grip páska</strong> je hrubý potah, který drží boty na desce. Časem se zanáší prachem a opotřebuje.</li>'
          '<li><strong>Osy (trucky)</strong> spojují desku s koly a řídí směr. Matice a gumové podložky určují, jak citlivě deska reaguje na náklon.</li>'
          '<li><strong>Kola</strong> se liší průměrem a tvrdostí. Menší tvrdá kola jsou rychlá na hladkém povrchu a pro triky, větší měkká tlumí nerovnosti.</li>'
          '<li><strong>Ložiska</strong> v kolech určují, jak dlouho se deska roztáčí. Udržujte je v suchu a čistá.</li>'
          '<li><strong>Šroubky a podložky</strong> drží osy. Při montáži je třeba utahovat rovnoměrně do kříže.</li></ul>'
          '<h2>Hotový komplet, nebo skládání z dílů</h2>'
          '<p>Hotový komplet je nejrychlejší cesta, jak začít. Prodejce všechny díly sladí a deska vám přijde připravená k jízdě. U nejlevnějších kompletů bývají ložiska kvalitativně slabší, ale pro první týdny stačí. Skládání z dílů vás naučí, jak deska funguje, a dovolí vám vyměňovat jednotlivé části podle potřeby. Vyplatí se, když už víte, jaký styl jízdy preferujete, nebo když vám dosluhuje jen jedna část. Jednotlivé díly se prodávají na samostatných kartách, proto při srovnání ceny sledujte, zda je v nabídce vždy kompletní sada.</p>'
          '<h2>Longboardy podle stylu jízdy</h2>'
          '<ul><li><strong>Cruising</strong> je pohodlné svezení po městě. Vyhovují měkká kola a pružnější deska.</li>'
          '<li><strong>Carving</strong> je plynulé klikatění, kdy se deska nakláněním zatáčí. Hodí se pružné osy a pružná deska.</li>'
          '<li><strong>Freeride a sjezdy</strong> vyžadují tuhou desku, kvalitní osy a ochranu, protože rychlost roste rychle.</li>'
          '<li><strong>Dancing</strong> je tanec po desce, kde jezdec přechází z nohy na nohu. Potřebuje dlouhou desku a dostatek místa.</li></ul>'
          '<h2>Elektrické boardy</h2>'
          '<p>Elektrický longboard má v kolech nebo pod deskou motor a baterii a řídí se dálkovým ovladačem. Dosah a rychlost závisí na kapacitě baterie a na terénu. Před nákupem zkontrolujte, zda lze baterii v dopravě vzít s sebou, protože pro lithiové články platí omezení u přepravy letecky. Elektrický board je těžší než klasický, proto se hůř nosí do schodů a musí se uzamykat jako kolo. Pro zájemce o alternativu k dopravě existují také <a href="/elektrokolobezky/">elektrokoloběžky</a>.</p>'
          '<h2>Pennyboardy a malé plastové boardy</h2>'
          '<p>Krátká plastová deska je lehká, vejde se do batohu a hodí se na krátké přesuny. Malá měkká kola ale hůř zvládají nerovnosti a ve vyšší rychlosti je deska nestabilní. Pro dlouhé vzdálenosti nebo hrubší povrch je lepší longboard nebo cruiser. Pennyboard je dobrý způsob, jak vyzkoušet, zda vás jízda baví, aniž byste investovali do větší sestavy.</p>'
          '<h2>Tvrdost kol a povrch</h2>'
          '<p>Tvrdost kol se udává v jednotkách durometru, u skateboardových kol se číslo uvádí s písmenem A. Vyšší číslo znamená tvrdší kolo, které je rychlé a vhodné na hladký beton nebo skatepark. Nižší číslo znamená měkčí kolo, které lépe přilne a tlumí vibrace, což se hodí na hrubší asfalt a při svezení po městě. Při výběru berte v úvahu, kde budete nejčastěji jezdit.</p>'
          '<h2>Výběr podle věku a výšky</h2>'
          '<p>Pro nejmenší jsou k dispozici desky s nižší výškou os a menším rozvorem, které se snadněji ovládají. Teenageři a dospělí vyberou standardní desku podle stylu. Vyšším jezdcům a těm s větší velikostí chodidla se hodí širší deska, která dává oporu celému chodidlu. Nechte dítě stoupnout na desku přímo v obchodě nebo si změřte chodidlo a porovnejte s údaji výrobce.</p>'
          '<h2>Ochrana: základ, který se nevynechává</h2>'
          '<p>Pád ze skateboardu je běžnou součástí učení. Nejčastěji se zraní zápěstí, lokty, kolena a hlava, proto se doporučuje helma a chrániče. Pro rychlou jízdu přidávají zkušení longboardisté ještě rukavice s plastovou podložkou, které chrání dlaň při smyku. Přehled najdete v kategorii <a href="/chranice-a-helmy/">chrániče a helmy</a>, kde jsou helmy, chrániče kolen a loktů i zápěstí. Pokud se při pádu něco stane, pomůže <a href="/prvni-pomoc/">lékárnička a první pomoc</a> a často i <a href="/bandaze-a-ortezy/">bandáže</a> na namožené klouby. Při koupi chráničů kontrolujte velikost podle obvodu končetiny a pohodlí při pohybu.</p>'
          '<h2>Obuv a oblečení</h2>'
          '<p>Skateboardista namáhá boty výrazněji než kdokoli jiný. Hrana desky a grip páska odírají svršek, proto se používají boty s plochou podrážkou, zesílenými švy a v místě úderu s extra výztuží. Plochá podrážka dává lepší cit pro desku než vysoce tlumená běžecká bota. Velký výběr najdete v kategoriích <a href="/sportovni-obuv/">sportovní obuv</a> a <a href="/tenisky/">tenisky</a>. Oblečení by mělo být volné a pevné, aby se v něm dalo pohybovat. Pro převoz boardu a ochran se hodí <a href="/batohy/">batoh</a> nebo <a href="/sportovni-tasky/">sportovní taška</a>.</p>'
          '<h2>Kde jezdit a jak začít</h2>'
          '<p>Hledejte hladký asfalt, rovné parkoviště mimo provoz nebo skatepark. Štěrk, spáry a kameny jsou pro malá kola nebezpečné, protože se do nich zaseknou a jezdec letí dopředu. Nejdřív se naučte stát na desce, odrážet se a brzdit pomocí nohy, teprve potom zkoušejte obraty a triky. Pokud je dítě malé nebo nejisté, začněte s <a href="/odrazedla/">odrážedlem</a> a postupujte přes <a href="/kolobezky/">koloběžku</a> a pennyboard. Dospělým začátečníkům se osvědčil longboard nebo cruiser, protože jsou stabilnější než klasický skateboard.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>Často nabízené jsou ' + B(('exway', 'Exway'), ('enuff', 'Enuff'), ('globe', 'Globe'), ('tempish', 'Tempish'), ('arbor', 'Arbor'), ('triple-eight', 'Triple Eight'), ('heelys', 'Heelys'), ('nils', 'Nils'), ('core', 'Core'), ('birdhouse', 'Birdhouse'), ('landyachtz', 'Landyachtz'), ('pro-tec', 'Pro-Tec'), ('rekd', 'Rekd'), ('decathlon', 'Decathlon'), ('hydroponic', 'Hydroponic'), ('187-killer-pads', '187 Killer Pads')) + '. Exway je zaměřený na elektrické boardy, Arbor a Landyachtz na longboardy, Birdhouse a Globe na klasické skateboardy a Heelys na obuv s kolečky. Triple Eight, Pro-Tec a 187 Killer Pads jsou typické pro ochranné pomůcky. Pokud se ve výběru objeví odlišný druh zboží než deska, ověřte si v popisu, co přesně kupujete.</p>'
          '<h2>Údržba</h2>'
          '<p>Ložiska se časem zanesou prachem a po dešti rezaví. Vyjměte je, očistěte a znovu promažte vhodným mazivem. Kola občas prohoďte mezi předními a zadními pozicemi, aby se opotřebovávala rovnoměrně, a vyměňte je ve chvíli, kdy jsou zploštělá. Matice os kontrolujte, protože se mohou uvolnit. Desku neskladujte venku ani v mokru, dřevo bobtná a vrství se. Grip pásku můžete zlehka očistit kartáčem.</p>'
          '<h2>Nejčastější chyby</h2>'
          '<ul><li>Koupit desku jen podle grafiky, bez ohledu na šířku a typ.</li>'
          '<li>Podcenit helmu a chrániče na začátku, kdy se padá nejčastěji.</li>'
          '<li>Použít tvrdá malá kola na hrubý povrch a divit se, že deska drncá.</li>'
          '<li>Zaměnit levný plastový board se skutečným skateboardem a očekávat stejné vlastnosti.</li>'
          '<li>Utahovat osy příliš silně, takže deska nereaguje na náklon.</li>'
          '<li>Zapomenout na zámek u elektrického boardu a nechat ho bez dozoru.</li></ul>'
          '<h2>Jak na Sportece porovnat nabídky</h2>'
          '<p>Vyberte konkrétní model a v kartě produktu uvidíte obchody a jejich ceny vedle sebe. Dávejte pozor, zda se jedná o kompletní board, nebo jen o desku či jiný díl. Zkontrolujte také rozměry, dopravu a dostupnost velikostí. Starší modely a ukončené kolekce bývají v akci, ale nemusí se již doplňovat, což je u dílů důležité.</p>',
    faq=[('Jaký je rozdíl mezi skateboardem a longboardem?', 'Skateboard má kratší symetrickou desku s malými tvrdými koly pro triky. Longboard je delší a širší s většími měkkými koly pro svezení, carving a cestování.'),
         ('Jakou velikost desky zvolit?', 'Podle věku, velikosti chodidel a stylu jízdy. Užší desky se lépe otáčejí, širší jsou stabilnější. Dětem se hodí menší desky, dospělým standardní šířka.'),
         ('Je lepší hotový komplet, nebo díly?', 'Začátečníkovi stačí hotový komplet, protože díly jsou sladěné a nemusíte nic skládat. Samostatné díly se hodí, až víte, jaký styl jízdy preferujete.'),
         ('Jak poznám dobrá kola?', 'Podle průměru a tvrdosti. Malá tvrdá kola jsou pro triky a hladký povrch, větší a měkčí kola tlumí nerovnosti a hodí se na svezení po městě.'),
         ('Potřebuji helmu a chrániče?', 'Doporučují se vždy, hlavně pro začátečníky a pro děti. Při pádu nejčastěji trpí zápěstí, lokty, kolena a hlava, proto patří k základní výbavě.'),
         ('Jak se udržují ložiska?', 'Udržujte je v suchu, občas je vyjměte, očistěte a znovu namažte. Po jízdě v dešti je vysušte, protože vlhkost způsobuje korozi a zpomaluje kolo.'),
         ('Jaké boty se hodí na skateboard?', 'Boty s plochou podrážkou a zesílenými švy, které snesou tření o grip pásku. Plochá podrážka dává lepší cit než silně tlumená běžecká obuv.'),
         ('Kolik jezdců unese elektrický board?', 'Zatížení uvádí výrobce u každého modelu. Zkontrolujte hmotnost jezdce, dosah baterie a pravidla pro přepravu lithiových článků před cestou.'),
         ('Kde se naučit jezdit?', 'Na hladkém asfaltu mimo provoz nebo ve skateparku. Začněte stáním, odrážením a brzděním, teprve potom zkoušejte obraty a triky. Pomůže zkušenější kamarád nebo kurz.'),
         ('Co jsou boty s kolečky?', 'Jsou to běžné boty s malým kolečkem v patě, určené pro zábavu. Nenahrazují skateboard a hodí se hlavně dětem, které si chtějí vyzkoušet jízdu.'),
         ('Od kolika let může dítě jezdit?', 'Záleží na jeho motorice a rovnováze. Mladší děti začínají na odrážedle nebo koloběžce, skateboard se zkouší, když dítě umí bezpečně stát a ovládat náklon.')])

# ------------------------------------------------------------------ vysoke-trekove-boty
NEW['vysoke-trekove-boty'] = dict(long=True,
    title='Vysoké trekové boty: pánské a dámské | Sporteka',
    desc='Vysoké trekové boty pánské i dámské: membrána, tuhost podrážky, velikost a péče. Průvodce výběrem a nabídky českých obchodů vedle sebe.',
    intro='<p><strong>Vysoké trekové boty</strong> sahají přes kotník a zpevňují nohu na kamenitých stezkách, v bahně nebo s těžším batohem na zádech. Nemají být nejlehčí ani nejlevnější, mají vydržet celý den chůze a ochránit nohu před vodou, kamením a zátěží; kotník podpoří, ale vyvrtnutí nezabrání. Pro krátké nenáročné výlety jsou zbytečně těžké a teplé, pro týdenní trek v horách naopak ideální.</p>'
          '<p>Na Sportece najdete <strong>pánské i dámské vysoké trekové boty</strong> z českých obchodů a nabídky porovnáte vedle sebe. Lehčí alternativu najdete v kategorii <a href="/nizke-trekove-boty/">nízkých trekových bot</a>, celý přehled pak v nadřazené skupině <a href="/trekova-obuv/">trekové boty</a>. K botám patří i <a href="/merino-ponozky/">merino ponožky</a>, <a href="/trekove-hole/">trekové hole</a> a <a href="/turisticke-batohy/">turistické batohy</a>.</p>',
    guide='<h2>Kdy zvolit vysokou botu a kdy nízkou</h2>'
          '<p>Vyšší svršek slibuje lepší oporu kotníku a ochranu proti kamení a sněhu, platí to ale jen částečně. Kotník skutečně uchrání především tuhá podrážka a pevné držení paty, ne samotná výška manžety. Vysoká bota ovšem zadrží drobné kamínky, bláto a rosu u kalhot a je užitečná tam, kde se jde po svažitém a kamenitém terénu.</p>'
          + T(['Situace', 'Vysoká bota', 'Nízká bota'], [
              ['Udržované stezky a krátké výlety', 'zbytečně těžká', 'lehčí a pohodlnější'],
              ['Kamenitý terén a svahy', 'lepší ochrana a stabilita', 'vyžaduje jistou techniku'],
              ['Těžký batoh a vícedenní treky', 'výhodná opora a odolnost', 'lehká, ale pro těžký náklad méně opěrná'],
              ['Mokro, bláto a sníh', 'vyšší manžeta chrání', 'rychleji se zahlcuje'],
              ['Léto a vedro', 'teplejší a těžší', 'lépe větraná']]) +
          '<h2>Typy vysokých trekových bot</h2>'
          '<ul><li><strong>Lehké vysoké boty</strong> mají pružnější podrážku a hodí se na turistiku a krátké treky s menším batohem.</li>'
          '<li><strong>Univerzální trekové boty</strong> mají střední tuhost a stačí na většinu českých a slovenských hor.</li>'
          '<li><strong>Těžké horské boty</strong> mají tuhou podrážku a pevný svršek. Unesou těžký náklad, ale jsou těžší a vyžadují delší rozchození.</li>'
          '<li><strong>Zimní trekové boty</strong> přidávají izolaci a vyšší manžetu. Pokud se zajímáte i o obuv do města, viz <a href="/zimni-obuv/">zimní obuv</a>.</li>'
          '<li><strong>Horolezecké a přechodové boty</strong> mají tuhou podrážku pro nesmeky nebo mačky, více v oboru <a href="/horolezectvi/">horolezectví</a>.</li></ul>'
          '<h2>Svršek: kůže, textil a membrána</h2>'
          '<p>Kožené boty jsou odolné, dlouho vydrží a po opotřebení se dají opravit u švece. Jsou těžší a vyžadují ošetřování. Textilní a syntetické jsou lehčí, rychleji schnou a vyžadují menší rozchození. Mnoho modelů má membránu, tedy vnitřní vrstvu, která propouští vodní páru, ale ne vodu. Membrána pomáhá v dešti a v mokrém sněhu, ale v horku dýchá hůř a pomalu schne, pokud se voda dostane dovnitř přes horní okraj boty. Bez membrány se noha ve vedru potí méně a boty se dají vysušit rychleji.</p>'
          '<h2>Podešev: tuhost a vzorek</h2>'
          '<p>Podrážka je pro trek rozhodující. Měkčí podrážka je pohodlnější na rovině, ale unavuje chodidlo při chůzi po kamenech. Tuhá podrážka drží nohu stabilně a dobře nese těžký batoh, ovšem hůř se s ní chodí po rovině. Hluboký vzorek s širokými vroubky se nezanáší bahnem a lépe kousá na svazích. Hrana podešve a zvýšená špice chrání při nárazu o kámen a pomáhají při stoupání. Měkčí pryž lépe drží na mokrých skalách, tvrdší pryž déle vydrží.</p>'
          '<h2>Střih a velikost</h2>'
          '<p>Správná velikost rozhoduje o tom, zda přežijete týdenní trek bez puchýřů. Boty zkoušejte odpoledne, kdy je noha nejvíc oteklá, a v ponožce, kterou budete na túru nosit. Prsty se nesmí dotýkat špičky při sestupu z kopce, takže potřebujete asi centimetr rezervy. Pata se při chůzi nahoru nesmí zvedat. Zavazujte boty pevně přes nárt a lehčeji v oblasti prstů, aby se noha nepohybovala dopředu. Pokud vás tlačí v šířce, vyzkoušejte jiný model nebo značku, protože střih se mezi výrobci liší.</p>'
          '<h2>Rozchození a prevence puchýřů</h2>'
          '<p>Nové boty si před dlouhou túrou vždy rozchoďte. Noste je doma, při procházkách a krátkých výletech, ideálně s batohem. Prevence puchýřů začíná ponožkou, bez švů a s dobrým odvodem vlhkosti. Vlněná nebo syntetická ponožka obstojí lépe než bavlněná. Na horká místa lepte náplast dřív, než se vytvoří puchýř. Základní výbava patří do <a href="/prvni-pomoc/">lékárničky a první pomoci</a> a ponožky najdete v kategoriích <a href="/sportovni-ponozky/">sportovních ponožek</a> a <a href="/merino-ponozky/">merino ponožek</a>.</p>'
          '<h2>Zavazování a práce s tkaničkami</h2>'
          '<p>Stejná bota může sedět pohodlně, nebo tlačit, podle toho, jak ji zavážete. Při stoupání povolte tkaničky v horní části, aby se kotník mohl ohýbat. Při sestupu je naopak utáhněte, aby noha neklouzala dopředu do špičky a neotloukala prsty. Při tlaku na nárt pomůže vynechat jeden pár háčků nebo provléknout tkaničku jinak. Dvojitý uzel zabrání rozvázání na stezce a konce tkaniček se dají zasunout do jazyka, aby se nezachytily o větve.</p>'
          '<h2>Výběr podle délky túry a nákladu</h2>'
          '<p>Na jednodenní výlety s lehkým batohem stačí lehčí vysoká bota se střední tuhostí. Při několikadenním treku s nákladem kolem deseti až patnácti kilogramů se vyplatí tužší podrážka a odolnější svršek, protože váha zvyšuje tlak na chodidlo. Při dlouhých sestupech s nákladem je důležité, aby prsty nenarážely do špičky boty. Kdo plánuje vysokohorské túry a přechody ledovců, potřebuje specializovanou obuv, kterou nahradit univerzální bota nedokáže.</p>'
          '<h2>Boty a roční období</h2>'
          '<p>Na jaře a na podzim, kdy je mokro a bláto, oceníte vyšší manžetu a dobře držící vzorek. V létě je hlavním problémem přehřátí a pocení, proto vybírejte prodyšný svršek a lehčí konstrukci. V zimě se vyplatí izolace a dostatek místa pro silnější ponožku, ale bez stlačování prstů. Vždy počítejte s tím, že boty drží teplo jen do té míry, jak je noha suchá a nestlačená. Při přestávkách proto zout boty, vyndat stélky a nechat nohy chvíli větrat, pokud to počasí dovolí.</p>'
          '<h2>Co patří k botám</h2>'
          '<ul><li><a href="/trekove-hole/">Trekové hole</a> odlehčují kolena při sestupu a stabilizují krok na svahu.</li>'
          '<li><a href="/turisticke-batohy/">Turistický batoh</a> s dobrým nosným systémem snižuje zátěž kotníků a zad.</li>'
          '<li><a href="/doplnky-k-obuvi/">Vložky, tkaničky a impregnace</a> prodlužují životnost a zlepšují pohodlí.</li>'
          '<li><a href="/nesmeky/">Nesmeky</a> se navlékají na boty při chůzi po zledovatělých úsecích.</li>'
          '<li><a href="/outdoorove-kalhoty/">Outdoorové kalhoty</a> a <a href="/nepromokave-bundy/">nepromokavé bundy</a> doplňují výbavu na horské počasí.</li>'
          '<li>Na sněhové túry se hodí <a href="/snezky/">sněžnice</a>, které se obvykle nasazují na vysokou vodotěsnou botu.</li></ul>'
          '<h2>Značky v nabídce</h2>'
          '<p>V kategorii je nejvíc zastoupená značka ' + B(('merrell', 'Merrell')) + ', dále ' + B(('la-sportiva', 'La Sportiva'), ('salomon', 'Salomon'), ('cmp', 'Cmp'), ('adidas', 'Adidas'), ('keen', 'Keen'), ('regatta', 'Regatta'), ('viking', 'Viking'), ('tecnica', 'Tecnica'), ('salewa', 'Salewa'), ('columbia', 'Columbia'), ('the-north-face', 'The North Face'), ('mammut', 'Mammut'), ('dynafit', 'Dynafit'), ('kilpi', 'Kilpi')) + '. Každá značka má vlastní kopyto, takže stejná velikost nemusí sedět stejně. Evropské horské značky bývají užší a tužší, americké a asijské pohodlnější a širší. Rozhodovat by měl váš skutečný tvar chodidla, ne logo.</p>'
          '<h2>Pánské, dámské a dětské modely</h2>'
          '<p>Dámské boty mají obvykle užší patu a střed chodidla a jinak tvarované kopyto, ne pouze jiné barvy. Pánské jsou širší a robustnější. Unisex modely pokrývají obě velikostní řady a výrobce uvádí převodní tabulku. U dětských bot se vyplatí nekupovat hodně na růst, protože příliš velká bota způsobuje otlaky. Dětem stačí lehčí konstrukce, pevné zapínání a pružnější podrážka.</p>'
          '<h2>Péče o vysoké trekové boty</h2>'
          '<p>Po túře boty očistěte od bláta měkkým kartáčem a vlažnou vodou. Vyndejte stélky a nechte boty vyschnout při pokojové teplotě, nikoli u kamen nebo radiátoru, kde se lepidlo uvolní a materiál vysuší. Kůži ošetřujte voskem nebo krémem určeným pro daný typ, textil impregnujte sprejem. Impregnace nenahrazuje membránu, ale pomáhá, aby voda stékala po povrchu a boty dýchaly. Tkaničky a stélky se dají vyměnit, proto je dobré je kontrolovat. Skladujte boty v suchu, mimo sluneční záření a nezavírejte je v neprodyšné tašce, pokud nejsou suché.</p>'
          '<h2>Kdy boty vyměnit</h2>'
          '<p>Při rozlepení podešve, hladkém vzorku nebo ztrátě tuhosti je čas na novou dvojici. Pozor na starší boty, které dlouho ležely: polyuretanová mezipodešev stárne i bez nošení a může se rozpadnout. Pokud bota přestala držet kotník nebo propouští vodu přes švy, je lepší ji nahradit než riskovat nepříjemnosti uprostřed túry.</p>'
          '<h2>Nejčastější chyby při výběru</h2>'
          '<ul><li>Koupit těsnou botu a doufat, že se rozchodí.</li>'
          '<li>Vybrat těžkou horskou botu na nenáročné výlety.</li>'
          '<li>Zkoušet boty v tenké ponožce místo té, kterou budete nosit.</li>'
          '<li>Spoléhat na membránu v horku a pak se divit, že se noha potí.</li>'
          '<li>Vyrazit na několikadenní trek s novými botami bez rozchození.</li>'
          '<li>Sušit mokré boty na topení.</li></ul>'
          '<h2>Jak na Sportece porovnat nabídky</h2>'
          '<p>Najděte konkrétní model, otevřete jeho kartu a porovnejte obchody. Kontrolujte, zda jsou k dispozici všechny velikosti, kolik obchod nabízí na vrácení a jak dlouhé je dodání. Starší kolekce bývají zlevněné, ale velikostní řada se tenčí. Pokud máte nohu na hranici dvou velikostí, objednejte raději dvě a nevyhovující vraťte, pokud to obchod umožňuje. Vrácení zboží si ověřte předem v podmínkách konkrétního obchodu, protože se mezi prodejci liší a lhůty nejsou stejné.</p>',
    faq=[('Jsou vysoké trekové boty lepší než nízké?', 'Záleží na terénu. Vysoké dávají větší ochranu a stabilitu s těžším batohem a na kamenitých svazích, nízké jsou lehčí a pohodlnější na udržovaných stezkách.'),
         ('Chrání vysoká bota kotník před vyvrtnutím?', 'Částečně. Rozhodující je tuhá podrážka a dobré držení paty, výška manžety pomáhá, ale kotník sama nezabrání ohnout. Pomoc nabízejí i správné zavázání a trekové hole.'),
         ('Potřebuji botu s membránou?', 'Membrána pomáhá v dešti a mokrém sněhu. V horku se noha pod ní více potí a boty pomaleji schnou, proto se v létě mnoha lidem hodí lehčí varianta bez ní.'),
         ('Jak vybrat správnou velikost?', 'Zkoušejte odpoledne v ponožce, kterou budete nosit. Měla by zbýt asi centimetr před prsty a pata se nesmí zvedat. Velikosti se mezi značkami liší.'),
         ('Jak dlouho rozchodit nové boty?', 'Několik krátkých výletů před dlouhou túrou. Boty noste s batohem a ve stejných ponožkách, aby se materiál přizpůsobil noze a odhalily se tlačící místa.'),
         ('Jak boty čistit a impregnovat?', 'Očistěte kartáčem a vlažnou vodou, nechte vyschnout při pokojové teplotě a použijte vosk na kůži nebo sprej na textil. Postup vždy kontrolujte u výrobce.'),
         ('Jaká ponožka se hodí do trekových bot?', 'Vlněná nebo syntetická ponožka bez tlustých švů, která odvádí vlhkost. Bavlna se namočí a podporuje puchýře, proto ji pro delší túry nedoporučujeme.'),
         ('Hodí se vysoké boty do zimy?', 'Ano, pokud mají izolaci, vyšší manžetu a podrážku s dobrým protiskluzem. Na led se navíc používají nesmeky nebo mačky podle terénu.'),
         ('Kdy boty vyměnit?', 'Když se podešev odlepuje, vzorek je ohlazený nebo bota přestala držet nohu a propouští vodu. Zkontrolujte také stáří, protože mezipodešev stárne i bez nošení.'),
         ('Mohu je používat i ve městě?', 'Ano, ale na dlažbě a v teple jsou těžké a teplé a podrážka se rychleji obrušuje. Pro město jsou vhodnější lehčí boty.'),
         ('Jaký je rozdíl mezi dámskou a pánskou botou?', 'Dámské mají užší patu a jiné kopyto, ne jen jiné barvy. Pánské jsou širší. Unisex modely mají převodní tabulku velikostí, kterou uvádí výrobce.')])
