"""sporteka.cz — guides wave 2b (16. 11. 2026): sections for the November wave 4 categories (boby, sáňky, whey and vegan protein,
dumbbells). The wave-2a dicts are copied and the new sections inserted after a named section (same mechanism as wave 2a)."""
import copy

from pruvodce_vlna2a import GUIDES as _P

GUIDES = {}
UPDATED = '2026-11-16'


def _extend(slug, after):
    g = copy.deepcopy(_P[slug])
    for anchor, new in after.items():
        i = next(i for i, s in enumerate(g['sections']) if s['h2'] == anchor)
        g['sections'][i + 1:i + 1] = new
    g['updated'] = UPDATED
    GUIDES[slug] = g


_extend('zimni-radovanky-s-detmi', {
    'Sáně a boby: co sledovat před koupí': [
        dict(h2='Boby: řiditelné, s brzdou, nebo úplně jednoduché', cat='boby', n=4,
             html='<p>Plastový bob je pro většinu dětí první zimní „vozidlo“. Nejjednodušší modely nemají řízení ani brzdu a jezdí se na nich hlavně na mírných svazích za domem. '
                  'Řiditelné boby s volantem a brzdami po stranách dávají staršímu dítěti víc kontroly, jsou ale těžší a na tvrdém sněhu rychlejší. '
                  'Než vyberete, podívejte se na hmotnost, kterou výrobce udává jako maximální, na tvar sedačky a na to, jestli má bob vpředu šňůru k tahání do kopce. '
                  'Celou nabídku porovnáte ve výpisu <a href="/boby/">boby</a>.</p>'),
        dict(h2='Sáňky a saně: dřevo, kov, nebo skládací', cat='sanky', n=4,
             html='<p>Klasické dřevěné saně vydrží roky a s opěrkou nebo ohrádkou se na nich vozí i malé dítě. Kovové a skládací sáňky jsou lehčí a vejdou se do kufru auta, '
                  'plastové saně zase nevadí mokro. Pro sáňkování z kopce se hodí delší saně s pevnými ližinami, na tahání batolete po rovině stačí kratší model s opěradlem. '
                  'Modely všech typů najdete ve výpisu <a href="/sanky/">sáňky a saně</a>.</p>'),
    ],
})

_extend('vyziva-pro-zacatecniky', {
    'Proteiny': [
        dict(h2='Whey: syrovátkový koncentrát, izolát a clear', cat='whey-proteiny', n=4,
             html='<p>Syrovátkový protein je nejrozšířenější typ proteinového prášku. Koncentrát obsahuje kromě bílkovin i trochu laktózy a tuku, izolát prochází další filtrací, '
                  'takže má vyšší podíl bílkovin a méně laktózy. Clear whey je izolát připravený tak, aby se pil jako ovocný nápoj místo mléčného koktejlu. '
                  'Rozdíly v chuti, rozpustnosti a složení porovnáte ve výpisu <a href="/whey-proteiny/">whey proteiny</a>.</p>'),
        dict(h2='Rostlinný protein pro vegany i při nesnášenlivosti mléka', cat='veganske-proteiny', n=4,
             html='<p>Kdo nejí živočišné produkty nebo mléčné bílkoviny nesnáší, sáhne po proteinu z hrachu, sóji, rýže nebo konopí. Jednotlivé rostliny mají odlišné složení aminokyselin, '
                  'proto výrobci často míchají několik zdrojů dohromady. Na etiketě se vyplatí sledovat podíl bílkovin v porci a sladidla. Nabídku najdete ve výpisu '
                  '<a href="/veganske-proteiny/">veganské a rostlinné proteiny</a>.</p>'),
    ],
})

_extend('domaci-posilovna', {
    'Činky a kotouče: základ, který se hodí vždycky': [
        dict(h2='Jednoruční činky: pevné, nebo nakládací', cat='jednorucni-cinky', n=4,
             html='<p>Pár jednoruček je nejuniverzálnější kus domácí posilovny. Pevné činky s gumovou nebo chromovanou úpravou jsou hned připravené a nic se na nich neuvolní, '
                  'zato pro postup zátěže jich potřebujete víc párů. Nakládací činky s kotouči a zámky ušetří místo i peníze, přehazování kotoučů ale zdržuje. '
                  'Neoprenové a vinylové činky s malou hmotností se hodí na rehabilitaci a aerobní cvičení. Porovnání najdete ve výpisu '
                  '<a href="/jednorucni-cinky/">jednoruční činky</a>.</p>'),
    ],
})
