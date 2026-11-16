"""sporteka.cz — guides wave 2a (16. 11. 2026): the wave-1 guides get sections for the January categories of waves 26 and 27, so
every new category has a text link and a product grid from a guide (internal links are what Google discovers first on a DR≈0 site).

The wave-1 dicts are copied and new sections inserted after a named existing section; pruvodce-export.py takes the later wave."""
import copy

from pruvodce_vlna1a import GUIDES as _A
from pruvodce_vlna1b import GUIDES as _B
from pruvodce_vlna1c import GUIDES as _C

GUIDES = {}
UPDATED = '2026-11-16'


def _extend(src, slug, after):
    """after = {h2 of an existing section: [new sections]}; new sections go right behind that section."""
    g = copy.deepcopy(src[slug])
    for anchor, new in after.items():
        i = next(i for i, s in enumerate(g['sections']) if s['h2'] == anchor)
        g['sections'][i + 1:i + 1] = new
    g['updated'] = UPDATED
    GUIDES[slug] = g


_extend(_A, 'domaci-posilovna', {
    'Činky a kotouče: základ, který se hodí vždycky': [dict(
        h2='Stojan na činky: pořádek a bezpečná podlaha', cat='stojany-na-cinky', n=4,
        html='<p>Jakmile máte víc než dvě jednoručky a pár kotoučů, začnou se válet po zemi. To je nepohodlné a hlavně nebezpečné: o volný kotouč se snadno zakopne a těžká činka puštěná na dlaždici ji umí prasknout. Řešením je <a href="/stojany-na-cinky/">stojan na činky nebo kotouče</a>. Pro jednoručky se hodí patrový regál, pro kotouče svislý stojan s trny, pro dlouhou osu nástěnný držák. Před koupí si ověřte průměr otvoru kotoučů (30, nebo 50 mm), nosnost stojanu a jeho půdorys – v malém bytě je často lepší svislé řešení než široký regál.</p>')],
    'Kettlebelly: jedna kulatá váha místo půlky sklepa': [dict(
        h2='Medicinbal a slam ball: výbušnost bez složité techniky', cat='medicinbaly', n=4,
        html='<p>Těžký míč patří k nejjednodušším nástrojům na celotělový trénink. <a href="/medicinbaly/">Medicinbaly a slam bally</a> se ale liší použitím. Klasický medicinbal má pevný povrch a odráží se, hodí se na hody o zeď, předávky a cviky na střed těla. Slam ball je plněný pískem nebo granulátem, po dopadu se neodrazí, a proto je určený na prudké hody o zem. Wall ball je měkký a větší, typický pro crossfit. Doma pozor na podlahu a sousedy: hody o zem dělejte jen na gumové podložce, nejlépe v garáži nebo na dvoře. Na začátek volte spíš lehčí míč; na hody a rotace obvykle stačí 2–5 kg.</p>')],
    'Hrazda a bradla: levný základ pro silná záda': [dict(
        h2='Žebřiny: hrazda, protahování i dětské lezení', cat='zebriny', n=4,
        html='<p><a href="/zebriny/">Žebřiny</a> zaberou na stěně kus místa, ale umějí víc než samotná hrazda. Kromě přítahů a visů na nich zvládnete zvedání nohou na břicho, protahování zad a s nástavci i kliky na bradlech. Doma je navíc ocení děti. Rozhoduje kotvení: dřevěné žebřiny se šroubují do nosné zdi a hmoždinky musí odpovídat materiálu stěny, jinak jde jen o dekoraci. Do sádrokartonu se bez zesílení nemontují vůbec. Před koupí změřte výšku stropu, protože horní příčka potřebuje volný prostor pro hlavu, a zkontrolujte nosnost uvedenou výrobcem.</p>')],
    'Posilovací gumy: nejmenší nákup s největším využitím': [
        dict(h2='Balanční podložka a BOSU: stabilita kotníků a středu těla', cat='balancni-podlozky-bosu', n=4,
             html='<p>Nestabilní povrch donutí pracovat drobné svaly kolem kotníků, kolen a trupu. Proto mají <a href="/balancni-podlozky-bosu/">balanční podložky a BOSU</a> místo v domácím vybavení, zvlášť pokud běháte, lyžujete nebo se vracíte ke cvičení po delší pauze. Nafukovací čočka nebo polštář stojí málo a dá se schovat do šuplíku. Polokoule typu BOSU je větší, dá se otočit oběma stranami nahoru a hodí se i na kliky nebo dřepy. Začínejte ve stoji na obou nohách vedle zdi a těžší varianty přidávejte postupně. Po úrazu se cviky vyplatí probrat s fyzioterapeutem.</p>'),
        dict(h2='Gymnastický míč: sezení, protažení a střed těla', cat='gymnasticke-mice', n=4,
             html='<p><a href="/gymnasticke-mice/">Gymnastický míč</a> slouží k protahování, cvikům na břicho a záda i k aktivnímu sezení u počítače. Velikost se volí podle výšky: při sedu by stehna měla být zhruba vodorovně s podlahou. Hledejte označení odolnosti proti prasknutí (anti-burst), které znamená, že se míč při poškození vyfoukne pomalu. Pumpičku mívá v balení, ale ne vždy, takže to před objednávkou zkontrolujte.</p>'),
    ],
})

