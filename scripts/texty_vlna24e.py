"""sporteka.cz — wave 24e (5. 11. 2026): long texts for silnicni-kola, jezdecke-kalhoty, spalovace-tuku, trekingova-elektrokola.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ silnicni-kola
NEW['silnicni-kola'] = dict(long=True,
    title='Silniční kola: geometrie, skupiny, velikost rámu',
    desc='Silniční kola pro asfalt: endurance, aero a lehká stoupací. Jak vybrat rám, skupinu, kotouče a velikost a porovnat nabídky českých obchodů.',
    intro='<p>Silniční kolo je stroj stavěný na efektivní jízdu po zpevněném povrchu. Má beranidlové řídítko, úzké a hladké pláště a lehký rám, takže na rovině i v kopci využijete skoro každý watt. Zároveň jde o kategorii s velkými rozdíly: od pohodlných modelů na celodenní výlety přes aerodynamické závodní stroje až po lehké kopcové speciály. Na Sportece vedle sebe uvidíte nabídky několika obchodů k témuž rámu a snadno poznáte, kde je skladem vaše velikost.</p>'
          '<p>V kategorii najdete značky ' + B(('van-rysel', 'VAN Rysel'), ('sava', 'Sava'), ('trek', 'Trek'), ('pinarello', 'Pinarello'), ('lapierre', 'Lapierre'), ('kellys', 'Kellys'), ('triban', 'Triban')) +
          '. Pro smíšený povrch se hodí <a href="/gravel-kola/">gravel kola</a>, pro rekreaci <a href="/trekingova-kola/">trekingová kola</a> a pro pomoc do kopců <a href="/silnicni-a-gravel-elektrokola/">silniční a gravel elektrokola</a>. K silničnímu kolu patří <a href="/silnicni-cyklohelmy/">silniční cyklohelma</a>.</p>',
    guide='<h2>Jaké druhy silničních kol existují</h2>'
          '<p>Slovo silničák skrývá několik různých konstrukcí. Liší se úhlem rámu, délkou zadní stavby, tvarem trubek i tím, jak daleko před sebou má jezdec řídítka. Dobrá volba proto začíná u vlastního stylu jízdy, ne u značky.</p>'
          + T(['Typ', 'Charakteristika', 'Hodí se pro'], [
              ['Endurance', 'delší hlavová trubka, vzpřímenější poloha, větší rezerva pro širší plášť', 'celodenní výlety, začátečníky, jezdce s bolavými zády'],
              ['Aero', 'tvarované trubky, integrované vedení lanek, nižší poloha', 'rychlé skupinové jízdy, časovky a závodníky'],
              ['Lehké stoupací', 'nízká hmotnost, tuhý středový box, sportovní geometrie', 'kopcovitý terén a vytrvalostní závody'],
              ['Univerzální závodní', 'kompromis mezi váhou a aerodynamikou', 'jezdce, kteří chtějí jedno kolo na všechno'],
              ['All-road', 'široké pláště, často 1× pohon a upevnění nosičů', 'zpevněné i štěrkové cesty, cestování'],
              ['Triatlonové a časovkářské', 'extrémně nízká poloha, aerodynamické nástavce', 'závody jednotlivců na čas']]) +
          '<p>Hranice mezi kategoriemi se stírají. Endurance kolo s širšími plášti zvládne i lehčí štěrk, a pokud plánujete jezdit hodně mimo asfalt, přečtěte si raději výběr mezi <a href="/gravel-kola/">gravel koly</a>. Pro rovinatý terén naopak oceníte aerodynamiku, v horách spíš nízkou váhu.</p>'
          '<h2>Rám, materiál a vidlice</h2>'
          '<p>Rám určuje, jak se kolo jezdí. Čtyři hlavní materiály mají každý svoje výhody.</p>'
          '<ul><li><strong>Hliník</strong> je dostupný, tuhý a odolný. Hodí se na tréninkové a první kolo, protože drobné poškození rámu snáší lépe než lehký karbon.</li>'
          '<li><strong>Karbon</strong> umožňuje tvarovat trubky a ladit tuhost v různých místech, je lehčí a tlumí drobné vibrace. Nezvládá ale tvrdé údery a nevhodné utažení šroubů.</li>'
          '<li><strong>Ocel</strong> je pružná a opravitelná, těžší a v nabídce vzácná.</li>'
          '<li><strong>Titan</strong> je trvanlivý a nekoroduje, ale najdete ho spíš u malých značek.</li></ul>'
          '<p>Vidlice u moderních kol bývá karbonová. U modelů s kotoučovými brzdami má osu s pevným uchycením, tzv. pevnou osu, která zlepšuje tuhost a přesnost vedení. Zkontrolujte také, jaké největší pláště rám a vidlice připouštějí, protože od toho závisí pohodlí.</p>'
          '<h2>Velikost rámu a nastavení polohy</h2>'
          '<p>Velikost rámu patří k nejdůležitějším rozhodnutím, protože špatně zvolené kolo nezachrání žádný komponent. U silničních kol se velikost udává v centimetrech nebo v označení XS až XL. Číslo ale není všechno, rozhoduje i délka horní trubky a výška hlavové trubky.</p>'
          + T(['Výška postavy', 'Orientační velikost rámu'], [['160–168 cm', '49–51 cm'], ['168–173 cm', '52–53 cm'], ['173–178 cm', '54–55 cm'], ['178–184 cm', '56–57 cm'], ['184–190 cm', '58–60 cm'], ['nad 190 cm', '60 cm a víc']]) +
          '<p>Tabulka je jen orientační a značky se liší. U Pinarella a Lapierra se často udávají jiné rozměry než u modelů Sava nebo Triban, protože geometrie se mění. Pomůže i rozměr, kterému se říká stack a reach: stack je svislá vzdálenost od středu šlapání k hlavové trubce a reach vodorovná. Delší reach znamená nataženější polohu.</p>'
          '<p>Po nákupu se nastavuje výška sedla (při šlapání má být koleno mírně pokrčené), předsunutí sedla a výška řídítek pomocí podložek pod představcem. Z původní podložkové sestavy se nic neřeže, dokud si nejste jistí finální polohou, jinak se zpětná úprava komplikuje. Od <a href="/cyklo-sedacky-a-voziky/">sedla</a> a <a href="/cyklo-riditka/">řídítek</a> se odvíjí pohodlí, takže se vyplatí zkusit je s kolem a případně vyměnit.</p>'
          '<h2>Převodové skupiny a řazení</h2>'
          '<p>Převodovka je druhý hlavní parametr po rámu. Dva nejrozšířenější výrobci jsou Shimano a SRAM, dále existuje Campagnolo. Řazení je mechanické nebo elektronické, bezdrátové či s kabelem.</p>'
          + T(['Výrobce', 'Úrovně od základní po špičkovou', 'Poznámka'], [
              ['Shimano', 'Claris, Sora, Tiagra, 105, Ultegra, Dura-Ace', 'Di2 je elektronické řazení, 105 i Ultegra jsou dostupné ve verzi s Di2'],
              ['SRAM', 'Apex, Rival, Force, Red', 'AXS je bezdrátové elektronické řazení, užívá se i 1× pohon'],
              ['Campagnolo', 'od základních po špičkové', 'v obchodech méně obvyklé']]) +
          '<p>Počet rychlostí se v popisech udává jako počet kol vpředu krát počet pastorků vzadu, například 2×12. Dvě převodníky vpředu dávají širší rozsah, 1× pohon je jednodušší a vhodný do smíšených podmínek. Pro rekreační jízdu stačí střední úroveň a zbytek peněz je rozumnější věnovat na lepší kola nebo kvalitní <a href="/cyklo-pohon/">pohon a komponenty</a>. Upozornění pro budoucí údržbu: elektronická řazení vyžadují nabíjení nebo výměnu baterie.</p>'
          '<h2>Brzdy, kola a pláště</h2>'
          '<p>Na silničních kolech dnes dominují kotoučové brzdy. Brzdí předvídatelně i za mokra a umožňují širší pláště. Starší ráfkové brzdy jsou lehčí a jednodušší, ale hůř brzdí v dešti. Kotoučové brzdy bývají hydraulické, u základních modelů se vyskytují i mechanické. Další informace najdete v kategorii <a href="/cyklo-brzdy/">cyklo brzdy</a>.</p>'
          '<p>Pláště se používají na silnici nejčastěji o šířce 28 až 32 mm. Širší plášť je pohodlnější a při nižším tlaku má dobrou přilnavost. Plášť může být drátový, skládací, nebo bezdušový (tubeless). Bezdušové sestavy snižují riziko defektu, vyžadují ale těsnicí tekutinu a správné ráfky. Ráfky mohou být hliníkové nebo karbonové, vyšší profil ráfku zlepšuje aerodynamiku, nižší je lehčí a méně citlivý na boční vítr. Více o výbavě je v kategorii <a href="/cyklo-kola-a-rafky/">kola a ráfky</a>.</p>'
          '<h2>Pedály, obuv a výbava jezdce</h2>'
          '<p>Silniční kolo se prodává často bez pedálů, protože si je jezdec volí podle obuvi. Nášlapné pedály pevně spojují botu s kolem a zlepšují účinnost šlapání. Vyžadují zvyk, hlavně při zastavování, proto první dny cvičte vyvazování na rovině. Nabídku najdete v kategorii <a href="/cyklo-pedaly/">cyklo pedály</a> a odpovídající boty v <a href="/cyklisticka-obuv/">cyklistické obuvi</a>.</p>'
          '<p>Základní výbava obsahuje <a href="/silnicni-cyklohelmy/">helmu</a>, <a href="/cyklisticke-rukavice/">rukavice</a>, <a href="/cyklisticke-kratasy-a-kalhoty/">cyklistické kraťasy a kalhoty</a> s vložkou, láhev v <a href="/cyklo-lahve-a-drzaky/">držáku</a>, <a href="/cyklo-pumpy-a-naradi/">pumpičku a nářadí</a> a světla z kategorie <a href="/cyklo-svetla/">cyklo světla</a>. Na delších trasách pomůže <a href="/cyklo-computery/">cyklocomputer</a> s navigací. Výživu na cestu řeší <a href="/energeticke-gely-a-tycinky/">energetické gely a tyčinky</a> a <a href="/iontove-napoje/">iontové nápoje</a>.</p>'
          '<h2>Péče a údržba</h2>'
          '<p>Silniční kolo je citlivější na údržbu než běžné městské kolo. Řetěz po každé větší jízdě otřete a pravidelně promazávejte mazivem na řetěz, nadbytek mazadla otírejte, aby se na něj nezachytával prach. Tlak v plášti kontrolujte před každou jízdou, protože úzké pláště ztrácejí vzduch rychleji než široké. Správný tlak závisí na hmotnosti jezdce, šířce pláště a tom, zda jedete s duší, či bez ní, a doporučení najdete na boku pláště.</p>'
          '<p>Z kotoučových brzd udržujte čisté kotouče, nikdy je nestříkejte olejem a při čištění používejte specializovaný čistič. Brzdové destičky se opotřebují, výměnu poznáte podle tenké vrstvy materiálu. Aspoň jednou ročně nechte v servisu zkontrolovat ložiska, vedení lanek a dotažení šroubů, především u karbonových dílů. Utahovací momenty se dodržují pomocí momentového klíče. Praktické nářadí a čističe najdete v kategorii <a href="/cyklo-udrzba/">cyklo údržba</a>.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li><strong>Špatná velikost rámu.</strong> Kolo, které sedí jen na papíře, bolí. Vždy ověřte geometrii, nejen číslo.</li>'
          '<li><strong>Honba za nejvyšší skupinou.</strong> Při omezeném rozpočtu je lepší střední úroveň a kvalitní kola než špičkový převod na slabých ráfcích.</li>'
          '<li><strong>Podceněná doprava a uložení.</strong> Karbonový rám neupínejte do stojanu za střední část trubky, pro přepravu v autě se hodí <a href="/cyklo-nosice-na-auto/">nosič na auto</a>.</li>'
          '<li><strong>Zapomenuté příslušenství.</strong> K ceně kola připočtěte pedály, helmu, světla, zámek ze skupiny <a href="/cyklo-zamky/">cyklo zámky</a> a nářadí.</li>'
          '<li><strong>Příliš úzké pláště.</strong> Pohodlí na hrubším asfaltu se výrazně zlepší u širšího pláště.</li></ul>'
          '<h2>Na co si dát pozor při nákupu v e-shopu</h2>'
          '<p>Silniční kola se prodávají v modelových ročnících. U kol Trek a Pinarello se vedle názvu objevuje označení ročníku, které naznačuje čerstvost konstrukce a barevného provedení. Starší ročník může být výhodný, pokud se komponenty shodují. Zjistěte, zda je kolo kompletně smontované, nebo ho obchod dodává částečně rozložené, a zda ho zdarma seřídí. U vyšších modelů si pročtěte záruční podmínky rámu. Na Sportece vidíte u téhož modelu více obchodů a velikosti, které mají právě skladem, takže snadno ověříte dostupnost rámu ve vaší velikosti.</p>',
    faq=[('Jaké silniční kolo vybrat pro začátečníka?', 'Nejlepší bývá endurance model s hliníkovým rámem, kotoučovými brzdami a převodem střední úrovně. Je pohodlnější, snáší širší pláště a odpustí chyby v nastavení.'),
         ('Jak poznat správnou velikost rámu?', 'Podle výšky postavy, délky kroku a délky horní trubky. Vyjděte z velikostní tabulky výrobce a ověřte také stack a reach. Pokud jste mezi velikostmi, zvažte, zda dáváte přednost sportovnější, nebo vzpřímenější poloze.'),
         ('Je lepší karbonový, nebo hliníkový rám?', 'Karbon je lehčí, lépe tlumí vibrace a dá se tvarovat. Hliník je odolnější vůči pádům a obvykle dostupnější. Pro rekreaci a tréninkové kolo obvykle stačí hliník.'),
         ('Co znamená 2×12 nebo 1×13 rychlostí?', 'První číslo je počet převodníků vpředu, druhé počet pastorků na kazetě. Dvě převodníky dávají širší rozsah, jeden je jednodušší a vhodný do smíšeného terénu.'),
         ('Jaký je rozdíl mezi silničním a gravel kolem?', 'Silniční kolo je optimalizované pro asfalt, má užší pláště a sportovní geometrii. Gravel kolo snáší širší pláště, má stabilnější geometrii a upevnění pro nosiče, takže se hodí i na štěrk.'),
         ('Jaké pláště zvolit?', 'Na silnici se dnes používá šířka 28 až 32 mm. Širší plášť je pohodlnější, užší o něco lehčí. Rozhodněte se podle povrchu a podle toho, kolik místa v rámu je k dispozici.'),
         ('Potřebuji nášlapné pedály?', 'Nutné nejsou, ale zlepšují přenos síly a stabilitu nohy. Začátečníkům se může hodit nejdřív jednodušší pedál s plochou a později přechod na nášlapné.'),
         ('Jak často servisovat silniční kolo?', 'Základní údržbu, tedy čištění a promazání řetězu a kontrolu tlaku, dělejte pravidelně. Komplexní servis v dílně se doporučuje jednou za sezonu, při větším nájezdu častěji.'),
         ('Hodí se silniční kolo na každodenní dojíždění?', 'Dá se použít, ale chybí mu blatníky, nosiče a pevné světlo. Na dojíždění je výhodnější trekingové nebo městské kolo, případně silniční model s upevněním blatníků.'),
         ('Mohu na silničním kole jezdit v zimě?', 'Ano, ale s širšími pláštěmi, blatníky a světly. Po jízdě po mokru nebo po soli kolo opláchněte a promažte řetěz, aby nezačal korodovat.')],
)

# ------------------------------------------------------------------ jezdecke-kalhoty
NEW['jezdecke-kalhoty'] = dict(long=True,
    title='Jezdecké kalhoty a rajtky: sed, velikost, údržba',
    desc='Jezdecké kalhoty, rajtky a legíny pro děti i dospělé. Jak vybrat sed, grip, materiál a velikost a porovnat nabídky českých obchodů.',
    intro='<p>Jezdecké kalhoty nejsou jen oblečení do sedla. Mají vyztužené místo uvnitř kolen a na zadní straně, takže jezdec lépe drží v sedle a nepřidírá si kůži o třmenový řemen. Kategorie zahrnuje rajtky s plným nebo částečným sedem, pohodlné jezdecké legíny, dětské i pánské modely a letní lehké varianty. Sporteka porovnává nabídky českých obchodů, abyste snadno zjistili, které velikosti jsou právě skladem.</p>'
          '<p>V kategorii najdete značky ' + B(('fouganza', 'Fouganza'), ('litex', 'Litex'), ('progress', 'Progress'), ('elt', 'ELT'), ('qhp', 'QHP'), ('jd-attack', 'JD Attack'), ('imperial-riding', 'Imperial Riding'), ('harrys-horse', 'Harrys Horse'), ('horze', 'Horze')) +
          '. K nim se hodí <a href="/jezdecke-helmy/">jezdecké helmy</a>, <a href="/jezdecka-obuv/">jezdecká obuv</a> a <a href="/jezdecke-obleceni/">jezdecké oblečení</a>.</p>',
    guide='<h2>Rajtky, legíny a jezdecké kalhoty: jaký je rozdíl</h2>'
          '<p>Výrazy se v obchodech míchají, přesto za nimi stojí tři různé střihy. Vybírejte podle disciplíny, ročního období a toho, jak citlivý je jezdec na tlak švů.</p>'
          + T(['Typ', 'Charakteristika', 'Hodí se pro'], [
              ['Klasické rajtky', 'pevnější materiál, vyztužený sed nebo kolena, střih nad boty', 'jezdecké kurzy, závody a práci ve stájích'],
              ['Jezdecké legíny', 'pružné, přiléhavé, s gripem nebo bez něj', 'denní jízdu, děti, teplé měsíce'],
              ['Kalhoty s koleny z gripu', 'protiskluzová plocha jen na vnitřní straně kolen', 'začátečníky a rekreační jezdce'],
              ['Kalhoty s plným sedem', 'protiskluzová vrstva se táhne přes celý sed', 'skok, drezúru a náročnější tréninky'],
              ['Zimní rajtky', 'hřejivá podšívka nebo silnější materiál', 'jízdu v chladných měsících'],
              ['Letní rajtky', 'tenký prodyšný úplet nebo perforovaný materiál', 'léto a horká počasí']]) +
          '<p>Slovo rajtky označuje původně kalhoty upravené pro jízdu na koni. Dnes pod ním obchody rozumějí všechny typy včetně legín. Pro tvrdší zátěže se vyplatí ověřit, jak je sed vyztužený a jak je šitý.</p>'
          '<h2>Typy sedu a gripu</h2>'
          '<p>Sed je nejdůležitější část kalhot. Ovlivňuje, jak pevně sedíte, jak se kalhoty opotřebují a kolik tření snesou.</p>'
          '<ul><li><strong>Silikonový grip</strong> je pryskyřičný nebo silikonový potisk, který zvyšuje přilnavost k sedlu. Dobře drží a omezuje sklouzávání kalhot po kůži sedla, zvlášť při změnách tempa.</li>'
          '<li><strong>Plný sed (full seat)</strong> pokrývá celou plochu sedu a vnitřní stranu stehen, využívají ho skokani a drezuristé.</li>'
          '<li><strong>Částečný sed</strong> pokrývá jen vnitřní stranu kolen a část sedu, je pružnější a pohodlnější pro děti a začátečníky.</li>'
          '<li><strong>Semišová nebo kožená výztuha</strong> je klasické řešení, odolné, ale na praní náročnější a pro některé jezdce příliš hladké.</li>'
          '<li><strong>Rajtfleky</strong> jsou plošky na vnitřní straně kolen z protiskluzového materiálu, které zjednodušují jízdu v krátkých jezdeckých botách. Pánské modely s rajtfleky najdete v nabídce značek Fouganza a Litex.</li></ul>'
          '<p>Silnější protiskluz neznamená vždy lepší výsledek. U začátečníka může příliš pevný sed zpomalit učení správné polohy, protože jezdec se drží kalhotami místo tělem. Rozumnou volbou je částečný sed a postupný přechod na plný.</p>'
          '<h2>Materiál a střih</h2>'
          '<p>Nejčastěji se šijí z elastického úpletu s příměsí elastanu, který dovoluje kalhotám pružně sledovat pohyb. Bavlněné směsi jsou příjemné na dotek a dobře odvádějí pot, syntetická vlákna rychleji schnou a snášejí častější praní. Zimní kalhoty mívají hřejivou vrstvu uvnitř. Perforované a síťované letní modely uleví v horku, při častém praní ale ztrácejí tvar, proto je perte šetrně.</p>'
          '<p>Střih má zásadní vliv na pohodlí. Vyšší pas chrání záda při předklonu, nižší pas bývá méně vidět pod bundou. Švy v koleni a v rozkroku by neměly tlačit. Zkontrolujte, zda ploché šití nedře na vnitřní straně lýtek, kde se noha tře o bok koně. Nohavice se obvykle nosí zasunuté do jezdecké obuvi nebo chapsů, proto je důležité, aby se neshrnovaly.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>Rajtky mají sedět těsně, ale nesmí omezovat pohyb ani zanechávat otlaky. Rozměry se v tabulkách udávají podle obvodu pasu, boků a délky nohavice, u dětí často podle výšky.</p>'
          + T(['Výška dítěte', 'Orientační velikost'], [['110–116 cm', '5–6 let'], ['122–128 cm', '7–8 let'], ['134–140 cm', '9–10 let'], ['146–152 cm', '11–12 let'], ['158–164 cm', '13–14 let']]) +
          '<p>Tabulka je jen orientační, každá značka počítá s jinou postavou. U dětí volte raději lehkou rezervu, protože rostou rychle, ale kalhoty nesmějí být tak velké, aby se pod kolenem mačkaly. Dospělí si před koupí změří pas, boky a vnitřní délku nohy a porovnají hodnoty s tabulkou výrobce. Elastické materiály se po několika praních mírně uvolní, proto je lepší koupit velikost, která je zpočátku těsná, ale pohodlná.</p>'
          '<h2>Dětské, dámské a pánské kalhoty</h2>'
          '<p>Dětské jezdecké kalhoty mají často měkký pas s gumou a bývají doplněné silikonovým gripem. Existují lehké letní i zimní provedení. Dětem se hodí zejména částečný sed a pružný pas, protože jezdecká poloha je pro menší tělo méně stabilní. Značka Fouganza nabízí kalhoty pro nejmenší jezdce, značky Imperial Riding a BR mají dívčí modely s gripem.</p>'
          '<p>Dámské modely jsou v pase užší a mívají tvarovaný sed a delší nohavici. Pánské modely mají širší střih v pase a bocích a nižší výstřih sedu, často s protiskluzovými rajtfleky. Pro těhotné a po porodu existují modely s nastavitelným pasem, vybírejte u nich elastický materiál s měkkou gumou.</p>'
          '<h2>Co nosit k jezdeckým kalhotám</h2>'
          '<p>Rajtky tvoří jen část výbavy. Bezpečnost začíná u <a href="/jezdecke-helmy/">jezdecké helmy</a>, která chrání při pádu, a pokračuje <a href="/jezdecka-obuv/">jezdeckou obuví</a> s malým podpatkem, který brání zasunutí nohy do třmenu. Doplňky z kategorie <a href="/jezdecke-doplnky/">jezdecké doplňky</a> zahrnují rukavice, opasky nebo chrániče. Další vybavení, například péči o koně, najdete ve skupině <a href="/vybaveni-pro-kone/">vybavení pro koně</a>. Celkový přehled kategorií nabízí stránka <a href="/jezdectvi/">jezdectví</a>.</p>'
          '<p>V chladu se pod kalhoty hodí termo spodní prádlo, v dešti pláštěnka a v teple lehká trička. Pro delší trénink v zimě si pořiďte i teplou bundu z kategorie <a href="/jezdecke-obleceni/">jezdecké oblečení</a>.</p>'
          '<h2>Péče a praní</h2>'
          '<p>Správná péče prodlužuje životnost gripu i materiálu. Postupujte podle štítku, obecně ale platí několik zásad.</p>'
          '<ul><li>Kalhoty perte naruby, aby se grip nepoškrábal o ostatní prádlo.</li>'
          '<li>Neperte při vysoké teplotě, doporučuje se vlažná voda a jemný prací prostředek.</li>'
          '<li>Nepoužívejte aviváž a bělicí přípravky, ucpávají vlákna a zhoršují přilnavost gripu.</li>'
          '<li>Sušte na vzduchu, ne na topení a v sušičce, vysoká teplota poškodí silikon i elastan.</li>'
          '<li>Skvrny od koně a bláta nechte nejdřív zaschnout a pak je vykartáčujte, vyperou se snáz.</li>'
          '<li>Zip a knoflíky před praním zapněte, aby nepoškodily látku.</li></ul>'
          '<h2>Časté chyby při koupi</h2>'
          '<p>Nejčastější omyl je volba podle barvy místo podle sedu. Bílé rajtky jsou ozdobou na závodech, na denní trénink se ale špiní a hůř čistí. Druhou chybou je příliš pevný grip pro začátečníka. Třetí je malá velikost, kdy se kalhoty při sezení stahují do rozkroku, a čtvrtá nákup jediného páru: při pravidelné jízdě se hodí aspoň dva kusy, aby jedny mohly schnout. A konečně se vyplatí počítat s tím, že tenké letní legíny nevydrží tak dlouho jako pevnější rajtky.</p>'
          '<h2>Jak číst nabídky na Sportece</h2>'
          '<p>Kalhoty se v nabídce liší názvem, pohlavím a typem gripu. Název často říká, zda jde o dětský, dámský nebo pánský střih, a počet na konci (například 100, 500) bývá označením modelové řady výrobce. Porovnáváním více obchodů uvidíte, zda je stejná velikost skladem jinde, a nemusíte brát první nabídku.</p>',
    faq=[('Jaký je rozdíl mezi rajtkami a jezdeckými legínami?', 'Rajtky mají obvykle pevnější materiál a vyztužený sed nebo kolena. Legíny jsou pružnější, přiléhavější a pohodlnější na denní jízdu, často s gripem.'),
         ('Co je to full grip?', 'Protiskluzová vrstva přes celý sed a vnitřní stranu stehen. Zlepšuje přilnavost k sedlu a hodí se pro skok a drezúru. Začátečníkům může stačit částečný sed.'),
         ('Jak poznám správnou velikost dětských rajtek?', 'Podle výšky a obvodu pasu, ne podle věku. Porovnejte rozměry s tabulkou konkrétní značky a vybírejte takovou velikost, která při sezení netlačí a v kolenou neztrácí tvar.'),
         ('Jak prát jezdecké kalhoty s gripem?', 'Naruby při vlažné vodě, bez aviváže a bělidel. Sušte na vzduchu, ne na topení nebo v sušičce, protože silikon a elastan při vysoké teplotě trpí.'),
         ('Hodí se jezdecké kalhoty i na jiný sport?', 'Jako pružné kalhoty ano, ale vyztužený sed a rajtfleky jsou přizpůsobené jízdě na koni. Pro běžné sporty bývají pohodlnější obyčejné sportovní legíny.'),
         ('Je nutné nosit jezdecké kalhoty na začátku?', 'Pro první hodiny se obejdete s pružnými kalhotami bez švů v rozkroku. Brzy ale oceníte vyztužená kolena a protiskluzové plochy, které zlepšují stabilitu v sedle.'),
         ('Jaké rajtky vybrat do léta?', 'Tenké, prodyšné nebo perforované modely s lehkým silikonovým gripem. Mají světlejší barvu a lépe odvádějí pot, ale méně vydrží.'),
         ('Co jsou rajtfleky?', 'Plošky z protiskluzového materiálu na vnitřní straně kolen, které zlepšují přilnavost ke třmenovému řemenu. Používají se hlavně u modelů pro krátkou jezdeckou obuv.'),
         ('Jak často měnit jezdecké kalhoty?', 'Záleží na četnosti jízdy. Vyměňte je, když se grip odlupuje, sed se prodřel nebo materiál ztratil pružnost. Při pravidelné jízdě se hodí mít aspoň dva páry.'),
         ('Jaké kalhoty pro zimní jízdu?', 'Zimní rajtky s hřejivou podšívkou nebo silnějším úpletem. Pod ně se hodí termo spodní prádlo a v mokru nepromokavé návleky.')],
)

# ------------------------------------------------------------------ spalovace-tuku
NEW['spalovace-tuku'] = dict(long=True,
    title='Spalovače tuků a karnitin: složení, užití, rizika',
    desc='Spalovače tuků, L-karnitin a termogenní doplňky stravy: formy, složení a obecná upozornění. Porovnejte nabídky českých obchodů.',
    intro='<p>Spalovače tuků jsou doplňky stravy, které mají být součástí režimu zaměřeného na redukci hmotnosti. Pod tímto názvem se prodávají velmi různé produkty: kapsle s kofeinem a rostlinnými extrakty, tekuté shoty, tablety i samostatný L-karnitin. Žádný z nich nenahradí pestrou stravu, pohyb a spánek. Sporteka porovnává nabídky českých obchodů, abyste snadno srovnali složení, formu a velikost balení.</p>'
          '<p>Najdete zde značky ' + B(('gymbeam', 'GymBeam'), ('amix', 'Amix'), ('extrifit', 'Extrifit'), ('nutrend', 'Nutrend'), ('penco', 'Penco'), ('ostrovit', 'OstroVit'), ('musclesport', 'Musclesport'), ('natural-protein', 'Natural Protein'), ('nero', 'Nero')) +
          '. Souvisejí s nimi <a href="/sportovni-vyziva/">sportovní výživa</a>, <a href="/predtreninkove-boostery/">předtréninkové boostery</a> a <a href="/aminokyseliny-bcaa/">aminokyseliny BCAA</a>. U všech platí: doplněk stravy není lék a před užíváním se poraďte s lékařem.</p>',
    guide='<h2>Co se pod pojmem spalovač tuků skrývá</h2>'
          '<p>Název je marketingový a nemá přesnou definici. Obsahuje-li složení kofein, zelený čaj a koření, jde o termogenní směs. Pokud je hlavní složkou L-karnitin, bývá produkt označen jako karnitinový doplněk. Rozdíl pochopíte jen čtením etiketa, ne jen názvu.</p>'
          + T(['Druh produktu', 'Typické složky', 'Forma'], [
              ['Termogenní směs', 'kofein, extrakt ze zeleného čaje, koření, někdy synefrin', 'kapsle, tablety'],
              ['Nestimulační směs', 'rostlinné extrakty bez kofeinu, vláknina, minerály', 'kapsle, prášek'],
              ['L-karnitin', 'L-karnitin, tartrát nebo acetyl-L-karnitin', 'kapsle, tablety, tekutý shot'],
              ['Spalovač pro ženy', 'rostlinné extrakty, vitaminy, často kofein', 'kapsle'],
              ['Tekutý shot', 'kofein, karnitin a příchutě v dávkované ampulce', 'ampule, láhve'],
              ['Čajové a bylinné směsi', 'rostlinné čaje v sáčcích', 'sáčky']]) +
          '<p>Tvrzení výrobců na obalech se u doplňků stravy řídí pravidly pro potraviny, nikoliv pro léky. Žádný produkt tedy neprokazuje léčebný účinek. Vnímejte ho spíš jako pomocníka, který neřeší nic bez změny jídelníčku.</p>'
          '<h2>Nejčastější složky a k čemu se používají</h2>'
          '<p>Při čtení složení se vyplatí znát základní položky. Seznam níže nepopisuje zdravotní účinky, jen říká, co která složka je.</p>'
          '<ul><li><strong>Kofein</strong> je stimulant, který se přirozeně vyskytuje v kávě a čaji. V doplňcích bývá bezvodý kofein nebo extrakt z guarany či maté. Při kombinaci s kávou a energetickými nápoji se celková dávka snadno zvýší.</li>'
          '<li><strong>Extrakt ze zeleného čaje</strong> obsahuje přírodní látky z čajovníku a často také kofein.</li>'
          '<li><strong>L-karnitin</strong> je látka, kterou si tělo vytváří samo a přijímáme ji i z masa. Prodává se v několika formách: L-karnitin tartrát, acetyl-L-karnitin a Carnipure, což je ochranná známka suroviny.</li>'
          '<li><strong>Kapsaicin a extrakty z koření</strong> se přidávají kvůli pocitu tepla.</li>'
          '<li><strong>Synefrin a podobné látky</strong> jsou stimulanty. Jejich užívání v různých zemích podléhá omezení a při kombinaci s kofeinem hrozí vyšší zátěž. Pokud si nejste jistí, produkty s těmito složkami vynechte.</li>'
          '<li><strong>Vitamíny a minerály</strong> doplňují složení, nejsou ale hlavním důvodem koupě.</li></ul>'
          '<p>Víc než názvy vypovídá množství. Hodnoty v tabulce na obalu se vztahují k doporučené denní dávce, a tu nepřekračujte. Pozor také na ty doplňky, které nuceně spojují desítky složek v tzv. proprietární směsi bez uvedení množství jednotlivých látek.</p>'
          '<h2>Formy: kapsle, shoty, prášek</h2>'
          '<p>Forma ovlivňuje pohodlí a způsob dávkování. Kapsle jsou nejrozšířenější a snadno se přenášejí, tablety bývají levnější na dávku a těžší na polykání. Tekuté shoty a ampule mají dávku v jednom balení, často s příchutí, kterou někdo nesnáší. Prášky se rozpouštějí ve vodě a hodí se, pokud nechcete polykat kapsle. Všechny formy se užívají podle návodu a s dostatkem tekutin. U karnitinu v tekuté formě pamatujte na to, že obsahuje také cukry nebo sladidla.</p>'
          '<p>Veganské produkty se označují přímo v názvu, například veganské kapsle nebo tablety. Pokud držíte vegetariánskou či veganskou dietu, ověřte na etiketě také obal kapsle, aby neobsahoval želatinu.</p>'
          '<h2>Jak se k doplňku postavit: obecná upozornění</h2>'
          '<p>Spalovače tuků nepatří do výbavy pro každého. Obecně platí několik pravidel.</p>'
          '<ul><li>Před užíváním se poraďte s lékařem nebo lékárníkem, zejména máte-li problémy se srdcem, krevním tlakem, štítnou žlázou, spánkem nebo úzkostmi.</li>'
          '<li>Nepoužívejte je v těhotenství a při kojení, ani u dětí a mladistvých.</li>'
          '<li>Kofein může zhoršit spánek, proto produkty s kofeinem neužívejte pozdě odpoledne.</li>'
          '<li>Neužívejte více produktů se stejnou složkou najednou, například spalovač spolu s předtréninkovým boosterem s kofeinem.</li>'
          '<li>Při nevolnosti, bušení srdce, závratích nebo třesu užívání přerušte.</li>'
          '<li>Dodržujte doporučené dávkování a uchovávejte mimo dosah dětí.</li></ul>'
          '<p>Doplňky stravy nenahrazují pestrou stravu. Shrnuto: nejdůležitější je vyvážený jídelníček, pohyb a spánek. Pokud chcete redukovat hmotnost zdravě, konzultujte plán s lékařem nebo nutričním terapeutem.</p>'
          '<h2>Jak číst etiketu a porovnávat nabídky</h2>'
          '<p>Při srovnání dvou produktů se nedívejte jen na cenu za balení. Důležitý je počet dávek v balení, množství účinné látky v jedné dávce a doporučený způsob užití. Balení po 60 nebo 90 kapslích může vydržet půl měsíce, nebo třikrát déle podle toho, kolik kapslí denně doporučuje výrobce. Zkontrolujte také datum minimální trvanlivosti, údaje o výrobci a upozornění na alergeny. Zdůrazněná slova na přední straně, jako extrémně silný, nejsou doklad kvality. Hodnotu má jen složení na zadní straně a certifikace výrobce.</p>'
          '<p>Produkty jednoho typu se liší hlavně složením a přídavky, přesto se dají řadit do podobných kategorií. Například Amix X-Fat, Penco Fat Burner nebo Nero Fat Burner patří mezi kapslové směsi, zatímco Extrifit FB-3 je tekutý shot. Pro rovnou volbu kvalitní suroviny sledujte samostatné karnitiny od značek Penco, GymBeam nebo Natural Protein.</p>'
          '<h2>Spalovače tuků a ostatní výživa</h2>'
          '<p>Doplněk se zapojuje do širšího systému. Příjem bílkovin pokrývají <a href="/proteiny/">proteiny</a> a <a href="/proteinove-tycinky-a-snacky/">proteinové tyčinky a snacky</a>, při tréninku pomáhají <a href="/iontove-napoje/">iontové nápoje</a> a <a href="/energeticke-gely-a-tycinky/">energetické gely a tyčinky</a> dodají energii při dlouhé zátěži. Pestrý přísun mikroživin podpoří <a href="/vitaminy-a-mineraly/">vitaminy a minerály</a>, regeneraci pak například <a href="/kreatin/">kreatin</a>. Pro méně obvyklé doplňky se hodí <a href="/ostatni-doplnky-stravy/">ostatní doplňky stravy</a>. K tréninku patří také nutnost mít vhodnou obuv a oblečení, například <a href="/bezecka-obuv/">běžeckou obuv</a>.</p>'
          '<p>Z hlediska trénování se redukce hmotnosti opírá o dlouhodobý mírný deficit energie, silový trénink a dostatek pohybu v běžném dni. Ani nejlepší doplněk to nenahradí. Pro začátek nepotřebujete žádný doplněk: pomůže pravidelný režim, dostatek spánku a pitný režim.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li><strong>Očekávání zázraku.</strong> Doplněk nedělá práci za vás. Bez změn v jídle a pohybu nemá smysl.</li>'
          '<li><strong>Kombinování více stimulantů.</strong> Kofein se v kávě, boosterech a spalovačích sčítá, což zvyšuje riziko nepříjemných účinků.</li>'
          '<li><strong>Překročení dávky.</strong> Víc neznamená lépe, doporučená denní dávka je hranice.</li>'
          '<li><strong>Užívání na dlouhou dobu bez přestávky.</strong> Vhodnost dlouhodobého užívání konzultujte s lékařem.</li>'
          '<li><strong>Nákup podle jediného nadšeného hodnocení.</strong> Důvěřujte složení a transparentnosti výrobce.</li>'
          '<li><strong>Ignorování alergií.</strong> Zkontrolujte etiketu na alergeny a složky v kapsli.</li></ul>',
    faq=[('Co je to spalovač tuků?', 'Doplněk stravy, obvykle směs rostlinných extraktů a kofeinu, nebo samostatný karnitin. Prodává se jako pomocník při redukci hmotnosti, ale nenahradí pohyb ani jídelníček a nemá léčebný účinek.'),
         ('Je L-karnitin spalovač tuků?', 'L-karnitin je látka, kterou si tělo vytváří samo a přijímáme ji i z masa. Obchody ho zařazují mezi spalovače, ale jde o samostatný typ doplňku. Jak ho užívat, se informujte u lékaře.'),
         ('Mohu užívat spalovač tuků v těhotenství?', 'Ne. V těhotenství a při kojení se obecně doporučuje se doplňkům s kofeinem a stimulanty vyhnout. Nevhodné jsou i pro děti a mladistvé.'),
         ('Kdy je lepší spalovač užívat?', 'Řiďte se návodem výrobce. Produkty s kofeinem se obvykle neužívají večer, aby neovlivnily spánek.'),
         ('Jak se liší kapsle, tablety a shoty?', 'Kapsle a tablety se polykají a jsou praktické na cesty. Shoty mají dávku v ampuli a bývají ochucené, někdy obsahují cukr nebo sladidla. Zvolte formu, která vám vyhovuje.'),
         ('Lze spalovač kombinovat s předtréninkovým boosterem?', 'Obojí často obsahuje kofein, takže celková dávka může být vysoká. Raději použijte jeden z produktů a poraďte se s lékařem.'),
         ('Co znamená proprietární směs?', 'Směs složek bez uvedení množství jednotlivých látek. Nelze tedy posoudit dávku, a proto je lepší vybírat produkty s plně rozepsaným složením.'),
         ('Existují spalovače bez kofeinu?', 'Ano, najdete nestimulační směsi s rostlinnými extrakty bez kofeinu. Přesto si přečtěte etiketu a ověřte u lékaře, zda se hodí.'),
         ('Jak dlouho se doplněk užívá?', 'Doba užívání se řídí návodem a radou lékaře. Neužívejte je dlouhodobě bez konzultace a dodržujte doporučené dávkování.'),
         ('Co dělat při nevolnosti nebo bušení srdce?', 'Užívání přerušte a poraďte se s lékařem. Při silných obtížích vyhledejte lékařskou pomoc.')],
)

# ------------------------------------------------------------------ trekingova-elektrokola
NEW['trekingova-elektrokola'] = dict(long=True,
    title='Trekingová elektrokola: motor, baterie, výbava',
    desc='Trekingová a cestovní elektrokola s nosičem, blatníky a světly. Jak vybrat motor, baterii, rám a výbavu a porovnat nabídky českých obchodů.',
    intro='<p>Trekingové elektrokolo je univerzální cestovní stroj: pohodlná poloha, nosič, blatníky, světla a motor, který zvládne i delší výlety s kopci a zavazadly. Vedle klasických modelů s vysokým rámem zahrnuje kategorie také nízké průchozí rámy a elektrokola na pomezí treku a crossu. Sporteka sbírá nabídky českých obchodů k jednotlivým modelům, a pokud se barva nebo velikost rámu liší, ukáže, ve kterém obchodě je kolo skladem.</p>'
          '<p>V nabídce najdete značky ' + B(('specialized', 'Specialized'), ('trek', 'Trek'), ('devron', 'Devron'), ('corwin', 'Corwin'), ('rockrider', 'Rockrider'), ('rcb', 'RCB'), ('hitway', 'Hitway'), ('urbanbiker', 'Urbanbiker'), ('evercross', 'Evercross')) +
          '. Pro dojíždění po městě se hodí <a href="/mestska-elektrokola/">městská elektrokola</a>, do terénu <a href="/horska-elektrokola/">horská elektrokola</a> a pro každodenní jízdu bez motoru <a href="/trekingova-kola/">trekingová kola</a>.</p>',
    guide='<h2>Čím se trekingové elektrokolo liší od ostatních</h2>'
          '<p>Trekingové elektrokolo spojuje komfort městského kola s výbavou pro cestování. Základ tvoří pevný rám, odpružená vidlice nebo odpružená sedlovka, blatníky, nosič a osvětlení napájené z hlavní baterie. Díky tomu se hodí na dlouhé jízdy, cyklostezky i dojíždění do práce, když se potřebuje převézt zavazadlo.</p>'
          + T(['Typ elektrokola', 'Charakteristika', 'Hodí se pro'], [
              ['Trekingové', 'nosič, blatníky, světla, pohodlná poloha', 'výlety, cestování, dojíždění s nákladem'],
              ['Městské', 'nízká váha, jednodušší výbava, často nízký nástup', 'krátké trasy po městě'],
              ['Crossové', 'sportovnější poloha, širší pláště do terénu', 'zpevněné i lesní cesty'],
              ['Horské', 'odpružení, hrubý vzorek plášťů, zdvih', 'jízdu v lese a terénu'],
              ['Nákladní', 'prodloužený rám, velká nosnost', 'rodiny, převoz nákladu'],
              ['Skládací', 'menší kola, nízká hmotnost, sklápění', 'kombinaci s dopravou a malými prostory']]) +
          '<p>Kategorie obsahuje i modely s nižší výbavou nebo výraznějším sportovním charakterem. Například řady Specialized Turbo Vado a Tero se profilují jako univerzální a rychlejší elektrokola, kdežto Trek Powerfly s odpružením míří spíš do terénu. Základní trekingové modely bez motoru najdete v kategorii <a href="/trekingova-kola/">trekingová kola</a>.</p>'
          '<h2>Motor: střed, zadní kolo, přední kolo</h2>'
          '<p>Motor je srdce elektrokola a ovlivňuje chování při jízdě.</p>'
          '<ul><li><strong>Středový motor</strong> je u šlapacího středu. Nízké těžiště a rozložení váhy dávají přirozenou jízdu a dobré stoupání. Využívá převodovku kola, takže při změně rychlosti pracuje efektivněji. Tato koncepce převažuje u kvalitnějších trekingových kol.</li>'
          '<li><strong>Zadní náboj</strong> je jednodušší a hodí se na rovinu a mírné stoupání. Kolo je ale vzadu těžší a při defektu se výměna komplikuje.</li>'
          '<li><strong>Přední náboj</strong> je u základních modelů, jízda může být nejméně přirozená, protože motor táhne přední kolo.</li></ul>'
          '<p>Pomoc se obvykle dělí do několika režimů, od úsporného po silný. Silnější režimy zkracují dojezd. Mnoho motorů má také tlačící asistent pro vedení kola do schodů a svahu. Důležitý je krouticí moment, který popisuje, jak silně motor pomáhá při rozjezdu a v kopci. Pomoc se v Evropě vypíná při překročení stanovené rychlosti, typicky 25 km/h, nad ni jedete sami.</p>'
          '<h2>Baterie, dojezd a nabíjení</h2>'
          '<p>Kapacita se udává ve watthodinách (Wh). Čím větší číslo, tím větší zásoba energie. Skutečný dojezd ale závisí na řadě faktorů: hmotnosti jezdce a nákladu, terénu, větru, teplotě, tlaku v pláštích a zvoleném režimu pomoci. Jednoznačné číslo dojezdu proto nikdo nezaručí, výrobcovy údaje berte jako orientační. V nabídce najdete modely s nižší kapacitou kolem 250 až 374 Wh, které vyhoví na krátké trasy, i výkonnější řešení.</p>'
          + T(['Využití', 'Vhodná volba baterie'], [['krátké trasy po městě a rovině', 'menší kapacita stačí'], ['celodenní výlety a kopce', 'větší kapacita nebo druhá baterie'], ['cestování s nákladem', 'větší kapacita a středový motor'], ['jízda v zimě', 'kapacita s rezervou, protože mráz ubírá výkon']]) +
          '<p>Baterii nabíjejte při pokojové teplotě a nenechávejte ji dlouho zcela vybitou. Při delším skladování ji ponechte zhruba v polovině nabití a v suchu. Odnímatelná baterie se dobíjí v bytě, integrovaná v rámu vypadá čistěji, ale vyžaduje nabíjení přímo na kole. Při dlouhodobém nepoužívání se řiďte návodem výrobce. Nikdy nepoužívejte cizí nabíječku a poškozenou baterii vyřaďte.</p>'
          '<h2>Rám, velikost a poloha</h2>'
          '<p>Trekingové kolo má obvykle vzpřímenou polohu, která šetří záda a ruce. Rámy se vyrábí v klasické vysoké verzi a v nízké průchozí, která usnadňuje nastupování a hodí se pro jezdce s menší pohyblivostí i pro jízdu s nákladem. Jízdní vlastnosti obou verzí jsou podobné, vyšší tuhost nabízí klasický rám. Pro ženy a nižší jezdce se hodí také <a href="/damska-elektrokola/">dámská elektrokola</a>.</p>'
          + T(['Výška postavy', 'Orientační velikost rámu'], [['155–165 cm', 'S (kolem 17 palců, 43–46 cm)'], ['165–175 cm', 'M (kolem 19 palců, 48–50 cm)'], ['175–185 cm', 'L (kolem 21 palců, 52–54 cm)'], ['nad 185 cm', 'XL (kolem 23 palců, 56 cm a víc)']]) +
          '<p>Velikost kola bývá 26, 27,5 nebo 28 palců, přičemž 28" je u trekingů nejběžnější. Hodnoty v tabulce jsou orientační a u značek se liší. Nastavte výšku sedla tak, aby noha při spodní poloze pedálu zůstala mírně pokrčená, a řídítka tak, abyste seděli vzpřímeně.</p>'
          '<h2>Výbava pro cestování</h2>'
          '<p>Hlavní rozdíl proti jiným elektrokolům tvoří kompletní výbava z výroby. Zkontrolujte ji před nákupem.</p>'
          '<ul><li><strong>Nosič</strong> se zatížitelností uvedenou výrobcem. Pro brašny na cestování využijete kategorii <a href="/cyklo-tasky-a-nosice/">cyklo tašky a nosiče</a>.</li>'
          '<li><strong>Blatníky</strong> chrání před blátem a vodou, náhradní najdete v kategorii <a href="/cyklo-blatniky/">cyklo blatníky</a>.</li>'
          '<li><strong>Světla</strong> napájená z hlavní baterie jsou praktická, další zdroje najdete v <a href="/cyklo-svetla/">cyklo světlech</a>.</li>'
          '<li><strong>Odpružená vidlice nebo sedlovka</strong> tlumí nárazy na dlouhých trasách.</li>'
          '<li><strong>Stojánek</strong> usnadňuje nakládání.</li>'
          '<li><strong>Brzdy</strong>: hydraulické kotoučové brzdy jsou na těžším kole výhodou. Více v <a href="/cyklo-brzdy/">cyklo brzdách</a>.</li>'
          '<li><strong>Zámek</strong> je nezbytnost, elektrokolo je lákavý cíl krádeže. Vyberte ze <a href="/cyklo-zamky/">cyklo zámků</a>.</li></ul>'
          '<p>K bezpečné jízdě patří také <a href="/mestske-cyklohelmy/">městská cyklohelma</a>, <a href="/cyklisticke-rukavice/">rukavice</a> a funkční oblečení z kategorie <a href="/cyklisticke-obleceni/">cyklistické oblečení</a>. Při zavazadlech na nosiči myslete na to, že těžiště kola se mění, a brzdná dráha prodlužuje.</p>'
          '<h2>Převody a komponenty</h2>'
          '<p>Trekingová elektrokola mají řazení s deseti až dvanácti rychlostmi, případně nábojovou převodovku s menšími nároky na údržbu. Nábojová převodovka je uzavřená a odolná, ale těžší. U středových motorů pracuje řetěz pod větším zatížením, takže se rychleji opotřebuje. Proto ho pravidelně kontrolujte a mažte, viz <a href="/cyklo-pohon/">cyklo pohon</a>. Pláště mají ochranný pás proti defektům, tlak v nich je důležitý pro dojezd i pohodlí.</p>'
          '<h2>Péče, servis a legislativa</h2>'
          '<p>Elektrokolo zatěžuje komponenty víc než běžné kolo, takže servis je častější. Kontrolujte řetěz, kazetu, brzdové destičky a pláště. Motor ani baterii sami neotevírejte, o jejich údržbu se stará autorizovaný servis. Kolo myjte jemným proudem vody, ne tlakovou myčkou, a baterii při mytí sundejte nebo zakryjte kontakty. Další pomůcky najdete v kategorii <a href="/cyklo-udrzba/">cyklo údržba</a> a <a href="/cyklo-pumpy-a-naradi/">cyklo pumpy a nářadí</a>.</p>'
          '<p>Z hlediska pravidel se elektrokolo do určité rychlosti a výkonu motoru považuje za jízdní kolo. Rychlejší modely a modely s tlačítkem plynu mohou spadat do jiné kategorie vozidel a vyžadovat registraci nebo řidičský průkaz. Před koupí si ověřte, zda produkt splňuje podmínky vašeho využití. Pro přepravu těžkého elektrokola na auto je nutné zvolit nosič s odpovídající nosností, viz <a href="/cyklo-nosice-na-auto/">cyklo nosiče na auto</a>.</p>'
          '<h2>Časté chyby při koupi</h2>'
          '<ul><li><strong>Podcenění hmotnosti.</strong> Elektrokolo je těžší než běžné, ověřte, zda ho zvládnete vynést po schodech nebo naložit na nosič.</li>'
          '<li><strong>Příliš malá baterie.</strong> Kapacita se hodí odhadnout podle nejdelší trasy a s rezervou.</li>'
          '<li><strong>Špatná velikost rámu.</strong> Na dlouhých trasách se projeví bolestí zad a zápěstí.</li>'
          '<li><strong>Nákup bez servisní sítě.</strong> Zjistěte, kdo vám kolo servisuje a zda jsou dostupné náhradní díly.</li>'
          '<li><strong>Zanedbání zámku.</strong> Elektrokolo patří mezi krádeží ohrožené zboží.</li>'
          '<li><strong>Výběr podle samotného výkonu.</strong> Důležitější než číslo v katalogu je komfort a servis.</li></ul>'
          '<h2>Porovnání nabídek</h2>'
          '<p>Modely se prodávají v různých barvách a velikostech a stejné kolo může mít v různých obchodech jiný název. Specialized Turbo Vado se proto objevuje s dovětky jako SL nebo Step-Through, což označuje odlehčenou a nízkou verzi. Porovnáním obchodů na Sportece zjistíte, kde je skladem vaše velikost a barva, a vyhnete se nákupu kola, které je potřeba objednávat několik týdnů.</p>',
    faq=[('Čím se trekingové elektrokolo liší od městského?', 'Má nosič, blatníky a světla od výrobce, odolnější rám a obvykle silnější baterii. Je určené pro delší výlety a cestování, městské kolo spíš pro krátké trasy.'),
         ('Jaký motor je lepší, středový, nebo v zadním náboji?', 'Středový motor dává přirozenější jízdu, lepší rozložení váhy a lepší stoupání. Zadní motor je jednodušší a vyhoví na rovinu a mírný terén.'),
         ('Jakou baterii zvolit?', 'Podle nejdelší trasy a terénu. Větší kapacita znamená delší dojezd, ale i vyšší hmotnost. Počítejte s rezervou, protože v zimě a při protivětru dojezd klesá.'),
         ('Jak daleko dojedu na jedno nabití?', 'Přesné číslo nelze zaručit, závisí na hmotnosti jezdce, terénu, větru, teplotě a režimu pomoci. Údaje výrobců jsou orientační.'),
         ('Jakou velikost rámu zvolit?', 'Podle výšky postavy a délky nohou. Orientačně S pro 155–165 cm, M pro 165–175 cm a L pro 175–185 cm. Při váhání se řiďte tabulkou konkrétní značky.'),
         ('Je lepší nízký, nebo klasický rám?', 'Nízký průchozí rám usnadňuje nastupování a nakládání, klasický je tužší. Pro jízdu bez omezení pohyblivosti jsou oba vhodné.'),
         ('Jak se starat o baterii?', 'Nabíjejte ji při pokojové teplotě, nenechávejte dlouho vybitou a při skladování ji udržujte zhruba v polovině nabití a v suchu. Používejte jen originální nabíječku.'),
         ('Mohu mýt elektrokolo vodou?', 'Ano, jemným proudem a bez tlakové myčky. Chraňte kontakty baterie a motor, nikdy nemiřte vodu přímo do ložisek.'),
         ('Potřebuji řidičský průkaz nebo registraci?', 'Běžné elektrokolo s pomocí do stanovené rychlosti se považuje za kolo. Rychlejší modely a modely s plynem mohou spadat do jiné kategorie, proto si ověřte parametry před koupí.'),
         ('Co s elektrokolem v zimě?', 'Jezděte, ale počítejte s nižším dojezdem. Baterii skladujte v teple, pláště mívejte vhodně nahuštěné a po jízdě po soli kolo opláchněte.')],
)


# ---- extensions (same wave)
NEW['silnicni-kola']['intro'] = NEW['silnicni-kola']['intro'].replace('<p>V kategorii najdete', '<p>Při výběru počítejte i s tím, že silniční kolo je kompletní systém: rám, převody, kola, brzdy a poloha jezdce se musí vzájemně doplňovat.</p><p>V kategorii najdete', 1)
NEW['silnicni-kola']['guide'] += (
    '<h2>Jak se jezdí na silničním kole poprvé</h2>'
    '<p>Prvních pár výjezdů je dobré věnovat zvykání na novou polohu. Řídítka jsou níž než u městského kola, ruce se střídají mezi horní částí, brzdovými páčkami a spodním obloukem. Na páčkách sedíte nejčastěji, spodní oblouk se využívá ve sjezdu a při sprintu. Brzdění zkoušejte předem na rovině, protože kotoučové brzdy reagují ostřeji než ráfkové a při prudkém zabrzdění přední brzdou se kolo snadno naklopí dopředu.</p>'
    '<p>Používejte vždy obě brzdy, přední dá větší část brzdného účinku, zadní stabilizuje směr. V zatáčce brzdění dokončete ještě před vjezdem, ne uprostřed oblouku. Při jízdě ve skupině držte stálý odstup, nebrzděte prudce a signalizujte překážky na vozovce. Při šlapání ve stoupání volte nižší převod dřív, než je nutný, aby se nohy příliš nezatěžovaly.</p>'
    '<h2>Silniční kolo a trénink</h2>'
    '<p>Pravidelná jízda zlepšuje kondici postupně. Začátečník může začít krátkými trasami do hodiny, s plynulým tempem, při kterém se dá ještě mluvit. Pak se prodlužuje délka a později přidávají intervaly. Měření pomáhá hrudní pás s tepem nebo wattmetr, který ukazuje výkon v pedálech. Wattmetr se montuje do klik, pedálů nebo do náboje, součásti kola Quarq v nabídce patří právě do této skupiny. Pro sledování trasy, rychlosti a tepu slouží <a href="/cyklo-computery/">cyklo computery</a>.</p>'
    '<p>Nezapomeňte na pitný režim a výživu. Na trasách delších než hodinu si vezměte láhev a jednoduchou energii v kapse dresu. Po výjezdu doplňte bílkoviny a sacharidy, výběr nabízejí <a href="/proteinove-tycinky-a-snacky/">proteinové tyčinky a snacky</a>.</p>'
    '<h2>Bezpečnost na silnici</h2>'
    '<p>Silniční kolo je rychlé a vozovka sdílená s auty. Nosit helmu a světla je základ, i ve dne se vyplatí blikačka vzadu. Oblečení volte výrazné barvy s reflexními prvky. Držte se vpravo, ale ne těsně u okraje, kde bývá štěrk a díry. Před odbočením se ohlédněte a dejte znamení rukou. Za horšího počasí a při nízké viditelnosti raději jízdu odložte. Mokrý asfalt prodlužuje brzdnou dráhu a bílé čáry i kanály jsou kluzké.</p>'
    '<h2>Přeprava, uskladnění a pojištění</h2>'
    '<p>Kolo uchovávejte v suchu a v teple, nejlépe zavěšené na stěně nebo ve stojanu. Při přepravě na střeše auta pamatujte na výšku, třeba při vjezdu do garáže. Pro delší cesty se hodí kufr na kolo nebo možnost kolo rozložit. Z hlediska krádeží nepoužívejte jen jeden tenký zámek, na parkování ve městě kombinujte dva různé typy a kolo nikdy nenechávejte zamčené celou noc na ulici. Hodnotnější kolo se vyplatí zahrnout do domácího pojištění nebo se informovat o samostatném pojištění.</p>'
    '<h2>Silniční kolo pro děti a ženy</h2>'
    '<p>Menší rámy se vyrábějí v rozměrech od zhruba 44 cm, často s užšími řídítky a kratšími klikami. Dámské geometrie mívají kratší horní trubku a užší řídítka, přesto jde spíš o doporučení než o pravidlo. Podstatné je, aby se jezdec pohodlně dosáhl na páčky a nemusel se příliš natahovat. Pokud hledáte kolo pro dospívajícího, který ještě roste, zvažte <a href="/detska-kola/">dětská kola</a> a až později přejděte na plnohodnotný silničák. Pro rodinné výlety je pohodlnější <a href="/krosova-kola/">krosové kolo</a>.</p>'
)

NEW['trekingova-elektrokola']['intro'] = NEW['trekingova-elektrokola']['intro'].replace('<p>V nabídce najdete', '<p>Při výběru sledujte především středový nebo zadní motor, kapacitu baterie, kvalitu brzd a výbavu, která z kola dělá opravdový cestovní nástroj.</p><p>V nabídce najdete', 1)
NEW['trekingova-elektrokola']['guide'] += (
    '<h2>Jak plánovat delší výlet na elektrokole</h2>'
    '<p>Před vyjetím si spočítejte, kolik kilometrů a převýšení vás čeká, a porovnejte to s kapacitou baterie. Důležité je počítat s rezervou, takže plánujte raději kratší etapy a nespoléhejte na to, že pojedete celou dobu v nejsilnějším režimu. Do kopce se vyplatí zařadit nižší převod a vyšší kadenci. Motor tak pracuje efektivněji a baterie vydrží déle. Na rovině a z kopce zvolte slabší pomoc nebo ji vypněte.</p>'
    '<p>Na delší trasy pomáhá mapa nebo navigace s plánováním cyklotras a nabíjecích bodů. Řada kaváren, penzionů a kempů nabíjení umožňuje, předem se ale zeptejte. Nabíječku a případně adaptér sbalte s sebou. Pamatujte, že ve větru a ve stoupání se dojezd zkracuje výrazněji než na rovině.</p>'
    '<h2>Zavazadla a převoz nákladu</h2>'
    '<p>Zatížitelnost nosiče uvádí výrobce a nesmí se překročit, jinak se zhorší vedení kola a může prasknout konstrukce. Těžší věci ukládejte nízko a rovnoměrně na obě strany, aby se kolo nenaklánělo. Nepřipevňujte těžké batohy na řídítka, kde ovlivňují řízení. Na nákupy se hodí koš a brašny, na dlouhé cesty dvojice bočních brašen. Zavazadla na kole zvyšují brzdnou dráhu, proto jezděte opatrněji a využívejte kvalitní brzdy. Výběr najdete v <a href="/cyklo-tasky-a-nosice/">kategorii cyklo tašky a nosiče</a>.</p>'
    '<h2>Elektrokolo pro seniory a méně zdatné jezdce</h2>'
    '<p>Pro starší jezdce a lidi po zdravotních potížích je elektrokolo způsob, jak se vrátit k pohybu. Hodí se nízký průchozí rám, sedlo s pohodlnou vložkou, vzpřímená poloha a motor s plynulým náběhem. Důležitá je také nižší hmotnost a stabilita kola při rozjezdu. Před koupí si kolo vyzkoušejte, případně zvolte model s tlačícím asistentem. Při zdravotních omezeních se o vhodnosti pohybu poraďte s lékařem. Pro větší pohodlí zvažte také <a href="/damska-elektrokola/">dámská elektrokola</a> s nízkým nástupem.</p>'
    '<h2>Pláště, tlak a pohodlí</h2>'
    '<p>Trekingové pláště mívají střední šířku a mírný vzorek, vhodný na asfalt i zpevněné cesty. Pláště s ochranným pásem proti defektům jsou pro cestování praktické. Tlak vzduchu ovlivňuje dojezd, pohodlí i brzdění. Příliš nízký tlak zvyšuje odpor a hrozí defekt, příliš vysoký ubírá pohodlí. Doporučený rozsah najdete na boku pláště, upravujte ho podle hmotnosti jezdce a nákladu. Hodí se kvalitní pumpa s manometrem, nabídku najdete v <a href="/cyklo-pumpy-a-naradi/">pumpách a nářadí</a>.</p>'
    '<h2>Doprava elektrokola a úschova</h2>'
    '<p>Elektrokolo je těžké a při zvedání na nosič snadno dojde ke zranění zad nebo poškození lakované plochy. Před nakládáním sundejte baterii a displej, ulehčíte váhu a ochráníte citlivé části. Zámek vždy provlékněte rámem a kolem a kolo připoutejte k pevnému objektu. Doma ho uchovávejte v suchu a při delším stání pravidelně kontrolujte nabití baterie. Pro přepravu na auto je nutné, aby nosič měl povolenou nosnost nejméně rovnou hmotnosti kola.</p>'
)

NEW['jezdecke-kalhoty']['intro'] = NEW['jezdecke-kalhoty']['intro'].replace('<p>V kategorii najdete', '<p>Správný výběr závisí na tom, zda jezdíte rekreačně, trénujete pravidelně, nebo startujete na závodech, a na ročním období.</p><p>V kategorii najdete', 1)
NEW['jezdecke-kalhoty']['guide'] += (
    '<h2>Jaké kalhoty podle disciplíny</h2>'
    '<p>Každá disciplína klade na kalhoty trochu jiné nároky. Ve skokové jízdě jezdec často stojí ve třmenech a nese váhu na kolenou, proto se hodí kolenní grip, který drží nohu u sedla. V drezúře jezdec sedí hluboko a potřebuje stálý kontakt se sedlem, takže se hodí plný sed s protiskluzovým potiskem na sedací části a ploché švy. V terénu a při vyjížďkách kalhoty snášejí déšť, trní a časté nasedání a slézání, a hodí se tedy odolnější materiál. Pro práci ve stáji, kde se nesedí na koni, je praktičtější obyčejná tmavá elasticita než drahé závodní rajtky.</p>'
    '<h2>Jak kalhoty sedí, když je zkoušíte</h2>'
    '<p>Při zkoušení kalhoty obujte do boty, ve kterých budete jezdit, a posaďte se do podřepu nebo si sedněte na židli s kolenem pokrčeným do pravého úhlu. Sed nesmí tlačit v rozkroku a šev na vnitřní straně stehen nesmí škrtit. Při předklonu se pas nemá stahovat dolů, a nohavice nemají vyjíždět vzhůru. Pokud je to možné, vyzkoušejte kalhoty i v sedle, protože v obchodě poznáte jen část.</p>'
    '<h2>Barvy a vzhled</h2>'
    '<p>Černé, tmavě modré a šedé kalhoty se nejméně špiní a hodí se na trénink. Světlé a bílé tóny jsou běžné na závodech, kde se předpokládá formální vzhled, ale vyžadují častější praní a pozornost při sezení na mokrém sedle. Vzor a potisk bývají u dětských modelů, často v barvách značky. Při volbě barvy myslete i na to, aby kalhoty ladily s vestou a sedlovou dečkou, protože jezdecký styl bývá sladěný.</p>'
    '<h2>Kalhoty pro rostoucí děti</h2>'
    '<p>Děti rostou rychle, proto se vyplatí kupovat kalhoty s pružným pasem a delší nohavicí, kterou lze první sezonu podvinout. Pro začátek stačí jeden pár univerzálních kalhot s částečným gripem, další se doplní po zjištění, jak často dítě jezdí. Starší děti si často rády vyberou barvu samy, což zvyšuje chuť nosit je. Dbejte na to, aby se švy v rozkroku nedřely, protože děti jinak odmítají nasedat. Menší jezdci často začínají v <a href="/jezdecke-helmy/">jezdecké helmě</a> a bezpečné obuvi dříve než v kalhotách, a právě tyto dvě části výbavy se nesmí šetřit.</p>'
    '<h2>Opravy a prodloužení životnosti</h2>'
    '<p>Když se začne sed odlepovat nebo trhat, nemusí to znamenat konec. Drobná poškození se dají zašít, ale při zásahu do gripu je výsledek nejistý, a kalhoty pak slouží spíš na práci ve stáji. Dbejte na to, aby se pasy a gumy nenatahovaly, a kalhoty střídejte. Vyřazené kalhoty využijte na práci v zahradě nebo na stájovou činnost. Pravidelné čištění gripu jemným kartáčkem prodlužuje jeho funkci.</p>'
)

NEW['spalovace-tuku']['intro'] = NEW['spalovace-tuku']['intro'].replace('<p>Najdete zde', '<p>Informace na této stránce jsou obecné a nenahrazují radu lékaře ani nutričního terapeuta.</p><p>Najdete zde', 1)
NEW['spalovace-tuku']['guide'] += (
    '<h2>Mýty o spalování tuku</h2>'
    '<p>Kolem tématu kolují zjednodušená tvrzení. Tělo nelze přimět ubírat tuk z konkrétního místa, takže cvičením na břicho se břicho samo nezmenší. Redukce tělesného tuku probíhá celkově a závisí na dlouhodobém rozdílu mezi příjmem a výdejem energie. Rychlé hubnutí o mnoho kilogramů za týden se obvykle týká vody, ne tuku. Marketingová slova jako extrémní nebo okamžitý účinek neodpovídají tomu, co o výživě vědí odborníci. Proto je lepší hledat informace u lékaře, dietologa nebo v důvěryhodných zdrojích a ne na obalu.</p>'
    '<h2>Pro koho spalovače nejsou</h2>'
    '<p>Doplňky tohoto typu nejsou určeny každému. Nehodí se pro děti a dospívající, těhotné a kojící ženy, lidi s onemocněním srdce a cév, vysokým tlakem, problémy se štítnou žlázou nebo poruchami spánku a úzkosti. Pozor mají dávat také lidé užívající léky, protože složky doplňků s nimi mohou reagovat. Neužívejte je ani při poruchách příjmu potravy. Také sportovci, kteří se podrobují antidopingovým kontrolám, by měli etiketu zkontrolovat a poradit se s odborníkem, protože některé složky mohou být na seznamu zakázaných látek.</p>'
    '<h2>Co je lepší než kupovat další doplněk</h2>'
    '<p>Z praktického hlediska se redukce opírá o několik jednoduchých návyků. Jíst pravidelně a z kvalitních surovin, zařadit dostatek zeleniny, bílkovin a vlákniny, omezit sladké nápoje a vysoce zpracované potraviny. Pohybovat se každý den, kombinovat vytrvalostní pohyb se silovým tréninkem a dopřát si 7 až 9 hodin spánku. Dostatek spánku souvisí s chutí k jídlu, a proto se nevyplatí šetřit na něm. Pokud plánujete zásadní změnu režimu, přizpůsobte ji svému zdraví a konzultujte ji s odborníkem.</p>'
    '<p>Na běžné aktivity se hodí kvalitní vybavení, ať už jde o <a href="/bezecke-boty/">běžecké boty</a>, nebo o <a href="/leginy/">legíny</a> na cvičení. Motivaci pomáhá udržet jednoduchý deník pohybu a jídla, který ukáže skutečné návyky.</p>'
    '<h2>Skladování a trvanlivost</h2>'
    '<p>Doplňky uchovávejte v původním obalu na suchém a chladném místě, mimo přímé slunce a mimo dosah dětí. Po otevření dobře uzavřete víčko, kapsle a tablety jsou citlivé na vlhkost. Tekuté shoty po otevření spotřebujte ihned. Nikdy nepoužívejte produkt po uplynutí data minimální trvanlivosti, a pokud se změní vůně, barva nebo konzistence, vyhoďte ho. Před cestou se zeptejte, zda si doplněk smíte vzít do letadla nebo přes hranice, protože pravidla se liší podle země.</p>'
)

NEW['spalovace-tuku']['guide'] += (
    '<h2>Jak si doplněk vybrat rozumně</h2>'
    '<p>Nejdřív si ujasněte, zda doplněk vůbec potřebujete. Pokud ano, začněte jednodušším produktem s krátkým a srozumitelným složením, ne největší směsí s tuctem stimulantů. Zkontrolujte, zda je na obalu česky uvedené složení, výrobce nebo distributor a upozornění pro rizikové skupiny. Produkty bez těchto údajů raději nekupujte. Pokud už užíváte kávu, energetické nápoje nebo předtréninkové boostery, spočítejte si celkový příjem kofeinu za den. Novinku zkoušejte po jednom produktu a sledujte, jak na ni reagujete, aby bylo jasné, co vám vyhovuje nebo vadí. Při pochybnostech se zeptejte lékárníka, který zná i vaše léky a může upozornit na nevhodné kombinace.</p>'
)
