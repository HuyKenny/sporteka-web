#!/usr/bin/env python3
"""sporteka.cz — extra filter parameters read from product titles (what Sportisimo / Decathlon offer as facets):

    material  Materiál a technologie   Gore-Tex, Merino, Softshell, Fleece, Péřové, PrimaLoft, Polartec, Bavlna, Kůže, Neopren, Karbon, Hliník, Titan
    sezona    Sezóna                   Zimní, Letní, Jaro/podzim                  (clothing, shoes, merino)
    objem     Objem                    do 20 l … 55 l a více                      (backpacks, bags, cooler boxes)
    osoby     Počet osob               1 osoba … 6 a více osob                     (tents)

params(texts, cat_slug) -> [(key, value)].  Values are what the filter prints; products matching none simply have no value (the filter
is only shown in a category where it covers enough products — Filtry.astro).
"""
import re
import unicodedata

import kategorie as K

MATERIAL = [
    ('Gore-Tex', r'gore-?tex|(^| )gtx( |$)|gore tex'), ('Merino', r'merino'), ('Softshell', r'softshell'), ('Fleece', r'fleec|flis'),
    ('Péřové', r'(^| )per(ov|i)|(^| )down( |$)|(^| )pernat|(^| )pernik'), ('PrimaLoft', r'primaloft'), ('Polartec', r'polartec'), ('Bavlna', r'bavln'),
    ('Kůže', r'(^| )koz(en|ene|ena|enou)|(^| )kuz(e|i)|leather'), ('Neopren', r'neopren'), ('Karbon', r'karbon|carbon'), ('Hliník', r'hlinik|aluminium|(^| )alu( |$)'),
    ('Titan', r'titan'),
]
SEASON = [('Zimní', r'zimn|sneh|zateplen|lyzarsk'), ('Letní', r'letn|sandal|(^| )lehk(a|e|y|ou) '), ('Jaro/podzim', r'jarn|podzimn|prechodov|(^| )3 sezon')]
WEAR = {'sportovni-obleceni', 'sportovni-obuv', 'merino', 'lyzarske-obleceni'}
BAGS = {'batohy', 'turisticke-batohy', 'mestske-batohy', 'skolni-batohy', 'sportovni-tasky', 'tasky-pres-rameno', 'chladici-boxy', 'cyklo-tasky-a-nosice', 'bezecke-vesty-a-batohy', 'lahve-a-termosky'}


SKIS = {'sjezdove-lyze', 'lyze-komplety', 'detske-lyze', 'skialpove-lyze', 'bezecke-lyze'}
BOARDS = {'snowboarding', 'snowboardy', 'snowboardove-sety'}
SKIS_ALL = {'zimni-sporty'}
LEN_BUCKETS_SKI = [(120, 'do 120 cm'), (140, '120–139 cm'), (160, '140–159 cm'), (170, '160–169 cm'), (180, '170–179 cm'), (999, '180 cm a více')]
LEN_BUCKETS_BOARD = [(140, 'do 140 cm'), (150, '140–149 cm'), (160, '150–159 cm'), (170, '160–169 cm'), (999, '170 cm a více')]
TYPE_RULES = [
    ('Freeride', r'freerid|off ?piste|backcountry|powder'), ('Freestyle', r'freestyle|(^|\W)park(\W|$)|twin ?tip|(^|\W)jib'),
    ('Závodní', r'(^|\W)(sl|gs|sg|fis|wc|race|racing|world cup|rc4|worldcup)(\W|$)'), ('Carving', r'carv|(^|\W)(rc|rtm|rapid)(\W|$)'),
    ('All-mountain', r'all.?mountain|allmountain|(^|\W)am(\W|$)|(^|\W)(allroad|all road)(\W|$)'),
    ('Klasika', r'klasik|classic|zaber|mohero|skin(\W|$)|twin skin'), ('Bruslení', r'bruslen|(^|\W)skate(\W|$)'),
]
MEMBRANE = r'(?<![\d.,])(\d{1,2}) ?k(?![a-z0-9])|(?<![\d.,])(\d{1,2})[ .]?000 ?mm|(?<![\d.,])(\d{4,5}) ?mm'

