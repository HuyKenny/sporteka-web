"""sporteka.cz — wave 23c (4. 11. 2026): long texts (>= 1650 words) for cyklo-computery, trekove-hole, cyklo-zvonky-a-zrcatka, golfove-hole.
General true facts only, no prices. Brands verified in the live catalogue."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ cyklo-computery
NEW['cyklo-computery'] = dict(long=True,
    title='Cyklopočítače a GPS navigace na kolo: jak vybrat',
    desc='Cyklopočítače, GPS navigace na kolo i držáky a ochranné kryty. Drátové, bezdrátové a GPS modely, srovnání funkcí a nabídek českých obchodů.',
    intro='<p>Cyklopočítač ukazuje rychlost, ujetou vzdálenost a čas jízdy, a jednodušší modely tím také končí. Chytřejší GPS přístroje zaznamenají trasu, vedou vás po nahrané stopě, spárují se se snímačem srdeční frekvence, kadence nebo výkonu a po jízdě pošlou data do aplikace. Sporteka porovnává nabídky českých obchodů u drátových i bezdrátových počítačů, u GPS navigací a také u doplňků, které k nim patří: držáků na řídítka, silikonových obalů, ochranných skel a fólií na displej nebo nabíjecích kabelů.</p>'
          '<p>V nabídce najdete značky ' + B(('cateye', 'Cateye'), ('garmin', 'Garmin'), ('sigma', 'Sigma'), ('igpsport', 'iGPSPORT'), ('bryton', 'Bryton'), ('cycplus', 'Cycplus'), ('rockbros', 'Rockbros'), ('west-biking', 'West Biking')) +
          '. K počítači se hodí <a href="/cyklo-svetla/">světla na kolo</a>, <a href="/cyklo-lahve-a-drzaky/">držáky telefonu</a> a <a href="/cyklo-prislusenstvi/">další příslušenství</a>.</p>',
    guide='<h2>Jaké druhy cyklopočítačů existují</h2>'
          '<p>Základní rozdíl je v tom, odkud počítač bere data. Jednoduchý model počítá otáčky kola podle magnetu u paprsku a snímače na vidlici, takže zná jen rychlost a vzdálenost. GPS přístroj polohu určuje ze signálu družic, mapuje trasu a rychlost počítá z pohybu, kolo proto nemusíte vybavovat žádným snímačem. Třetí cestou je telefon na řídítkách, který ale spotřebuje baterii a není stavěný na déšť a otřesy tak jako výrobek určený pro kolo.</p>'
          + T(['Typ', 'Co měří a jak', 'Hodí se pro'], [
              ['Drátový počítač', 'magnet a snímač spojené kabelem, rychlost a vzdálenost', 'městská a rekreační jízda, nejmenší nároky na údržbu'],
              ['Bezdrátový počítač', 'stejný princip, signál se přenáší vzduchem', 'kola, kde by kabel překážel nebo se špatně vedl'],
              ['GPS počítač', 'družicová poloha, záznam trasy, často i mapy', 'vyjížďky, tréninky, delší výlety a závody'],
              ['GPS navigace s mapou', 'barevný displej, navigace po trase, upozornění na odbočky', 'cykloturistika a neznámý terén'],
              ['Držák a ochrana', 'držák na řídítka nebo představec, kryt, sklo, fólie', 'chrání displej a posouvá počítač na vhodné místo']]) +
          '<h2>Drátový, nebo bezdrátový počítač</h2>'
          '<p>Drátový počítač je nenáročný a poměrně spolehlivý, protože signál neruší cizí vysílač a baterie v řídítkové jednotce vydrží dlouho. Nevýhodou je kabel, který se musí vést po vidlici a brzdovém bowdenu. U kol s odpruženou vidlicí nebo masivním rámem se pokládá hůř. Bezdrátový model kabel nepotřebuje, ale při montáži záleží na vzdálenosti vysílače od jednotky a na tom, aby mezi nimi nebyl kovový předmět. Pro běžnou jízdu po městě a po cyklostezkách obě varianty fungují dobře.</p>'
          '<p>Při montáži vždy zkontrolujte, že magnet míjí snímač v mezeře, kterou udává návod, a že je počítač nastaven na správný obvod kola. Bez zadání obvodu se rychlost i vzdálenost počítají chybně. Obvod najdete na tabulkách výrobce podle rozměru pláště, přesnější je ale změřit rozvinutí jednoho otočení kola s nahuštěnou gumou a jezdcem v sedle.</p>'
          '<h2>Co dělá GPS počítač navíc</h2>'
          '<p>GPS model zaznamenává trasu, nadmořskou výšku a převýšení, často i teplotu. Po jízdě data nahrajete do aplikace nebo na web, kde si ji můžete prohlédnout na mapě a porovnat s dřívějšími vyjížďkami. Kdo chce trénovat podle tepu, zapojí hrudní pás nebo čtečku na paži, kdo sleduje kadenci nebo výkon, přidá snímač v pedálu či v klice. Spojení se snímači většinou probíhá standardy ANT+ nebo Bluetooth, proto při výběru zkontrolujte, co přístroj a snímač spolu podporují.</p>'
          '<ul><li><strong>Navigace po trase.</strong> Přístroj vede po nahrané stopě a upozorní na odbočku. Tuto funkci oceníte při cestě mimo známé silnice.</li>'
          '<li><strong>Mapy.</strong> Lepší modely mají podrobné mapy cest a stezek, jednodušší jen ukazují čáru trasy bez okolí.</li>'
          '<li><strong>Upozornění z telefonu.</strong> Zobrazení hovoru nebo zprávy na displeji je pohodlné, vypíná se ale kvůli výdrži.</li>'
          '<li><strong>Výdrž baterie.</strong> Udává se v hodinách záznamu při běžném nastavení, silné podsvícení a mapa ji zkracují.</li>'
          '<li><strong>Odolnost.</strong> Hledejte krytí proti dešti a prachu, ať vás nezaskočí první přeháňka.</li></ul>'
          '<h2>Značky a rozdíly v nabídce</h2>'
          '<p>' + B(('garmin', 'Garmin')) + ' patří mezi největší výrobce GPS počítačů a v katalogu jsou k nim i obaly, skla a držáky. ' + B(('cateye', 'Cateye')) + ' a ' + B(('sigma', 'Sigma')) + ' jsou tradiční výrobci jednodušších počítačů, od základních drátových po bezdrátové s několika funkcemi. ' + B(('igpsport', 'iGPSPORT')) + ', ' + B(('bryton', 'Bryton')) + ' a ' + B(('cycplus', 'Cycplus')) + ' nabízejí GPS jednotky pro ty, kdo chtějí záznam trasy bez největších nároků na rozpočet. Značky ' + B(('rockbros', 'Rockbros')) + ' a ' + B(('west-biking', 'West Biking')) + ' najdete spíše u cenově nenáročných počítačů a drobného příslušenství. Označení dále uvádí, zda jde o drátovou či bezdrátovou verzi, takže si ji při porovnání ověřte.</p>'
          '<h2>Jak vybrat podle toho, jak jezdíte</h2>'
          '<h3>Městská jízda a dojíždění</h3>'
          '<p>Nejde o výkon, ale o přehled. Stačí počítač s rychlostí, ujetou vzdáleností a časem, který se sám zapne při rozjezdu. Praktické bývá podsvícení displeje na večerní jízdu. Počítač tohoto druhu je levný na údržbu a při krádeži kola vás nestojí víc, než kolik dává smysl.</p>'
          '<h3>Silnice a trénink</h3>'
          '<p>Sportovní jezdec ocení GPS s propojením na snímače tepu a kadence, s intervalovými režimy a rychlým zobrazením několika údajů na jedné stránce. Důležité je čitelné rozložení datových polí a rychlá odezva tlačítek v rukavicích.</p>'
          '<h3>Cykloturistika a terén</h3>'
          '<p>Při vícedenním výletu rozhoduje výdrž baterie a navigace. Počítač s mapou dovede vyhnout rušným silnicím a ukáže vrstevnice. Do terénu se hodí odolný přístroj s displejem, který se čte na slunci, a pevný držák, který vydrží otřesy.</p>'
          '<h2>Montáž, držáky a ochrana displeje</h2>'
          '<p>Držák určuje, jak dobře počítač vidíte a jak dlouho vydrží na kole. Klasický držák se nasazuje na řídítka, prodloužený drží jednotku před představcem, aby zůstalo místo pro světlo nebo kameru. Hliníkové držáky jsou pevnější než plastové, neohýbají se, když na ně přijde větší síla. Silikonový obal chrání před škrábanci a drobnými nárazy, tvrzené sklo nebo hydrogelová fólie chrání dotykový displej. Při lepení skla dbejte na čistý povrch bez prachu, jinak zůstanou bubliny.</p>'
          + T(['Doplněk', 'K čemu slouží', 'Na co dát pozor'], [
              ['Držák na řídítka', 'drží počítač v zorném poli', 'průměr řídítek a kompatibilita s přístrojem'],
              ['Silikonový obal', 'chrání před škrábanci a pády', 'vývody tlačítek a konektorů musí zůstat volné'],
              ['Tvrzené sklo nebo fólie', 'chrání displej', 'přesný model přístroje, citlivost dotyku'],
              ['Nabíjecí kabel', 'dobíjí jednotku', 'typ konektoru a délka'],
              ['Náhradní magnet a snímač', 'obnova drátové soupravy', 'shoda s typem počítače']]) +
          '<h2>Zima, déšť a dlouhé trasy</h2>'
          '<p>V chladu klesá výkon baterií, proto zimní vyjížďky zkracují výdrž o znatelný kus. Pomůže nosit přístroj do poslední chvíle v teple a při delší pauze ho schovat do kapsy. Dotykový displej v mokrých rukavicích reaguje špatně, takže pro špatné počasí volte model s tlačítky. Před dlouhou trasou si nahrajte stopu do přístroje ještě doma a otestujte, že ji navigace skutečně vede, protože na místě se připojení k mobilní síti nezaručuje. Rezervní zdroj v podobě malé powerbanky a krátkého kabelu zabere v brašně minimum místa.</p>'
          '<h2>Časté chyby při koupi a používání</h2>'
          '<ul><li>Koupit GPS přístroj bez ověření, že rozumí snímači, který již máte. Kontrolujte ANT+ a Bluetooth.</li>'
          '<li>Zapomenout nastavit obvod kola u drátového či bezdrátového počítače, takže údaje o rychlosti nesedí.</li>'
          '<li>Pořídit obal nebo sklo pro podobný, ale jiný model. U doplňků se rozdíl několika milimetrů pozná hned.</li>'
          '<li>Nechat přístroj nabít jen na polovinu před dlouhou jízdou a spoléhat na údaj výrobce o výdrži.</li>'
          '<li>Nechat přístroj v horkém autě nebo na slunci, což stárne baterii i displej.</li></ul>'
          '<h2>Péče o počítač</h2>'
          '<p>Po jízdě v dešti nebo blátě očistěte jednotku vlhkým hadříkem a nechte ji uschnout, nesmíte ji ale sušit horkým vzduchem. Kontakty u baterie čistěte suchým hadříkem. Před delším skladováním přístroj nabijte zhruba na polovinu a uložte v suchu a chladu. Drátový počítač potřebuje občas vyměnit knoflíkovou baterii, což zvládnete bez nářadí. Firmware GPS přístroje aktualizujte přes aplikaci výrobce, opravuje chyby a někdy přidává funkce.</p>'
          '<h2>Pro koho které řešení</h2>'
          '<p>Začátečník na kole do práce nepotřebuje navigaci a stačí mu jednoduchý počítač. Rodina na cyklostezkách ocení čitelné údaje o ujeté vzdálenosti. Sportovec bude chtít GPS s tréninkovými režimy a propojením na tep. Cykloturista si vybere navigaci s mapou. Před koupí si projděte také <a href="/jizdni-kola/">jízdní kola</a>, abyste věděli, jaký držák se vejde na řídítka, a ke komplexnímu vybavení patří <a href="/cyklisticke-helmy/">helmy</a> a <a href="/cyklo-zamky/">zámky</a>.</p>'
          '<h2>Kde porovnat a nakoupit</h2>'
          '<p>U každého výrobku srovnáváme nabídky obchodů a vidíte, kde je skladem. Před objednávkou si ověřte přesný model, zejména u doplňků, a podmínky vrácení zboží. Související nářadí najdete v kategorii <a href="/cyklo-pumpy-a-naradi/">pumpy a nářadí</a>, bezpečnost doplní <a href="/cyklisticke-obleceni/">cyklistické oblečení</a> a při delších výletech pomůže <a href="/powerbanky-a-nabijeni/">powerbanka</a>.</p>',
    faq=[
        ('Jaký je rozdíl mezi cyklopočítačem a GPS navigací?', 'Cyklopočítač zpravidla počítá rychlost a vzdálenost z otáček kola a nezná polohu. GPS navigace určuje polohu z družic, ukládá trasu a může vás vést po zadané stopě. Některé GPS počítače jsou jen záznamníky bez map, jiné mají plnohodnotné mapy s navigací.'),
        ('Je lepší drátový, nebo bezdrátový cyklopočítač?', 'Záleží na kole. Drátový je jednoduchý a nemá problém s rušením, ale kabel se musí vést po vidlici. Bezdrátový nemá kabel, jen je třeba dodržet vzdálenost mezi vysílačem a jednotkou. Pro běžnou jízdu fungují obě varianty dobře.'),
        ('Proč mi počítač ukazuje špatnou rychlost?', 'Nejčastěji je v nastavení chybný obvod kola nebo magnet míjí snímač ve větší mezeře, než povoluje návod. Zkontrolujte také, že je snímač upevněn na vidlici a magnet pevně na paprsku, a že baterie v jednotkách nejsou slabé.'),
        ('Jak změřím obvod kola?', 'Nahustěte pláště na provozní tlak, nasedněte na kolo a označte na zemi bod pod ventilkem. Ujeďte jedno úplné otočení kola a změřte vzdálenost mezi značkami. Takto získaná hodnota je přesnější než tabulková.'),
        ('Co znamená ANT+ a Bluetooth u cyklopočítače?', 'Jde o způsoby bezdrátového spojení se snímači tepu, kadence nebo výkonu a s telefonem. Aby se přístroj se snímačem spároval, musí si rozumět alespoň jedním z protokolů. Před koupí ověřte specifikaci obou zařízení.'),
        ('Jak dlouho vydrží baterie GPS počítače?', 'Výrobce udává výdrž v hodinách záznamu za běžných podmínek. Skutečná doba je kratší při silném podsvícení, zobrazování map, upozorněních z telefonu nebo v chladu. Na dlouhé výlety s sebou berte powerbanku nebo používejte úsporný režim.'),
        ('Hodí se držák od jednoho modelu i na jiný?', 'Ne vždy. Mnoho výrobců používá vlastní uchycení, které se liší i mezi generacemi. Držák, obal i sklo vybírejte podle přesného označení přístroje v názvu a popisu výrobku.'),
        ('Potřebuji ochranné sklo nebo fólii na displej?', 'Není povinné, ale kdo jezdí v terénu nebo přístroj nosí v kapse, ochranu ocení. Tvrzené sklo odolá škrábancům i drobným nárazům a fólie je tenčí a snadno se lepí. U dotykového displeje ověřte, že vrstva nezhoršuje odezvu.'),
        ('Dá se počítač přenést na jiné kolo?', 'Většina GPS přístrojů ano, stačí mít držák na každém kole nebo ho přesouvat. U drátového a bezdrátového počítače se musí snímač a magnet umístit na každé kolo zvlášť a nastavit odpovídající obvod, případně lze používat více profilů kol.'),
        ('Mám raději telefon na řídítkách, nebo samostatný počítač?', 'Telefon je pohodlný, ale rychleji vybije baterii, hůř snáší déšť a otřesy a displej se na slunci hůř čte. Samostatný počítač je odolnější, má delší výdrž a tlačítka použitelná v rukavicích. Pro příležitostné jízdy stačí telefon s dobrým držákem.')])

# ------------------------------------------------------------------ trekove-hole
NEW['trekove-hole'] = dict(long=True,
    title='Trekové a nordic walking hole: jak vybrat délku a typ',
    desc='Trekové, skládací a nordic walking hole z karbonu i hliníku. Jak vybrat délku, držadla a poutka a porovnat nabídky českých obchodů.',
    intro='<p>Dobře zvolená hůl odlehčí kolenům při sestupu, pomůže udržet rytmus do kopce a na kluzkém povrchu přidá oporu. Trekové hole se používají na turistice a v horách, nordic walking hole slouží k aktivní chůzi s důrazem na zapojení paží. Obě skupiny vypadají podobně, liší se však poutkem, délkou, držadlem a hrotem. Sporteka porovnává nabídky českých obchodů u pevných, teleskopických i skládacích holí a u příbuzných kousků, jako jsou náhradní hroty, pouzdra nebo dětské turistické hůlky.</p>'
          '<p>Najdete zde značky ' + B(('leki', 'Leki'), ('fizan', 'Fizan'), ('yate', 'Yate'), ('viking', 'Viking'), ('nils', 'Nils'), ('gabel', 'Gabel'), ('forclaz', 'Forclaz'), ('naturehike', 'Naturehike'), ('spokey', 'Spokey')) +
          '. K holím patří <a href="/turisticke-batohy/">turistické batohy</a>, <a href="/nesmeky/">nesmeky</a> a <a href="/outdoor-doplnky/">outdoorové doplňky</a>.</p>',
    guide='<h2>Trekové hole, nordic walking a jejich rozdíly</h2>'
          '<p>Na první pohled jsou si podobné, ale používají se jinak. Treková hůl slouží jako opora na nerovném terénu. Drží se rukou za držadlo, poutko jen zachytí zápěstí při uklouznutí a délka se mění podle sklonu, takže se při stoupání zkracuje a při klesání prodlužuje. Hůl pro nordic walking se zapichuje šikmo za tělo, aby se odrazem zapojil horní trup. Poutko je u ní pevnější, obvykle ve tvaru rukavice, a hrot bývá krátký, pro asfalt doplněný gumovou botkou.</p>'
          + T(['Typ hole', 'Typické provedení', 'Hodí se pro'], [
              ['Treková teleskopická', 'dvoudílná či třídílná, nastavitelná délka, hrot s kolečkem', 'turistika v kopcích, různě dlouhé etapy'],
              ['Skládací (Z-systém)', 'sklápí se na kratší délku, vejde se do batohu', 'trailrunning, cestování, vysokohorské túry'],
              ['Nordic walking', 'pevná nebo nastavitelná délka, poutko s rukavicí, gumová botka', 'zdravotní chůze, kondiční trénink, rovinky'],
              ['Dětská turistická', 'kratší, lehká, nastavitelná', 'výlety s dětmi, první zkušenosti s holí'],
              ['Příslušenství', 'pouzdra, botky, hroty, talířky', 'údržba a přizpůsobení terénu']]) +
          '<h2>Materiál: hliník, nebo karbon</h2>'
          '<p>Většina holí v nabídce je ze slitin hliníku, případně z karbonu a kombinací obou. Hliník je pevný, ohebný a při přetížení se zpravidla jen ohne a nezlomí, takže hůl často přežije náraz do kamene. Je těžší než karbon a v chladu citlivější na dotek studeného kovu. Karbon je lehký a dobře tlumí vibrace, ale jeho pevnost se ztrácí při poškození povrchu, třeba po nárazu mezi kameny. Na dlouhých túrách se lehkost projeví v únavě paže, při běžné chůzi po cestách ale stačí hliník. Hole označené jako „100 % karbon“ jsou určené hlavně pro nordic walking, kde se hůl zatěžuje pravidelně, ale ne hrubě.</p>'
          '<h2>Jak zvolit délku hole</h2>'
          '<p>Základní pravidlo pro nordic walking říká, že při stání s holí svisle má být předloktí vodorovně, tedy loket pokrčený zhruba v pravém úhlu. Pro treking se nastavuje podobně, jen s tím, že do kopce se hůl zkracuje a z kopce prodlužuje. Orientačně se délka pro nordic walking odvozuje od výšky postavy, u trekových holí s nastavitelnou délkou se správná poloha najde při chůzi. Je-li hůl příliš dlouhá, zvedají se ramena, je-li krátká, ohýbáte záda. Pevná hůl bez nastavení vyžaduje přesnou volbu, proto při koupi zkontrolujte velikostní tabulku výrobce.</p>'
          '<h3>Výška postavy a tabulky</h3>'
          '<p>Výrobci uvádějí doporučenou délku podle výšky těla, zpravidla po pěti nebo deseti centimetrech. Pokud padnete mezi dvě velikosti, zvolte u klidné chůze po rovině delší, u rychlé sportovní chůze kratší, protože zkrácená hůl umožňuje svižnější rytmus.</p>'
          '<h2>Držadla a poutka</h2>'
          '<p>Držadlo bývá z pěny, korku, gumy nebo plastu. Korek dobře saje pot a nepodkluzuje, pěna je měkká a příjemná na dotek i v chladu, guma je odolná, ale na dlouhé túře může tlačit. Prodloužená spodní část držadla se hodí pro přehmatávání při traverzu. Poutko musí sedět pohodlně, nesmí škrtit zápěstí. Ve skalnatém nebo lavinovém terénu se doporučuje rozepnutelné poutko nebo ruku z poutka vyvléknout. U nordic walkingu je poutko součástí techniky a drží ruku při odrazu.</p>'
          '<h2>Zámky, hroty a botky</h2>'
          '<p>Teleskopické hole se zajišťují vnějším zámkem na páčku nebo vnitřním zámkem s otočným mechanismem. Páčkový zámek se nastavuje rychle i v rukavicích, snadno se kontroluje a umožňuje nastavit sílu přítlaku šroubem. Otočný zámek je štíhlejší, ale pozná se, že přestává držet, až když hůl poklesne. Spodek hole končí hrotem z tvrdokovu, který se zabodává do země. Na zpevněných cestách a asfaltu se nasazuje gumová botka, aby hrot neklouzal a nehlučel. Talířek v dolní části brání zapadnutí do sněhu nebo bahna a jeho velikost se vybírá podle terénu.</p>'
          '<h2>Značky v nabídce</h2>'
          '<p>' + B(('leki', 'Leki')) + ' a ' + B(('fizan', 'Fizan')) + ' jsou specialisté na hole a mají široký sortiment od základních po lehké sportovní. ' + B(('yate', 'Yate')) + ', ' + B(('viking', 'Viking')) + ' a ' + B(('nils', 'Nils')) + ' nabízejí běžné hole pro turistiku i nordic walking. ' + B(('forclaz', 'Forclaz')) + ' a ' + B(('newfeel', 'Newfeel')) + ' jsou značky, které mají jednodušší modely pro začátečníky a pro rodiny. ' + B(('naturehike', 'Naturehike')) + ' staví na lehkých skládacích holích. Ve sbírce jsou i ' + B(('spokey', 'Spokey')) + ', ' + B(('gabel', 'Gabel')) + ' a další.</p>'
          '<h2>Pro koho jaká hůl</h2>'
          '<h3>Vysokohorská turistika</h3>'
          '<p>Využijete robustní teleskopickou hůl s páčkovým zámkem, která snese zátěž batohu a nepodklouzne na šikmých sutích. Skládací hole se vejdou na batoh při lezeckém úseku, kde ruce potřebujete volné. K tomu se hodí <a href="/horolezectvi/">vybavení pro ferraty</a> a <a href="/nesmeky/">nesmeky</a> na zledovatělé úseky.</p>'
          '<h3>Nordic walking a zdravotní chůze</h3>'
          '<p>Hole s pevným rukavicovým poutkem, lehké a s dobrou botkou. Chůze s holemi je šetrná k pohybovému aparátu, ale před zahájením pravidelného tréninku je vhodné poradit se s lékařem, zejména při zdravotních potížích.</p>'
          '<h3>Děti a rodiny</h3>'
          '<p>Dětská turistická hůl je kratší a lehčí. Dítě si ji nastaví samo a naučí se rytmus chůze. K výletům se hodí <a href="/lahve-a-termosky/">láhve a termosky</a> a <a href="/plastenky/">pláštěnky</a>.</p>'
          '<h2>Hole podle ročního období</h2>'
          '<p>V létě stačí malé talířky a hrot, který se v suchu zabodává spolehlivě. V zimě na sněhu potřebujete talířky větší, jinak se hůl propadne až po rukojeť. Při mrazu se hliníkové díly studí v dlani, proto pomáhají rukavice a držadlo z pěny. Vlhký sníh se na teleskopických spojích může srazit a zamrznout, takže po túře hole rozložte a osušte. Na jaře a na podzim, kdy je v lese blátivo a mokré listí, se hůl hodí hlavně jako třetí bod opory při sestupu. Na kluzkém ledu ji nespoléhejte, tam pomohou spíše <a href="/nesmeky/">nesmeky</a>, a pro náročnější terén teprve zkušenosti a vhodná obuv.</p>'
          '<h3>Jak hole zvolit na delší výlet</h3>'
          '<p>Při vícedenní túře s těžším batohem se vyplatí hole s robustním zámkem a odolným hrotem, i když jsou o něco těžší. Rozhoduje také, kolik zátěže přenesete na hole, protože batoh s plnou výbavou zvyšuje tlak na kolena při sestupu a pravidelná opora ulehčuje práci kloubům. Před výpravou si hole nastavte doma a vyzkoušejte celý den.</p>'
          '<h3>Dětské a rodinné hole</h3>'
          '<p>Děti rostou rychle, proto se vyplatí hole s nastavitelnou délkou. Hůl by měla být lehká a držadlo malé, aby ho dítě sevřelo. Sdílení holí v rodině je možné, jen si každý musí délku znovu nastavit.</p>'
          '<h2>Jak s holemi chodit</h2>'
          '<p>Do kopce se hole zapichují před tělo a tělo se o ně opře, rytmus drží paže a nohy křížem. Z kopce se hole prodlužují, zapichují se před tělo a odlehčují kolena. Na traverzu se hůl na straně svahu zkracuje, aby ruka nebyla příliš zvednutá. Při chůzi bez hole v dlani zbytečně nedržte, nechte ji zavěšenou na poutku nebo ji sklopte. Hrot nezapichujte tam, kde ho nemáte jak zajistit, a při předávání holí mezi lidmi dávejte pozor na hroty.</p>'
          '<h2>Údržba a skladování</h2>'
          '<p>Po mokré túře hole rozložte, otřete a nechte oschnout, jinak se zámek i vnitřek zanáší nečistotami a hliník koroduje. Dvakrát za sezónu zkontrolujte hrot, botky a poutka a při opotřebení je vyměňte. Hole nenechávejte v horkém autě. Skládací hole vyžadují čisté lanko uvnitř, nepoužívejte mazivo, které by zhoršilo tření zámku. Pouzdro ochrání hole při dopravě, protože hroty nepoškodí batoh ani auto.</p>'
          '<h2>Časté chyby</h2>'
          '<ul><li>Koupit nordic walking hole na horskou túru. Poutko a hrot jsou stavěné pro jiný způsob zatížení.</li>'
          '<li>Nechat hole příliš dlouhé, což přetěžuje ramena.</li>'
          '<li>Nepřekontrolovat zámek před sestupem po delší pauze.</li>'
          '<li>Zapomínat na gumovou botku na zpevněných cestách.</li>'
          '<li>Skladovat vlhké hole zavřené v pouzdře.</li></ul>'
          '<h2>Co ještě patří do výbavy</h2>'
          '<p>Hole jsou jen část výbavy. K túře patří <a href="/batohy/">batoh</a>, <a href="/celovky-a-svitilny/">čelovka</a>, <a href="/sportovni-bryle/">sportovní brýle</a>, <a href="/prvni-pomoc/">lékárnička</a> a v nepřehledném terénu <a href="/dalekohledy-a-kompasy/">kompas</a> či <a href="/sportovni-hodinky/">sportovní hodinky</a>. Ke spaní venku pak <a href="/turisticke-stany/">stan</a>. Nabídky obchodů u každé hole porovnáme tak, abyste věděli, kde je váš model skladem.</p>',
    faq=[
        ('Jaký je rozdíl mezi trekovou holí a holí na nordic walking?', 'Treková hůl je opora pro nerovný terén s nastavitelnou délkou a lehkým poutkem. Nordic walking hůl má pevnější poutko ve tvaru rukavice, je delší a je určená k odrazu při aktivní chůzi s podporou horního trupu. Na horách je lepší treková, na rovině nordic walking.'),
        ('Jak dlouhou hůl zvolit?', 'Při stání má být loket pokrčený zhruba v pravém úhlu, když držíte hůl svisle a hrot stojí na zemi. U nordic walkingu se délka odvozuje z výšky postavy podle tabulky výrobce. Treková hůl s nastavením se upravuje podle sklonu terénu.'),
        ('Je lepší karbonová, nebo hliníková hůl?', 'Karbon je lehčí a tlumí otřesy, hliník je odolnější vůči nárazům a ohýbá se místo zlomení. Na pravidelné chůzi po cestách se hodí obě varianty, na horách a v kamenitém terénu bývá hliník praktičtější.'),
        ('Na co si dát pozor u skládacích holí?', 'Na pevnost mechanismu a na to, aby se zámek při zatížení nepovolil. Skládací hole se vejdou na batoh, ale spoje mají větší počet dílů, a proto je kontrolujte po každé túře a udržujte je čisté.'),
        ('Mám hole používat s poutky?', 'Na rovném terénu a při nordic walkingu ano, poutko pomáhá držet hůl a zapojit paži. V lavinovém nebo skalnatém terénu je bezpečnější mít ruku volnou a poutko nepoužít nebo ho rozepnout, aby při pádu nezůstala ruka zachycená.'),
        ('K čemu je gumová botka na hrotu?', 'Chrání hrot, tlumí zvuk a zabraňuje klouzání po asfaltu a dlažbě. Na zpevněných cestách ji ponechte, v lese a na kamenech ji sundejte, aby hrot lépe zabíral.'),
        ('Jak poznám, že je zámek opotřebovaný?', 'Hůl pomalu klesá pod zatížením, zámek nedrží přes utažení nebo se pohybuje s vůlí. Přitáhněte šroub u páčkového zámku, a pokud to nepomůže, vyměňte zámek nebo celý díl.'),
        ('Hodí se hole pro děti?', 'Ano, dětské turistické hole jsou kratší a lehčí a pomáhají dětem udržet tempo. Délka se nastavuje podle výšky dítěte a hole dítěti zpočátku ukažte, jak je správně držet a zapichovat.'),
        ('Dají se hole vzít do letadla?', 'Pravidla se liší podle dopravce a letiště. Hole mají hrot, proto se obvykle ukládají do odbavených zavazadel. Skládací hole se vejdou do menšího kufru, ale před cestou si ověřte podmínky aerolinky.'),
        ('Jak hole uložit po sezóně?', 'Očistěte je, nechte uschnout, uvolněte zámky a uložte na suché a chladné místo. Vlhkost způsobuje korozi a plíseň na držadlech. Před novou sezónou zkontrolujte hroty, botky a poutka.')])

# ------------------------------------------------------------------ cyklo-zvonky-a-zrcatka
NEW['cyklo-zvonky-a-zrcatka'] = dict(long=True,
    title='Zvonky a zrcátka na kolo: dětské, retro i klaksony',
    desc='Zvonky, klaksony a zpětná zrcátka na kolo pro děti i dospělé. Jak vybrat průměr řídítek, zvuk a typ upevnění a porovnat nabídky obchodů.',
    intro='<p>Zvonek je malá věc, která zákon vyžaduje, a mnohdy zabrání srážce s chodcem, který vás neslyší. Zpětné zrcátko přidává přehled o provozu za zády, aniž byste se museli otáčet a trhat řídítky. Sporteka porovnává nabídky českých obchodů u klasických kovových zvonků, retro modelů z mosazi, elektrických zvonků, dětských klaksonů s pohádkovými motivy i zpětných zrcátek na řídítka. Podle popisu u každého výrobku poznáte průměr uchycení, materiál a to, jestli se hodí pro dítě, pro městské kolo, nebo pro sportovní stroj.</p>'
          '<p>Zastoupené jsou značky ' + B(('force', 'Force'), ('m-wave', 'M-Wave'), ('knog', 'Knog'), ('btwin', 'Btwin'), ('arcore', 'Arcore'), ('disney', 'Disney'), ('nickelodeon', 'Nickelodeon'), ('kellys', 'Kellys'), ('velobel', 'Velobel'), ('max1', 'Max1')) +
          '. K zvonku se hodí <a href="/cyklo-svetla/">světla na kolo</a>, <a href="/cyklisticke-helmy/">helmy</a> a <a href="/cyklo-chranice/">chrániče</a>.</p>',
    guide='<h2>Jaké zvonky a zrcátka najdete v nabídce</h2>'
          '<p>Kategorie je rozdělena podle toho, jak zařízení pracuje, a také podle toho, komu je určeno. Nejpočetnější skupinu tvoří klasické zvonky se spouštěním palcem. Vedle nich se objevují klaksony s gumovou bublinou, které znáte z dětských kol, elektrické zvonky s tlačítkem a baterií a zpětná zrcátka s ohebným ramenem.</p>'
          + T(['Typ', 'Princip a provedení', 'Hodí se pro'], [
              ['Klasický zvonek', 'kovová nebo plastová kalota, kladívko spouštěné palcem', 'městská kola, trekingová kola, běžná jízda'],
              ['Retro zvonek z mosazi', 'větší průměr, dlouhý zvuk, ozdobný kryt', 'holandská a městská kola, doplněk stylu'],
              ['Mini zvonek', 'nízký profil, úzká montáž na řídítka', 'silniční a sportovní kola, kde nezavazí'],
              ['Dětský klakson a zvonek', 'barevné provedení, pohádkové motivy, gumová bublina', 'dětská kola a odrážedla'],
              ['Elektrický zvonek', 'tlačítko a reproduktor, zvuk různé hlasitosti', 'kdo chce hlasitou signalizaci s lehkým ovládáním'],
              ['Zpětné zrcátko', 'ramínko na řídítka nebo do konce řídítek', 'městská jízda, elektrokola, jízda v kolonách']]) +
          '<h2>Kolik zvonků má kolo mít</h2>'
          '<p>Silniční provoz v České republice vyžaduje, aby kolo mělo funkční zvukové zařízení, tedy zvonek. Při jízdě mezi chodci, na cyklostezkách a stezkách pro bruslaře se zvonek používá víc než na silnici, protože tam upozorníte lidi, kteří nepočítají s rychlejším provozem. Je tedy rozumné mít zvonek na každém kole, včetně toho, na které občas sednou děti.</p>'
          '<h2>Jak vybrat zvonek podle řídítek</h2>'
          '<p>Zvonek se upíná na řídítka a rozhoduje o tom hlavně průměr trubky. Nejběžnější řídítka mají na místě upnutí průměr 22,2 mm, silniční řídítka bývají u představce silnější a jejich tenká část se pro zvonek používá jen zřídka. Zvonky s gumovými vložkami nebo stavitelným šroubem zvládnou více průměrů, ale vždy zkontrolujte údaj u výrobku. Zvonek, který se otáčí na řídítkách, je třeba utáhnout, ne ho přetáčet, aby nepraskl plastový třmen.</p>'
          '<h3>Poloha na řídítkách</h3>'
          '<p>Zvonek patří tam, kam dosáhne palec bez uvolnění úchopu. U řidítek s řazením pod rukojetí hledejte volné místo mezi brzdou a rukojetí. Příliš vyčnívající zvonek hrozí poškozením při pádu a při parkování. Mini zvonky se montují blíže k představci a nepřekážejí držáku počítače nebo světla.</p>'
          '<h2>Zvuk a materiál</h2>'
          '<p>Zvuk zvonku závisí na materiálu a tvaru kaloty. Mosazný zvonek zní jasně a vytrvale, hliníkový má zvonivý a ostřejší tón, plastový je tišší a hodí se spíše pro děti. U zvonků, které zvoní jen jednou, slyšíte signál kratší dobu, což stačí v městské zástavbě, ale na polních cestách nemusí. Elektrický zvonek se dá nastavit na delší tón, ale potřebuje baterii, kterou je třeba hlídat. Vše zvažte podle toho, kde nejčastěji jezdíte.</p>'
          '<h2>Dětské zvonky a klaksony</h2>'
          '<p>Dětské kolo má většinou barevný zvonek s motivem postavy z pohádky, což dítě motivuje, aby ho používalo. V nabídce najdete motivy od značek ' + B(('disney', 'Disney')) + ' a ' + B(('nickelodeon', 'Nickelodeon')) + ' a také jednobarevné zvonky ' + B(('arcore', 'Arcore')) + ' nebo ' + B(('max1', 'Max1')) + '. U dětských modelů hlídejte zaoblené hrany, pevné upnutí a to, aby zvonek nemohl dítěti skřípnout prst. Dětské klaksony mají gumovou bublinu a zní hravě, ale bývají hlasitější než malý zvonek, proto jejich použití dítěti vysvětlete. K prvnímu kolu patří také <a href="/cyklo-sedacky-a-voziky/">sedačky a vozíky</a>, jestliže budete vozit mladší sourozence, a přilba z <a href="/cyklisticke-helmy/">kategorie helmy</a>.</p>'
          '<h2>Zpětná zrcátka na kolo</h2>'
          '<p>Zrcátko se montuje buď na řídítka, nebo do jejich konce. Ramínko by mělo být dostatečně pevné, aby se zrcátko neotáčelo při jízdě po dlažbě, a zároveň mělo dostatečný rozsah nastavení. Menší zrcátko je nenápadné, ale ukazuje užší výřez, větší dává lepší přehled a víc vibruje. Nikdy se nespoléhejte jen na zrcátko, před odbočením nebo předjetím se otočte a ověřte situaci, protože zrcátko má mrtvé úhly. Zrcátko se hodí především na elektrokolech a pro jezdce, kteří se nechtějí otáčet kvůli bolesti krku.</p>'
          '<h3>Montáž zrcátka</h3>'
          '<p>Zrcátko nastavte při sezení na kole v obvyklé poloze, tak aby v něm bylo vidět vaše rameno a prostor za vámi. Při nastavování musí kolo stát na rovině a řídítka být v přímém směru. Nastavení zkontrolujte po pár kilometrech a zbytečně nepřitahujte šroub.</p>'
          '<h2>Zvonek podle typu kola</h2>'
          '<p>Na městském a trekingovém kole je dost místa a můžete zvolit větší zvonek s dlouhým zvukem. Na horském kole se zvonek často schovává blízko představce, aby nepřekážel řazení ani brzdám. Na silničním kole s beraními řídítky se používají mini zvonky upevněné na představci nebo pod ním, případně modely, které se schovají do konce řídítek. Elektrokolo jezdí rychleji, než jezdec čeká, a upozornit chodce včas je zde ještě důležitější. Na skládacích kolech se hodí malý zvonek, který nepřekáží při skládání. Na odrážedlech a malých kolech pro děti je zvonek spíš hračka než výstraha, přesto se z něj stane první cyklistický zvyk.</p>'
          '<h3>Jak zvonek správně používat</h3>'
          '<p>Zazvoňte včas a krátce, ne až těsně za zády chodce. Dvojí zazvonění je přívětivější než dlouhý nepřetržitý zvuk, který lidi spíš leká. Před předjetím zpomalte, počkejte, až chodec uhne, a při průjezdu mu poděkujte. Na stezkách sdílených s bruslaři a pěšími se nikdy nespoléhejte jen na zvonek, pokud lidé nosí sluchátka.</p>'
          '<h2>Kontrolní seznam před koupí</h2>'
          '<ul><li>Průměr řídítek v místě upnutí a volné místo mezi brzdou a rukojetí.</li>'
          '<li>Materiál kaloty a hlasitost zvuku pro vaše podmínky.</li>'
          '<li>U dětí pevné upnutí, zaoblené hrany a snadné spouštění palcem.</li>'
          '<li>U zrcátka rozsah nastavení, pevnost ramínka a způsob upnutí na řídítka.</li>'
          '<li>Zda se zvonek nebo zrcátko nebude střetávat s držákem počítače nebo světlem.</li>'
          '<li>Barva a design, jestli ladí s kolem a nepůsobí rušivě.</li></ul>'
          '<h2>Značky v katalogu</h2>'
          '<p>' + B(('force', 'Force')) + ' a ' + B(('m-wave', 'M-Wave')) + ' nabízejí klasické kovové zvonky pro běžná kola. ' + B(('knog', 'Knog')) + ' je známý designovými zvonky s nízkým profilem. ' + B(('btwin', 'Btwin')) + ' a ' + B(('decathlon', 'Decathlon')) + ' mají jednoduché řešení pro rodiny a začátečníky. ' + B(('kellys', 'Kellys')) + ' doplňuje kola téže značky, ' + B(('velobel', 'Velobel')) + ' a ' + B(('quick', 'Quick')) + ' se objevují u cenově nenáročných zvonků. Výběr podle značky ale nahraďte porovnáním průměru upínání a materiálu.</p>'
          '<h2>Zvonek, který je slyšet</h2>'
          '<p>Hlasitost zvonku se posuzuje hlavně podle toho, jak daleko je slyšet v hluku města. Větší kalota zní výrazněji než malá, mosazný tón je hlubší a nese se dál. Kvalitní zvonek by měl zvonit zřetelně i při jízdě rychlostí, kdy vítr přehlušuje drobné zvuky. Zvonek vyzkoušejte hned po montáži a pak i na ulici. Pokud zní příliš tiše, nepomůže dotahování, ale výměna kaloty nebo celého zvonku.</p>'
          '<h2>Nenápadné detaily, které rozhodují</h2>'
          '<p>Všímejte si, jakou má zvonek pružinu a jak snadno se spouští při větším tlaku palce. Slabá pružina v zimě, kdy jezdíte v rukavicích, selhává častěji. Pokud je třmen plastový, volte raději pevný a široký než tenký, protože se při tahu protočí. Šroub z nerezu vydrží déle než ocelový bez povrchové úpravy.</p>'
          '<h2>Údržba a časté závady</h2>'
          '<ul><li><strong>Zvonek chraptí.</strong> Kalota se uvolnila nebo je ucpaná nečistotami. Rozeberte, očistěte a znovu utáhněte středový šroub.</li>'
          '<li><strong>Zvonek nezvoní.</strong> Kladívko se zadrhává nebo pružina ztratila sílu. Vyčistěte mechanismus a vyzkoušejte, zda se pohybuje volně.</li>'
          '<li><strong>Zvonek se otáčí.</strong> Upínací třmen povolil. Utáhněte šroub a v případě potřeby vložte gumovou podložku.</li>'
          '<li><strong>Zrcátko se třese.</strong> Utáhněte kloub nebo vyměňte ramínko, jestliže se materiál opotřebil.</li>'
          '<li><strong>Rez.</strong> Ocelové části po mokré jízdě osušte a lehce potřete olejem z <a href="/cyklo-udrzba/">kategorie údržba</a>.</li></ul>'
          '<h2>Pro koho které řešení</h2>'
          '<p>Městský jezdec zvolí kovový zvonek s dlouhým zvukem. Majitel retro kola přidá mosazný model, který ladí s kolem. Silničář vybere mini zvonek s nízkým profilem. Rodiče vyberou barevný zvonek s motivem a bezpečným upnutím. Kdo jezdí na elektrokole nebo v hustém provozu, ocení zrcátko. Kompletní bezpečnost dotváří <a href="/cyklo-svetla/">světla</a>, <a href="/cyklo-zamky/">zámek</a>, <a href="/cyklisticke-bryle/">brýle</a> a <a href="/cyklo-pumpy-a-naradi/">pumpa s nářadím</a>.</p>'
          '<h2>Kde porovnat a koupit</h2>'
          '<p>U každého zvonku vidíte nabídky více obchodů a dostupnost. Před objednávkou ověřte průměr upínání, barvu a materiál, protože podobně vypadající výrobky se liší. Další doplňky najdete v nadřazené kategorii <a href="/cyklo-prislusenstvi/">cyklo příslušenství</a>, a pokud shánite nové kolo, podívejte se na <a href="/jizdni-kola/">jízdní kola</a> a <a href="/cyklo-tasky-a-nosice/">brašny a nosiče</a>.</p>',
    faq=[
        ('Musí mít kolo zvonek?', 'Ano. Podle pravidel silničního provozu musí mít kolo funkční zvukové výstražné zařízení, tedy zvonek. Slouží k upozornění chodců a ostatních účastníků provozu a na rozdíl od houkání nebo volání je spolehlivý za každého počasí.'),
        ('Jaký průměr řídítek mají zvonky?', 'Většina zvonků je určena pro řídítka o průměru 22,2 mm, což je nejběžnější rozměr. Některé modely mají gumové vložky nebo pružný třmen pro více průměrů. U silničních řídítek s tlustším středem hledejte zvonek s nastavitelným upnutím.'),
        ('Který materiál zvonku je nejlepší?', 'Mosaz a hliník dávají nejvýraznější zvuk. Ocel je pevná, ale může rezavět, plast je lehký a vhodný pro děti. Při běžné jízdě rozhoduje spíše zvuk a upnutí než samotný materiál.'),
        ('Je elektrický zvonek lepší než klasický?', 'Elektrický zvonek je hlasitější a ovládá se tlačítkem, ale potřebuje baterii a může se při dešti poškodit, pokud nemá krytí. Klasický je jednoduchý, nepotřebuje údržbu a funguje vždy.'),
        ('Jaký zvonek koupit dítěti?', 'Takový, který má pevné upnutí, zaoblené hrany a dítě ho umí spustit palcem. Motiv postavy z pohádky dítě motivuje, aby zvonek používalo. Dětské klaksony jsou hravé, ale hlasitější než malé zvonky.'),
        ('Proč zvonek chraptí?', 'Uvolněná kalota nebo nečistoty uvnitř mechanismu zhoršují zvuk. Zvonek rozeberte, očistěte a utáhněte středový šroub. Pokud je kalota prasklá, je lepší vyměnit celý zvonek.'),
        ('Jak namontuji zvonek na kolo?', 'Uvolněte šroub třmenu, nasuňte zvonek na řídítka mezi brzdu a rukojeť, nastavte polohu pro palec a šroub utáhněte. Nepřetahujte, aby se nepoškodil třmen. Vyzkoušejte, že zvonek funguje i v rukavicích.'),
        ('Hodí se zpětné zrcátko na každé kolo?', 'Hodí se na městská kola, elektrokola a trekingová kola s rovnými řídítky. Na silničních kolech s beraními řídítky se zrcátko montuje hůř. Kdo sportuje, ho obvykle nepotřebuje, ale před manévrem se pořád musí ohlédnout.'),
        ('Jak nastavit zpětné zrcátko?', 'Sedněte na kolo do obvyklé polohy, držte řídítka rovně a nastavte zrcátko tak, aby bylo vidět vaše rameno a prostor za vámi. Po první jízdě nastavení zkontrolujte a případně doladíte.'),
        ('Dá se zvonek přenést na jiné kolo?', 'Ano, pokud mají obě kola řídítka stejného průměru. Zvonek stačí uvolnit šroubem a znovu upnout. Při přesouvání zkontrolujte, že se třmen nepoškodil a že zvonek pevně drží.')])

# ------------------------------------------------------------------ golfove-hole
NEW['golfove-hole'] = dict(long=True,
    title='Golfové hole: sety želez, dřeva, wedge a putter',
    desc='Golfové hole pro praváky i leváky: sety želez, dřeva, hybridy, wedge a putter. Jak vybrat flex, loft a materiál a porovnat nabídky obchodů.',
    intro='<p>Golfová hůl je nástroj s přesně danou funkcí. Dřevo posílá míček na dlouhou vzdálenost, železo dovoluje zahrát na určený cíl, wedge řeší krátkou hru z písku nebo z vysoké trávy a putter ukončuje jamku na greenu. Výběr se řídí tělesnou výškou, silou, úrovní a tím, jestli hrajete pravou, nebo levou rukou. Sporteka porovnává nabídky českých obchodů u samostatných holí, kompletních setů, dřev, hybridů, wedgů a putterů a také u drobných golfových doplňků, jako je sběrač míčků na putter.</p>'
          '<p>V nabídce převažují značky ' + B(('inesis', 'Inesis'), ('sulov', 'Sulov'), ('taylormade', 'Taylormade'), ('titleist', 'Titleist'), ('callaway', 'Callaway'), ('odyssey', 'Odyssey'), ('wilson', 'Wilson')) +
          '. K holím patří <a href="/golfove-micky/">golfové míčky</a>, <a href="/golfove-tasky-a-voziky/">tašky a vozíky</a> a <a href="/golfove-obleceni-a-obuv/">golfové oblečení a obuv</a>.</p>',
    guide='<h2>Z čeho se skládá souprava holí</h2>'
          '<p>Pravidla golfu dovolují mít v bagu nejvýše čtrnáct holí. Žádná z nich není stejná, každá má jinou délku a sklon úderové plochy, zvaný loft. Čím větší loft, tím výš a kratší dolet. Souprava se tedy sestavuje tak, aby se doletové vzdálenosti postupně odstupňovaly a žádná hůl nedělala dvě stejné práce. Začátečník bohatě vystačí s menším setem, který tvoří dřevo, hybrid, několik želez, wedge a putter.</p>'
          + T(['Typ hole', 'K čemu slouží', 'Poznámka'], [
              ['Driver a dřeva', 'dlouhé údery z odpaliště nebo z fairwaye', 'nízký loft, velká hlava, delší násada'],
              ['Hybridy', 'náhrada dlouhých želez', 'odpustivější než dlouhé železo, snadno se hrají z roughu'],
              ['Železa 5–9', 'střední vzdálenosti na cíl', 'každé číslo má o něco vyšší loft a kratší násadu'],
              ['Wedge (PW, GW, SW, LW)', 'krátká hra, písek, zvedání míčku', 'nejvyšší loft, nejkratší dolet'],
              ['Putter', 'hra po greenu', 'tvar hlavy ovlivňuje pocit a vedení'],
              ['Sety', 'kompletní souprava pro hráče', 'vhodné pro začátečníky a juniory']]) +
          '<h2>Dřevo, driver a hybridy</h2>'
          '<p>Driver je nejdelší hůl s největší hlavou a nejnižším loftem, určená pro dlouhé odpaly z odpaliště. Fairwayová dřeva, třeba trojka nebo pětka, se hrají z čisté trávy i z odpaliště na kratších jamkách. Hybridy jsou něco mezi dřevem a železem a nahrazují obtížné dlouhé železo, protože míček vyzvednou snadněji. Název typu „Dřevo 3 SIM2 Max“ říká, že jde o fairwayové dřevo s přidanou odpustivostí. Hlava dnes bývá kovová, i když se pořád říká dřevo.</p>'
          '<h2>Železa, wedge a sety</h2>'
          '<p>Sada želez bývá označena od 5 do PW, případně 4–SW. Čím vyšší číslo, tím větší loft, kratší násada a menší vzdálenost. Železa s širší hlavou a větší odpustivostí se hodí začátečníkům, tzv. blade železa s tenkou hlavou vyžadují čistý úder. Wedge je nejkratší železo: pitching wedge (PW), gap wedge (GW), sand wedge (SW) a lob wedge (LW) se liší lofty a použitím. Pro začátečníka je rozumné pořídit PW a SW, další přidat podle potřeby. Kompletní sety, které v katalogu najdete, šetří čas, protože hole k sobě ladí a jsou odstupňované.</p>'
          '<h3>Putter</h3>'
          '<p>Putter se vybírá podle pocitu a způsobu úderu. Hlava typu blade je malá a klasická, mallet je větší a odpustivější při špatném zásahu středu. Rovná čára na hlavě usnadňuje zamíření, délka musí odpovídat postoji, aby oči byly nad míčkem. V nabídce jsou i značky ' + B(('odyssey', 'Odyssey')) + ', ' + B(('evenroll', 'Evenroll')) + ' a ' + B(('pareto', 'Pareto')) + ', které se na putter specializují.</p>'
          '<h2>Flex násady a materiál</h2>'
          '<p>Flex označuje ohebnost násady. Běžné značky jsou L (lady), A nebo M (senior), R (regular), S (stiff) a X (extra stiff). Pomalejší švih potřebuje ohebnější násadu, rychlý švih tužší. Špatný flex mění směr a výšku letu míčku, proto ho nepodceňujte. Násady bývají ocelové nebo grafitové: ocel je těžší a pevnější, grafit lehčí a tlumí vibrace, což ocení starší hráči a ženy. V názvu produktu často najdete označení „ocel“ nebo „grafit“. V popisu se objevuje i tvar hlavy a materiál, který určuje odpustivost a pocit z úderu.</p>'
          + T(['Hráč', 'Doporučený flex', 'Materiál násady'], [
              ['Žena nebo pomalý švih', 'L nebo A', 'grafit, lehčí'],
              ['Senior', 'A nebo R', 'grafit nebo lehká ocel'],
              ['Běžný rekreační hráč', 'R', 'ocel nebo grafit'],
              ['Rychlý švih, silný hráč', 'S nebo X', 'ocel'],
              ['Junior', 'podle délky a váhy', 'lehké, krátké hole']]) +
          '<h2>Praváci, leváci a velikost</h2>'
          '<p>Hole se vyrábějí zvlášť pro praváky a leváky a u většiny nabídek je v názvu uvedeno „Pro praváky“ nebo „Pro leváky“. Hůl pro leváky se na pravé ruce nedá správně hrát. Velikost násady se označuje číslem u juniorů, například velikost 1 až 3, nebo délkou v palcích u dospělých. Dospělý standard zvládne většina hráčů, ale výška nad 190 cm nebo pod 160 cm často potřebuje delší či kratší násadu. Pokud si nejste jistí, vyzkoušejte hole v golfovém klubu nebo na driving range.</p>'
          '<h2>Délka a lie úhel</h2>'
          '<p>Délka násady a lie úhel, tedy sklon násady vůči zemi při správném postoji, rozhodují o tom, zda hlava hole dosedá na trávu celou plochou. Příliš strmý úhel nechá špičku hlavy ve vzduchu a míček poletí doleva, příliš plochý způsobí opak. Výrobci udávají standardní hodnoty pro průměrnou postavu a většina hráčů se do nich vejde. Pokud jste výrazně vyšší či nižší, nechte si v klubu udělat měření na podložce. U jednodušších sad pro začátečníky si většinou vystačíte s údajem o velikosti a flexu.</p>'
          '<h2>Kdy měnit hole za nové</h2>'
          '<p>Hole ztrácejí účinnost pomaleji než jiné vybavení. Měnit je má smysl, až když hráč zlepší švih, naroste nebo se hole opotřebí. Dospívající hráč potřebuje delší násady každých pár let. Železa s hlubokým opotřebením drážek zhorší spin a vedení míčku. Prasklý grip nebo uvolněná hlava jsou důvod k opravě, ne nutně k nové sadě. Před výměnou si ověřte, jestli hole nepotřebují jen nový grip nebo seřízení u servisu.</p>'
          '<h2>Jak číst názvy produktů</h2>'
          '<p>Názvy golfových holí obsahují několik údajů za sebou, například typ hole, číslo, ruku, flex, materiál nebo loft. Údaj „Pro praváky“ určuje ruku, „Regular“ nebo „Senior“ flex, „Ocel“ a „Grafit“ materiál násady a číslo ve stupních loft. U setů se uvádí rozsah, například 5–PW, což znamená železa od pětky po pitching wedge. Označení „Lady“ upozorňuje na lehčí násady a měkčí flex pro ženy. Takto si rychle odfiltrujete, co vám sedí, a nemusíte číst každý popis.</p>'
          '<h2>Značky a rozdíly</h2>'
          '<p>' + B(('inesis', 'Inesis')) + ' je největší zastoupenou značkou, nabízí komplety i jednotlivé hole pro začátečníky a juniory, často s volbou velikosti a flexu. ' + B(('sulov', 'Sulov')) + ' dodává jednotlivá železa a dřeva v jednoduchém provedení. ' + B(('taylormade', 'Taylormade')) + ', ' + B(('titleist', 'Titleist')) + ', ' + B(('callaway', 'Callaway')) + ' a ' + B(('wilson', 'Wilson')) + ' patří mezi tradiční golfové značky. Při výběru nehleďte jen na jméno, ale na loft, flex a velikost, protože ty rozhodují o tom, jak se vám bude hrát.</p>'
          '<h2>Jak vybrat hole pro začátečníka</h2>'
          '<p>Začátečník nemusí kupovat čtrnáct holí. Dobrý start tvoří set se čtyřmi až osmi holemi, který obsahuje dřevo nebo hybrid, několik želez, wedge a putter. Důležitá je odpustivost, tedy schopnost hole odpustit nečistý zásah, a lehčí násada. Kupujte raději sadu určenou pro začátečníky a postupně ji doplňujte, až zjistíte, kterých vzdáleností vám chybí. Před nákupem si projděte lekce, ve kterých vám trenér poradí správnou délku a flex.</p>'
          '<h3>Junioři a dorost</h3>'
          '<p>Děti rychle rostou, proto se kupují hole podle výšky a stupně velikosti. Příliš dlouhá hůl vede ke špatnému postoji a ztěžuje učení. Juniorské sady jsou lehčí, mají měkčí flex a kratší násady a v katalogu je poznáte podle označení velikosti.</p>'
          '<h2>Péče o hole</h2>'
          '<p>Po každém kole očistěte drážky úderové plochy kartáčkem a vlhkým hadříkem, protože zablácené drážky snižují spin. Hlavy dřev chraňte návleky, aby se nepoškrábaly. Grip občas omyjte vodou a mýdlem, opotřebený vyměňte, protože kluzký úchop nutí držet hůl pevněji. Hole neskladujte dlouho v horkém autě, kde se může uvolnit lepení hlavy. Putter po použití osušte a nenechávejte ho opřený o zeď.</p>'
          '<h2>Časté chyby při výběru</h2>'
          '<ul><li>Koupit hole pro leváka místo pro praváka nebo naopak.</li>'
          '<li>Podcenit flex násady, což mění let míčku.</li>'
          '<li>Pořídit set pro profesionály, který pro začátečníka není odpustivý.</li>'
          '<li>Koupit příliš dlouhé hole pro dítě, aby mu vydržely déle.</li>'
          '<li>Zapomenout na putter nebo wedge, které rozhodují o skóre u jamky.</li></ul>'
          '<h2>Co ještě patří do golfové výbavy</h2>'
          '<p>K holím patří <a href="/golfove-micky/">míčky</a>, <a href="/golfove-tasky-a-voziky/">taška nebo vozík</a>, <a href="/golfove-obleceni-a-obuv/">oblečení a obuv</a> a <a href="/golfove-doplnky/">doplňky</a> jako rukavice, tiče a ukazatele. Při hraní venku se hodí <a href="/sportovni-bryle/">sluneční brýle</a>, <a href="/lahve-a-termosky/">láhev</a>, <a href="/plastenky/">pláštěnka</a>, <a href="/sportovni-tasky/">ledvinka</a> a <a href="/dalekohledy-a-kompasy/">dálkoměr či dalekohled</a>. Přehled celé oblasti najdete v nadřazené kategorii <a href="/golf/">golf</a>.</p>',
    faq=[
        ('Kolik holí smí mít hráč v bagu?', 'Pravidla golfu povolují nejvýše čtrnáct holí. Hráč si sestavuje sadu podle potřeby a není povinen mít všech čtrnáct. Začátečníci obvykle hrají s menší sadou, než kterou používají zkušení hráči.'),
        ('Co znamená loft hole?', 'Loft je sklon úderové plochy vůči svislici. Vyšší loft zvedá míček výš a dopraví ho na kratší vzdálenost, nižší loft vede míček dál a níž. Proto má driver nejnižší loft a wedge nejvyšší.'),
        ('Jak vybrat flex násady?', 'Flex se volí podle rychlosti švihu. Pomalejší švih potřebuje ohebnější násadu L, A nebo R, rychlý švih tužší S nebo X. Špatný flex mění výšku a směr letu míčku, proto ho před nákupem zkuste na driving range.'),
        ('Jaký je rozdíl mezi ocelovou a grafitovou násadou?', 'Ocel je těžší a pevnější, grafit lehčí a tlumí vibrace. Grafit se obvykle doporučuje ženám, seniorům a hráčům s pomalejším švihem, ocel těm, kteří potřebují přesnost při rychlém švihu.'),
        ('Mám začít se setem, nebo samostatnými holemi?', 'Začátečníkovi se vyplatí kompletní set, protože hole spolu ladí a jsou odstupňované. Samostatné hole se hodí k doplnění chybějící vzdálenosti nebo k výměně opotřebené hole.'),
        ('Jak poznám, jestli potřebuji hole pro leváka?', 'Levák drží hůl pravou rukou nad levou a švihá směrem doprava. Hole pro leváky mají hlavu otočenou opačně a v názvu výrobku bývá uvedeno „Pro leváky“. Hole pro praváky se na levou ruku nehodí.'),
        ('Co je hybrid a kdy ho použít?', 'Hybrid je hůl mezi dřevem a železem, která se hraje snáze než dlouhé železo. Hodí se z roughu a ze špatných lie, kde dlouhé železo selhává. Mnoho hráčů hybridem nahrazuje železa 3 až 5.'),
        ('Jaký putter vybrat?', 'Záleží na pocitu. Blade putter je klasický a vyžaduje přesný zásah středu, mallet je odpustivější. Důležitá je délka odpovídající vašemu postoji a rovná orientační čára na hlavě. Nejlepší je vyzkoušet několik na cvičném greenu.'),
        ('Jak o hole pečovat?', 'Po každém kole vyčistěte drážky na úderové ploše, osušte hlavy a grip omyjte vodou s mýdlem. Chraňte hole před přehřátím a vlhkem. Opotřebený grip vyměňte, protože klouzavý úchop zhoršuje úder.'),
        ('Dají se hole upravit na míru?', 'Ano, golfový klub nebo servis může upravit délku, loft, lie úhel a vyměnit grip nebo násadu. Pro začátečníka je to zbytečné, ale zkušený hráč s nestandardní výškou nebo švihem z úpravy získá.')])