_extend(_B, 'zaciname-behat-v-zime', {
    'Tma ve čtyři odpoledne: čelovka a viditelnost': [dict(
        h2='Reflexní vesta: aby vás řidič viděl včas', cat='reflexni-vesty', n=4,
        html='<p>Černé zimní oblečení je ve tmě skoro neviditelné. Lehká <a href="/reflexni-vesty/">reflexní vesta</a> přes bundu to změní víc než malé reflexní proužky na botách. Pro běh se hodí síťovaná nebo elastická vesta s popruhy, která na těle neplandá a nepřekáží při pohybu rukou. Chodec, který jde za snížené viditelnosti mimo obec po neosvětlené krajnici nebo okraji silnice, musí mít podle zákona o silničním provozu na sobě prvky z retroreflexního materiálu – a běžec na silnici je chodec. Vestu kombinujte s čelovkou: světlo vám ukazuje cestu, reflexní plocha vás ukazuje řidičům.</p>')],
    'Čepice, čelenky a rukavice': [dict(
        h2='Kukla do silného mrazu a větru', cat='kukly', n=4,
        html='<p>Když teplota klesne hluboko pod nulu nebo fouká ledový vítr, čepice a nákrčník nestačí. Tenká <a href="/kukly/">kukla</a> kryje hlavu, krk i bradu najednou a pod kapucí nebo čepicí téměř nezabere místo. Na běh vybírejte prodyšný materiál s otvorem kolem úst nebo s možností stáhnout spodní část pod bradu, aby se vám nesrážel dech. Merino méně páchne, syntetika rychleji schne. Na mírnou zimu je kukla zbytečná a v teple se v ní člověk rychle zpotí.</p>')],
})

_extend(_B, 'bezky-pro-zacatecniky', {
    'Oblečení na běžky: méně, než čekáte': [dict(
        h2='Vyhřívané rukavice a ponožky pro zimomřivé', cat='vyhrivane-obleceni', n=4,
        html='<p>Při běžkování se člověk zahřeje rychle, ale prsty na rukou a nohou zebou i tak, hlavně při zastávkách nebo u lidí se slabším prokrvením. Pro ně existují <a href="/vyhrivane-obleceni/">vyhřívané rukavice, ponožky a vložky</a> s baterií. Na běžky volte lehčí modely, které neomezují úchop hole, a počítejte s tím, že na nejvyšší stupeň vydrží baterie nejkratší dobu. Pro většinu výletů stačí zapnout ohřev jen při pauzách a na zpáteční cestě.</p>')],
})

_extend(_C, 'zimni-radovanky-s-detmi', {
    'Helmy': [dict(
        h2='Chránič páteře pro malé lyžaře a snowboardisty', cat='chranice-pater', n=4,
        html='<p>Helma je na svahu samozřejmost, <a href="/chranice-pater/">chránič páteře</a> zatím ne. Přitom se hodí zejména dětem, které jezdí v terénním parku, na snowboardu nebo už rychle. Vybírá se podle délky zad, ne podle věku: chránič má krýt záda od horní části po kříž a nesmí omezovat pohyb. Měkké chrániče z materiálu, který při nárazu ztuhne, jsou pohodlnější než tvrdé skořepiny. Hledejte označení normy EN 1621-2 a vyzkoušejte ho pod bundou.</p>')],
    'Rukavice': [dict(
        h2='Impregnace: suché boty i kombinéza', cat='impregnace', n=4,
        html='<p>Mokré rukavice a boty ukončí den na sněhu rychleji než únava. Kombinézy a zimní boty mají z výroby vodoodpudivou úpravu, která praním a nošením slábne. <a href="/impregnace/">Impregnace</a> ve spreji nebo pracím prostředku ji obnoví. Postup je vždy stejný: nejdřív oblečení vyprat nebo boty vyčistit, potom impregnovat podle návodu a nechat řádně vyschnout. Na kůži se používají jiné přípravky než na textil a membrány, proto čtěte, pro jaký materiál je přípravek určený.</p>')],
})