# Features people search for (Marketing Miner, 11/2026): helmet visor, photochromic / OTG goggles, bib trousers, gloves vs mittens,
# skin vs scale cross-country skis, quick-entry snowboard bindings, Boa lacing, thermal-underwear piece.
# 22. 11. 2026: what Top4running / Sportisimo offer as shoe facets (carbon plate, waterproof membrane, wide toe box, zero drop); demand is small
# (Ahrefs: 150 / 150 / 20 / 40 searches) — a filter for the visitor, not a landing page
_SHOE_FEATURES = [
    ('Karbonová deska', r'carbon|karbon|vaporfly|alphafly|metaspeed|adios pro|endorphin (pro|elite)|cielo x1|rocket x|sc elite|rebellion pro|fast-?r(\W|$)'),
    ('Nepromokavé (Gore-Tex, membrána)', r'gore.?tex|(^|\W)gtx(\W|$)|waterproof|nepromok|vodotes|vodeodoln|(^|\W)wp(\W|$)|(^|\W)tex(\W|$)'),
    ('Široká špička', r'(^|\W)(wide|extra wide|2e|4e)(\W|$)|sirok\w* (spick|stih|stopa)|sirsi'),
    ('Zero drop', r'zero.?drop|(^|\W)altra(\W|$)'),
]
FEATURES = {
    **{c: _SHOE_FEATURES for c in ('silnicni-bezecke-boty', 'trailove-boty', 'vysoke-trekove-boty', 'nizke-trekove-boty', 'treninkova-obuv')},
    'lyzarske-helmy': [('Se štítem', r'stit|visor|shield'), ('MIPS', r'mips|koroyd|wavecel'), ('Audio / Bluetooth', r'bluetooth|audio|reproduktor'), ('S brýlemi v setu', r's bryle|s bryl|\+ bryle|combo')],
    'lyzarske-bryle': [('Fotochromatické', r'fotochrom|photochrom|chromapop|transition|variotint|prizm'), ('Polarizační', r'polariz'), ('OTG (přes dioptrické brýle)', r'(^|\W)otg(\W|$)|pres dioptr|na dioptr'),
                       ('Zrcadlové', r'zrcadl|mirror|revo|iridium'), ('S výměnným sklem', r'vymenn|2 skl|dvoje skl|\+ nahradni'),
                       ('Magnetická výměna zorníků', r'magnet|magne.?lens|quick ?lens'), ('Dvojsklo / dvojitý zorník', r'dvojsklo|dvojit\w* (zornik|sklo)|double|dual lens|doubleflex'),
                       ('Antifog', r'anti ?fog|protiroset|proti zamlz|nezamlz|odmlz')],
    'lyzarske-kalhoty': [('S laclem / kšandami', r'lacl|ksand|sle(\W|$)|bib(\W|$)|bibs'), ('Zateplené', r'zateplen|insulat|primaloft|(^|\W)prosiv'), ('Softshell', r'softshell'), ('Slim střih', r'(^|\W)slim(\W|$)')],
    'lyzarske-bundy': [('S kapucí', r'kapuc|hood'), ('Zateplené', r'zateplen|insulat|primaloft|(^|\W)prosiv|perov|(^|\W)down(\W|$)'), ('Softshell', r'softshell'), ('2v1 / 3v1', r'2v1|2 v 1|3v1|3 v 1|s vest')],
    'lyzarske-kombinezy': [('Zateplené', r'zateplen|insulat|primaloft')],
    'lyzarske-rukavice': [('Palčáky', r'palcak|mitten|mitt(\W|$)'), ('Vyhřívané', r'vyhriva|heated'), ('S chrániči zápěstí', r'chranic|wrist guard|zapest'), ('Pro dotykový displej', r'touch|dotyk|screen')],
    'bezecke-lyze': [('S tulením pásem (skin)', r'skin|tuleni|zaber|mohair|mohero'), ('Šupinové', r'supin|fishscale|nowax|no-wax|zero'), ('S vázáním', r's vazanim|\+ vazani|set |komplet|combi set')],
    'bezecke-boty': [('Skate (bruslení)', r'skate|bruslen'), ('Klasika', r'klasik|classic'), ('Kombi', r'combi|kombi|prolink|turing|touring'), ('Zateplené', r'zateplen|insulat|thinsulate|arctic')],
    'bezecke-vazani': [('NNN', r'(^|\W)nnn(\W|$)'), ('SNS', r'(^|\W)sns(\W|$)'), ('Prolink', r'prolink'), ('NIS', r'(^|\W)nis(\W|$)|turnamic|xcelerator')],
    'snowboardova-vazani': [('Rychloupínací (Flow, step-in)', r'flow|step.?in|rychloup|nasl?apn|strap.?in|speed ?entry|clew|express|rapid'), ('Klasické (strap)', r'klasick|strap|(^|\W)2 pas'), ('Splitboard', r'splitboard')],
    'snowboardove-boty': [('Boa', r'(^|\W)boa(\W|$)|atop|bsl'), ('Rychlošněrování', r'rychlosner|speed ?lace|quick ?lace|fast ?lace'), ('Šněrovací', r'snerov|lace(\W|$)')],
    'snowboardy': [('Splitboard', r'splitboard')],
    'snowboardove-sety': [('Splitboard', r'splitboard'), ('S dětským vázáním', r'detsk\w* (snb )?vazani|wildcat|(^|\W)s160')],
    'skialpove-lyze': [('Set s pásy', r'set|komplet|s pasy|\+ pasy|s vazanim'), ('Freeride', r'freerid|backcountry|powder'), ('Závodní (race)', r'(^|\W)race|skimo|competition|zavod|pierra|(^|\W)wc(\W|$)')],
    'skialpove-boty': [('Race / lehké', r'(^|\W)race|skimo|pierra|lehk|zavod|ultra'), ('Freeride', r'freerid|backcountry'), ('Boa', r'(^|\W)boa(\W|$)')],
    'skialpove-vazani': [('Pin / tech', r'tech|pin(\W|$)|dynafit|speed|race'), ('Rámové', r'ramov|frame|hybrid|duke|kingpin|shift')],
    'lyzarske-boty': [('Boa / rychlé zapínání', r'(^|\W)boa(\W|$)|rychl|speedfit|speed ?mach'), ('Pro širokou nohu', r'sirok|wide|(^|\W)10[2-4] ?mm'), ('Walk / do chůze', r'walk|hike|touring|freetour|(^|\W)tr(\W|$)')],
    'lyzarske-vazani': [('Pro širokou botu', r'(^|\W)1[0-2]\d ?mm|sirok|wide')],
    'lyzarske-vosky': [('Sprej / tekutý', r'sprej|spray|tekut|liquid|rychlovosk'), ('Tuhý', r'tuh|bloc|block|hot|wax(\W|$)|vosk(\W|$)'), ('Základní', r'zaklad|base'), ('Čistič / odstraňovač', r'odstran|remover|cistic|cleaner')],
    'lyzarske-vaky-a-tasky': [('Na lyže', r'na lyze|ski bag|skibag|obal na lyz|vak na lyz|lyzar.{0,6} vak'), ('Na boty', r'na boty|boot bag|bootbag|batoh na boty'), ('Na snowboard', r'snowboard|board bag')],
    'lyzarske-cepice-a-nakrcniky': [('Čepice', r'cepic|beanie|kulich'), ('Nákrčník', r'nakrcn|neck|tube|multifunk|bandana|snood'), ('Čelenka', r'celenk|headband'), ('Kukla / šátek', r'kukla|balaclava|satek')],
}
FLEX_CATS = {'lyzarske-boty', 'skialpove-boty'}
FLEX = [(70, 'do 70 (měkká)'), (95, '80–90 (střední)'), (115, '100–110 (pevná)'), (999, '120 a více (závodní)')]
TERMO_TYPE = [('Set (tričko + kalhoty)', r'(^|\W)(set|komplet|souprav)(\W|$)'), ('Tričko / body', r'tricko|triko|top(\W|$)|body|mikina|rolak|rollneck|zip neck|dlouhy rukav|long sleeve'),
              ('Kalhoty / spodky', r'kalhoty|spodky|spodni|legin|long john|pants|tights|boxerk|slip'), ('Ponožky', r'ponoz|podkolenk'), ('Kukla / čelenka', r'kukla|celenk|nakrcn')]


