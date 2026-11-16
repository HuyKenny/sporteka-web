"""sporteka.cz — wave 27d (16. 11. 2026): long texts for reflexni-vesty, kukly, chranice-pater, impregnace.
General true facts only, no prices. Norms named only in general terms. Brands linked only if present in znacky.json."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

# ------------------------------------------------------------------ reflexni-vesty
NEW['reflexni-vesty'] = dict(long=True,
    title='Reflexní vesty: na běh, kolo, pro děti i s LED světly',
    desc='Reflexní vesty na běh, kolo i do práce, dětské vesty a modely s LED. Normy, velikost, praní. Porovnejte nabídky českých obchodů na jednom místě.',
    intro='<p>Reflexní vesta je jeden z nejlevnějších a nejúčinnějších způsobů, jak být na silnici vidět. Řidič v tlumených světlech zahlédne chodce v tmavé bundě často až na poslední chvíli, kdežto reflexní plochy mu světlo vrátí přímo do očí a postavu ukážou mnohem dřív. V zimě to platí dvojnásob: v lednu vychází slunce zhruba mezi půl osmou a osmou a zapadá mezi čtvrtou a pátou odpoledne, takže běh do práce nebo cesta ze školy vede často potmě.</p>'
          '<p>Sporteka shromažďuje nabídky českých e-shopů na běžecké a cyklistické reflexní vesty, dětské vesty, pracovní a bezpečnostní vesty i modely s LED světly nabíjenými přes USB. Najdete tu třeba ' + B(('craft', 'Craft'), ('gymbeam', 'GymBeam')) + ', Wowow, Accezzi, Endurance nebo M-Wave a také reflexní vesty pro psy. Kategorie patří pod <a href="/sportovni-vesty/">sportovní vesty</a>; vybíráte u nás, platíte a objednáváte přímo v obchodě.</p>',
    guide='<h2>Jak reflexní vesta funguje</h2>'
          '<p>Na vestě se potkávají dva různé materiály. Fluorescenční látka (typicky žlutozelená nebo oranžová) přeměňuje část ultrafialového světla na viditelné, a proto svítí za šera, v mlze a za soumraku. V úplné tmě ale sama nepomůže. Tam nastupují retroreflexní pruhy, které světlo z reflektorů neodrážejí do stran, ale zpátky ke zdroji. Řidič tak vidí jasně zářící pruhy, zatímco chodec vedle sebe nevidí nic zvláštního. Dobrá vesta proto kombinuje obojí: barevný podklad pro den a soumrak, odrazky pro noc.</p>'
          '<p>Na umístění záleží víc, než se zdá. Lidské oko rychleji pozná člověka, když vidí pohyb paží a nohou. Vesta pokrývá trup, takže ji je dobré doplnit reflexními pásky na kotníky nebo zápěstí. Běžce s páskem na kotníku proto řidič snáz rozpozná jako člověka, ne jen jako svítící obdélník u krajnice.</p>'
          '<h2>Druhy vest v nabídce</h2>'
          + T(['Typ', 'Typické použití', 'Čím se pozná'], [
              ['Běžecká reflexní vesta', 'běh a chůze za tmy, otužilci a pejskaři', 'lehká síťovina, pružné boky, malá hmotnost, někdy kapsička'],
              ['Vesta s LED světly', 'běh a kolo v úplné tmě, mimo osvětlené ulice', 'aktivní světla, nabíjení přes USB, režimy svícení, odolnost proti vodě'],
              ['Cyklistická vesta', 'jízda na kole, dojíždění do práce', 'delší záda, pruhy na ramenou a bocích, někdy větruodolná přední část'],
              ['Dětská vesta', 'cesta do školy, výlety se školkou, kolo a koloběžka', 'menší velikosti podle obvodu hrudníku, výrazná barva, často celoreflexní'],
              ['Bezpečnostní a pracovní vesta', 'do auta, na stavbu, k silnici, pořadatelé akcí', 'široké pruhy, suchý zip, univerzální velikost, často certifikace pro pracovní použití'],
              ['Celoreflexní nebo softshellová vesta', 'chladné ráno, kolo do města', 'reflexní celá plocha nebo zateplení, chrání i před větrem'],
              ['Reflexní vesta pro psa', 'večerní venčení', 'zapínání pod břichem, velikost podle obvodu hrudníku psa']]) +
          '<h2>Normy: co znamenají zkratky na štítku</h2>'
          '<p>U reflexních vest se nejčastěji setkáte se třemi evropskými normami a každá míří na jinou situaci.</p>'
          '<ul><li><strong>EN ISO 20471</strong> se týká výstražných oděvů s vysokou viditelností pro pracovní použití. Dělí je do tříd podle plochy fluorescenčního a retroreflexního materiálu, třída 3 je nejvyšší. Takové vesty nosí silničáři, záchranáři nebo lidé na stavbě a stejný typ se běžně vozí v autě.</li>'
          '<li><strong>EN 1150</strong> je starší norma pro výstražné oděvy k neprofesionálnímu použití, tedy třeba dětské vesty nebo vesty pro chodce a cyklisty. Dnes ji nahradila EN 17353, na štítcích starších modelů ji ale pořád najdete.</li>'
          '<li><strong>EN 17353</strong> je novější norma pro prostředky zvýšené viditelnosti v situacích se středním rizikem, kde není potřeba pracovní oděv podle EN ISO 20471. Nahradila normy EN 1150 a EN 13356 pro reflexní oděvy a doplňky a rozlišuje vybavení pro denní světlo, pro tmu a kombinované, takže se hodí pro sportovce, kteří se pohybují u silnice.</li></ul>'
          '<p>Norma na štítku znamená, že materiál prošel zkouškou. U levných vest bez označení nevíte, kolik světla pruhy skutečně vracejí. Pro běh a kolo není nutné kupovat pracovní vestu třídy 3, ale certifikace je užitečné vodítko, zvlášť u dětí.</p>'
          '<h2>Co říká zákon</h2>'
          '<p>Zákon o provozu na pozemních komunikacích (361/2000 Sb.) od 20. února 2016 ukládá chodci, který jde mimo obec za snížené viditelnosti po krajnici nebo po okraji vozovky na místě bez veřejného osvětlení, mít na sobě prvky z retroreflexního materiálu. Musí být umístěné tak, aby je ostatní účastníci provozu viděli. Sníženou viditelností zákon myslí hlavně dobu od soumraku do svítání, ale také mlhu, sněžení nebo hustý déšť. Počet ani velikost prvků předpis nestanoví a konkrétně vestu nepředepisuje, povinnost tedy splní i dobře viditelné pásky. Vesta je ale nejjednodušší řešení, protože kryje trup zepředu i zezadu. Pro běžce, kteří vybíhají po neosvětlené silnici mezi vesnicemi, se tak z dobrého zvyku stává povinnost.</p><p>Povinnost má i řidič auta: když se v souvislosti s nouzovým stáním pohybuje mimo vozidlo na pozemní komunikaci, musí mít na sobě oděvní doplněk s retroreflexním označením. Pro řidiče motocyklů a mopedů to neplatí. V praxi jde o reflexní vestu, kterou je rozumné vozit v kabině na dosah, ne v zavazadlovém prostoru.</p>'
          '<h2>Vesty s LED světly</h2>'
          '<p>LED vesta má kromě odrazek i vlastní světla, nejčastěji pásy po obvodu nebo na ramenou. Výhoda je zřejmá: odrazka zazáří jen tehdy, když na ni dopadne světlo, kdežto LED svítí i do tmy, kde žádné auto nejede. Hodí se na neosvětlené cesty, polní a lesní stezky nebo místa, kde se potkáváte s cyklisty bez světel. V popisu hledejte způsob nabíjení (dnes převážně USB), počet režimů (trvalé svícení a blikání), stupeň odolnosti proti vodě (například IPX6 zvládne déšť) a jak se baterie vyjímá před praním. Pamatujte, že vesta se světly nenahrazuje předepsané osvětlení kola ani čelovku, kterou potřebujete, abyste viděli pod nohy.</p>'
          '<h2>Dětské reflexní vesty</h2>'
          '<p>Dítě je menší než dospělý, takže ho řidič za tmy snáz přehlédne. Proto dětské vesty bývají celé reflexní nebo s velmi širokými pruhy. Výrobci jako Wowow, Author nebo M-Wave nabízejí vesty v dětských velikostech, některé i s kapucí nebo v módnějším střihu, který děti nosí raději. Velikost se volí podle obvodu hrudníku a výšky, s rezervou na zimní bundu. Dobrá dětská vesta se zapíná na suchý zip nebo zip, který dítě zvládne samo, a nemá dlouhé tkanice, které by se mohly zachytit. Pro školky a skupinové výlety se hodí výrazné barvy, ve kterých učitelky děti snadno spočítají.</p>'
          '<h2>Jak vybrat velikost a střih</h2>'
          '<p>Vesta se nosí přes vrchní vrstvu, v zimě tedy přes bundu. Zkuste ji s oblečením, ve kterém poběžíte nebo pojedete. Běžecké modely mají pružné boky nebo nastavitelné popruhy, aby při pohybu neplandaly a nepleskaly. Pracovní vesty v univerzální velikosti bývají široké a na běh nevhodné, protože vlají a zachytávají vítr. U cyklistických vest je praktická delší záda: v předklonu na kole se jinak vesta vyhrne a pruhy na kříži zmizí. Pokud vozíte batoh, vyberte vestu s reflexními prvky i na ramenou, nebo použijte reflexní potah na batoh. Na <a href="/bezecke-vesty-a-batohy/">běžecké vesty a batohy</a> se dá reflexní vesta navléct jen tehdy, je-li dost volná.</p>'
          '<h2>Praní a životnost</h2>'
          '<p>Retroreflexní materiál se praním a ohýbáním postupně opotřebovává. Na štítku certifikovaných vest bývá uveden maximální počet pracích cyklů, po kterých výrobce ještě ručí za vlastnosti. Perte na nízkou teplotu, bez aviváže a bez sušičky, pruhy nežehlete. Vybledlou fluorescenční barvu nebo popraskané odrazky poznáte snadno: posviťte na vestu baterkou ze vzdálenosti několika metrů a porovnejte ji s novou. Pokud pruhy už jen matně šednou, je čas na výměnu. U LED vest před praním vždy vyndejte baterii a řiďte se návodem.</p>'
          '<h2>Komu se reflexní vesta vyplatí</h2>'
          '<ul><li><strong>Běžcům</strong>, kteří trénují ráno nebo večer, zvlášť po silnicích bez chodníku.</li>'
          '<li><strong>Cyklistům</strong> dojíždějícím do práce, k osvětlení kola jako doplněk.</li>'
          '<li><strong>Dětem</strong> na cestě do školy, na kole, koloběžce nebo při výletech.</li>'
          '<li><strong>Pejskařům</strong>, kteří venčí za tmy, a jejich psům.</li>'
          '<li><strong>Turistům a poutníkům</strong>, kteří kus trasy jdou po silnici mezi obcemi.</li>'
          '<li><strong>Řidičům</strong>, kteří chtějí mít v autě vestu pro každého spolujezdce.</li></ul>'
          '<h2>Jaká barva je nejlepší</h2>'
          '<p>Nejvýraznější je fluorescenční žlutozelená, kterou oko za šera vnímá nejsilněji. V podzimním listí se ale může ztrácet, a proto se hodí i oranžová. Černé nebo šedé vesty s LED vypadají elegantněji a ve tmě díky světlům fungují dobře, za denního světla a soumraku však výrazně zaostávají. Rozhodující je kombinace: barva pro den, odrazky a případně světla pro noc. Kdo běhá jen po osvětlených ulicích, vystačí s lehkou vestou s pruhy; na okreskách mezi vesnicemi se vyplatí maximum reflexní plochy.</p>'
          '<h2>Na co se při porovnání dívat</h2>'
          '<p>Porovnávejte hlavně plochu a umístění reflexních pruhů, certifikaci, hmotnost a způsob zapínání. U LED modelů kapacitu baterie a odolnost proti vodě. Cena mezi obchody se u stejné vesty může lišit, proto se vyplatí podívat na více nabídek najednou; objednávka i reklamace pak probíhají u konkrétního prodejce. Další bezpečnostní výbavu na tmu najdete v kategorii <a href="/celovky-a-svitilny/">čelovky a svítilny</a> a pro kolo v sekci <a href="/cyklo-svetla/">cyklo světla</a>.</p>',
    faq=[
        ('Musím mít jako chodec reflexní vestu?',
         'Zákon nevyžaduje přímo vestu. Chodec, který jde mimo obec za snížené viditelnosti po krajnici nebo okraji vozovky na místě bez veřejného osvětlení, musí mít na sobě retroreflexní prvky viditelné pro ostatní účastníky provozu. Vesta je nejjednodušší způsob, jak tuto povinnost splnit, stačí ale i reflexní pásky.'),
        ('Jaký je rozdíl mezi fluorescenční a reflexní barvou?',
         'Fluorescenční látka svítí za denního světla, za šera a v mlze, ale v úplné tmě nepomůže. Retroreflexní pruhy fungují v noci, kdy vracejí světlo reflektorů zpět k řidiči. Ideální vesta má obojí.'),
        ('Je lepší vesta s LED, nebo obyčejná reflexní?',
         'Obyčejná vesta stačí tam, kde jezdí auta se zapnutými světly. LED vesta je vidět i bez cizího světla, takže se hodí na neosvětlené cesty a stezky, kde se potkáváte s chodci a cyklisty. Vyžaduje ale nabíjení a opatrnější praní.'),
        ('Jakou velikost reflexní vesty vybrat?',
         'Vesta se nosí přes bundu, takže ji zkoušejte s oblečením, ve kterém ji budete nosit. Na běh vyberte model s pružnými boky nebo popruhy, aby neplandal. U dětí se řiďte obvodem hrudníku a výškou a nechte rezervu na zimní bundu.'),
        ('Co znamená norma EN ISO 20471?',
         'Je to norma pro výstražné oděvy s vysokou viditelností pro pracovní použití. Rozlišuje třídy 1 až 3 podle plochy fluorescenčního a reflexního materiálu. Pro sport ji nepotřebujete, ale potvrzuje, že materiál prošel zkouškami.'),
        ('Jak dlouho reflexní vesta vydrží?',
         'Záleží na četnosti praní a nošení. Odrazky se praním a lámáním postupně opotřebují, certifikované vesty uvádějí počet pracích cyklů. Jednoduchý test: posviťte na vestu baterkou z dálky a porovnejte ji s novou.'),
        ('Mají reflexní vestu nosit i děti ve městě?',
         'Ve městě to zákon nepředepisuje, přesto se vesta nebo reflexní prvky dětem vyplatí. Dítě je menší a řidič ho za tmy mezi zaparkovanými auty vidí později. Pro cestu do školy v zimních měsících je vesta levná a účinná ochrana.'),
        ('Stačí reflexní pásky místo vesty?',
         'Pásky na kotníky a zápěstí jsou výborný doplněk, protože ukazují pohyb a řidič rychleji pozná člověka. Samotné však kryjí jen malou plochu. Nejlepší výsledek dává vesta na trup a pásky na končetiny dohromady.'),
    ])

# ------------------------------------------------------------------ kukly
NEW['kukly'] = dict(long=True,
    title='Kukly a balaclavy: lyžařské, merino, fleece, pod helmu',
    desc='Kukly a balaclavy na lyže, kolo i běh: fleece, merino, tenké pod helmu, dětské. Materiály, otvory a velikost. Porovnejte nabídky českých obchodů.',
    intro='<p>Kukla, anglicky balaclava, zakryje hlavu, krk a většinu obličeje jedním kusem oblečení. Na lyžích v mrazu a větru chrání tváře a bradu, které čepice ani nákrčník nekryjí celé, a pod helmou nezabere skoro žádné místo. Hodí se ale i na zimní běh, kolo, motorku, rybaření na ledu nebo práci venku. Složená zabere v kapse bundy jen málo místa, takže ji lze mít s sebou pro případ, že se na hřebeni zvedne vítr.</p>'
          '<p>Sporteka porovnává nabídky českých e-shopů na lyžařské kukly pro děti i dospělé, tenké kukly pod helmu, teplé fleecové a pletené kukly i merino modely. V katalogu jsou například ' + B(('reima', 'Reima'), ('viking', 'Viking'), ('smartwool', 'Smartwool'), ('husky', 'Husky'), ('lasting', 'Lasting'), ('sensor', 'Sensor'), ('under-armour', 'Under Armour'), ('rothco', 'Rothco'), ('mfh', 'MFH')) + ' nebo Zanier a POC. Kukly patří pod <a href="/nakrcniky-a-satky/">nákrčníky a šátky</a>; vyberete si u nás, nakoupíte v obchodě, který kuklu nabízí.</p>',
    guide='<h2>Proč kukla a ne čepice s nákrčníkem</h2>'
          '<p>Čepice a nákrčník spolu nikdy úplně nenavazují. Mezi nimi zůstane pruh kůže na krku nebo za ušima, kudy fouká, a nákrčník se při jízdě shrnuje. Kukla tvoří jeden souvislý celek od temene po ramena, takže nikde nezatéká studený vzduch. Navíc je tenčí než čepice, a tak se pohodlně vejde pod <a href="/lyzarske-helmy/">lyžařskou helmu</a>. U dětí má ještě jednu výhodu: nemá volné konce jako šála, které by se mohly zachytit o kotvu vleku nebo o sedačku lanovky.</p>'
          '<p>Nevýhodou je menší variabilita. Nákrčník stáhnete pod bradu jedním pohybem, kuklu musíte sundat celou, nebo vybrat model, kde se obličejová část dá shrnout. Kdo se při výstupu hodně zahřeje, ocení kombinaci tenké čepice a nákrčníku. Při sjezdu, na vleku a v silném větru je kukla pohodlnější.</p>'
          '<h2>Tvary a otvory</h2>'
          + T(['Provedení', 'Jak vypadá', 'Kdy se hodí'], [
              ['Jeden otvor', 'otvor pro oči, nos a ústa, obličej zakryje maska nebo nákrčník', 'nejuniverzálnější, pod helmu i bez ní'],
              ['Otvor pro brýle', 'oválný výřez přizpůsobený lyžařským brýlím, nos a ústa jsou kryté', 'lyže a snowboard v mrazu a větru'],
              ['Tři otvory', 'zvlášť pro oči a pro ústa, často pletená', 'práce venku, myslivost, armádní a outdoorové použití'],
              ['Kukla s odklopnou částí', 'obličejovou část lze shrnout pod bradu nebo zapnout', 'když se střídá výstup a sjezd'],
              ['Kukla s dýchací síťkou', 'v oblasti úst je prodyšná nebo perforovaná látka', 'menší zamlžování brýlí, rychlejší schnutí'],
              ['Dětská kukla', 'menší velikosti, měkčí švy, často veselé barvy', 'děti na lyžích, na saních, do školky']]) +
          '<h2>Materiály</h2>'
          '<p>Materiál rozhoduje o tom, jak bude kukla hřát, jak rychle uschne a jestli se vejde pod helmu.</p>'
          '<ul><li><strong>Fleece</strong> je teplý, měkký a levný. Dobře drží teplo i ve větru, ale je objemnější, a pod přiléhavou helmu se proto hodí jen tenký mikrofleece. Fleecové kukly vedou hlavně Rothco, MFH, Brandit nebo Litex.</li>'
          '<li><strong>Merino vlna</strong> hřeje i ve vlhku, reguluje teplotu a pomalu načichne. Proto je oblíbená na vícedenní túry a skialpy. Tenká merino kukla se pohodlně nosí pod helmou, dražší je a perte ji šetrně. Najdete ji u značek Smartwool, Lasting, Viking, Reima nebo Zanier; další vlněné doplňky nabízí kategorie <a href="/merino-doplnky/">merino doplňky</a>.</li>'
          '<li><strong>Syntetické tenké úplety</strong> (polyester, elastan) rychle schnou a sedí jako druhá kůže. Hodí se na běh, kolo nebo pod motorkářskou přilbu.</li>'
          '<li><strong>Pletené kukly</strong> z vlny nebo akrylu jsou teplé a klasické, často se třemi otvory. Pod helmu bývají příliš silné.</li>'
          '<li><strong>Letní a chladivé kukly</strong> z lehkých úpletů chrání před sluncem a prachem, třeba na kole nebo motorce v létě.</li></ul>'
          '<h2>Kukla pod lyžařskou helmu</h2>'
          '<p>Helma musí sedět pevně, aby při pádu fungovala. Proto si ji nasazujte a seřizujte s tou kuklou, se kterou budete jezdit. Tlustá kukla posune helmu výš a ta pak nekryje čelo, tenká naopak nic nemění. U modelů určených pod helmu bývají ploché švy a tenčí temeno, aby nikde netlačily. Dobrá kukla navazuje na lyžařské brýle bez mezery: horní okraj otvoru by měl končit pod obroučkou brýlí, ne nad ní. Jinak na čele zůstane pruh kůže, který v mrazu a protivětru omrzá jako první. Pokud kuklu kupujete k nové helmě, vezměte ji na zkoušku s sebou, případně se podívejte i na <a href="/lyzarske-cepice-a-nakrcniky/">lyžařské čepice a nákrčníky</a> jako alternativu na teplejší dny.</p>'
          '<h2>Zamlžování brýlí a dýchání</h2>'
          '<p>Nejčastější stížnost na kukly je mlžení brýlí. Teplý vydechovaný vzduch stoupá pod kuklou nahoru a sráží se na studeném zorníku. Pomůže kukla s prodyšnou nebo perforovanou částí u úst, která vede dech dolů a ven. Pomůže i to, když kukla nesahá vysoko přes kořen nosu a nepřekrývá spodní hranu brýlí. Ve frontě na lanovku si obličejovou část klidně stáhněte pod bradu, při sjezdu ji vraťte zpět. Vlhkou kuklu na obědě vyndejte a nechte proschnout, mokrý materiál totiž hřeje mnohem hůř.</p>'
          '<h2>Dětské kukly</h2>'
          '<p>Pro děti je kukla často praktičtější než čepice se šálou. Nespadne, nesesune se do očí a nemá konce, které by se zachytily. Dětské kukly nabízejí Reima, Husky, Sensor nebo Lego Wear, některé z merina, jiné z fleece nebo s oboustranným úpletem. Velikost se řídí obvodem hlavy. Kukla nesmí škrtit pod bradou ani tlačit na uši, a když ji dítě nosí pod helmou, musí přilba i nadále dobře sedět. Některé malé děti nechtějí mít zakrytý obličej; pomůže model, kde se obličejová část dá snadno stáhnout.</p>'
          '<h2>Kukly pro jiné sporty</h2>'
          '<p>Na <strong>zimní běh</strong> stačí tenká syntetická nebo merino kukla, která zakryje krk a uši a v mrazu ohřeje vdechovaný vzduch. Na <strong>kolo</strong> se hodí kukla pod cyklistickou helmu s přiléhavým střihem, nejlépe s větruodolnou přední částí. <strong>Motorkáři</strong> nosí kukly pod integrální přilbu jako hygienickou vrstvu i jako ochranu proti průvanu. Pro <strong>rybáře na ledu, myslivce a práci venku</strong> se hodí teplejší fleecové nebo pletené modely, třeba od Savage Gear, Rothco nebo Mil-Tec.</p>'
          '<h2>Mráz, vítr a omrzliny</h2>'
          '<p>Na sedačkové lanovce nebo při rychlém sjezdu fouká do obličeje vítr, který ochlazuje kůži mnohem víc, než ukazuje teploměr. Nejvíc ohrožené jsou nos, tváře, brada a ušní boltce, protože jsou chladu a větru vystavené nejvíc. Omrzlina začíná nenápadně: kůže zbledne a znecitliví, takže si jí člověk sám často nevšimne. Kukla tato místa zakryje a udrží u kůže vrstvu teplého vzduchu. Na horách se proto vyplatí mít ji v kapse bundy i tehdy, když ráno u auta vypadá počasí mírně. Na hřebenech a ledovcích se podmínky mění rychle a kukla zabere méně místa než další čepice.</p>'
          '<h2>Velikost a střih</h2>'
          '<p>Většina kukel se prodává v jedné univerzální velikosti, která díky pružnému materiálu sedne na většinu hlav dospělých. U merino a technických modelů se objevují velikosti podle obvodu hlavy. Kukla má přiléhat, ale neškrtit krk ani netlačit na uši. Spodní část by měla být dost dlouhá, aby šla zastrčit pod límec bundy nebo pod <a href="/termopradlo/">termoprádlo</a> a nevyklouzla při otáčení hlavy.</p>'
          '<h2>Praní a péče</h2>'
          '<p>Kukla je ve styku s dechem i potem, takže potřebuje prát častěji než čepice. Syntetiku a fleece perte podle štítku na nižší teplotu, bez aviváže, která zhoršuje odvod vlhkosti. Merino perte na vlnu nebo ručně s přípravkem na vlnu a sušte naležato. Kukly s membránou nebo větruodolnou vrstvou nesušte na topení. Na vícedenní lyžovačku je praktické mít dvě: jedna schne, druhou nosíte.</p>'
          '<h2>Jak vybírat podle použití</h2>'
          '<ul><li><strong>Sjezd a snowboard:</strong> tenká kukla pod helmu s otvorem pro brýle, ideálně s dýchací síťkou.</li>'
          '<li><strong>Skialp a běžky:</strong> merino nebo tenký úplet, který se snadno stáhne při výstupu.</li>'
          '<li><strong>Velký mráz a stání venku:</strong> fleece nebo silnější pletená kukla.</li>'
          '<li><strong>Běh a kolo:</strong> syntetický nebo merino úplet, přiléhavý střih.</li>'
          '<li><strong>Děti:</strong> kukla s měkkými švy v dětské velikosti, nejlépe s možností stáhnout obličejovou část.</li></ul>',
    faq=[
        ('Jaký je rozdíl mezi kuklou a balaclavou?',
         'Žádný, jde o totéž. Balaclava je anglický název, který se běžně používá i v popisech českých obchodů. Obojí označuje pokrývku hlavy, krku a části obličeje z jednoho kusu.'),
        ('Je lepší merino, nebo fleecová kukla?',
         'Merino hřeje i ve vlhku, pomalu zapáchá a je tenké, takže se hodí pod helmu a na aktivní sport. Fleece je teplejší na stání v mrazu a levnější, ale objemnější. Pod přiléhavou lyžařskou helmu se hodí jen tenký mikrofleece.'),
        ('Vejde se kukla pod lyžařskou helmu?',
         'Tenká kukla ano a helma s ní obvykle sedí dobře. Helmu si ale nastavte s kuklou, se kterou budete jezdit. Silná pletená nebo fleecová kukla může helmu nadzvednout a pak nesedí správně.'),
        ('Jak zabránit mlžení brýlí s kuklou?',
         'Vyberte kuklu s prodyšnou nebo perforovanou částí u úst a dbejte, aby nepřekrývala spodní okraj brýlí. Dech pak míří dolů, ne k zorníku. Ve frontě na vlek obličejovou část stáhněte pod bradu a mokrou kuklu včas vyměňte.'),
        ('Jakou velikost kukly vybrat dítěti?',
         'Řiďte se obvodem hlavy a tabulkou výrobce. Kukla nesmí škrtit pod bradou ani tlačit na uši. Pokud ji dítě nosí pod helmou, vyzkoušejte obojí najednou.'),
        ('Je kukla vhodná i na běh nebo kolo?',
         'Ano, v mrazu se tenká kukla hodí na běh i jízdu na kole. Volte syntetický nebo merino úplet, který rychle schne a nevadí pod cyklistickou helmou. Na mírnější počasí stačí nákrčník a čepice.'),
        ('Jak často kuklu prát?',
         'Častěji než čepici, protože do ní dýcháte a potíte se. Na vícedenní lyžovačce se vyplatí mít dvě a střídat je. Merino perte šetrně na vlnu, fleece a syntetiku bez aviváže.'),
        ('Nahradí kukla čepici?',
         'Tenká kukla pod helmou čepici nahradí a pod helmou bývá pohodlnější. Bez helmy v mrazu ale tenká kukla nehřeje tolik jako silná zimní čepice. Na procházku nebo stání venku proto zvolte teplejší fleecovou či pletenou kuklu, případně kombinaci tenké kukly a čepice.'),
    ])

# ------------------------------------------------------------------ chranice-pater
NEW['chranice-pater'] = dict(long=True,
    title='Chrániče páteře: na lyže, snowboard a kolo, jak vybrat',
    desc='Chrániče páteře na lyže, snowboard a kolo: vesty i chrániče na popruzích, dětské i dospělé. Normy, velikost a péče. Porovnejte nabídky českých obchodů.',
    intro='<p>Chránič páteře tlumí náraz na záda při pádu na tvrdý sníh, led, kameny nebo kořeny. Na sjezdovce ho nosí stále víc dětí i rekreačních lyžařů a u závodníků, ve snowparku a na freeridu patří k běžné výbavě. Lehké měkké chrániče se nosí pod bundou a téměř je necítíte, takže už nejsou jen výbavou pro extrémní jezdce.</p>'
          '<p>Sporteka porovnává nabídky českých e-shopů na chrániče páteře pro lyžaře, snowboardisty a cyklisty: ochranné vesty, chrániče na popruzích s bederním pásem i batohy s vloženým chráničem. V nabídce jsou například ' + B(('alpina', 'Alpina'), ('salomon', 'Salomon'), ('rossignol', 'Rossignol')) + ', Atomic, POC, Scott, Dainese, Komperdell, Relax, Etape nebo Arcore, v dospělých i juniorských velikostech. Kategorie patří do sekce <a href="/zimni-sporty/">zimní sporty</a>; porovnáte zde, nakoupíte v e-shopu.</p>',
    guide='<h2>Jak chránič páteře funguje</h2>'
          '<p>Chránič nemá za úkol zabránit každému zranění. Rozkládá energii nárazu na větší plochu a část ji pohltí, takže na obratle a žebra dopadne menší síla. Pomáhá také proti ostrým předmětům, například hraně lyže, kameni nebo řídítkům. Záda bývají ohrožená hlavně při pádu dozadu na tvrdou nebo ledovou plochu a při nárazu do překážky. Chránič je proto smysluplný hlavně tam, kde se jezdí rychle, skáče se nebo je terén nepředvídatelný.</p>'
          '<h2>Typy chráničů</h2>'
          + T(['Provedení', 'Popis', 'Hodí se pro'], [
              ['Ochranná vesta', 'chránič zad všitý do přiléhavé vesty, někdy i s ochranou hrudníku a žeber', 'lyže a snowboard, děti, každodenní nošení pod bundou'],
              ['Chránič na popruzích', 'samostatná deska s ramenními popruhy a širokým bederním pásem', 'freeride, snowpark, kolo; lze snadno přendat mezi oblečením'],
              ['Vesta se zateplením', 'chránič zad kombinovaný s teplou vestou', 'děti a rekreační lyžaři, kteří chtějí jednu vrstvu navíc'],
              ['Batoh s chráničem', 'zádová deska je součástí batohu', 'skialp, freeride a enduro na kole, kdy batoh nosíte stejně'],
              ['Chránič s tvrdými segmenty', 'skořepinové plasty spojené do pohyblivého pásu', 'rychlá jízda, kamenitý terén, motokros'],
              ['Měkký viskoelastický chránič', 'pěna, která při nárazu ztuhne (například D3O nebo POC VPD)', 'pohodlné celodenní nošení na sjezdovce']]) +
          '<h2>Měkký, nebo tvrdý chránič</h2>'
          '<p>Starší a závodní chrániče mají tvrdou skořepinu z plastových segmentů, pod nimiž je tlumicí pěna. Skořepina rozkládá sílu a dobře chrání proti ostrým předmětům, je ale tužší a méně se přizpůsobí tělu. Měkké chrániče používají viskoelastické materiály, které jsou za normálních okolností ohebné a při prudkém nárazu na okamžik ztuhnou. Známé jsou například D3O nebo VPD od značky POC, další výrobci používají vlastní pěny a struktury. Měkký chránič kopíruje záda, dýchá a v sedačce lanovky nepřekáží. Mnoho výrobců oba principy kombinuje: na povrchu tenká tvrdší vrstva, uvnitř měkká pěna. Pro rekreační lyžování a pro děti se dnes nejčastěji volí měkký chránič, pro freeride s kameny a rychlé skoky stojí za úvahu chránič se skořepinou.</p>'
          '<h2>Normy a úrovně ochrany</h2>'
          '<p>Chrániče páteře pro motorkáře testuje norma EN 1621-2. Rozlišuje dvě úrovně: úroveň 1 a vyšší úroveň 2, která propustí na záda menší sílu. Výrobci chráničů pro lyže, snowboard i kolo ji běžně uvádějí také a v popisech zimních chráničů zad se s ní setkáte nejčastěji. Zkouška měří, jakou sílu chránič propustí při úderu zkušebního tělesa; povolená průměrná hodnota je u úrovně 2 poloviční než u úrovně 1, tedy 9 kN proti 18 kN. Úroveň 2 je pro rychlou jízdu lepší volba, chránič úrovně 1 bývá lehčí a ohebnější. Pokud popis neuvádí žádnou normu, nevíte, jak chránič v testu obstál. Vždy proto hledejte údaj o certifikaci, ideálně přímo na štítku chrániče.</p>'
          '<h2>Kdy chránič páteře dává největší smysl</h2>'
          '<p>Riziko pádu na záda roste s rychlostí a s tvrdostí podkladu. Zledovatělá sjezdovka po ranní úpravě nebo odpolední hrboly jsou pro záda horší než měkký prašan. Chránič se vyplatí zejména v těchto situacích:</p>'
          '<ul><li><strong>Snowpark:</strong> skoky, zábradlí a boxy, kde se padá často a nečekaně.</li>'
          '<li><strong>Freeride a jízda mimo sjezdovku:</strong> kameny, stromy a skryté překážky pod sněhem.</li>'
          '<li><strong>Závody a tréninky:</strong> vysoká rychlost a tyče brány.</li>'
          '<li><strong>Děti a začátečníci:</strong> padají častěji a hůř odhadnou ostatní na svahu.</li>'
          '<li><strong>Plné sjezdovky:</strong> o víkendech a o prázdninách hrozí srážka s jiným lyžařem.</li>'
          '<li><strong>Sjezd a enduro na kole:</strong> kořeny, skály a rychlé úseky.</li></ul>'
          '<p>Pro klidné carvingové oblouky na upravené sjezdovce je chránič spíš otázkou osobní volby. Kdo ho jednou vyzkouší v měkkém provedení, ten si na něj obvykle zvykne a přestane ho vnímat.</p>'
          '<h2>Dámské, pánské a juniorské střihy</h2>'
          '<p>Chrániče se vyrábějí v pánských, dámských a dětských variantách. Dámská vesta bývá kratší v trupu, užší v pase a s jiným tvarem v oblasti hrudníku, aby vesta neodstávala a chránič ležel přesně na páteři. Pánská má delší záda a širší ramena. Unisex chrániče na popruzích se dají seřídit, ale i u nich rozhoduje délka desky. Pokud si nejste jistí, mezi dvěma velikostmi u chrániče páteře obvykle volte tu, která lépe odpovídá délce zad, ne obvodu hrudníku.</p>'
          '<h2>Jak vybrat velikost</h2>'
          '<p>U chráničů páteře nerozhoduje oblečení, které nosíte, ale délka zad. Výrobci uvádějí rozměr chrániče nebo doporučenou výšku postavy a délku trupu. Délku zad změříte vestoje od výrazného obratle na spodní části krku (při předklonu hlavy ho nahmatáte) po bederní linii zhruba v úrovni pasu. Chránič by měl krýt páteř od lopatek po kříž. Když je příliš dlouhý, při sezení na lanovce se opře o sedačku a vystrčí se nahoru, případně narazí zezadu do helmy. Když je krátký, nechá nechráněná bedra. Zkoušejte ho v předklonu a v podřepu, jako byste stáli v jízdním postoji. Vesta má přiléhat a nesmí klouzat do stran, ale nesmí ani omezovat dýchání.</p>'
          '<h2>Dětské chrániče</h2>'
          '<p>Děti na lyžích padají často a v závodních oddílech je chránič běžnou součástí výbavy. Juniorské vesty nabízí řada značek, například Scott, POC (POCito), Rossignol, Relax, Etape, Arcore nebo Cairn, často v jasných barvách, aby bylo dítě na svahu dobře vidět. Neplatí tu pravidlo „koupíme větší, doroste“. Velký chránič sjíždí, tlačí do helmy a v kritické chvíli nekryje správné místo. Velikost volte podle aktuální výšky a délky zad. Vesty s chráničem bývají výhodné i tím, že dítě nemusí řešit popruhy a zapínání.</p>'
          '<h2>Chrániče na kolo</h2>'
          '<p>Na horském kole, zejména v enduru a sjezdu, se chrániče páteře nosí jako samostatné vesty pod dres, nebo jako součást ochranné bundy či batohu. Na kole se víc potíte, takže je důležitá prodyšnost a síťované zádové panely. Pro kolo jsou typické modely od TSG, Dainese nebo batohy s vloženou deskou. Další ochranu kolen, loktů a trupu najdete v kategorii <a href="/cyklo-chranice/">cyklo chrániče</a>, pro snowboardisty jsou chrániče kostrče, zápěstí a kolen v kategorii <a href="/snowboardove-chranice/">snowboardové chrániče</a>.</p>'
          '<h2>Jak chránič nosit</h2>'
          '<p>Vestu nebo chránič na popruzích nosíte přes <a href="/termopradlo/">funkční prádlo</a> a pod mikinou nebo bundou. Měkké chrániče na přímém kontaktu s tělem jsou příjemnější a lépe sedí, pokud je k tomu výrobce určil. Bederní pás utáhněte tak, aby chránič nesklouzl na stranu. Na lanovku si nezapomeňte, že vesta zabere v zádech pár centimetrů; dětem pomozte sednout si dost hluboko. Chránič páteře je doplněk <a href="/lyzarske-helmy/">helmy</a>, ne její náhrada. Helmu potřebujete vždy, chránič zad tam, kde hrozí rychlé pády.</p>'
          '<h2>Péče a životnost</h2>'
          '<p>Většinu chráničů lze vyjmout z vesty a vestu prát podle štítku. Samotný chránič otírejte vlhkým hadříkem, nepoužívejte rozpouštědla a nesušte ho na topení ani na slunci za oknem auta. Viskoelastické pěny mají v teple a chladu jinou tuhost, což je jejich vlastnost, ne vada. Po velkém nárazu nebo při viditelné prasklině ve skořepině chránič vyměňte, protože už nemusí chránit stejně. I nepoškozené pěny časem stárnou; řiďte se doporučením výrobce o životnosti.</p>'
          '<h2>Na co se dívat při porovnání</h2>'
          '<ul><li><strong>Certifikace</strong> podle EN 1621-2 a úroveň ochrany.</li>'
          '<li><strong>Velikost</strong> podle délky zad, ne jen podle velikosti oblečení.</li>'
          '<li><strong>Typ:</strong> vesta, chránič na popruzích, nebo batoh.</li>'
          '<li><strong>Prodyšnost a hmotnost</strong> pro celodenní nošení.</li>'
          '<li><strong>Ochrana hrudníku a žeber</strong>, pokud ji chcete navíc.</li>'
          '<li><strong>Dámský střih</strong>, který respektuje tvar hrudníku.</li></ul>'
          '<p>Ceny chráničů se mezi obchody liší, zvlášť když sezóna vrcholí v lednu a o jarních prázdninách. Proto je rozumné porovnat nabídky ještě před odjezdem na hory a objednat s rezervou pro případnou výměnu velikosti.</p>',
    faq=[
        ('Potřebuji chránič páteře na sjezdovku?',
         'Pro pomalou rekreační jízdu není nutný, ale lehký měkký chránič pod bundou výrazně nepřekáží a při pádu na led nebo do překážky pomůže. Pro děti, rychlou jízdu, snowpark a freeride je rozumnou součástí výbavy.'),
        ('Co znamená úroveň 1 a 2 u chráničů páteře?',
         'Jde o úrovně ochrany podle normy EN 1621-2. Úroveň 2 propustí při testu na záda menší sílu než úroveň 1, takže chrání lépe. Chrániče úrovně 1 bývají lehčí a ohebnější.'),
        ('Je lepší měkký, nebo tvrdý chránič?',
         'Měkký viskoelastický chránič se lépe přizpůsobí zádům a je pohodlný na celý den. Tvrdá skořepina lépe chrání před ostrými předměty, jako jsou kameny. Mnoho chráničů obě vrstvy kombinuje.'),
        ('Jak vybrat velikost chrániče páteře?',
         'Podle délky zad, ne podle velikosti trička. Změřte vzdálenost od výrazného obratle na spodní části krku po bederní linii a porovnejte ji s tabulkou výrobce. Chránič nesmí při sezení narážet do helmy ani do sedačky.'),
        ('Mohu koupit dítěti chránič na dva roky dopředu?',
         'Raději ne. Příliš velký chránič sjíždí, tlačí do helmy a při pádu nekryje správné místo. Vybírejte podle aktuální výšky a délky zad dítěte.'),
        ('Lze lyžařský chránič páteře použít i na kolo?',
         'Často ano, pokud je dost prodyšný a nebrání v pohybu. Na kole se ale víc potíte, takže se hodí síťované provedení. Chrániče na popruzích se přenášejí mezi sporty snadněji než zateplené vesty.'),
        ('Kdy je potřeba chránič páteře vyměnit?',
         'Po velkém nárazu, při prasklé skořepině nebo viditelně poškozené pěně. I nepoškozený chránič časem stárne, proto se řiďte doporučenou životností od výrobce.'),
        ('Nosí se chránič páteře pod bundou, nebo přes ni?',
         'Pod bundou, obvykle přes funkční prádlo nebo tenkou mikinu. Tak chránič sedí těsně na zádech a nesjíždí. Některé chrániče na popruzích se dají nosit i přes dres na kole, záleží na určení od výrobce.'),
    ])

# ------------------------------------------------------------------ impregnace
NEW['impregnace'] = dict(long=True,
    title='Impregnace na boty a oblečení: spreje, prací, vosky',
    desc='Impregnace na boty, bundy, softshell, péřové věci i stany: spreje, prací přípravky, vosky a čističe. Jak na membrány. Porovnejte nabídky českých obchodů.',
    intro='<p>Nepromokavá bunda ani kožené boty nezůstanou voděodpudivé napořád. Povrchová úprava se nošením, třením o batoh a praním postupně ztrácí a voda se přestane perlit. Látka pak nasákne, bunda studí a membrána pod ní hůř dýchá. Správné vyčištění a nová impregnace obvykle vrátí výbavě velkou část původních vlastností a prodlouží jí život o několik sezón. Vyplatí se to hlavně na podzim a před zimou, kdy výbavu čeká sníh, rozbředlé cesty a déšť se sněhem.</p>'
          '<p>Sporteka porovnává nabídky českých e-shopů na impregnační spreje, prací impregnace, vosky a balzámy na kůži, technické prací prostředky i přípravky na péřové spacáky, stany nebo stoupací pásy. V nabídce jsou například Nikwax, Granger’s, Toko, Swix, Siga, Lowa, Collonil, Tarrago, Jason Markk a ' + B(('kilpi', 'Kilpi')) + '. Kategorie patří pod <a href="/doplnky-k-obuvi/">doplňky k obuvi</a>; vyberete zde, koupíte přímo v obchodě.</p>',
    guide='<h2>Proč výbava přestane odpuzovat vodu</h2>'
          '<p>Většina nepromokavých a softshellových materiálů má na povrchu tenkou voděodpudivou úpravu, často označovanou zkratkou DWR. Ta způsobí, že voda vytvoří kapky a steče. Úprava se ale opotřebovává třením, nečistotami a mastnotou z kůže a také praním v obyčejném prášku. Když přestane fungovat, vnější látka nasákne vodou. Membrána pod ní sice obvykle dál nepropustí vodu dovnitř, jenže mokrá vrchní vrstva brání odvodu páry. Pot pak kondenzuje uvnitř a máte pocit, že bunda promokla, i když membrána je v pořádku.</p>'
          '<h2>Nejdřív čistit, pak impregnovat</h2>'
          '<p>Nejčastější chyba je nastříkat impregnaci na špinavou bundu nebo zablácené boty. Nečistoty, prach a mastnota brání tomu, aby se přípravek navázal na vlákna, a samy přitahují vodu. Proto se výbava nejdřív vypere v technickém pracím prostředku nebo vyčistí speciálním čističem. Obyčejné prací prášky a aviváže zanechávají na látce zbytky, které vodu přitahují, takže na funkční oblečení se nehodí. Často stačí samotné vyprání v technickém prostředku a oživení teplem a voda se začne znovu perlit; teprve když to nepomůže, přichází na řadu impregnace. Nikwax, Granger’s i další výrobci prodávají výhodné sady prací prostředek plus impregnace.</p>'
          '<h2>Sprej, nebo prací impregnace</h2>'
          + T(['Způsob', 'Jak se používá', 'Kdy se hodí'], [
              ['Sprej (spray-on)', 'nastříká se na čistou vlhkou nebo suchou látku podle návodu', 'bundy s podšívkou, boty, batohy, místa s větším opotřebením'],
              ['Prací impregnace (wash-in)', 'přidá se do pračky místo pracího prostředku po vyprání', 'softshell, fleece, zateplené oblečení, kalhoty'],
              ['Vosk a balzám', 'vtírá se do kůže nebo do voskované bavlny', 'kožené trekové boty, oděvy z voskované tkaniny'],
              ['Krém', 'nanáší se na hladkou kůži, často s barvou', 'hladká useň, městská a pracovní obuv'],
              ['Nano sprej na tenisky', 'tenká ochranná vrstva proti vodě a skvrnám', 'semiš, nubuk, textilní tenisky'],
              ['Speciální přípravky', 'péřové věci, vlna, stany, stoupací pásy', 'podle typu výbavy']]) +
          '<p>Sprej nanesete jen tam, kde ho chcete mít, tedy na vnější stranu. To je výhoda u bund s vnitřní podšívkou nebo membránou, jejichž vnitřek má odvádět pot, nikoli odpuzovat vodu. Prací impregnace se rozprostře rovnoměrně po celém kusu a hodí se na softshell, fleece a oblečení bez membrány. U bund s membránou se řiďte doporučením na štítku nebo u výrobce přípravku; některé prací impregnace jsou na membrány přímo určené.</p>'
          '<h2>Membrány a oživení teplem</h2>'
          '<p>U oblečení s membránou typu Gore-Tex je základ pravidelné praní v technickém prostředku. Mnoho výrobců doporučuje po vyprání bundu sušit v sušičce na mírnou teplotu nebo ji přežehlit přes látku, protože teplo voděodpudivou úpravu oživí. To ale platí jen tehdy, když to štítek dovoluje. Některé materiály, lepené švy nebo reflexní prvky teplo nesnášejí. Po impregnaci postupujte podle návodu přípravku; některé vyžadují tepelnou aktivaci, jiné stačí nechat volně uschnout. Na membránové bundy existují i přípravky výslovně určené pro tyto materiály, například Revivex nebo Nikwax TX.Direct.</p>'
          '<h2>Impregnace bez fluoru</h2>'
          '<p>Starší impregnace stály na fluorovaných sloučeninách (PFC, širší skupina PFAS), které vodu i mastnotu odpuzují velmi účinně, ale v přírodě se prakticky nerozkládají. Evropská regulace je proto postupně omezuje a výrobci outdoorové výbavy i přípravků přecházejí na impregnace bez fluoru. Ty odpuzují vodu dobře, mastnotu a špínu o něco hůř, takže výbavu je potřeba čistit a obnovovat častěji. Na obalech hledejte označení „PFC free“ nebo „bez PFAS“. Údaj „bez PFOA/PFOS“ znamená jen to, že přípravek neobsahuje dvě konkrétní nejznámější látky, nikoli že je zcela bez fluoru.</p>'
          '<h2>Péče o kožené a membránové boty</h2>'
          '<p>Kožené trekové boty potřebují nejen impregnaci, ale i výživu kůže, jinak vysychá a praská. Hladká useň snese vosk, balzám nebo krém, které ji zároveň chrání proti vodě. Nubuk a semiš běžným voskem ani krémem neošetřujte, protože změní jejich vzhled a strukturu; na ně patří sprej určený pro broušenou kůži. Boty s membránou ošetřujte přípravky, které kůži nezalepí, jinak se zhorší prodyšnost. Silné tuky a oleje kůži také výrazně změkčují, což u pevných <a href="/trekova-obuv/">trekových bot</a> nemusí být žádoucí. Před ošetřením boty vyčistěte kartáčem a vlažnou vodou a vyndejte vložky i tkaničky. Impregnaci nanášejte na čistou, lehce vlhkou nebo suchou kůži podle návodu a boty pak nechte schnout při pokojové teplotě, nikdy u topení nebo kamen. U <a href="/zimni-obuv/">zimních bot</a> se vyplatí ošetřit je ještě před sezónou, ne až po prvním promoknutí.</p>'
          '<h2>Péřové věci, vlna a stany</h2>'
          '<p>Peří se v běžném prášku slepí a ztratí objem. Na <a href="/perove-spacaky/">péřové spacáky</a> a bundy se proto používá speciální prací prostředek na peří a případně impregnace, která peří chrání před vlhkem. Důkladné vysušení je u peří klíčové: sušte v sušičce na nízkou teplotu se sušicími míčky, pokud to štítek dovoluje, nebo naležato a trpělivě, dokud peří nebude úplně suché. Vlněné a merino oblečení perte v přípravku na vlnu. Stany a celty mají vlastní impregnace, často s ochranou proti UV záření, které tkaninu postupně ničí. Velké plochy se ošetřují postřikem na postaveném a vyčištěném stanu za suchého počasí.</p>'
          '<h2>Impregnace stoupacích pásů</h2>'
          '<p>Do kategorie patří i přípravky pro skialpinisty. Stoupací pásy z mohéru nebo směsi mohéru se syntetikou se impregnují, aby na nich nenamrzal sníh a dobře klouzaly. Nabízí je Swix, Toko, Skivo nebo Nikwax ve formě spreje, vosku či tyčinky. Samotné pásy najdete v kategorii <a href="/skialpove-pasy/">skialpové pásy</a>.</p>'
          '<h2>Jak poznat, že impregnace funguje</h2>'
          '<p>Nejjednodušší je kapková zkouška. Kápněte na látku nebo botu trochu vody: když vytvoří kulaté kapky, které se při naklonění skutálejí, úprava funguje. Když se kapka rozteče a látka v místě ztmavne, je čas na čištění a obnovu. Zkoušejte hlavně namáhaná místa, tedy ramena, rukávy, sedací část kalhot a špičky bot. Právě tam se úprava opotřebuje nejdřív, zatímco záda bundy mohou ještě perlit. Po nové impregnaci zkoušku zopakujte, až přípravek zaschne nebo se aktivuje teplem. Nečekejte, že starší bunda bude odpuzovat vodu jako nová; i správně ošetřená výbava časem ztrácí a úprava se musí obnovovat opakovaně.</p>'
          '<h2>Jak impregnovat správně</h2>'
          '<ul><li>Výbavu nejdřív vyčistěte nebo vyperte v technickém prostředku.</li>'
          '<li>Spreje používejte venku nebo v dobře větrané místnosti a nevdechujte je.</li>'
          '<li>Nový přípravek vyzkoušejte na nenápadném místě, hlavně u světlé kůže a semiše.</li>'
          '<li>Naneste rovnoměrně, přebytek otřete hadříkem a nechte zaschnout podle návodu.</li>'
          '<li>Švy a místa namáhaná třením (ramena pod batohem, špička boty) ošetřete pečlivěji.</li>'
          '<li>Impregnaci obnovte, jakmile se voda přestane perlit, ne až když výbava promokne.</li></ul>'
          '<h2>Jak vybírat a porovnávat</h2>'
          '<p>Nejdřív si ujasněte materiál: membránová bunda, softshell, hladká kůže, nubuk, peří, nebo stan. Podle toho zvolte typ přípravku a sledujte, zda je určený pro membrány a zda je bez fluoru. Velká balení a náhradní náplně se vyplatí, pokud ošetřujete výbavu celé rodiny. Ceny stejného přípravku se mezi e-shopy liší, a tak se vyplatí porovnat více obchodů; objednávka se dokončí u vybraného prodejce. Pokud právě vybíráte novou výbavu, podívejte se i na <a href="/nepromokave-bundy/">nepromokavé bundy</a> a <a href="/softshellove-bundy/">softshellové bundy</a>.</p>',
    faq=[
        ('Jak často impregnovat bundu?',
         'Podle toho, jak často ji nosíte. Signálem je, že se voda na povrchu přestane perlit a látka tmavne, jak nasakuje. Nejdřív zkuste bundu vyprat v technickém prostředku a případně oživit teplem podle štítku, impregnaci použijte, až když to nestačí.'),
        ('Je lepší impregnace ve spreji, nebo do pračky?',
         'Sprej ošetří jen vnější stranu, což se hodí u bund s podšívkou nebo membránou a u bot. Prací impregnace pokryje celý kus rovnoměrně a je vhodná pro softshell, fleece a oblečení bez membrány. Řiďte se doporučením výrobce oblečení i přípravku.'),
        ('Můžu bundu s membránou Gore-Tex prát v pračce?',
         'Většinou ano, ale v technickém pracím prostředku, bez aviváže a podle štítku. Pravidelné praní membráně neškodí, naopak odstraní nečistoty, které zhoršují prodyšnost. Teplo k oživení úpravy použijte, jen pokud to štítek povoluje.'),
        ('Proč bunda promoká, když má membránu?',
         'Často nepromoká, jen nasákne vnější látka. Mokrý povrch brání odvodu páry, pot kondenzuje uvnitř a působí to jako promoknutí. Pomůže vyprání a obnova voděodpudivé úpravy.'),
        ('Čím impregnovat semišové a nubukové boty?',
         'Sprejem určeným pro semiš a nubuk. Vosky a krémy mění vzhled a strukturu broušené kůže, proto se na ni nehodí. Boty nejdřív vyčistěte kartáčem a nechte je úplně uschnout.'),
        ('Co znamená impregnace bez PFC?',
         'Že neobsahuje fluorované sloučeniny, které se v přírodě nerozkládají. Taková impregnace odpuzuje vodu dobře, mastnotu o něco hůř, a proto ji je třeba obnovovat častěji. Označení „bez PFOA/PFOS“ neznamená, že přípravek je bez fluoru úplně.'),
        ('Jak prát péřový spacák nebo bundu?',
         'Ve speciálním prostředku na peří, na šetrný program a s důkladným mácháním. Pak sušte v sušičce na nízkou teplotu se sušicími míčky, pokud to štítek dovoluje, a dokud peří nebude úplně suché. Vlhké peří se slepí a může plesnivět.'),
        ('Mám nové boty impregnovat hned po koupi?',
         'U semišových, nubukových a textilních bot se to vyplatí, protože ochranná vrstva brání vsakování vody i skvrn od začátku. Kožené trekové boty bývají z výroby ošetřené, takže stačí je impregnovat, až se voda přestane perlit. Vždy se řiďte doporučením výrobce bot.'),
    ])