_extend(_C, 'vyziva-pro-zacatecniky', {
    'Iontové nápoje': [
        dict(h2='Elektrolyty a solné tablety', cat='elektrolyty', n=4,
             html='<p>Iontový nápoj doplňuje tekutiny i sacharidy, <a href="/elektrolyty/">elektrolyty</a> v tabletách nebo prášku jsou většinou jen minerály, tedy hlavně sodík a draslík, často bez cukru a kalorií. Při běžném hodinovém tréninku stačí voda. Elektrolyty dávají smysl při dlouhém nebo velmi potivém výkonu, třeba v horké posilovně, na dlouhém běhu nebo na skialpech. Sledujte obsah sodíku na porci, protože ten se mezi výrobky liší nejvíc.</p>'),
        dict(h2='Šejkr: malá věc, kterou použijete denně', cat='sejkry', n=4,
             html='<p>Protein rozmíchaný lžičkou ve sklenici tvoří hrudky. <a href="/sejkry/">Šejkr</a> se sítkem nebo míchací kuličkou to vyřeší za pár vteřin. Vybírejte objem podle porce (500–700 ml stačí), těsnost víčka a to, jestli se dá mýt v myčce. Šejkr s přihrádkou na prášek se hodí, když si protein nosíte do posilovny. Po použití ho hned vypláchněte, zaschlé mléčné zbytky v plastu rychle zapáchají.</p>'),
    ],
    'Vitamín D': [
        dict(h2='Vitamín C a zinek', cat='vitamin-c', n=4,
             html='<p>V zimě jsou <a href="/vitamin-c/">vitamín C</a> a <a href="/zinek/">zinek</a> nejčastější doplňky vedle vitamínu D. Podle schválených tvrzení EU oba přispívají k normální funkci imunitního systému. Zelenina, ovoce, maso, luštěniny a ořechy je obvykle pokryjí. Doplněk dává smysl hlavně tehdy, když jídelníček pestrý není. U zinku se nevyplatí kombinovat víc přípravků najednou, protože se snadno překročí horní hranice bezpečného denního příjmu, kterou EFSA pro dospělé stanovila na 25 mg.</p>'),
        dict(h2='Multivitamín: jedna tableta místo deseti', cat='multivitaminy', n=4,
             html='<p>Kdo nechce skládat doplňky po jednom, sáhne po <a href="/multivitaminy/">multivitamínu</a>. Kvalitu poznáte podle tabulky na obalu: kolik procent referenční hodnoty příjmu (RHP) pokryje jedna dávka a v jaké formě jsou minerály. Pokud už užíváte vitamín D, hořčík nebo zinek zvlášť, sečtěte množství z obou přípravků. Multivitamín nenahrazuje jídlo a pestrou stravu.</p>'),
    ],
    'Spalovače tuků a co od doplňků nečekat': [dict(
        h2='L-karnitin: oblíbený, ale bez schváleného tvrzení', cat='l-karnitin', n=4,
        html='<p><a href="/l-karnitin/">L-karnitin</a> je jeden z nejprodávanějších doplňků „na hubnutí“. EU pro něj ale neschválila žádné zdravotní tvrzení, tedy ani tvrzení o spalování tuků. Tělo si ho samo vyrábí a další přijímá v mase. Pokud ho chcete vyzkoušet, srovnávejte množství karnitinu na porci a formu (tekutý, kapsle, tartrát). O výsledku ale rozhodne kalorický příjem, pohyb a spánek.</p>')],
    'Kreatin': [dict(
        h2='Glutamin', cat='glutamin', n=4,
        html='<p><a href="/glutamin/">Glutamin</a> je nejhojnější volná aminokyselina v těle a v obchodech se prodává jako prášek nebo kapsle. Tělo si ho umí vyrobit samo, a pokud jíte dost bílkovin, přijímáte ho i ze stravy. Pro začátečníka nepatří mezi nutné doplňky. Kdo ho chce zkusit, ať ho kupuje samostatně a čte, kolik ho je v jedné porci.</p>')],
})