def winter_params(t, cat, chain, desc=''):
    """Ski / snowboard length, type of use and the water column of ski clothing, read from the folded titles."""
    out = []
    if cat in SKIS | BOARDS:
        buckets = LEN_BUCKETS_BOARD if cat in BOARDS else LEN_BUCKETS_SKI
        lo, hi = (120, 175) if cat in BOARDS else (60, 215)
        for m in re.finditer(r'(?<![\d.,/x+-])(\d{2,3})(?![\d.,]|\s?(mm|g|ml|w|l|kc|%|v\b|ah|mah|cm\s?x))', t):
            n = int(m.group(1))
            if lo <= n <= hi and not re.search(r'(^|\W)(20\d\d|2[5-9])(\W|$)', m.group(0)):
                out.append(('delka', next(lbl for top, lbl in buckets if n < top)))
                break
        for name, rx in TYPE_RULES:
            if re.search(rx, t):
                out.append(('typ', name))
                break
    if 'lyzarske-obleceni' in chain and cat in ('lyzarske-bundy', 'lyzarske-kalhoty', 'lyzarske-kombinezy'):
        m = re.search(MEMBRANE, t)
        if m:
            n = int(m.group(1) or m.group(2) or 0) * 1000 if (m.group(1) or m.group(2)) else int(m.group(3))
            if 1000 <= n <= 40000:
                out.append(('membrana', 'do 5 000 mm' if n < 5000 else '5 000–9 999 mm' if n < 10000 else '10 000–19 999 mm' if n < 20000 else '20 000 mm a více'))
    for rx_cat in [cat]:
        ft = t + ' ' + desc if cat in GOGGLE_CATS or cat in BOARDS else t
        for name, rx in FEATURES.get(rx_cat, []):
            if re.search(rx, ft):
                out.append(('vlastnost', name))
    if cat in BOARDS or cat in GOGGLE_CATS:
        out += spec_params(t, desc, cat, chain)
    if cat in FLEX_CATS:
        m = re.search(r'(?<![\d.,/-])(5\d|[6-9]\d|1[0-4]\d)(?![\d.,]|\s?(cm|mm|l|g|w|kc|%|/))', t)
        if m and int(m.group(1)) % 5 == 0:
            n = int(m.group(1))
            out.append(('flex', next(lbl for top, lbl in FLEX if n < top)))
    if cat == 'lyzarske-termopradlo':
        for name, rx in TERMO_TYPE:
            if re.search(rx, t):
                out.append(('typ', name))
                break
    return out


# ---- specs read from the product description (audit 3. 11. 2026: snowboards, goggles, sleeping bags) ----
GOGGLE_CATS = {'lyzarske-bryle'}
SEPARATE_BAG = 'spaci-pytle'
FILTER_CAT = {'0': 'S0 (čiré, noc a mlha)', '1': 'S1 (zataženo)', '2': 'S2 (proměnlivo)', '3': 'S3 (slunečno)', '4': 'S4 (ledovec)'}
SB_LEVEL = [('Začátečník', r'zacatecn|zacatek|beginner|entry|zacinajic|prvni (snowboard|deska)'), ('Pokročilý', r'pokrocil|intermediate|advanced|zkusen'), ('Expert / závodní', r'expert|zavodn|profesion|pro riders?|elite|racing')]
SB_PROFILE = [('Hybrid (camber + rocker)', r'hybrid|camber.{0,20}rocker|rocker.{0,20}camber|kombinovan\w* profil|combi camber'), ('Rocker', r'(^|\W)rocker|reverse camber|banana|bez camber'),
              ('Camber', r'(^|\W)camber|pozitivn\w* prohnut'), ('Flat (rovný)', r'(^|\W)flat(\W|$)|rovn\w* profil|zero camber')]
SB_SHAPE = [('Directional twin', r'directional twin|dir\.? twin|smerov\w* twin'), ('Twin', r'(^|\W)true twin|(^|\W)twin(\W|$)|symetrick'), ('Directional', r'directional|smerov')]
BAG_TEMP = [(-10, 'Extrémní (pod −10 °C)'), (0, 'Zimní (−10 až 0 °C)'), (10, 'Přechodový (0 až 10 °C)'), (99, 'Letní (nad 10 °C)')]
BAG_FILL = [('Péřová', r'perov|(^|\W)peri(\W|$)|(^|\W)down(\W|$)|husi|kachni|duck|goose|(^|\W)pera(\W|$)'), ('Syntetická', r'syntetick|duta vlakn|dutym vlaknem|primaloft|climashield|thermolite|hollow|isosoft|polarguard|vlakn\w* vypln|3d vlakn')]
BAG_TYPE = [('Mumie', r'mumi|(^|\W)mummy'), ('Dekový', r'dekov|(^|\W)deka(\W|$)|(^|\W)blanket|kvadrat|obdelnik')]
BAG_SEASON = [('Zimní', r'(^|\W)zimn|(^|\W)4 ?(season|sezon)|ctyr ?sezon|(^|\W)5 ?(season|sezon)|extreme'), ('Třísezónní', r'(^|\W)3 ?(season|sezon)|tri ?sezon|jaro.{0,10}podzim|prechodov'), ('Letní', r'(^|\W)letn|(^|\W)summer')]
BAG_WEIGHT = [(700, 'do 700 g'), (1200, '700–1 200 g'), (2000, '1,2–2 kg'), (99999, 'nad 2 kg')]


def _first(rules, t):
    return next((n for n, rx in rules if re.search(rx, t)), None)


def spec_params(t, d, cat, chain):
    """Specs that need the description (d = folded, tag-free, first ~1400 characters); t = folded titles."""
    out = []
    full = t + ' ' + d
    if cat in BOARDS:
        lead = t + ' ' + d[:420]
        for lbl, rx in SB_SHAPE:
            if re.search(rx, full):
                out.append(('tvar', lbl))
                break
        pr = _first(SB_PROFILE, full)
        if pr:
            out.append(('profil', pr))
        m = re.search(r'(tuhost|flex\w*|ohebnost|pruznost)[^.]{0,40}?(mekk|stredn|tuh|stiff|soft|medium)', full)
        if m:
            out.append(('tuhost', 'Měkká' if m.group(2) in ('mekk', 'soft') else 'Střední' if m.group(2) in ('stredn', 'medium') else 'Tuhá'))
        for lbl, rx in SB_LEVEL:
            if re.search(rx, lead):
                out.append(('uroven', lbl))
        types = [n for n, rx in TYPE_RULES if n in ('Freeride', 'Freestyle', 'All-mountain', 'Carving') and re.search(rx, lead)]
        out += [('typ', n) for n in types[:2]]
    if cat in GOGGLE_CATS:
        cats = set()
        for m in re.finditer(r'(?:cat\w*\.?|kat\w*\.?|kategori\w*\.?|filtr\w*)\s?([0-4])(?:\s?[-/+–]\s?([0-4]))?|(?<![a-z0-9])s([0-4])(?:\s?[-/+–]\s?s?([0-4]))?(?![a-z0-9])', full):
            nums = [int(x) for x in m.groups() if x]
            for n in range(min(nums), max(nums) + 1):
                cats.add(str(n))
        out += [('filtr', FILTER_CAT[c]) for c in sorted(cats)[:3]]
        if re.search(r'cylindr', full):
            out.append(('tvar', 'Cylindrické'))
        elif re.search(r'sfer|toric', full):
            out.append(('tvar', 'Sférické'))
    if SEPARATE_BAG in chain:
        x = re.sub(r'(?<![\d)])[−–—](?=\d)', '-', full).replace('−', '-')
        m = re.search(r'(?<![\d,.])(-?\d{1,2})\s?°', t.replace('−', '-')) or re.search(r'komfort\w*[^0-9-]{0,25}(-?\d{1,2})\s?°', x) or re.search(r'(?:extrem|limit|do)\w*\s*[^0-9-]{0,12}(-?\d{1,2})\s?°', x)
        if m:
            n = int(m.group(1))
            if -50 <= n <= 30:
                out.append(('teplota', next(lbl for top, lbl in BAG_TEMP if n < top)))
        fl = _first(BAG_FILL, full)
        if fl:
            out.append(('vypln', fl))
        ty = _first(BAG_TYPE, t + ' ' + d[:300])
        if ty:
            out.append(('typ', ty))
        zp = re.search(r'(lev\w*|prav\w*) zip', t + ' ' + d[:300])
        if zp:
            out.append(('zip', 'Levý zip' if zp.group(1).startswith('lev') else 'Pravý zip'))
        se = _first(BAG_SEASON, full)
        if se:
            out.append(('sezona', se))
        w = re.search(r'(?:hmotnost|vaha)\w*[^0-9]{0,22}(\d[\d., ]{0,6}\d|\d)\s?(kg|g)(?![a-z])', d)
        if w:
            try:
                v = float(w.group(1).replace(' ', '').replace(',', '.'))
                g = v * 1000 if w.group(2) == 'kg' else v
                if 150 <= g <= 9000:
                    out.append(('vaha', next(lbl for top, lbl in BAG_WEIGHT if g < top)))
            except ValueError:
                pass
    return out


def desc_text(html, n=1400):
    """Folded, tag-free start of a product description (the source of the spec filters)."""
    return K.fold(re.sub(r'<[^>]+>', ' ', html or ''))[:n]


# 16. 11. 2026: sneaker / shoe models (MM: 543k searches a month for model names, reports/sporteka/content-gap-2026-11d.md). A product gets
# ('model', name) when its titles name the model; models that need the brand to be unambiguous ("530", "Forum", "Suede") require it.
# (name shown in the filter, landing base category, required brand regex or '', model regex) — the landing slug is valueSlug(name).
MODELS = [
    ('Nike Air Force 1', 'tenisky', '', r'air ?force( ?1|1)?(\W|$)|(^|\W)af ?1(\W|$)'),
    ('Nike Air Max', 'tenisky', '', r'air ?max(\W|$|\d)'),
    ('Jordan 4', 'tenisky', '', r'jordan (4|iv)(\W|$)|(^|\W)aj ?4(\W|$)'),
    ('Jordan 1', 'tenisky', '', r'jordan (1|i)(\W|$)|(^|\W)aj ?1(\W|$)'),
    ('Nike Dunk', 'tenisky', '', r'(^|\W)dunk(\W|$)'),
    ('Nike Cortez', 'tenisky', '', r'cortez'),
    ('Nike Vomero', 'sportovni-obuv', '', r'vomero'),
    ('Nike Pegasus', 'sportovni-obuv', r'nike', r'pegasus'),
    ('Adidas Samba', 'tenisky', r'adidas', r'(^|\W)samba(\W|$)'),
    ('Adidas Spezial', 'tenisky', '', r'spezial'),
    ('Adidas Handball Spezial', 'tenisky', '', r'handball spezial'),
    ('Adidas Campus', 'tenisky', r'adidas', r'(^|\W)campus(\W|$)'),
    ('Adidas Gazelle', 'tenisky', r'adidas', r'gazelle'),
    ('Adidas Superstar', 'tenisky', r'adidas', r'superstar'),
    ('Adidas Stan Smith', 'tenisky', '', r'stan ?smith'),
    ('Adidas Forum', 'tenisky', r'adidas', r'(^|\W)forum(\W|$)'),
    ('Adidas Ultraboost', 'sportovni-obuv', '', r'ultra ?boost'),
    ('New Balance 530', 'tenisky', r'new balance|(^|\W)nb(\W|$)', r'(^|\W)m?w?u?530(\W|$)'),
    ('New Balance 550', 'tenisky', r'new balance|(^|\W)nb(\W|$)', r'(^|\W)(bb|gsb|psb)?550(\W|$)'),
    ('New Balance 574', 'tenisky', r'new balance|(^|\W)nb(\W|$)', r'(^|\W)[mwug]?l?574(\W|$)'),
    ('New Balance 327', 'tenisky', r'new balance|(^|\W)nb(\W|$)', r'(^|\W)[mwu]?s?327(\W|$)'),
    ('New Balance 2002R', 'tenisky', r'new balance|(^|\W)nb(\W|$)', r'2002 ?r'),
    ('New Balance 9060', 'tenisky', r'new balance|(^|\W)nb(\W|$)', r'(^|\W)u?9060'),
    ('New Balance 1906', 'tenisky', r'new balance|(^|\W)nb(\W|$)', r'(^|\W)m?1906'),
    ('Asics Gel-NYC', 'tenisky', '', r'gel.?nyc'),
    ('Asics Gel-Kayano', 'sportovni-obuv', '', r'kayano'),
    ('Asics Gel-1130', 'tenisky', r'asics', r'(^|\W)(gel.?)?1130(\W|$)'),
    ('Vans Old Skool', 'tenisky', '', r'old ?skool'),
    ('Converse Chuck Taylor', 'tenisky', r'converse|chuck', r'chuck ?taylor|chuck ?70|all ?star'),
    ('Puma Suede', 'tenisky', r'puma', r'(^|\W)suede(\W|$)'),
    ('Puma Palermo', 'tenisky', r'puma', r'palermo'),
    ('Puma Speedcat', 'tenisky', '', r'speedcat'),
    ('Salomon Speedcross', 'sportovni-obuv', '', r'speedcross'),
    ('Salomon XT-6', 'sportovni-obuv', r'salomon', r'xt.?6(\W|$)'),
    ('Salomon X Ultra', 'sportovni-obuv', r'salomon', r'x.?ultra'),
    ('Merrell Moab', 'sportovni-obuv', '', r'(^|\W)moab(\W|$)'),
    ('On Cloudmonster', 'sportovni-obuv', '', r'cloudmonster'),
    ('Hoka Clifton', 'sportovni-obuv', r'hoka', r'clifton'),
    ('Nike Tech Fleece', 'sportovni-obleceni', '', r'tech ?fleece'),
    # 22. 11. 2026 wave 34 (Ahrefs gap vs Sportvision / Top4running: reports/sporteka/gap/ahrefs-gap-2026-11-22.md)
    ('Nike Air Max 90', 'tenisky', '', r'air ?max ?90'),
    ('Nike Air Max 95', 'tenisky', '', r'air ?max ?95'),
    ('Nike Air Max Plus', 'tenisky', '', r'air ?max ?(plus|tn)(\W|$)'),
    ('Nike Air Max 97', 'tenisky', '', r'air ?max ?97'),
    ('Nike Air Max 1', 'tenisky', '', r'air ?max ?1(\W|$)'),
    ('Nike P-6000', 'tenisky', '', r'(^|\W)p.?6000'),
    ('Nike V2K Run', 'tenisky', '', r'(^|\W)v2k'),
    ('Adidas Campus 00s', 'tenisky', r'adidas', r'campus ?00s'),
    ('New Balance 740', 'tenisky', r'new balance|(^|\W)nb(\W|$)', r'(^|\W)[mwu]?740'),
    ('New Balance 990', 'tenisky', r'new balance|(^|\W)nb(\W|$)', r'(^|\W)[mwu]?990'),
    ('Adidas Adizero Evo SL', 'sportovni-obuv', '', r'evo ?sl(\W|$)'),
    ('Nike Metcon', 'sportovni-obuv', '', r'metcon'),
    ('Nike Pegasus Trail', 'sportovni-obuv', r'nike', r'pegasus.?trail'),
    ('Hoka Speedgoat', 'sportovni-obuv', r'hoka', r'speedgoat'),
    ('Hoka Bondi', 'sportovni-obuv', r'hoka', r'(^|\W)bondi'),
    ('Hoka Challenger', 'sportovni-obuv', r'hoka', r'challenger'),
    ('Asics Gel-Nimbus', 'sportovni-obuv', r'asics', r'nimbus'),
    ('Asics Novablast', 'sportovni-obuv', r'asics', r'novablast'),
    ('Altra Olympus', 'sportovni-obuv', r'altra', r'olympus'),
    ('Brooks Ghost', 'sportovni-obuv', r'brooks', r'ghost'),
    ('Salomon XA Pro 3D', 'sportovni-obuv', r'salomon', r'xa.?pro'),
]
_MODELS = [(n, base, re.compile(b) if b else None, re.compile(m)) for n, base, b, m in MODELS]


def models(t, chain):
    """('model', name) for a shoe (or Nike Tech Fleece clothing) whose titles name a known model."""
    out = []
    for n, base, b, m in _MODELS:
        if base not in chain and not (base == 'tenisky' and 'sportovni-obuv' in chain):
            continue
        if m.search(t) and (b is None or b.search(t)):
            out.append(('model', n))
    return out


def _chain(slug):
    out, t = [], K.BY_SLUG.get(slug)
    while t:
        out.append(t[1])
        t = K.BY_SLUG.get(t[3]) if t[3] else None
    return out


def params(texts, cat, desc=''):
    """texts = the folded titles of all offers of the product (one string); cat = the product's category slug."""
    t = texts
    chain = set(_chain(cat))
    out = []
    mats = [name for name, rx in MATERIAL if re.search(rx, t)]
    if chain & (WEAR | {'outdoor', 'kemping', 'cyklistika', 'zimni-sporty', 'vodni-sporty', 'fitness', 'rybareni'}):
        out += [('material', m) for m in mats]
    if chain & WEAR:
        seas = [name for name, rx in SEASON if re.search(rx, t)]
        out += [('sezona', x) for x in seas[:2]]
    if chain & {'sportovni-obuv', 'sportovni-obleceni'}:
        out += models(t, chain)
    if chain & BAGS and cat != 'lahve-a-termosky':
        m = re.search(r'(?<![\d.,])(\d{1,3})\s?l(?![a-z])', t)
        if m:
            n = int(m.group(1))
            if 5 <= n <= 150:
                out.append(('objem', 'do 20 l' if n < 20 else '20–30 l' if n < 30 else '30–40 l' if n < 40 else '40–55 l' if n < 55 else '55 l a více'))
    if chain & SKIS_ALL:
        out += winter_params(t, cat, chain, desc)
    if SEPARATE_BAG in chain:
        out += spec_params(t, desc, cat, chain)
    if 'stany' in chain:
        m = re.search(r'(?<![\d.,])([1-9])\s?(os\b|osob|osoby|mistn|person|p\b|man\b)|(?<![\d.,])([1-9])\s?-\s?(os|osob)', t)
        if m:
            n = int(m.group(1) or m.group(3))
            out.append(('osoby', '1 osoba' if n == 1 else f'{n} osoby' if n < 5 else '5 a více osob'))
    return out
