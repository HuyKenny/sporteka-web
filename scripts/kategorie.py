"""sporteka.cz — category tree and the rules that put a feed item into it.

TREE: (id, slug, name, parent_slug). Ids are stable (they are the D1 primary keys): sections are 100, 200 …,
their children 101, 102 …; grandchildren 1xx0 + n. Never renumber an existing category, only add.

categorize(item) → slug or None (None = not our assortment). Rules run on ASCII-folded, lower-cased text:
  path  = the shop's own category path (productType), " > " separated
  title = product name
  gpc   = Google product category
The first matching rule wins, so specific rules come before generic ones. Every new rule must be checked on a sample
of real titles (scripts/katalog.py --report prints unmapped paths and a sample per category).
"""
import html
import re
import unicodedata

TREE = [
    # ---------- clothing ----------
    (100, 'sportovni-obleceni', 'Sportovní oblečení', None),
    (101, 'sportovni-bundy', 'Sportovní bundy a vesty', 'sportovni-obleceni'),
    (1011, 'lyzarske-bundy', 'Lyžařské a snowboardové bundy', 'lyzarske-obleceni'),
    (1012, 'softshellove-bundy', 'Softshellové bundy', 'sportovni-bundy'),
    (1013, 'zimni-bundy', 'Zimní a péřové bundy', 'sportovni-bundy'),
    (1014, 'nepromokave-bundy', 'Nepromokavé a outdoorové bundy', 'sportovni-bundy'),
    (1015, 'sportovni-vesty', 'Vesty', 'sportovni-bundy'),
    (1016, 'sportovni-bundy-jaro-podzim', 'Jarní a podzimní bundy', 'sportovni-bundy'),
    (102, 'mikiny', 'Mikiny', 'sportovni-obleceni'),
    (1021, 'fleecove-mikiny', 'Fleecové mikiny', 'mikiny'),
    (1022, 'funkcni-mikiny', 'Funkční mikiny', 'mikiny'),
    (103, 'sportovni-tricka', 'Trička a tílka', 'sportovni-obleceni'),
    (1031, 'funkcni-tricka', 'Funkční trička', 'sportovni-tricka'),
    (1032, 'tilka', 'Tílka a topy', 'sportovni-tricka'),
    (1033, 'polokosile', 'Polokošile', 'sportovni-tricka'),
    (104, 'sportovni-kalhoty', 'Sportovní kalhoty', 'sportovni-obleceni'),
    (1041, 'lyzarske-kalhoty', 'Lyžařské a snowboardové kalhoty', 'lyzarske-obleceni'),
    (1042, 'outdoorove-kalhoty', 'Outdoorové kalhoty', 'sportovni-kalhoty'),
    (1043, 'teplaky', 'Tepláky', 'sportovni-kalhoty'),
    (105, 'sportovni-kratasy', 'Kraťasy', 'sportovni-obleceni'),
    (106, 'leginy', 'Legíny', 'sportovni-obleceni'),
    (107, 'soupravy', 'Soupravy a komplety', 'sportovni-obleceni'),
    (108, 'termopradlo', 'Funkční a termo prádlo', 'sportovni-obleceni'),
    (109, 'sportovni-podprsenky', 'Sportovní podprsenky', 'sportovni-obleceni'),
    (110, 'sportovni-spodni-pradlo', 'Sportovní spodní prádlo', 'sportovni-obleceni'),
    (111, 'sportovni-ponozky', 'Sportovní ponožky', 'sportovni-obleceni'),
    (112, 'cepice-a-celenky', 'Čepice, kšiltovky a čelenky', 'sportovni-obleceni'),
    (113, 'sportovni-rukavice', 'Rukavice', 'sportovni-obleceni'),
    (114, 'nakrcniky-a-satky', 'Nákrčníky a kukly', 'sportovni-obleceni'),
    (115, 'plavky', 'Plavky', 'sportovni-obleceni'),
    (1151, 'damske-plavky', 'Dámské plavky', 'plavky'),
    (1152, 'panske-plavky', 'Pánské plavky', 'plavky'),
    (1153, 'detske-plavky', 'Dětské plavky', 'plavky'),
    (116, 'dresy', 'Dresy', 'sportovni-obleceni'),
    (117, 'sportovni-sukne-a-saty', 'Sportovní sukně a šaty', 'sportovni-obleceni'),
    (120, 'kosile', 'Turistické a outdoorové košile', 'sportovni-obleceni'),
    # ---------- footwear ----------
    (200, 'sportovni-obuv', 'Sportovní obuv', None),
    (201, 'bezecka-obuv', 'Běžecké boty', 'sportovni-obuv'),
    (2011, 'silnicni-bezecke-boty', 'Silniční běžecké boty', 'bezecka-obuv'),
    (2012, 'trailove-boty', 'Trailové běžecké boty', 'bezecka-obuv'),
    (202, 'trekova-obuv', 'Trekové boty', 'sportovni-obuv'),
    (2021, 'nizke-trekove-boty', 'Nízké trekové boty', 'trekova-obuv'),
    (2022, 'vysoke-trekove-boty', 'Vysoké trekové boty', 'trekova-obuv'),
    (203, 'tenisky', 'Tenisky a volnočasové boty', 'sportovni-obuv'),
    (204, 'kopacky', 'Kopačky', 'sportovni-obuv'),
    (205, 'salova-obuv', 'Sálová a halová obuv', 'sportovni-obuv'),
    (206, 'treninkova-obuv', 'Fitness a tréninková obuv', 'sportovni-obuv'),
    (207, 'tenisova-obuv', 'Tenisová obuv', 'sportovni-obuv'),
    (208, 'zimni-obuv', 'Zimní boty a sněhule', 'sportovni-obuv'),
    (209, 'sandaly', 'Sportovní sandály', 'sportovni-obuv'),
    (210, 'pantofle-a-zabky', 'Pantofle a žabky', 'sportovni-obuv'),
    (211, 'barefoot-obuv', 'Barefoot boty', 'sportovni-obuv'),
    (2111, 'ponozkoboty', 'Ponožkoboty', 'barefoot-obuv'),
    (212, 'obuv-do-vody', 'Boty do vody', 'sportovni-obuv'),
    (213, 'holinky', 'Holínky', 'sportovni-obuv'),
    (214, 'basketbalova-obuv', 'Basketbalové boty', 'sportovni-obuv'),
    (215, 'doplnky-k-obuvi', 'Tkaničky, vložky a péče o boty', 'sportovni-obuv'),
    # ---------- outdoor ----------
    (300, 'outdoor', 'Outdoor a turistika', None),
    (301, 'batohy', 'Batohy', 'outdoor'),
    (3011, 'turisticke-batohy', 'Turistické batohy', 'batohy'),
    (3012, 'mestske-batohy', 'Městské a sportovní batohy', 'batohy'),
    (302, 'sportovni-tasky', 'Sportovní tašky a ledvinky', 'outdoor'),
    (303, 'trekove-hole', 'Trekové a nordic walking hole', 'outdoor'),
    (304, 'celovky-a-svitilny', 'Čelovky a svítilny', 'outdoor'),
    (305, 'lahve-a-termosky', 'Láhve a termosky', 'outdoor'),
    (306, 'sportovni-bryle', 'Sportovní a sluneční brýle', 'outdoor'),
    (307, 'horolezectvi', 'Horolezectví a ferraty', 'outdoor'),
    (308, 'outdoor-doplnky', 'Outdoorové doplňky', 'outdoor'),
    (309, 'sportovni-hodinky', 'Sportovní hodinky a elektronika', 'outdoor'),
    (3091, 'chytre-hodinky', 'Chytré hodinky a fitness náramky', 'sportovni-hodinky'),
    # ---------- camping ----------
    (400, 'kemping', 'Kemping', None),
    (401, 'stany', 'Stany', 'kemping'),
    (402, 'spaci-pytle', 'Spací pytle', 'kemping'),
    (403, 'karimatky-a-matrace', 'Karimatky a matrace', 'kemping'),
    (404, 'kempingovy-nabytek', 'Kempingový nábytek', 'kemping'),
    (405, 'vareni-v-prirode', 'Vaření v přírodě', 'kemping'),
    (406, 'chladici-boxy', 'Chladicí boxy a tašky', 'kemping'),
    (407, 'hamaky', 'Hamaky', 'kemping'),
    (408, 'kempingove-doplnky', 'Kempingové doplňky', 'kemping'),
    # ---------- cycling ----------
    (500, 'cyklistika', 'Cyklistika', None),
    (501, 'jizdni-kola', 'Jízdní kola', 'cyklistika'),
    (5011, 'horska-kola', 'Horská kola', 'jizdni-kola'),
    (5012, 'elektrokola', 'Elektrokola', 'jizdni-kola'),
    (5013, 'silnicni-a-gravel-kola', 'Silniční a gravel kola', 'jizdni-kola'),
    (5014, 'detska-kola', 'Dětská kola a odrážedla', 'jizdni-kola'),
    (5015, 'trekingova-kola', 'Trekingová a městská kola', 'jizdni-kola'),
    (50121, 'trekingova-a-mestska-elektrokola', 'Trekingová a městská elektrokola', 'elektrokola'),
    (50122, 'horska-elektrokola', 'Horská elektrokola', 'elektrokola'),
    (50123, 'skladaci-elektrokola', 'Skládací elektrokola', 'elektrokola'),
    (50124, 'nakladni-elektrokola', 'Nákladní elektrokola', 'elektrokola'),
    (50131, 'skladaci-kola', 'Skládací kola', 'jizdni-kola'),
    (50132, 'bmx-a-dirt-kola', 'BMX a dirt kola', 'jizdni-kola'),
    (50141, 'odrazedla', 'Odrážedla', 'detska-kola'),
    # 3. 11. 2026: bike types as their own categories (feed titles carry the type; bike_rule gives only the parent)
    (50111, 'celoodpruzena-horska-kola', 'Celoodpružená horská kola', 'horska-kola'),
    (50112, 'fatbiky', 'Fatbiky', 'horska-kola'),
    (50133, 'gravel-kola', 'Gravel kola', 'silnicni-a-gravel-kola'),
    (50134, 'silnicni-kola', 'Silniční kola', 'silnicni-a-gravel-kola'),
    (50151, 'mestska-kola', 'Městská kola', 'trekingova-kola'),
    (50152, 'krosova-kola', 'Krosová kola', 'trekingova-kola'),
    (50153, 'damska-kola', 'Dámská kola', 'trekingova-kola'),
    (50142, 'detska-kola-12-14-palcu', 'Dětská kola 12 a 14 palců', 'detska-kola'),
    (50143, 'detska-kola-16-palcu', 'Dětská kola 16 palců', 'detska-kola'),
    (50144, 'detska-kola-20-palcu', 'Dětská kola 20 palců', 'detska-kola'),
    (50145, 'detska-kola-24-palcu', 'Dětská kola 24 palců', 'detska-kola'),
    (50146, 'detske-trikolky', 'Dětské tříkolky', 'detska-kola'),
    (501211, 'mestska-elektrokola', 'Městská elektrokola', 'trekingova-a-mestska-elektrokola'),
    (501212, 'trekingova-elektrokola', 'Trekingová elektrokola', 'trekingova-a-mestska-elektrokola'),
    (50125, 'fatbike-elektrokola', 'Fatbike elektrokola', 'elektrokola'),
    (50126, 'silnicni-a-gravel-elektrokola', 'Silniční a gravel elektrokola', 'elektrokola'),
    (50127, 'damska-elektrokola', 'Dámská elektrokola', 'elektrokola'),
    (50128, 'detska-elektrokola', 'Dětská a juniorská elektrokola', 'elektrokola'),
    (5021, 'detske-cyklohelmy', 'Dětské cyklohelmy', 'cyklisticke-helmy'),
    (5022, 'mtb-a-integralni-helmy', 'MTB, enduro a integrální helmy', 'cyklisticke-helmy'),
    (5023, 'silnicni-cyklohelmy', 'Silniční a gravel helmy', 'cyklisticke-helmy'),
    (5024, 'mestske-cyklohelmy', 'Městské cyklohelmy', 'cyklisticke-helmy'),
    (5031, 'cyklisticke-dresy', 'Cyklistické dresy', 'cyklisticke-obleceni'),
    (5032, 'cyklisticke-kratasy-a-kalhoty', 'Cyklistické kraťasy a kalhoty', 'cyklisticke-obleceni'),
    (5033, 'cyklisticke-bundy-a-vesty', 'Cyklistické bundy a vesty', 'cyklisticke-obleceni'),
    (5034, 'cyklisticke-rukavice', 'Cyklistické rukavice', 'cyklisticke-obleceni'),
    (5035, 'cyklisticke-ponozky', 'Cyklistické ponožky', 'cyklisticke-obleceni'),
    (5036, 'cyklisticke-navleky', 'Návleky a rukávky', 'cyklisticke-obleceni'),
    (5051, 'cyklisticke-bryle', 'Cyklistické brýle', 'cyklo-prislusenstvi'),
    (5052, 'cyklo-chranice', 'Chrániče pro cyklisty', 'cyklo-prislusenstvi'),
    (5053, 'cyklo-lahve-a-drzaky', 'Lahve, košíky a držáky telefonu', 'cyklo-prislusenstvi'),
    (5054, 'cyklo-zvonky-a-zrcatka', 'Zvonky a zrcátka', 'cyklo-prislusenstvi'),
    (502, 'cyklisticke-helmy', 'Cyklistické helmy', 'cyklistika'),
    (503, 'cyklisticke-obleceni', 'Cyklistické oblečení', 'cyklistika'),
    (504, 'cyklisticka-obuv', 'Cyklistické tretry', 'cyklistika'),
    (505, 'cyklo-prislusenstvi', 'Cyklo příslušenství', 'cyklistika'),
    (5055, 'cyklo-stojany-a-drzaky', 'Stojany a držáky na kola', 'cyklo-prislusenstvi'),
    (506, 'cyklo-dily', 'Díly a pláště', 'cyklistika'),
    # ---------- winter ----------
    (600, 'zimni-sporty', 'Zimní sporty', None),
    (601, 'sjezdove-lyze', 'Sjezdové lyže', 'zimni-sporty'),
    (602, 'lyzarske-boty', 'Lyžařské boty', 'zimni-sporty'),
    (603, 'lyzarske-helmy', 'Lyžařské helmy', 'zimni-sporty'),
    (604, 'lyzarske-bryle', 'Lyžařské brýle', 'zimni-sporty'),
    (6041, 'nahradni-zorniky', 'Náhradní zorníky a příslušenství k brýlím', 'lyzarske-bryle'),
    (605, 'bezecke-lyzovani', 'Běžecké lyžování', 'zimni-sporty'),
    (606, 'snowboarding', 'Snowboarding', 'zimni-sporty'),
    (607, 'brusle', 'Zimní brusle', 'zimni-sporty'),
    (608, 'sane-a-boby', 'Sáně a boby', 'zimni-sporty'),
    (609, 'lyzarske-doplnky', 'Lyžařské hůlky a doplňky', 'zimni-sporty'),
    (610, 'skialpinismus', 'Skialpinismus', 'zimni-sporty'),
    (6100, 'lyzarske-obleceni', 'Lyžařské a snowboardové oblečení', 'zimni-sporty'),
    (6101, 'lyzarske-kombinezy', 'Lyžařské kombinézy a overaly', 'lyzarske-obleceni'),
    (6102, 'lyzarske-rukavice', 'Lyžařské rukavice a palčáky', 'lyzarske-obleceni'),
    (6103, 'lyzarske-termopradlo', 'Lyžařské termoprádlo', 'lyzarske-obleceni'),
    (6104, 'lyzarske-cepice-a-nakrcniky', 'Lyžařské čepice a nákrčníky', 'lyzarske-obleceni'),
    (6111, 'lyze-komplety', 'Lyže s vázáním (komplety)', 'sjezdove-lyze'),
    (6112, 'detske-lyze', 'Dětské lyže', 'sjezdove-lyze'),
    (6113, 'lyzarske-vazani', 'Lyžařské vázání', 'sjezdove-lyze'),
    (6121, 'snowboardy', 'Snowboardy', 'snowboarding'),
    (6125, 'snowboardove-sety', 'Snowboardy s vázáním (sety)', 'snowboardy'),
    (6122, 'snowboardove-boty', 'Snowboardové boty', 'snowboarding'),
    (6123, 'snowboardova-vazani', 'Snowboardová vázání', 'snowboarding'),
    (6124, 'snowboardove-chranice', 'Chrániče páteře a boků na lyže a snowboard', 'snowboarding'),
    (6131, 'bezecke-lyze', 'Běžecké lyže', 'bezecke-lyzovani'),
    (6132, 'bezecke-boty', 'Boty na běžky', 'bezecke-lyzovani'),
    (6133, 'bezecke-vazani', 'Vázání na běžky', 'bezecke-lyzovani'),
    (6141, 'skialpove-lyze', 'Skialpové lyže', 'skialpinismus'),
    (6142, 'skialpove-boty', 'Skialpové boty', 'skialpinismus'),
    (6143, 'skialpove-vazani', 'Skialpová vázání', 'skialpinismus'),
    (6144, 'skialpove-pasy', 'Skialpové stoupací pásy', 'skialpinismus'),
    (6151, 'lyzarske-vosky', 'Vosky a mazání na lyže a snowboardy', 'lyzarske-doplnky'),
    (6152, 'lyzarske-vaky-a-tasky', 'Vaky a tašky na lyže a boty', 'lyzarske-doplnky'),
    (6161, 'snezky', 'Sněžnice', 'zimni-sporty'),
    # ---- 16. 11. 2026 January wave (reports/sporteka/audit-2026-11-16.md, MM seasonality: January peak) ----
    (6162, 'vyhrivane-obleceni', 'Vyhřívané oblečení a doplňky', 'zimni-sporty'),
    (6081, 'kluzaky-na-snih', 'Kluzáky na sníh', 'sane-a-boby'),
    (7022, 'posilovaci-veze', 'Posilovací věže a multistanice', 'posilovaci-stroje'),
    (7054, 'gymnasticke-mice', 'Gymnastické a balanční míče', 'fitness-pomucky'),
    (7062, 'zatezove-vesty', 'Zátěžové vesty', 'funkcni-trenink'),
    (708021, 'glutamin', 'Glutamin', 'aminokyseliny-bcaa'),
    (708073, 'vitamin-d', 'Vitamín D a D3', 'vitaminy-a-mineraly'),
    (708074, 'vitamin-c', 'Vitamín C', 'vitaminy-a-mineraly'),
    (708075, 'zinek', 'Zinek', 'vitaminy-a-mineraly'),
    (70813, 'fit-potraviny', 'Fit potraviny a arašídová másla', 'sportovni-vyziva'),
    (6171, 'krasobruslarske-brusle', 'Krasobruslařské brusle', 'brusle'),
    (6172, 'rekreacni-brusle', 'Rekreační brusle na led', 'brusle'),
    # ---- 16. 11. 2026 January wave 2 (reports/sporteka/content-gap-2026-11c.md: MM January data + specialist shops' content gap) ----
    (708091, 'elektrolyty', 'Elektrolyty a solné tablety', 'iontove-napoje'),
    (708076, 'multivitaminy', 'Multivitamíny', 'vitaminy-a-mineraly'),
    (708061, 'l-karnitin', 'L-karnitin', 'spalovace-tuku'),
    (708112, 'probiotika', 'Probiotika', 'ostatni-doplnky-stravy'),
    (708113, 'tribulus', 'Tribulus terrestris (kotvičník)', 'ostatni-doplnky-stravy'),
    (708114, 'kurkuma', 'Kurkuma a kurkumin', 'ostatni-doplnky-stravy'),
    (708115, 'spirulina-chlorella', 'Spirulina, chlorella a zelené superpotraviny', 'ostatni-doplnky-stravy'),
    (3051, 'sejkry', 'Šejkry na protein', 'lahve-a-termosky'),
    (70531, 'balancni-podlozky-bosu', 'Balanční podložky a BOSU', 'balancni-pomucky'),
    (7063, 'medicinbaly', 'Medicinbaly a slam bally', 'funkcni-trenink'),
    (70611, 'zebriny', 'Žebřiny', 'hrazdy-a-bradla'),
    (7012, 'stojany-na-cinky', 'Stojany na činky a kotouče', 'cinky-a-kotouce'),
    (10151, 'reflexni-vesty', 'Reflexní vesty', 'sportovni-vesty'),
    (1141, 'kukly', 'Kukly (balaclavy)', 'nakrcniky-a-satky'),
    (6163, 'chranice-pater', 'Chrániče páteře', 'zimni-sporty'),
    (2151, 'impregnace', 'Impregnace a péče o boty a oblečení', 'doplnky-k-obuvi'),
    # ---- 16. 11. 2026 November wave 3 (reports/sporteka/content-gap-2026-11d.md: searched product types without a page) ----
    (1121, 'ksiltovky', 'Kšiltovky', 'cepice-a-celenky'),
    (1071, 'teplakove-soupravy', 'Teplákové soupravy', 'soupravy'),
    (10321, 'crop-topy', 'Crop topy', 'tilka'),
    (30211, 'ledvinky', 'Ledvinky', 'tasky-pres-rameno'),
    (3052, 'termohrnky', 'Termohrnky', 'lahve-a-termosky'),
    (4031, 'nafukovaci-matrace', 'Nafukovací matrace a lehátka', 'karimatky-a-matrace'),
    (4032, 'samonafukovaci-karimatky', 'Samonafukovací karimatky', 'karimatky-a-matrace'),
    (7091, 'tejpy', 'Tejpy a kineziologické pásky', 'bandaze-a-ortezy'),
    (10131, 'perove-bundy', 'Péřové bundy', 'zimni-bundy'),
    (10421, 'softshellove-kalhoty', 'Softshellové kalhoty', 'outdoorove-kalhoty'),
    (30121, 'batohy-na-notebook', 'Batohy na notebook', 'mestske-batohy'),
    (11511, 'jednodilne-plavky', 'Jednodílné plavky', 'damske-plavky'),
    (11512, 'dvoudilne-plavky', 'Dvoudílné plavky a bikiny', 'damske-plavky'),
    (2041, 'turfy', 'Turfy', 'kopacky'),
    (7035, 'steppery', 'Steppery', 'kardio-trenazery'),
    (11105, 'kompresni-ponozky', 'Kompresní ponožky a podkolenky', 'sportovni-ponozky'),
    (708022, 'arginin-a-citrulin', 'Arginin a citrulin', 'aminokyseliny-bcaa'),
    (50531, 'drzaky-na-mobil-na-kolo', 'Držáky na mobil na kolo', 'cyklo-lahve-a-drzaky'),
    (4081, 'piknikove-deky', 'Piknikové deky a koše', 'kempingove-doplnky'),
    (4041, 'kempingove-zidle', 'Kempingové židle a křesla', 'kempingovy-nabytek'),
    (4042, 'kempingove-stoly', 'Kempingové stoly', 'kempingovy-nabytek'),
    (70532, 'balancni-desky', 'Balanční desky', 'balancni-pomucky'),
    (110011, 'mma-rukavice', 'MMA rukavice', 'boxerske-rukavice'),
    # ---- 16. 11. 2026 November wave 4 (reports/sporteka/content-gap-2026-11e.md) ----
    (6082, 'boby', 'Boby', 'sane-a-boby'),
    (6083, 'sanky', 'Sáňky a saně', 'sane-a-boby'),
    (708011, 'whey-proteiny', 'Whey proteiny (syrovátkové)', 'proteiny'),
    (708012, 'veganske-proteiny', 'Veganské a rostlinné proteiny', 'proteiny'),
    (1023, 'mikiny-na-zip', 'Mikiny na zip', 'mikiny'),
    (1024, 'mikiny-s-kapuci', 'Mikiny s kapucí', 'mikiny'),
    (7013, 'jednorucni-cinky', 'Jednoruční činky', 'cinky-a-kotouce'),
    (7092, 'ortezy-na-koleno', 'Ortézy a chrániče na koleno', 'bandaze-a-ortezy'),
    (7093, 'ortezy-na-kotnik', 'Ortézy a bandáže na kotník', 'bandaze-a-ortezy'),
    (3022, 'cestovni-tasky', 'Cestovní tašky a duffle bagy', 'sportovni-tasky'),
    (1161, 'fotbalove-dresy', 'Fotbalové dresy', 'dresy'),
    (1101, 'boxerky', 'Boxerky a trenky', 'sportovni-spodni-pradlo'),
    (1102, 'kalhotky', 'Sportovní kalhotky', 'sportovni-spodni-pradlo'),
    (120031, 'pennyboardy', 'Pennyboardy', 'skateboardy'),
    (8042, 'basketbalove-kose', 'Basketbalové koše', 'basketbal'),
    # ---- 17. 11. 2026 November wave 5: what sportisimo.cz / decathlon.cz rank with and we lacked (reports/sporteka/content-gap-2026-11f.md) ----
    (2081, 'snehule', 'Sněhule', 'zimni-obuv'),
    (10441, 'cargo-kalhoty', 'Cargo kalhoty a kapsáče', 'sportovni-kalhoty'),
    (1061, 'zateplene-leginy', 'Zateplené a termo legíny', 'leginy'),
    (2152, 'vlozky-do-bot', 'Vložky do bot', 'doplnky-k-obuvi'),
    (90721, 'rucniky', 'Ručníky a osušky', 'plazove-doplnky'),
    (2101, 'domaci-pantofle', 'Papuče a domácí pantofle', 'pantofle-a-zabky'),
    (8081, 'pingpongove-stoly', 'Pingpongové stoly', 'stolni-tenis'),
    (7072, 'masazni-valce', 'Masážní válce', 'masazni-pomucky'),
    (3101, 'buzoly-a-kompasy', 'Buzoly a kompasy', 'dalekohledy-a-kompasy'),
    (2121, 'neoprenove-boty-a-ponozky', 'Neoprenové boty a ponožky', 'obuv-do-vody'),
    (40521, 'esusy', 'Ešusy', 'kempingove-nadobi'),
    # ---- 17. 11. 2026 November wave 6: Ahrefs content gap vs 14 shops (reports/sporteka/content-gap-2026-11g.md) ----
    (7073, 'akupresurni-podlozky', 'Akupresurní podložky', 'masazni-pomucky'),
    (70511, 'chodici-pasy', 'Chodicí pásy (walking pady)', 'behaci-pasy'),
    (17041, 'airtracky-a-zinenky', 'Airtracky a žíněnky', 'gymnasticke-pomucky'),
    (1053, 'prosivane-bundy', 'Prošívané bundy', 'zimni-bundy'),
    (10541, 'nepromokave-kalhoty', 'Nepromokavé kalhoty', 'outdoorove-kalhoty'),
    (6031, 'snowboardove-bundy', 'Snowboardové bundy', 'lyzarske-bundy'),
    (6032, 'snowboardove-kalhoty', 'Snowboardové kalhoty', 'lyzarske-kalhoty'),
    (2153, 'navleky-na-boty', 'Návleky na boty a gamaše', 'doplnky-k-obuvi'),
    (8014, 'fotbalove-branky', 'Fotbalové branky', 'fotbal'),
    (3121, 'moskytiery', 'Moskytiéry', 'hygiena-a-repelenty'),
    (4061, 'chladici-tasky', 'Chladicí tašky a termotašky', 'chladici-boxy'),
    (80221, 'hokejove-rukavice', 'Hokejové rukavice', 'hokejove-chranice'),
    (110031, 'chranice-zubu', 'Chrániče zubů', 'chranice-bojove-sporty'),
    (7074, 'otuzovaci-kade', 'Otužovací kádě a vany', 'fitness'),
    (180021, 'joga-bloky', 'Jógové bloky', 'jogove-pomucky'),
    (70111, 'kotouce-na-cinky', 'Kotouče a osy na činky', 'cinky-a-kotouce'),
    (70121, 'zavazi-na-kotniky', 'Závaží na kotníky a zápěstí', 'cinky-a-kotouce'),
    (30731, 'via-ferrata', 'Via ferrata: sety, lonže a rukavice', 'horolezectvi'),
    # ---- 18. 11. 2026 November wave 7: small categories competitors earn traffic with (Ahrefs top pages + gap 100-199, content-gap-2026-11h.md) ----
    (30732, 'karabiny', 'Karabiny', 'lezecka-lana-a-karabiny'),
    (30733, 'horolezecka-lana', 'Horolezecká lana', 'lezecka-lana-a-karabiny'),
    (3074, 'cepiny-a-macky', 'Cepíny a mačky', 'horolezectvi'),
    (4101, 'tarpy', 'Tarpy a celty', 'stanove-doplnky'),
    (3023, 'kosmeticke-tasky', 'Kosmetické a toaletní tašky', 'sportovni-tasky'),
    (3024, 'nepromokave-vaky', 'Nepromokavé vaky a dry bagy', 'sportovni-tasky'),
    (7023, 'posilovaci-kladky', 'Posilovací kladky', 'posilovaci-stroje'),
    (3081, 'filtry-na-vodu', 'Filtry na vodu', 'outdoor-doplnky'),
    (3053, 'hydrovaky', 'Hydrovaky a vaky na vodu', 'lahve-a-termosky'),
    (3054, 'termosky-na-jidlo', 'Termosky na jídlo', 'lahve-a-termosky'),
    (3092, 'hrudni-pasy', 'Hrudní pásy a snímače tepu', 'sportovni-hodinky'),
    (1112, 'nepromokave-ponozky', 'Nepromokavé ponožky', 'sportovni-ponozky'),
    (5101, 'brasny-na-kolo', 'Brašny na kolo', 'cyklo-tasky-a-nosice'),
    (5102, 'kosiky-na-kolo', 'Košíky na kolo', 'cyklo-tasky-a-nosice'),
    (5103, 'cyklisticke-batohy', 'Cyklistické batohy', 'cyklo-tasky-a-nosice'),
    (180031, 'pilates-reformery', 'Pilates reformery', 'pilates-pomucky'),
    (110032, 'suspenzory', 'Suspenzory', 'chranice-bojove-sporty'),
    (3031, 'nordic-walking-hole', 'Nordic walking hole', 'trekove-hole'),
    (3141, 'solarni-nabijecky', 'Solární nabíječky a panely', 'powerbanky-a-nabijeni'),
    (7075, 'vibracni-plosiny', 'Vibrační plošiny', 'masazni-pomucky'),
    (7064, 'zavesne-systemy-trx', 'Závěsné systémy TRX', 'funkcni-trenink'),
    (1122, 'potitka', 'Potítka', 'cepice-a-celenky'),
    (130031, 'petanque', 'Pétanque', 'hry-na-zahradu'),
    # ---- 19. 11. 2026 November wave 8: Sportano / Decathlon / Sportisimo / inSPORTline (content-gap-2026-11i.md) ----
    (216, 'volejbalova-obuv', 'Volejbalové boty', 'sportovni-obuv'),
    (217, 'boxerske-boty', 'Boxerské a zápasnické boty', 'sportovni-obuv'),
    (7055, 'posilovaci-kolecka', 'Posilovací kolečka', 'fitness-pomucky'),
    # ---------- fitness ----------
    (700, 'fitness', 'Fitness a posilování', None),
    (701, 'cinky-a-kotouce', 'Činky a kotouče', 'fitness'),
    (702, 'posilovaci-stroje', 'Posilovací stroje a lavice', 'fitness'),
    (7021, 'posilovaci-lavice', 'Posilovací lavice', 'posilovaci-stroje'),
    (703, 'kardio-trenazery', 'Rotopedy a trenažéry', 'fitness'),
    (7031, 'rotopedy', 'Rotopedy a spinning kola', 'kardio-trenazery'),
    (7032, 'behaci-pasy', 'Běžecké a chodicí pásy', 'kardio-trenazery'),
    (7033, 'elipticke-trenazery', 'Eliptické trenažéry', 'kardio-trenazery'),
    (7034, 'veslovaci-trenazery', 'Veslovací trenažéry', 'kardio-trenazery'),
    (704, 'joga-a-podlozky', 'Jógové podložky', 'joga-a-pilates'),
    (705, 'fitness-pomucky', 'Fitness pomůcky', 'fitness'),
    (706, 'funkcni-trenink', 'Funkční trénink a hrazdy', 'fitness'),
    (707, 'masazni-pomucky', 'Masážní pomůcky', 'fitness'),
    (7071, 'masazni-pistole', 'Masážní pistole', 'masazni-pomucky'),
    (708, 'sportovni-vyziva', 'Sportovní výživa', None),
    (709, 'bandaze-a-ortezy', 'Bandáže a ortézy', 'fitness'),
    # ---------- ball & racket ----------
    (800, 'micove-sporty', 'Míčové a raketové sporty', None),
    (801, 'fotbal', 'Fotbal', 'micove-sporty'),
    (802, 'hokej', 'Hokej', 'micove-sporty'),
    (803, 'florbal', 'Florbal', 'micove-sporty'),
    (804, 'basketbal', 'Basketbal', 'micove-sporty'),
    (805, 'volejbal', 'Volejbal', 'micove-sporty'),
    (806, 'tenis', 'Tenis', 'micove-sporty'),
    (807, 'badminton', 'Badminton', 'micove-sporty'),
    (808, 'stolni-tenis', 'Stolní tenis', 'micove-sporty'),
    (809, 'ostatni-micove-sporty', 'Další míčové sporty', 'micove-sporty'),
    # ---------- water ----------
    (900, 'vodni-sporty', 'Vodní sporty a plavání', None),
    (901, 'plavecke-bryle', 'Plavecké brýle', 'vodni-sporty'),
    (902, 'plavecke-cepice', 'Plavecké čepice', 'vodni-sporty'),
    (903, 'plavecke-pomucky', 'Plavecké pomůcky', 'vodni-sporty'),
    (904, 'neopreny', 'Neopreny', 'vodni-sporty'),
    (905, 'paddleboardy', 'Paddleboardy a kajaky', 'vodni-sporty'),
    (906, 'snorchlovani', 'Šnorchlování a potápění', 'vodni-sporty'),
    (907, 'plazove-doplnky', 'Plážové doplňky a osušky', 'vodni-sporty'),
    # ---------- fishing ----------
    (1000, 'rybareni', 'Rybaření', None),
    (10001, 'rybarske-pruty', 'Rybářské pruty', 'rybareni'),
    (10002, 'rybarske-navijaky', 'Navijáky', 'rybareni'),
    (10003, 'nastrahy-a-navnady', 'Nástrahy a návnady', 'rybareni'),
    (10004, 'vlasce-a-snury', 'Vlasce a šňůry', 'rybareni'),
    (10005, 'rybarske-doplnky', 'Rybářské doplňky', 'rybareni'),
    (10006, 'rybarske-tasky', 'Tašky, pouzdra a krabičky', 'rybareni'),
    (10007, 'rybarske-obleceni', 'Rybářské oblečení a obuv', 'rybareni'),
    (10008, 'bivaky-a-kresla', 'Bivaky, lehátka a křesla', 'rybareni'),
    (10009, 'muskareni', 'Muškaření', 'rybareni'),
    # ---------- combat ----------
    (1100, 'bojove-sporty', 'Bojové sporty', None),
    (11001, 'boxerske-rukavice', 'Boxerské rukavice', 'bojove-sporty'),
    (11002, 'boxovaci-pytle', 'Boxovací pytle a hrušky', 'bojove-sporty'),
    (11003, 'chranice-bojove-sporty', 'Chrániče', 'bojove-sporty'),
    (11004, 'obleceni-bojove-sporty', 'Kimona a oblečení', 'bojove-sporty'),
    (110041, 'kimona', 'Kimona a bojová oblečení', 'obleceni-bojove-sporty'),
    # ---------- wheels ----------
    (1200, 'kolobezky-a-brusle', 'Koloběžky, brusle a skateboardy', None),
    (12001, 'inline-brusle', 'Inline brusle', 'kolobezky-a-brusle'),
    (12002, 'kolobezky', 'Koloběžky', 'kolobezky-a-brusle'),
    (12003, 'skateboardy', 'Skateboardy a longboardy', 'kolobezky-a-brusle'),
    (12004, 'chranice-a-helmy', 'Chrániče a helmy', 'kolobezky-a-brusle'),
    # ---------- leisure ----------
    (1300, 'volny-cas', 'Hry a volný čas', None),
    (13001, 'trampoliny', 'Trampolíny', 'volny-cas'),
    (13002, 'sipky', 'Šipky', 'volny-cas'),
    (13003, 'hry-na-zahradu', 'Hry na zahradu a pláž', 'volny-cas'),
    (13004, 'lukostrelba', 'Lukostřelba', 'volny-cas'),
    # ---------- v2 (1. 11. 2026): content gap from Decathlon sports + Marketing Miner ----------
    (70801, 'proteiny', 'Proteiny', 'sportovni-vyziva'),
    (70802, 'aminokyseliny-bcaa', 'Aminokyseliny a BCAA', 'sportovni-vyziva'),
    (70803, 'kreatin', 'Kreatin', 'sportovni-vyziva'),
    (70804, 'gainery', 'Gainery', 'sportovni-vyziva'),
    (70805, 'predtreninkove-boostery', 'Předtréninkové boostery', 'sportovni-vyziva'),
    (70806, 'spalovace-tuku', 'Spalovače tuků', 'sportovni-vyziva'),
    (70807, 'vitaminy-a-mineraly', 'Vitamíny, minerály a omega-3', 'sportovni-vyziva'),
    (708071, 'omega-3', 'Omega-3 a rybí olej', 'vitaminy-a-mineraly'),
    (708072, 'horcik', 'Hořčík (magnesium)', 'vitaminy-a-mineraly'),
    (70808, 'energeticke-gely-a-tycinky', 'Energetické gely a tyčinky', 'sportovni-vyziva'),
    (70812, 'proteinove-tycinky-a-snacky', 'Proteinové tyčinky a snacky', 'sportovni-vyziva'),
    (70809, 'iontove-napoje', 'Iontové nápoje a hydratace', 'sportovni-vyziva'),
    (70810, 'kolagen-a-klouby', 'Kolagen a kloubní výživa', 'sportovni-vyziva'),
    (70811, 'ostatni-doplnky-stravy', 'Další doplňky stravy', 'sportovni-vyziva'),
    (708111, 'ashwagandha', 'Ashwagandha', 'ostatni-doplnky-stravy'),
    (1800, 'joga-a-pilates', 'Jóga, pilates a meditace', None),
    (18001, 'jogove-pomucky', 'Jógové bloky, popruhy a bolstery', 'joga-a-pilates'),
    (18002, 'meditace', 'Meditační polštáře a pomůcky', 'joga-a-pilates'),
    (18003, 'pilates-pomucky', 'Pilates pomůcky', 'joga-a-pilates'),
    (1700, 'tanec-a-gymnastika', 'Tanec, balet a gymnastika', None),
    (17001, 'baletni-obuv', 'Baletní obuv a piškoty', 'tanec-a-gymnastika'),
    (17002, 'tanecni-obuv', 'Taneční obuv', 'tanec-a-gymnastika'),
    (17003, 'tanecni-obleceni', 'Taneční a baletní oblečení', 'tanec-a-gymnastika'),
    (17004, 'gymnasticke-pomucky', 'Gymnastické pomůcky', 'tanec-a-gymnastika'),
    (1400, 'jezdectvi', 'Jezdectví', None),
    (14001, 'jezdecka-obuv', 'Jezdecká obuv a chapsy', 'jezdectvi'),
    (14002, 'jezdecke-kalhoty', 'Jezdecké kalhoty a rajtky', 'jezdectvi'),
    (14003, 'jezdecke-helmy', 'Jezdecké helmy', 'jezdectvi'),
    (14004, 'jezdecke-obleceni', 'Jezdecké oblečení', 'jezdectvi'),
    (14005, 'vybaveni-pro-kone', 'Vybavení pro koně', 'jezdectvi'),
    (14006, 'jezdecke-doplnky', 'Jezdecké doplňky', 'jezdectvi'),
    (1500, 'golf', 'Golf', None),
    (15001, 'golfove-hole', 'Golfové hole', 'golf'),
    (15002, 'golfove-micky', 'Golfové míčky', 'golf'),
    (15003, 'golfove-tasky-a-voziky', 'Golfové tašky a vozíky', 'golf'),
    (15004, 'golfove-obleceni-a-obuv', 'Golfové oblečení a obuv', 'golf'),
    (15005, 'golfove-doplnky', 'Golfové doplňky', 'golf'),
    (1600, 'lov-a-priroda', 'Lov a příroda', None),
    (16001, 'lovecke-obleceni', 'Lovecké oblečení a obuv', 'lov-a-priroda'),
    (16002, 'lovecke-vybaveni', 'Lovecké vybavení', 'lov-a-priroda'),
    (1900, 'beh', 'Běh, triatlon a atletika', None),
    (19001, 'bezecke-vesty-a-batohy', 'Běžecké vesty a batohy', 'beh'),
    (19002, 'bezecke-opasky', 'Běžecké opasky a pouzdra', 'beh'),
    (19003, 'triatlon', 'Triatlon', 'beh'),
    (19004, 'atletika', 'Atletika', 'beh'),
    (4051, 'varice-a-kartuse', 'Vařiče a kartuše', 'vareni-v-prirode'),
    (4052, 'kempingove-nadobi', 'Kempingové nádobí a příbory', 'vareni-v-prirode'),
    (409, 'stanove-kolky', 'Stanové kolíky a kotvení', 'stany'),
    (410, 'stanove-doplnky', 'Plachty, podlážky a opravy stanů', 'stany'),
    (310, 'dalekohledy-a-kompasy', 'Dalekohledy, kompasy a navigace', 'outdoor'),
    (311, 'prvni-pomoc', 'Lékárničky a první pomoc', 'outdoor'),
    (312, 'hygiena-a-repelenty', 'Hygiena, repelenty a úprava vody', 'outdoor'),
    (313, 'outdoorove-noze-a-multitoola', 'Outdoorové nože a multitoolly', 'outdoor'),
    (314, 'powerbanky-a-nabijeni', 'Powerbanky a nabíjení', 'outdoor'),
    (315, 'outdoorova-strava', 'Outdoorová a lyofilizovaná strava', 'outdoor'),
    (507, 'cyklo-svetla', 'Světla na kolo', 'cyklistika'),
    (508, 'cyklo-zamky', 'Zámky na kolo', 'cyklistika'),
    (509, 'cyklo-pumpy-a-naradi', 'Pumpy a nářadí', 'cyklistika'),
    (510, 'cyklo-tasky-a-nosice', 'Brašny, nosiče a košíky', 'cyklistika'),
    (5061, 'plaste-a-duse', 'Pláště a duše', 'cyklo-dily'),
    (5062, 'sedla-a-gripy', 'Sedla, gripy a potahy', 'cyklo-dily'),
    (5063, 'cyklo-pohon', 'Pohon: přehazovačky, řetězy, kazety a kliky', 'cyklo-dily'),
    (5064, 'cyklo-brzdy', 'Brzdy a brzdové destičky', 'cyklo-dily'),
    (5065, 'cyklo-kola-a-rafky', 'Zapletená kola, ráfky a náboje', 'cyklo-dily'),
    (5066, 'cyklo-riditka', 'Řídítka, představce a sedlovky', 'cyklo-dily'),
    (5067, 'cyklo-pedaly', 'Pedály', 'cyklo-dily'),
    (5068, 'cyklo-blatniky', 'Blatníky', 'cyklo-dily'),
    (5069, 'cyklo-vidlice-a-tlumice', 'Vidlice a tlumiče', 'cyklo-dily'),
    (50610, 'ebike-baterie', 'Baterie, motory a nabíječky pro e-kola', 'cyklo-dily'),
    (50611, 'cyklo-sedacky-a-voziky', 'Dětské sedačky a vozíky za kolo', 'cyklistika'),
    (50612, 'cyklo-udrzba', 'Údržba kola: mazadla a čističe', 'cyklistika'),
    (50613, 'cyklo-nosice-na-auto', 'Nosiče kol na auto a stojany', 'cyklistika'),
    (511, 'cyklo-computery', 'Cyklopočítače a navigace', 'cyklistika'),
    (7051, 'svihadla', 'Švihadla', 'fitness-pomucky'),
    (7052, 'posilovaci-gumy', 'Posilovací gumy a expandery', 'fitness-pomucky'),
    (7053, 'balancni-pomucky', 'Balanční pomůcky', 'fitness-pomucky'),
    (810, 'padel', 'Padel', 'micove-sporty'),
    (811, 'squash', 'Squash', 'micove-sporty'),
    (812, 'ragby-a-americky-fotbal', 'Ragby a americký fotbal', 'micove-sporty'),
    (813, 'baseball-a-softball', 'Baseball a softball', 'micove-sporty'),
    (814, 'hazena', 'Házená', 'micove-sporty'),    # ---------- v3 (1. 11. 2026, večer): Ahrefs (Sportisimo/Decathlon top pages) + Marketing Miner gaps ----------
    (2000, 'merino', 'Merino oblečení', None),
    (20001, 'merino-tricka', 'Merino trička a tílka', 'merino'),
    (20002, 'merino-ponozky', 'Merino ponožky', 'merino'),
    (20003, 'merino-pradlo', 'Merino spodní prádlo a legíny', 'merino'),
    (20004, 'merino-mikiny', 'Merino mikiny a svetry', 'merino'),
    (20005, 'merino-doplnky', 'Merino čepice, nákrčníky a rukavice', 'merino'),
    (3071, 'lezecke-boty', 'Lezečky', 'horolezectvi'),
    (3072, 'lezecke-sedaky-a-pomucky', 'Lezecké sedáky, přilby a pomůcky', 'horolezectvi'),
    (3073, 'lezecka-lana-a-karabiny', 'Lana, karabiny a ferraty', 'horolezectvi'),
    (3013, 'skolni-batohy', 'Školní a studentské batohy', 'batohy'),
    (3021, 'tasky-pres-rameno', 'Tašky přes rameno a dokladovky', 'sportovni-tasky'),
    (316, 'plastenky', 'Pláštěnky a pončo', 'outdoor'),
    (4011, 'strechni-stany', 'Střešní stany, autostany a předstany', 'stany'),
    (4012, 'turisticke-stany', 'Turistické a trekové stany', 'stany'),
    (4013, 'rodinne-stany', 'Rodinné a kempingové stany', 'stany'),
    (4014, 'pop-up-a-plazove-stany', 'Pop-up a plážové stany', 'stany'),
    (4015, 'tipi-a-lavvu', 'Týpí a lavvu', 'stany'),
    (4016, 'expedicni-stany', 'Expediční a čtyřsezónní stany', 'stany'),
    (4017, 'pristresky-a-party-stany', 'Přístřešky a párty stany', 'stany'),
    (4018, 'rybarske-stany', 'Rybářské stany a bivaky', 'stany'),
    (4019, 'detske-stany', 'Dětské stany', 'stany'),
    (4021, 'detske-spacaky', 'Dětské spacáky', 'spaci-pytle'),
    (4022, 'perove-spacaky', 'Péřové spacáky', 'spaci-pytle'),
    (4023, 'dekove-spacaky', 'Dekové spacáky', 'spaci-pytle'),
    (4024, 'vlozky-do-spacaku', 'Vložky a obaly na spacáky', 'spaci-pytle'),
    (4025, 'rybarske-spacaky', 'Rybářské spacáky a lehátka se spacákem', 'spaci-pytle'),
    (118, 'kombinezy', 'Kombinézy a overaly', 'sportovni-obleceni'),
    (9051, 'kajaky-a-cluny', 'Kajaky a čluny', 'paddleboardy'),
    (9052, 'plovaci-vesty', 'Plovací a záchranné vesty', 'paddleboardy'),
    (120021, 'elektrokolobezky', 'Elektrokoloběžky', 'kolobezky'),
    (120022, 'freestyle-kolobezky', 'Freestyle koloběžky', 'kolobezky'),
    (13005, 'discgolf', 'Discgolf a frisbee', 'volny-cas'),
    (130021, 'sipkove-terce', 'Šipkové terče a stojany', 'sipky'),
    (130022, 'sipkove-doplnky', 'Letky, násadky, hroty a pouzdra na šipky', 'sipky'),
    (119, 'kabaty-a-parky', 'Kabáty a parky', 'sportovni-obleceni'),
    (1017, 'vetrovky', 'Větrovky a šusťákové bundy', 'sportovni-bundy'),
    (908, 'lycra-a-uv-tricka', 'Lycra a UV trička do vody', 'vodni-sporty'),
    (7011, 'kettlebelly', 'Kettlebelly', 'cinky-a-kotouce'),
    (7061, 'hrazdy-a-bradla', 'Hrazdy a bradla', 'funkcni-trenink'),
    (9031, 'ploutve', 'Plavecké a potápěčské ploutve', 'plavecke-pomucky'),
    (317, 'nesmeky', 'Nesmeky a protiskluzové návleky', 'outdoor'),
    (9071, 'nafukovaci-hracky', 'Nafukovací hračky a lehátka do vody', 'plazove-doplnky'),
    (9072, 'bazeny', 'Bazény a nafukovadla', 'vodni-sporty'),
    (1111, 'lyzarske-ponozky', 'Lyžařské ponožky', 'lyzarske-obleceni'),
    (10010, 'rybarske-lode-a-elektronika', 'Rybářské lodě, motory a echolóty', 'rybareni'),
    (8021, 'hokejky', 'Hokejky', 'hokej'),
    (8022, 'hokejove-chranice', 'Hokejová výstroj a chrániče', 'hokej'),
    (8023, 'hokejove-brankarske-vybaveni', 'Brankářská výstroj', 'hokej'),
    (8024, 'hokejove-brusle', 'Hokejové brusle', 'hokej'),
    (8025, 'hokejove-helmy-a-mrizky', 'Hokejové helmy a mřížky', 'hokej'),
    (8026, 'hokejove-dresy-a-obleceni', 'Hokejové dresy a oblečení', 'hokej'),
    (8027, 'hokejove-tasky', 'Hokejové tašky a batohy', 'hokej'),
    (8028, 'hokejove-cepele-a-nasady', 'Hokejové čepele a násady', 'hokej'),
    (8029, 'hokejove-puky-a-branky', 'Puky, branky a tréninkové pomůcky', 'hokej'),
    (8030, 'hokejove-pasky-a-doplnky', 'Hokejové pásky, tkaničky a doplňky', 'hokej'),
    (8032, 'pozemni-hokej', 'Pozemní hokej', 'hokej'),
    (8033, 'hokejove-suveniry-a-karty', 'Hokejové karty a suvenýry', 'hokej'),
    (8061, 'tenisove-rakety', 'Tenisové rakety', 'tenis'),
    (6091, 'lyzarske-hole', 'Lyžařské hole', 'zimni-sporty'),
    (8011, 'fotbalove-mice', 'Fotbalové míče', 'fotbal'),
    (8012, 'brankarske-rukavice', 'Brankářské rukavice', 'fotbal'),
    (8013, 'fotbalove-chranice-a-stulpny', 'Chrániče a štulpny', 'fotbal'),
    (8031, 'florbalove-hole', 'Florbalové hole', 'florbal'),
    (8041, 'basketbalove-mice', 'Basketbalové míče a koše', 'basketbal'),
    (8051, 'volejbalove-mice', 'Volejbalové míče a sítě', 'volejbal'),
]
BY_SLUG = {t[1]: t for t in TREE}
assert len({t[0] for t in TREE}) == len(TREE) and len(BY_SLUG) == len(TREE), "duplicate category id or slug in TREE"


def fold(s):
    s = html.unescape(str(s or '')).lower()
    s = unicodedata.normalize('NFKD', s)
    return ''.join(c for c in s if not unicodedata.combining(c))


# items that are never our assortment (checked first, on path + title)
EXCLUDE = re.compile(r'(^|\W)(moto(\W|cykl|kros|rkar)|motocross|motokros|motork|skutr|sperk|bizuter|nausnic|naramk|prsten|nahrdelnik|kabelk|penezenk|pasek'
                     r'|kravat|pyzam|nocni kosil|zupan|podvazk|tanga|parfem|toaletni voda|kosmetik|destnik|kufr|obaly na kufr|rousk'
                     r'|skolni(?!\w* (batoh|taska|vak))|penal|aktovk|plysov|dekorac|domacnost|home(\W|$)|povleceni|svickov|obal na mobil|kryt na mobil|sluchatk'
                     r'|(?<!meditacni )(?<!jogovy )polstar|poukaz|zdrava vyziva|vybava pro miminka|chovatelsk|sebeobran|obusek|vzduchov\w* (pusk|pistol)|airsoft|body pro miminka|masazni kresl|smazat)')

# apparel types that are fashion, not sport (dropped unless the title says sport)
FASHION = re.compile(r'(^|\W)(saty|sukne|halenk|tunik|dzin|jeans|kosile|sako|oblek|kabat|kardigan|svetr|pulovr|balerin|lodick|kozack|polobot|mokasin|espadril|salonk|spodni pradlo|podprsenk|kalhotky|boxerk|slipy|trenky|leginy push|topy(?! sport))')
SPORTY = re.compile(r'(sport|funkcni|bezeck|beh(\W|$)|trenink|fitness|outdoor|treking|trek|lyz|ski(\W|$)|snowboard|cyklo|cyklist|termo|thermo|merino|softshell|fleece|flis|gore|dri.?fit|climalite|run(\W|ning)|training|yoga|joga|tenis|fotbal|basket|volejbal|hokej|plav|swim|hike|hiking|trail)')

R = re.compile


def rules():
    """(slug, path regex, title regex, gpc regex) — None = don't care; all given parts must match."""
    return [
        # --- early, type words that beat any sport context ---
        ('cepice-a-celenky', None, R(r'ksiltovk|baseball ?cap|kulich|(^|\W)beanie(\W|$)'), None),
        ('lyzarske-doplnky', None, R(r'(vak|task|obal|pouzdr|batoh|rucksack|bag)\w* (na |pro )?(lyz|helm|snowboard|bezk)|ski bag|boot bag|ski rucksack'), None),
        ('rybarske-tasky', None, R(r'(pouzdr|obal|vak|task|krabick)\w* (na |pro )?pruty?'), None),
        ('paddleboardy', None, R(r'plovac\w* vest|zachrann\w* vest'), None),
        ('funkcni-trenink', None, R(r'tatami|zinenk'), None),
        # --- fishing (AZfishing paths; generic titles) ---
        ('muskareni', R(r'muskar'), None, None),
        ('rybarske-pruty', R(r'prut'), None, None),
        ('rybarske-pruty', None, R(r'(^|\W)prut(y)?(\W|$)'), R(r'rybar')),
        ('rybarske-navijaky', R(r'navijak'), None, None),
        ('nastrahy-a-navnady', R(r'nastrah|navnad|boilies|wobler|trpytk|(^|\W)pelet|krmen|(^|\W)jig'), None, None),
        ('vlasce-a-snury', R(r'vlasc|snur|navazc|montaz'), None, R(r'rybar|^$')),
        ('rybarske-tasky', R(r'(lov|ryb).*(task|pouzdr|krabick|kbelik)|pouzdra na pruty'), None, None),
        ('bivaky-a-kresla', R(r'(camping|lov kapru).*(bivak|kresl|lehatk|stolk)|bivak'), None, R(r'rybar|^$')),
        ('rybarske-obleceni', R(r'^oblecen.*|polarizacni'), None, R(r'rybar')),
        ('rybarske-doplnky', None, None, R(r'rybar')),
        ('rybarske-doplnky', R(r'lov kapru|lov dravcu|feeder|morsky rybolov|rybar'), None, None),
        # --- swimming (Swimaholic + generic) ---
        ('plavecke-bryle', R(r'plavecke bryle|plaveck.*bryl'), None, None),
        ('plavecke-bryle', None, R(r'plaveck\w* bryl'), None),
        ('plavecke-cepice', R(r'plavecke cepice'), None, None),
        ('plavecke-cepice', None, R(r'plaveck\w* cepi|koupaci cepi'), None),
        ('neopreny', R(r'neopren'), None, None),
        ('neopreny', None, R(r'neopren\w* (oblek|kombin|body|vest|top|trick|trik|kratas|kalhot|bund)|(oblek|kombinez)\w* .*neopren|wetsuit'), None),
        ('snorchlovani', R(r'snorch|potap'), None, None),
        ('snorchlovani', None, R(r'snorch|potapec|ploutv\w* na potap|maska na potap'), None),
        ('plavecke-pomucky', R(r'^pomucky|plavecke (ploutve|desky|packy|piskoty|pomucky)|plaveck'), None, None),
        ('plavecke-pomucky', None, R(r'plaveck\w* (desk|ploutv|pack|pisko|pas|kolec|rukav)|ploutve|nadlehcov'), None),
        ('paddleboardy', None, R(r'paddleboard|paddle board|(^|\W)sup(\W|$)|kajak|kanoe|nafukovaci clun'), None),
        ('plazove-doplnky', R(r'osusk|plazov|rucnik'), None, None),
        ('plazove-doplnky', None, R(r'osusk|rucnik|plazov\w* (task|dek|osusk)'), None),
        ('detske-plavky', R(r'(kojeneck|divc|chlapeck|detsk).*plavk'), None, None),
        ('damske-plavky', R(r'damsk\w* plavk|zeny.*plavk|plavky.*damsk|bikin'), None, None),
        ('panske-plavky', R(r'pansk\w* plavk|muzi.*plavk|plavky.*pansk|jammer|aquashort|brief|trunk'), None, None),
        ('plavky', R(r'plavk'), None, None),
        ('plavky', None, R(r'plavk|bikin'), None),
        # --- combat ---
        ('boxerske-rukavice', None, R(r'boxersk\w* rukavic|rukavice na box|mma rukavic|rukavice na bojov'), None),
        ('boxerske-rukavice', R(r'rukavice na bojove'), None, None),
        ('boxovaci-pytle', None, R(r'boxovac\w* (pytel|hrusk)|speedbag|(^|\W)(lapy|lapa)(\W|$)|^(?!.*(jog|yog|pilat|kostk|cihl)).*(^|\W)blok(\W|$)'), R(r'box|bojov|^$')),
        ('boxovaci-pytle', R(r'boxovac|lapy a bloky'), None, None),
        ('chranice-bojove-sporty', R(r'chranice (na|pro) bojov'), None, None),
        ('chranice-bojove-sporty', None, R(r'chranic zubu|suspenzor|chranic\w* holeni.*(mma|thai|kickbox)'), None),
        ('obleceni-bojove-sporty', R(r'obleceni na bojov'), None, None),
        ('obleceni-bojove-sporty', None, R(r'kimon|(^|\W)gi(\W|$)|judo|karate'), None),
        # --- wheels ---
        ('inline-brusle', None, R(r'inline|in-line|kolieckov|koleckov\w* brusl|rostouci brusl|slalomov\w* brusl'), None),
        ('inline-brusle', R(r'inline brusl|kolieckove brusle|koleckove brusle'), None, None),
        ('inline-brusle', None, R(r'^(?!.*(kolecka|kolecko|loziska|loziskov|chranic|helma|helmy|taska|batoh|ponozk|kuzel|kryt|coque|sada pr|nahradni|klic|podlozk|slider))(?=.*(powerslide|rollerblade|freeskate|(^|\W)roller(\W|$)))'), None),
        ('kolobezky', None, R(r'kolobez'), None),
        ('kolobezky', R(r'kolobez'), None, None),
        ('skateboardy', None, R(r'skateboard|longboard|pennyboard|penny board|waveboard|fingerboard'), None),
        ('chranice-a-helmy', R(r'chranice in.?line|ochranne pomucky > (helmy|chranice)'), None, None),
        ('chranice-a-helmy', R(r'chranice|helmy'), R(r'chranic|helm|prilb'), R(r'^$|in-line|brusl|skate')),
        ('bandaze-a-ortezy', R(r'zpevneni tela'), None, None),
        # --- leisure ---
        ('trampoliny', None, R(r'trampolin'), None),
        ('sipky', R(r'sipky'), None, None),
        ('sipky', None, R(r'sipk|(^|\W)terc(e|ov\w*)?(\W|$)'), R(r'^$|sipk|hry')),
        ('lukostrelba', R(r'(^|\W)luky'), None, None),
        ('lukostrelba', None, R(r'(^|\W)luk(\W|$)|sipy do luku|lukostrel'), None),
        ('hry-na-zahradu', None, R(r'petanque|kroket|frisbee|soft tenis|plazov\w* hra|hra na zahradu|badmintonova sada'), None),
        # --- winter (before clothing: "lyžařská bunda" is clothing, handled by clothing rules below via path) ---
        ('lyzarske-boty', None, R(r'lyzarsk\w* bot|lyzaky|skiboty|sjezdov\w* bot'), None),
        ('lyzarske-boty', R(r'lyzarske boty'), None, None),
        ('lyzarske-helmy', None, R(r'lyzarsk\w* (helm|prilb)|helma na lyz|ski helm|snowboardov\w* helm'), None),
        ('lyzarske-helmy', R(r'lyzarske helmy'), None, None),
        ('lyzarske-bryle', None, R(r'lyzarsk\w* bryl|bryle na lyz|ski goggle|snowboardov\w* bryl'), None),
        ('lyzarske-bryle', R(r'lyzarske bryle|bryle > lyzarske'), None, None),
        ('bezecke-lyzovani', R(r'bezecke lyzovani|bezky'), None, None),
        ('bezecke-lyzovani', None, R(r'bezk[ya](\W|$)|bezeck\w* lyz|boty na bezky'), None),
        ('skialpinismus', None, R(r'skialp|skitour|ski tour|stoupac\w* pas'), None),
        ('snowboarding', None, R(r'^(?!.*(bund|kalhot|helm|bryl|rukavic|cepic|mikin)).*snowboard'), None),
        ('sjezdove-lyze', None, R(r'sjezdov\w* lyz|(^|\W)lyze(\W|$)|carvingov'), R(r'^$|lyz|zimni')),
        ('sjezdove-lyze', R(r'sjezdove lyze'), None, None),
        ('brusle', None, R(r'(hokejov|krasobrusl|zimn|ledn|rekreacn)\w* brusl|brusle na led'), None),
        ('brusle', R(r'zimni brusle|hokejove brusle'), None, None),
        ('snezky', None, R(r'(^|\W)(sneznic\w*|snowshoes?|snezky)(\W|$)'), None),
        ('sane-a-boby', None, R(r'(^|\W)sane(\W|$)|(^|\W)bob(y)?(\W|$)|kluzak|snezn\w* (lopat|klouz)|rohacsk'), None),
        ('lyzarske-doplnky', None, R(r'lyzarsk\w* (hul|vak|taska|zamek|vosk)|hulky na lyz|vazani'), None),
        # --- cycling ---
        ('cyklisticke-helmy', None, R(r'(cyklistick|cyklo)\w* (helm|prilb)|helma na kolo|prilba na kolo'), None),
        ('cyklisticke-helmy', R(r'cyklistika.*helmy'), None, None),
        ('cyklisticka-obuv', None, R(r'tretr|cyklistick\w* (bot|obuv)'), None),
        ('cyklisticke-obleceni', None, R(r'cyklistick\w* (dres|kalhot|kratas|bund|vest|rukav|ponoz)|cyklodres|cyklokalhot|cyklo (dres|kalhot|kratas|bund|rukav)'), None),
        ('cyklo-dily', None, R(r'(^|\W)(plast|plaste|duse|retez|retezy|kazeta|kazety|brzdov\w*|prehazovack\w*|sedlo|sedla|pedal(y|u|ech)?|riditka|riditk\w*|vidlice|ram kola|gripy?|pastorek|klika|kliky)(\W|$)'), R(r'^$|cykl|kol')),
        ('cyklo-prislusenstvi', None, R(r'(svetl[oa]|blikac|zamek|pumpa|nosic|kosik|blatnik|stojan|tachometr|drzak).*(kol|cykl)|cyklopocitac|cyklo'), None),
        # --- camping / outdoor gear ---
        ('stany', None, R(r'^(?!.*stan smith).*?(?:(^|\W)stan(y)?(\W|$)|plazov\w* stan|(^|\W)stanov(y|a|e|ou|ych)?(\W|$))'), None),   # not "kastanova" / "stanoviste"
        ('spaci-pytle', None, R(r'spaci\w* pyt|spacak'), None),
        ('karimatky-a-matrace', None, R(r'karimat|samonafukov|nafukovac\w* matrac|matrace do stanu|kempingov\w* matrac'), None),
        ('hamaky', None, R(r'hamak|houpaci sit'), None),
        ('kempingovy-nabytek', None, R(r'kempingov\w* (zidl|kresl|stol|stolek|lehatk|nabytek)|skladac\w* (zidl|kresl|stol)|rybarsk\w* kresl'), None),
        ('kempingovy-nabytek', R(r'kresla|skladaci kresla a zidle'), None, None),
        ('vareni-v-prirode', None, R(r'varic|kartus|ešus|esus|kempingov\w* (nadobi|hrnec|panev|sada)|outdoorov\w* nadobi|jidelni set|(^|\W)spork|termohrnek'), None),
        ('chladici-boxy', None, R(r'chladic\w* (box|task)|autochladnick|termotask|chladnic'), None),
        ('lahve-a-termosky', None, R(r'termosk|termoska|lahev|lahve|bidon|termohrnek|hydrovak|camelbak|vak na vodu'), None),
        ('celovky-a-svitilny', None, R(r'celovk|svitiln|lucern|baterk'), None),
        ('trekove-hole', None, R(r'(trekov|nordic|turistick|walking)\w* hul|hole na nordic|nordic walking|trekingov\w* hul'), None),
        ('horolezectvi', None, R(r'horolez|lezeck|ferrat|karabin|sedak|jistic|magnezi|cepin|maceska|lano na lez|dynamick\w* lano'), None),
        ('turisticke-batohy', None, R(r'(turistick|trekov|outdoor|horsk|skialp|expedic)\w* batoh|batoh .*\d{2} ?l'), None),
        ('mestske-batohy', None, R(r'batoh|batuz|backpack|gymsac|vak na zada'), None),
        ('sportovni-tasky', None, R(r'sportovn\w* task|taska na (trenink|sport|fitness)|ledvink|(^|\W)vak(\W|$)|cestovni task|duffel|bag(\W|$)'), None),
        ('sportovni-bryle', None, R(r'(slunecn|sportovn|cyklistick|bezeck|polarizac)\w* bryl|bryle .*uv'), None),
        ('sportovni-hodinky', None, R(r'sportestr|sporttester|chytr\w* hodink|gps hodink|hrudni pas|fitness naramek|smartwatch'), None),
        ('kempingove-doplnky', None, R(r'piknikov\w* dek|kempingov|stanov\w* kolik|moskytier|nepromokav\w* vak|lodni vak'), None),
        # --- fitness ---
        ('sportovni-vyziva', None, R(r'protein|kreatin|bcaa|gainer|tycinka|iontov|energeticky gel|aminokyselin|spalovac|pre-?workout|kolagen|vitamin'), None),
        ('sportovni-vyziva', R(r'vyziva'), None, None),
        ('cinky-a-kotouce', None, R(r'(^|\W)cink|jednorucka|kotouc|kettlebel|osa na cink|olympijsk\w* osa|zavazi|vzperac\w* (tyc|osa)|zatezov\w* (vest|manzet|kotouc)|bucl'), R(r'^$|cink|fitness|posil|cvicen')),
        ('cinky-a-kotouce', R(r'cinky|kotouce'), None, None),
        ('kardio-trenazery', None, R(r'rotoped|bezeck\w* pas|eliptick|stepper|veslovac\w* (trenazer|stroj)|spinningov|cyklotrenazer|trenazer'), None),
        ('posilovaci-stroje', None, R(r'posilovac\w* (vez|lavic|stroj|stanic)|(^|\W)bench(?!made)|stojan na cink|multi.?posilov|fitness kladk|power rack|klec na'), None),
        ('posilovaci-stroje', R(r'posilovaci stroje|posilovaci veze|komercni stroje'), None, None),
        ('funkcni-trenink', None, R(r'hrazd|bradla|zebrin|trx|zavesn\w* system|kruhy na cvicen|slam ball|medicinbal|wall ball|bosu|plyometr|zinenk|crossfit'), None),
        ('funkcni-trenink', R(r'funkcni trenink|venkovni posilovna'), None, None),
        ('joga-a-podlozky', None, R(r'(^|\W)jog(a|y|u|ou|ov\w*)(\W|$)|yoga|pilates|podlozk\w* na cvicen|cvicebn\w* podlozk|jogamat'), None),
        ('masazni-pomucky', None, R(r'masazn|masaz|foam roller|valec na masaz|masazni pistol|vibracni ploš|vibracni plos'), None),
        ('bandaze-a-ortezy', None, R(r'bandaz|(^|\W)ortez|kinesio|tejp|kompresn\w* (navlek|rukav)|chranic\w* kolen(?!.*(brusl|inline))'), None),
        ('fitness-pomucky', None, R(r'svihadl|posilovac\w* gum|odporov\w* gum|expander|hula hoop|gymnasticky mic|overball|posilovac\w* kolec|rukavice na fitness|fitness rukavic|stahovadl|posilovac\w* pomuck|balancn'), None),
        # --- ball & racket sports ---
        ('stolni-tenis', None, R(r'stoln\w* tenis|pingpong|ping-pong|palk\w* na stol'), None),
        ('stolni-tenis', R(r'stolni tenis'), None, None),
        ('badminton', None, R(r'badminton|bedminton|(^|\W)pirk|raketa na badminton'), None),
        ('badminton', R(r'badminton'), None, None),
        ('tenis', None, R(r'tenisov\w* (raket|mic|taska|vypleten)|raketa na tenis|tenisky na tenis|squash|padel'), None),
        ('florbal', None, R(r'florbal'), None),
        ('florbal', R(r'florbal'), None, None),
        ('hokej', None, R(r'hokej(?!ov\w* bot)|hokejk|puk(\W|$)|nahrazk|holenni chranic.*hokej|lokty hokej'), None),
        ('hokej', R(r'hokej'), None, None),
        ('basketbal', None, R(r'basketbal\w* (mic|kos|desk|sit)|basketbalov\w* (mic|kos)|basketbalovy kos|basketbal(\W|$)(?!.*(bot|obuv|tenisk))'), R(r'^$|mic|sport')),
        ('basketbal', R(r'basketbal(?!ov\w* (bot|obuv|tenisk))'), None, None),
        ('volejbal', None, R(r'volejbal|volleyball'), None),
        ('fotbal', None, R(r'fotbalov\w* (\w+ )?(mic|branka|chranic|rukavic|sit|taska)|brankarsk\w* rukavic|chranic\w* holeni|(^|\W)mic na fotbal|futsalov\w* mic'), None),
        ('fotbal', R(r'fotbal > (fotbalove vybaveni|brankarske|mice|chranice)|fotbalove vybaveni'), None, None),
        # --- footwear (path or title says shoes) ---
        ('barefoot-obuv', None, R(r'barefoot|ponozkobot'), None),
        ('barefoot-obuv', R(r'barefoot'), None, None),
        ('kopacky', None, R(r'kopack|lisovk|lisokolik|turf(y|\W|$)|(^|\W)fg(\W|$).*bot|(?<!\d)(^|\W)(fg|ag|sg|mg|tf)(\W|$)'), R(r'^$|obuv|bot')),   # not after a number: '500 mg' is a supplement (15. 11.)
        ('kopacky', R(r'kopacky'), None, None),
        ('salova-obuv', R(r'salov|halov|sálov|indoor'), None, None),
        ('salova-obuv', None, R(r'salov\w* (bot|obuv)|halov\w* (bot|obuv)|sálovk|salovk|indoor (bot|obuv)|futsal\w* (bot|obuv)|volejbalov\w* (bot|obuv)|hazenk'), None),
        ('basketbalova-obuv', R(r'basketbalove tenisky|basketbalove boty'), None, None),
        ('basketbalova-obuv', None, R(r'basketbalov\w* (bot|obuv|tenisk)'), None),
        ('tenisova-obuv', R(r'tenisove boty|tenisova obuv'), None, None),
        ('tenisova-obuv', None, R(r'tenisov\w* (bot|obuv)|bot\w* na tenis'), None),
        ('trailove-boty', R(r'terenni bezecke|trailov'), None, None),
        ('trailove-boty', None, R(r'trail\w* (bot|obuv|bezeck)|(bot|obuv)\w* .*trail|terenni bezeck|trailrun|trail running'), R(r'^$|obuv')),
        ('silnicni-bezecke-boty', R(r'silnicni bezecke|bezecke boty|bezecka obuv'), None, None),
        ('silnicni-bezecke-boty', None, R(r'bezeck\w* (bot|obuv)|(bot|obuv)\w* na beh|running shoe'), None),
        ('vysoke-trekove-boty', R(r'vysoke trekove'), None, None),
        ('nizke-trekove-boty', R(r'nizke trekove'), None, None),
        ('trekova-obuv', R(r'trekove boty|trekova obuv|outdoorova obuv|turisticka obuv'), None, None),
        ('vysoke-trekove-boty', None, R(r'(trekov|turistick|outdoorov|horsk)\w* (bot|obuv).*(mid|hi(gh)?)(\W|$)|(mid|high)\W.*(gtx|gore-tex|wp)'), R(r'^$|obuv')),
        ('trekova-obuv', None, R(r'(trekov|turistick|outdoorov|horsk|hikingov)\w* (bot|obuv)|hiking|trekking (shoe|boot)'), R(r'^$|obuv')),
        ('treninkova-obuv', R(r'fitness boty|treninkove boty'), None, None),
        ('treninkova-obuv', None, R(r'(fitness|treninkov|crossfit)\w* (bot|obuv)|(bot|obuv)\w* na fitness'), None),
        ('obuv-do-vody', R(r'boty do vody'), None, None),
        ('obuv-do-vody', None, R(r'(bot|obuv|pantofl|sandal)\w* do vody|neoprenov\w* bot|aqua shoe'), None),
        ('holinky', R(r'holink'), None, None),
        ('holinky', None, R(r'holink|gumak'), None),
        ('zimni-obuv', R(r'zimni (boty|obuv)|snehul|podzimni boty'), None, R(r'^$|obuv')),
        ('zimni-obuv', None, R(r'snehul|zimn\w* (bot|obuv)|(bot|obuv)\w* .*zimn|apres'), R(r'^$|obuv')),
        ('sandaly', R(r'sandal'), None, None),
        ('sandaly', None, R(r'sandal'), R(r'^$|obuv')),
        ('pantofle-a-zabky', R(r'pantofl|zabky|nazouvak'), None, None),
        ('pantofle-a-zabky', None, R(r'^(?!.*(mikin|bund|tricko|trika|triko|tilk|(^|\W)sort|kratas|ponozk|kalhot|(^|\W)vest|rukavic|brusl|kolecka|batoh|sukn|saty|(^|\W)leg(g|in)))(?=.*(pantofl|zabk|nazouva[kc]|crocs|(^|\W)(slides?|clogs?)(\W|$)))'), R(r'^$|obuv')),
        ('doplnky-k-obuvi', R(r'tkanick|pece o boty|impregnace|vlozky|cistici prostredky na boty'), None, None),
        ('doplnky-k-obuvi', None, R(r'tkanick|vlozky do bot|impregnac|napinak do bot|cistic\w* (na )?bot'), None),
        ('tenisky', R(r'tenisky|volnocasove|boty pro volny cas|nizka obuv|kotnikova obuv|^boty$|^obuv$|> obuv$|> boty$'), None, R(r'^$|obuv')),
        # titles that start with a footwear noun phrase ("Pánské sportovní boty Skechers …"; Decathlon feed has no Google category)
        ('tenisky', None, R(r'^((pansk|damsk|detsk|dospel)\w* )?((sportovni|kozene|volnocasove|zimni|kotnikove|nizke|vysoke) )*(boty|botky|obuv|tenisky|sneakers|polobotky)( |$)'), None),
        ('tenisky', R(r'^(sportovni obuv|boticka)$'), R(r'(^|\W)(boty|botky|tenisky|obuv)(\W|$)'), None),
        ('tenisky', None, R(r'tenisk|sneaker|(^|\W)(bot[ya]|obuv)(\W|$)'), R(r'obuv')),
        # --- clothing ---
        ('dresy', None, R(r'(^|\W)dres(y)?(\W|$)|replik\w* dres|fotbalov\w* (dres|tricko)|hokejov\w* dres'), None),
        ('dresy', R(r'fotbalove obleceni|hokej > hrac'), None, None),
        ('sportovni-podprsenky', None, R(r'sportovn\w* podprsenk|bra (top)?(\W|$)|podprsenka.*(sport|fitness|run|beh)'), None),
        ('sportovni-podprsenky', R(r'sportovni podprsenk|> podprsenky|podprsenky na jogu'), None, None),
        ('sportovni-podprsenky', None, R(r'(fitness|jogov|sportovni)?\s*podprsenk'), None),
        ('termopradlo', R(r'termopradlo|funkcni pradlo|merino pradlo|termo prad|zimni termo'), None, None),
        ('termopradlo', None, R(r'termopradl|termo (trick|trik|kalhot|spodk|tricko|nátel|natel)|funkcni (pradl|spodk|natel)|merino (trick|trik|spodk|natel|kosil)|thermo|base ?layer|spodky'), None),
        ('sportovni-ponozky', None, R(r'ponozk|podkolenk|stulpn|kompresni podkol|sneaker socks|socks'), None),
        ('sportovni-ponozky', R(r'ponozk'), None, None),
        ('sportovni-rukavice', None, R(r'rukavic|palcak'), None),
        ('nakrcniky-a-satky', None, R(r'nakrcnik|kukl|satek|buff|balaclava|sala(\W|$)'), None),
        ('cepice-a-celenky', None, R(r'cepic|ksiltovk|celenk|kulich|klobouk|baseballk|snapback|potitk|beanie|(^|\W)cap(\W|$)'), None),
        ('cepice-a-celenky', R(r'cepice|ksiltovk|celenk'), None, None),
        ('lyzarske-bundy', None, R(r'(lyzarsk|snowboardov|ski)\w* bund'), None),
        ('lyzarske-kalhoty', None, R(r'(lyzarsk|snowboardov|ski)\w* kalhot|kalhoty na lyz'), None),
        ('lyzarske-kalhoty', R(r'lyzarske kalhoty|zimni a lyzarske kalhoty'), None, None),
        ('lyzarske-bundy', R(r'lyzarske bundy|zimni a lyzarske bundy'), None, None),
        ('softshellove-bundy', None, R(r'softshell\w* bund|bunda .*softshell'), None),
        ('softshellove-bundy', R(r'softshell'), None, None),
        ('sportovni-vesty', None, R(r'(^|\W)vest(a|y)(\W|$)'), None),
        ('zimni-bundy', None, R(r'(zimn|perov|prosivan|parka)\w* bund|bunda .*(perov|zimn|prosiv)|parka|puffer|down jacket'), None),
        ('zimni-bundy', R(r'zimni bundy|perove'), None, None),
        ('nepromokave-bundy', None, R(r'(nepromokav|outdoorov|hardshell|membrán|membran|gore-?tex|turistick)\w* bund|bunda .*(gore|nepromok)|vetrovk|sustak|sustakov|vetrovka'), None),
        ('sportovni-bundy-jaro-podzim', None, R(r'(^|\W)bund(a|y)(\W|$)|jacket'), None),
        ('sportovni-bundy-jaro-podzim', R(r'bundy'), None, None),
        ('fleecove-mikiny', None, R(r'^(?!.*(pant|kalhot|short|kratas|tight|legin|jogger|teplak)).*(fleec|flees|flisov|polartec)'), R(r'^$|mikin|top|kosile|oblecen|svetr|kalhot')),
        ('funkcni-mikiny', None, R(r'funkcni mikin|mikina .*(funkcni|bezeck|trenink|technic)|(bezeck|treninkov)\w* mikin|stretch mikin'), None),
        ('mikiny', None, R(r'mikin|hoodie|sweatshirt|crewneck|full.?zip'), None),
        ('mikiny', R(r'mikiny'), None, None),
        ('teplaky', None, R(r'teplak|jogger|sweatpant'), None),
        ('outdoorove-kalhoty', None, R(r'(outdoorov|trekov|turistick|softshellov|horolezeck)\w* kalhot|kalhoty .*(outdoor|trek|softshell)'), None),
        ('sportovni-kalhoty', None, R(r'kalhot|pants'), None),
        ('sportovni-kalhoty', R(r'kalhoty'), None, None),
        ('leginy', None, R(r'legin|leggings|tight'), None),
        ('sportovni-kratasy', None, R(r'kratas|sortk|shorts|bermud'), None),
        ('soupravy', None, R(r'souprav|komplet|tracksuit'), None),
        ('soupravy', R(r'komplety|soupravy'), None, None),
        ('sportovni-spodni-pradlo', None, R(r'boxerk|slipy|trenk|kalhotky|spodni pradlo'), None),
        ('polokosile', None, R(r'polokosil|polo trick|polo shirt|(^|\W)polo(\W|$)'), None),
        ('tilka', None, R(r'tilk|(^|\W)top(\W|$)|crop'), None),
        ('funkcni-tricka', None, R(r'funkcni (trick|triko)|(tricko|triko) .*(funkcni|bezeck|technic|dri.?fit|merino)|(bezeck|treninkov|sportovn|funkcn)\w* (trick|triko)|dlouhy rukav.*funkcni|tee .*(run|training)|running (tee|top)'), None),
        ('sportovni-tricka', None, R(r'(^|\W)(tricko|tricka|trickem|tricku|tricek|triko|trika|trikem|triku|t-shirt|tee|longsleeve)(\W|$)|dlouhy rukav|kratky rukav'), None),
        ('sportovni-tricka', R(r'tricka|trika'), None, None),
        ('sportovni-sukne-a-saty', None, R(r'(tenisov|sportovn|bezeck|golfov|outdoorov|funkcn|zatepl|primaloft|softshell|treninkov|turisticky|hi-therm)\w* (sukn|sat)|skort'), None),
        ('sportovni-sukne-a-saty', R(r'(^|> )(saty|sukne)$|sukne a saty|saty a sukne'), None, None),
        ('kosile', None, R(r'(^|\W)kosil\w*|flannel shirt|(^|\W)shirt(\W|$)'), R(r'^$|oble')),
        ('chranice-a-helmy', None, R(r'chranic\w* (na|pro) (brusl|kolen|lokt|skate|kolob|in-?line|kolo)|chranic\w* (kolen|lokt)'), None),
        # --- shop paths whose product titles name only brand + model (Spartoo, Allegro, Decathlon marketplace; 2. 11. 2026 analysis of unmapped rows) ---
        ('trailove-boty', R(r'boty > (bezecke > krosove|trail)'), None, None),
        ('silnicni-bezecke-boty', R(r'boty > bezecke( >|$)|behani > obuv'), None, None),
        ('kopacky', R(r'boty > fotbal$'), None, None),
        ('treninkova-obuv', R(r'boty > fitness$'), None, None),
        ('tenisova-obuv', R(r'boty > tenis$'), None, None),
        ('trekova-obuv', R(r'boty > pohorky$|turistika > obuv > trekingove'), None, None),
        ('trekova-obuv', None, R(r'(bot|polobot)\w* trek\w*|trek\w* (bot|polobot)'), R(r'^$|obuv')),
        ('treninkova-obuv', None, R(r'(bot|tenisk)\w* treninkov'), None),
        ('silnicni-bezecke-boty', None, R(r'(tenisk|bot)\w* na behani'), None),
        ('lyzarske-hole', R(r'(^|> )hulky'), None, None),
        ('lyzarske-hole', None, R(r'(bezeck|skiov|sjezdar)\w* (hul|hole)'), None),
        ('dresy', R(r'fanshop|fotbalove kluby|fotbalova souprava'), None, None),
        # --- 9. vlna (2. 11. 2026): Dognet feeds — Heureka paths (sport365, mastersport, sportago), Sportby paths, GymBeam paths, brand-only ski-shop titles ---
        ('snowboarding', R(r'snowboarding > (snowboardy|boty na snowboard|vazani|snowboardove)'), None, None),
        ('tenisove-rakety', R(r'tenis > tenisove rakety'), None, None),
        ('lyzarske-hole', R(r'sjezdove hulky|sjezdove lyzovani > hulky'), None, None),
        ('sportovni-rukavice', R(r'lyzarske rukavice|> zimni rukavice$'), None, None),
        ('lyzarske-boty', R(r'sjezdove lyzovani > lyzarky|> lyzarky'), None, None),
        ('lyzarske-helmy', R(r'lyzarske prilby'), None, None),
        ('sjezdove-lyze', R(r'sjezdove lyzovani > lyze'), None, None),
        ('kombinezy', R(r'lyzarske obleceni > overal'), None, None),
        ('zimni-obuv', R(r'obuv > obuv podzimni a zimni'), None, None),
        ('tenisky', R(r'(muzi|zeny|deti|kluci|divky) > obuv > tenisky$'), None, None),
        ('sportovni-kratasy', R(r'fitness obleceni > sortky'), None, None),
        ('leginy', R(r'fitness obleceni > leginy'), None, None),
        ('brusle', R(r'zimni sporty > brusle na led'), None, None),
        ('paddleboardy', R(r'vodacke vybaveni|vodni sporty > vodacke'), None, None),
        ('trampoliny', R(r'trampoliny a prislusenstvi'), None, None),
        ('balancni-pomucky', R(r'balancni podlozky|steppery|stepmustky'), None, None),
        ('gymnasticke-pomucky', R(r'gymnasticke mice'), None, None),
        ('posilovaci-gumy', None, R(r'gumov\w* (pas|posilovac)|posilovac\w* guma|(^|\W)expander'), None),
        ('mestske-batohy', R(r'batohy, tasky a kabelky > batohy$'), None, None),
        ('sportovni-tasky', R(r'batohy, tasky a kabelky > tasky$|tasky na jidlo'), None, None),
        ('chranice-bojove-sporty', R(r'pomucky podle aktivity > bojove sporty'), None, None),
        ('boxerske-rukavice', None, R(r'boxing gloves|boxerske rukavice'), None),
        ('posilovaci-stroje', R(r'posilovaci klece a stojany'), None, None),
        ('masazni-pomucky', R(r'rehabilitacni pomucky > masazni valce'), None, None),
        ('plavecke-pomucky', R(r'pomucky podle aktivity > plavani'), None, None),
        ('vareni-v-prirode', None, R(r'^(petromax|primus)(\W|$)'), None),
        ('sportovni-bryle', None, R(r'^oakley\W(?!.*(helm|rukav|glove|taska|tricko|mikina|bunda|boty|ksilt|aro3|mod[135])).*prizm'), None),
        ('lyzarske-doplnky', None, R(r'^holmenkol(\W|$)'), None),
        ('outdoor-doplnky', None, R(r'^(tasmanian tiger|travelsafe|lifeventure)(\W|$)'), None),
        # ski-shop titles are "Brand Model, type, gender, colour": the type word sits after the first comma
        ('doplnky-k-obuvi', None, R(r', (stelka|vlozky|stelky)(,|$)'), None),
        ('mikiny', None, R(r', (damsky |pansky )?svetr( pansky| damsky| se zipem)?(,|$)|(^|\W)svetr se zipem'), None),
        ('soupravy', None, R(r'(lyzarsk\w*|lyzarskeho spodniho pradla|zimniho obleceni) sada|, (sada|set), (damska|damsky|panska|pansky|unisex|junior|deti)|(lyzarska|zimni) sada'), None),
        ('trekova-obuv', None, R(r', outdoor (boty|obuv)(,|$)'), None),
        ('tenisky', None, R(r', (boty|volnocasova obuv|gumove boty)(,| damske| panske|$)|, boty (damske|panske)(,|$)'), None),
        ('lyzarske-doplnky', None, R(r', (chranic zad|chranic patere|paterak|lyzarske navleky|navleky)(,|$)|(^|\W)(lyzarsk|snowboard|skluzn)\w* (vosk|mast)|vosk\w* (na|pro) (lyz|snowboard)|brusny papir|hrany?.* pilnik|diamantov\w* pilnik'), None),
        ('cyklisticke-helmy', None, R(r'cyklisticka (pilba|prilba)|cyklisticka helma'), None),
        # --- 19. 11. 2026: Exisport (Dognet) — Heureka "Módní doplňky / Obuv" paths and the "Home > Sporty" tree ---
        ('mestske-batohy', R(r'batohy, tasky a kabelky > batohy$'), None, None),
        ('sportovni-tasky', R(r'batohy, tasky a kabelky > (tasky|saccky|sacky na|gymbag)|tenisove tasky|taska na tenis'), None, None),
        ('tenisky', R(r'obuv > (panske|damske|detske) boty > (panske|damske|detske) (polobotky|kotnikove boty|balerinky)'), None, None),
        ('sjezdove-lyze', R(r'lyze s vazanim, flat lyze|zavodni lyze'), None, None),
        ('boxerky', R(r'spodni pradlo > boxerky'), None, None),
        ('cyklo-dily', R(r'cyklistika > nahradni dily na kola'), None, None),
        ('sportovni-bryle', R(r'slunecni bryle > polarizacni'), None, None),
        ('teplaky', R(r'kalhoty, leginy a kratasy > zateplene teplaky'), None, None),
        ('mikiny', R(r'mikiny a vesty > zateplene mikiny|turisticke mikiny'), None, None),
        ('leginy', R(r'kalhoty, leginy a kratasy > (jeggins|kompresni)'), None, None),
        ('trekova-obuv', R(r'turisticka obuv > turisticka celokozena obuv'), None, None),
        ('sane-a-boby', R(r'sankovani > sanky a boby|zimni radovanky > detske boby a sane'), None, None),
        ('barefoot-obuv', R(r'sportovni moda > obuv > barefoot obuv'), None, None),
        ('softshellove-bundy', R(r'turisticke bundy a vesty > softshellove'), None, None),
        ('silnicni-kola', R(r'kola > silnicni kola'), None, None),
        ('lyzarske-rukavice', R(r'lyzarske rukavice > lyzarske palcaky'), None, None),
        ('cyklisticke-ponozky', R(r'cyklisticke ponozky a podkolenky'), None, None),
        ('skialpove-vazani', R(r'skialp vazani'), None, None),
        ('padel', R(r'padel > padel rakety'), None, None),
        ('trekove-hole', R(r'trekingove hole|turisticke hole'), None, None),
        ('pantofle-a-zabky', R(r'sandaly, flip-flopy a pantofle > pantofle'), None, None),
        # --- 19. 11. 2026: BUSHCRAFTshop.cz (Dognet) — Shoptet tree "Survival > …", titles often without a type word (Victorinox Bantam) ---
        ('outdoorove-noze-a-multitoola', R(r'^survival > noze a naradi > (noze|sekery|rucni pily|rezbarske nastroje|brouseni nozu|polni lopatky)|^survival > noze a naradi$'), None, None),
        ('kempingove-nadobi', R(r'^survival > vareni v prirode > (outdoorove nadobi|varice > outdoorove kotliky)'), None, None),
        ('varice-a-kartuse', R(r'^survival > vareni v prirode > varice'), None, None),
        ('vareni-v-prirode', R(r'^survival > vareni v prirode$'), None, None),
        ('outdoorova-strava', R(r'^survival > vareni v prirode > strava a napoje'), None, None),
        ('filtry-na-vodu', R(r'^survival > vareni v prirode > uprava pitne vody'), None, None),
        ('lahve-a-termosky', R(r'^survival > vareni v prirode > lahev na vodu'), None, None),
        ('outdoor-doplnky', R(r'^survival > vareni v prirode > rozdelani ohne|^survival > outdoor survival > (signalizace|popruhy|vazaci draty|vodotesna schranka|termofolie|krabicka posledni zachrany)|^survival > outdoorove obleceni > outdoor doplnky > (outdoorovy opasek|outdoor destniky|ksandy|nasivky)|^survival > spani v prirode > outdoor ohrivace'), None, None),
        ('celovky-a-svitilny', R(r'^survival > spani v prirode > svitilny > (lampy|lucerny|chemicke svetlo)'), None, None),
        ('powerbanky-a-nabijeni', R(r'^survival > spani v prirode > svitilny > dobijeci baterie'), None, None),
        ('karimatky-a-matrace', R(r'^survival > spani v prirode > karimatky$'), None, None),
        ('kempingovy-nabytek', R(r'^survival > spani v prirode > karimatky > outdoorove sedatko'), None, None),
        ('tarpy', R(r'^survival > spani v prirode > celty'), None, None),
        ('kempingove-doplnky', R(r'^survival > spani v prirode > deky'), None, None),
        ('tasky-pres-rameno', R(r'^survival > outdoorove batohy > (sumky|brasny)'), None, None),
        ('nepromokave-vaky', R(r'^survival > outdoorove batohy > organizery'), None, None),
        ('hydrovaky', R(r'^survival > outdoorove batohy > hydratacni vaky'), None, None),
        ('karabiny', R(r'^survival > outdoor survival > karabiny'), None, None),
        ('prvni-pomoc', R(r'^survival > outdoor survival > prvni pomoc'), None, None),
        ('hygiena-a-repelenty', R(r'^survival > outdoor survival > osobni hygiena'), None, None),
        ('impregnace', R(r'^survival > outdoorove obleceni > cistici prostredky'), None, None),
        ('mikiny', R(r'^survival > outdoorove obleceni > outdoor svetry'), None, None),
        ('sportovni-ponozky', R(r'^survival > outdoorove obleceni > outdoorova obuv > outdoorove ponozky'), None, None),
        ('sportovni-bundy-jaro-podzim', None, R(r', anorak(,|$)'), None),
        ('sportovni-sukne-a-saty', None, R(r', sukne( damska)?(,|$)'), None),
        ('sjezdove-lyze', None, R(r'^\S+ .+ \+ \S+ .*(gw|pr|ca|qc|ac|tcx|jrs|rsw|erc|slr)$'), None),
    ]



# v2 rules: specific product types / sports that must beat the generic ones ("stanové kolíky" are not "stany", a protein bar
# is not a protein). Checked first. Same tuple shape as rules().
TOP_RULES = [
    # v4 (2. 11.): more specific product types (Sportisimo / Decathlon category lists)
    ('rybarske-lode-a-elektronika', None, R(r'sonar|echolot|plotter|zavazec\w* (lod|lodk)|bait ?boat|lodni motor|elektromotor|trolling motor|rybarsk\w* (clun|lod)|motor (parsun|wolong|minn)|(^|\W)motor (joy|flowstar)'), None),
    ('hokejove-brankarske-vybaveni', None, R(r'brankarsk\w*.*(hokej|chranic|lapak|vyrazec|maska|betonka)|(hokej\w*|goalie).*brankarsk|lapacka|vyrazecka'), None),
    ('hokejky', None, R(r'hokejk|hokejov\w* (hul|hole)|(^|\W)hul\w* (ccm|bauer|warrior|true)'), None),
    ('hokejove-chranice', None, R(r'hokej\w*.*(chranic|prilb|helm|rukavic|kalhot|nahrdeln)|(chranic|prilb|nahrdeln)\w*.*hokej'), None),
    ('tenisove-rakety', None, R(r'tenisov\w* raket|raketa na tenis|tenisova raketa'), None),
    ('lyzarske-hole', None, R(r'lyzarsk\w* (hul|hole)|(hulky|hole) (na|pro) lyz|sjezdov\w* (hul|hole)|(^|\W)lyzarske hole'), None),
    ('lyzarske-ponozky', None, R(r'lyzarsk\w* (ponozk|podkolenk)|ski ?sock|ponozk\w* (na|do) lyz|ponozky lyzarske'), None),
    ('vetrovky', None, R(r'vetrovk|sustak|windbreaker|wind ?jacket'), None),
    ('kabaty-a-parky', None, R(r'(^|\W)kabat\w*|(^|\W)(parka|parky)(\W|$)'), None),
    ('lycra-a-uv-tricka', None, R(r'uv (tricko|triko|top)|lycr\w*|rash ?guard|(tricko|triko) do vody|plavecke tricko'), None),
    ('kettlebelly', None, R(r'kettlebel|kettle ?bell|girja'), None),
    ('hrazdy-a-bradla', None, R(r'(^|\W)(hrazd\w*|bradla|zebrik na cvic)'), None),
    ('ploutve', None, R(r'ploutv'), None),
    ('nesmeky', None, R(r'nesmek|protiskluzov\w* (naslapn|retizk)|ledov\w* (hroty|racny)'), None),
    # electrically heated clothing (16. 11.); "hřejivý" = only warm, stays in its clothing category
    ('vyhrivane-obleceni', None, R(r'^(?!.*(masaz|bandaz|brusl|grip|deka|podlozk|sedak|sedadl|kreslo|lahev|hrnek)).*(vyhrivan|s vyhrivanim|heated|heat ?(glove|sock|bag)|(^|\W)heateo|ohrivac\w* (ruk|nohou|tela)|vyhrivac\w* (vlozk|ponozk|rukavic|vest))'), None),
    ('nafukovaci-hracky', None, R(r'nafukovac\w* (hrack|lehatk|kruh|mic|matrac|zvire|flamin|jednorozec|ostrov)|(lehatko|kruh|rukavky|kolo) do vody|plavac\w* kruh|plovouci ostrov'), None),
    ('bazeny', None, R(r'(^|\W)bazen(y|u|ek|ky)?(\W|$)|nafukovac\w* bazen'), None),
    ('plavky', None, R(r'(plavecke?|koupaci|plazove|aquashort)\w* ?(kratas\w*|sortk\w*)|(kratas\w*|sortk\w*) (do vody|na plavani|plavecke)'), None),
    # bike parts (complete bikes are decided by bike_rule() before the rules run)
    ('ebike-baterie', None, R(r'(baterie|akumulator\w*|nabijec\w*|motor\w*|stredov\w* motor|kryt motoru).*(kolo|kola|ebike|e-bike|elektrokol|elops|bosch|yamaha|bafang|36 ?v|48 ?v)|(kolo|ebike|e-bike|elektrokol|elops).*(baterie|nabijec)'), None),
    ('cyklo-nosice-na-auto', None, R(r'nosic\w* (kol|na kola|jizdnich)|stojan (na|pro) kol|(strechni|tazny|zadni) nosic\w* .*kol'), None),
    ('cyklo-sedacky-a-voziky', None, R(r'(sedack\w*|vozik\w*|prives\w*) (na|pro|za) (kolo|jizdn|dit)|cyklovozik|detsk\w* sedack\w* (na|za) kolo'), None),
    ('cyklo-udrzba', None, R(r'(mazadl\w*|mazivo|mazani|olej|cistic\w*|odmastovac|lubrikant|lube|vosk(?!a)|wax|sprej|cistici|sampon|degreaser|lubricant).*(retez|chain|kolo|kola|cykl|brzd|bike|e-bike)|(retez|chain|kolo|cykl|bike|e-bike).*(mazadl\w*|mazivo|cistic\w*|odmastovac|lubrikant|lube|wax|vosk(?!a)|degreaser)'), None),
    ('kardio-trenazery', None, R(r'(posilovac\w*|domaci|fitness|spinning\w*|magnetick\w*) (kolo|kola)|rotoped|ergometr|airbike|air bike|veloergometr|cyklotrenazer'), None),
    ('cyklo-vidlice-a-tlumice', None, R(r'(^|\W)(vidlic(?!k)\w*|tlumic\w*)(\W|$)(?!.*(hokej|lyz|snow))'), R(r'^$|cykl|kol|bike|mtb')),
    ('cyklo-brzdy', None, R(r'(^|\W)(brzd(a|y|u|ov\w*)|desticky|brzdov\w* (kotouc|packa|paka))(\W|$)'), R(r'^$|cykl|kol|bike|mtb|brzd')),
    ('cyklo-pedaly', None, R(r'(^|\W)pedal(y|u|ech|ek)?(\W|$)'), R(r'^$|cykl|kol|bike|mtb')),
    ('cyklo-blatniky', None, R(r'(^|\W)blatnik\w*'), None),
    ('cyklo-riditka', None, R(r'(^|\W)(riditk\w*|predstavec|predstavce|sedlovk\w*|cockpit)(\W|$)'), None),
    ('cyklo-kola-a-rafky', None, R(r'zapleten\w*|dvojkoli|(^|\W)(rafek|rafky|naboj|naboje|paprsk\w*)(\W|$)'), None),
    ('cyklo-pohon', None, R(r'prehazovack\w*|prehazovac\w*|(^|\W)(kazeta|kazety|retez|retezy|kliky|klika|pastorek|pastorky|vendlik|stredove loz\w*|lanko|lanka|bowden)(\W|$)|ozubene kolo|kolecko prehazovacky|(^|\W)groupset'), R(r'^$|cykl|kol|bike|mtb|retez')),
    ('sedla-a-gripy', None, R(r'(^|\W)(sedlo|sedla|grip|gripy)(\W|$)|potah (na|sedla)|kryt sedla'), R(r'^$|cykl|kol|bike|mtb|sedl|grip')),
    # fishing bait named like food must not become nutrition
    ('nastrahy-a-navnady', None, R(r'boilie|(^|\W)pelet|nastrah|krmen[ií] na ryb'), None),
    # nutrition: the most specific wording first
    ('lahve-a-termosky', None, R(r'shaker'), None),
    ('proteinove-tycinky-a-snacky', R(r'proteinove tycinky|snacky > proteinove|proteinove snacky'), None, None),
    ('proteinove-tycinky-a-snacky', None, R(r'proteinov\w* (tycink|susenk|snack|chips|palacink|chlebic|oplatk|cookie)|protein (bar|bars|cookie|cookies|crisps)|(^|\W)(tycinka|tycinky) .*protein'), None),
    ('energeticke-gely-a-tycinky', None, R(r'energeticky gel|energy gel|(proteinov|energeticke?|ovesn|datlov)\w* (tycinka|tycinky|susenk|oplatk|kase)|(^|\W)tycink\w*(?!.*(reflex|vyplet|hokej|kolo))|sportovni gel'), None),
    ('kreatin', None, R(r'kreatin|creatine'), None),
    ('aminokyseliny-bcaa', None, R(r'bcaa|(^|\W)eaa(\W|$)|aminokyselin|glutamin|arginin|citrulin|beta.?alanin'), None),
    ('kolagen-a-klouby', None, R(r'kolagen|glukosamin|chondroitin|klouby|kloubni vyziv|msm'), None),
    ('gainery', None, R(r'gainer|nabirani hmotnosti|na hmotu|mass gain'), None),
    ('iontove-napoje', None, R(r'iontov|isoton|izoton|napojov\w* (prasek|koncentrat)|elektrolyt|rehydrat|hydrate(\W|$)|sport drink'), None),
    ('spalovace-tuku', None, R(r'spalovac\w* tuk|fat burner|l-?karnitin|(^|\W)karnitin|termogen'), None),
    ('predtreninkove-boostery', None, R(r'pre-?workout|predtreninkov|(^|\W)pump(\W|$).*(formul|prasek|stack)'), None),
    ('proteiny', None, R(r'^(?!.*(boilie|rybar|nastrah|kapr|feeder|krmiv|tinktur|pro psy|pro kone|stavka|stava|sacharid)).*(protein|syrovatk|(^|\W)whey|kasein|casein|izolat)'), None),
    ('vitaminy-a-mineraly', None, R(r'vitamin|multivit|omega.?3|probiotik|spirulin|chlorell|(^|\W)vapnik'), None),
    ('vitaminy-a-mineraly', R(r'vitamin|mineral|doplnk|vyziva|supplement'), R(r'zelezo|magnesium|horcik|(^|\W)zinek|omega|(^|\W)zinc'), None),
    ('ostatni-doplnky-stravy', R(r'potravinov\w* doplnek|doplnk\w* strav|supplement|zdravi a vyziva > doplnky'), None, None),
    ('ostatni-doplnky-stravy', None, R(r'potravinov\w* doplnek|doplnek stravy|doplnky stravy'), None),
    # camping details
    ('stanove-kolky', R(r'stany|ke stanum|stanove kolik|turisticke vybaveni'), R(r'(^|\W)kolik(y|u|ek)?(\W|$)|(^|\W)v-peg|(^|\W)pegs?(\W|$)'), None),
    ('stanove-kolky', None, R(r'stanov\w* kolik|kolik\w* (do|na|ke|k) (stan|plachty|snehu)|kolik\w* na stan|stanov\w* (kotv|lank)|lanka? (na|ke) stan|odtahov\w* lank|tent pegs?'), None),
    ('stanove-doplnky', None, R(r'podlazk\w* (pod|do) stan|footprint|plachta (pod|na) stan|stanov\w* (plachta|tyc|opravn|zaplat|impregn|zavetr|predstan|podlaha)|opravn\w* (sada|zaplat).*stan|(^|\W)tarp(\W|$)|zavetri(\W|$)|predstan'), None),
    # what is NOT a tent although the title says "stan…" (owner 2. 11.: /stany/ must hold tents only): fishing swims, poles, cords, floors, lamps, shelters
    ('rybarske-doplnky', None, R(r'(^|\W)(rod ?pod|rodpod)|(^|\W)stanovist\w*|bivvy stol|stanov\w* stolek'), None),
    ('celovky-a-svitilny', None, R(r'(stanov|kempingov)\w* lamp'), None),
    ('stanove-doplnky', None, R(r'(dural|durawrap)\w* pruty|stanov\w* (pruty|snur\w*|podlazk\w*|koberec|postel|prist\w+|okap|lank\w*|zavesn\w* system)|stanova (podlazka|snura|postel)|okap na .*(stanov|pristresk)|nahradn\w* (tycky|tyce|sada tyci) (ke|k) (stan|bivak)|bocni stena|obal na stany'), None),
    ('varice-a-kartuse', None, R(r'(^|\W)varic|kartus|plynov\w* (varic|hori|lahev)|kempingov\w* (varic|hori)|lihov\w* varic|jetboil|(^|\W)hori(ak|k)(\W|$)'), None),
    ('kempingove-nadobi', R(r'^(?!.*(kluby|suvenyr|miminka|chovatel|detsk\w* vyziva|saneck|hazec|hry)).*$'), R(r'(^|\W)(esus|spork|sporka|sada nadobi|kempingov\w* (nadobi|hrnek|hrnec|pribor|miska|sada)|outdoorov\w* (nadobi|pribor|hrnek)|turisticke? (nadobi|pribor|hrnek)|skladaci (pribor|hrnek|miska|sporka)|titanov\w* (hrnek|hrnec|pribor|misk)|(pribor|hrnek|hrnec)\w* (ultralight|titan|outdoor|turist|do kempu))'), None),
    ('kempingove-nadobi', R(r'(nadobi|vareni v kempu|nadobi na vareni)'), R(r'(^|\W)(hrnek|hrnec|pribor|miska|sada|talir|lzice|vidlicka)'), None),
    # outdoor accessories
    ('outdoorova-strava', None, R(r'expres menu|lyofood|lyofiliz|hotove jidlo|(^|\W)susen\w* (maso|ovoce|zelenin)|outdoorov\w* (strava|jidlo)|instantn\w* (jidlo|kase|polevka)'), None),
    ('powerbanky-a-nabijeni', None, R(r'powerbank|solarn\w* nabijec|nabijec\w* (baterie|solarn)'), None),
    ('dalekohledy-a-kompasy', None, R(r'dalekohled|monokular|(^|\W)kompas|teleskop(?!ick)|(^|\W)lupa(\W|$)|outdoorov\w* navigac'), None),
    ('prvni-pomoc', None, R(r'lekarnick|first aid|prvni pomoc|izotermick\w* folie|zachrann\w* folie|naplast|nouzov\w* (deka|folie)'), None),
    ('hygiena-a-repelenty', None, R(r'^(?!.*(kone|poni|kratas|kalhot|bund|tricko|kosil|obleceni)).*(repelent)|filtr\w* (na )?vod|(tablet|kapky)\w* (na|do) vod|kempingov\w* (wc|mydl)|biologick\w* mydl|cestovn\w* (mydl|rucnik)|(^|\W)moskyt|antiparazit'), None),
    ('outdoorove-noze-a-multitoola', None, R(r'(^|\W)(nuz|noz|nuzek|nuze)(\W|$)|multitool|multifunkcn\w* (nuz|kleste|nastroj)|kapesn\w* nuz|(^|\W)sekyr|(^|\W)pila(\W|$).*(skladac|outdoor)'), None),
    # cycling details (before the generic "cyklo-dily" / "cyklo-prislusenstvi")
    ('plaste-a-duse', None, R(r'(duse|plast|plaste) (na|pro) (kolo|kola|bike)|(kolov|cyklo|cyklisticke?)\w* (plast|duse)|(^|\W)(plast|duse) .*(mtb|bmx|silnic|\d{2}"|\d{2}x\d)'), None),
    ('cyklo-svetla', None, R(r'(predni|zadni) svetl\w* (na )?(kolo|cykl|bike)|cyklo ?svetl|svetl\w* (na|pro) (kolo|cykl|bike)|blikac|cyklisticke svetl|svetla na kolo'), None),
    ('cyklo-zamky', None, R(r'zamek (na|pro) (kolo|kola|jizdn)|cyklo ?zam|retezov\w* zam|(^|\W)u-?lock|zamek.*(kolo|cykl)|(kolo|cykl).*zamek'), None),
    ('cyklo-pumpy-a-naradi', None, R(r'(pump|hustilk)\w*.*(kol|cykl|bike|duse|co2)|(kol|cykl|bike).*(pump|hustilk)|co2 (patron|hustil)|montpak|multiklic|cyklo ?naradi|lepeni na duse|zaplat\w* (na )?(duse|plast)|naradi na kolo|nastroj\w* (na|pro) kolo'), None),
    ('cyklo-tasky-a-nosice', None, R(r'(brasna|task\w*|nosic|kosik|batoh).*(na (kolo|ram|riditk|sedlo|zavazadlov)|podsedlov|cyklo)|(podsedlov|ramov|riditkov|cyklo\w*) (brasn|task)|nosic na kol|zavazadlov\w* nosic'), None),
    ('cyklisticke-helmy', None, R(r'(cyklistick|cyklo|mtb|silnicn)\w* (helm|prilb)|helma na kolo|prilba na kolo'), None),
    ('kardio-trenazery', None, R(r'cyklotrenazer|rotoped|(^|\W)trenazer'), None),
    ('cyklisticke-obleceni', R(r'cykl'), R(r'navlek|lacl'), None),
    ('cyklisticke-obleceni', None, R(r'(navlek|lacl)\w*.*(cykl|kolo|silnic)|(cykl|silnic)\w*.*(navlek|lacl)'), None),
    ('cyklisticke-obleceni', None, R(r'(cyklo|cyklist\w*|na kolo|bike|mtb)\w* \w*\s?(sortk|kratas|navlek|ponozk|rukavic|vest|triko|tricko|kalhot|bund|dres)|(sortk|kratas|navlek|ponozk|rukavic|vest|bund|dres|kalhot)\w* (na (horske |silnicni )?kolo|cyklo|cyklist|bike|mtb)'), None),
    ('cyklo-computery', None, R(r'cyklopocitac|cyklocomput|cyklonavigac|garmin edge|cyklo ?gps|wahoo|bryton|(^|\W)cyklo\w* (gps|navigac)'), None),
    ('cyklo-svetla', R(r'cykl.*svetl|svetla na kolo'), None, None),
    ('cyklo-zamky', R(r'cykl.*zamk|zamky na kolo'), None, None),
    ('cyklo-pumpy-a-naradi', R(r'cykl.*(pump|naradi|servis a udrzba)'), None, None),
    ('cyklo-tasky-a-nosice', R(r'cykl.*(kosik|brasn|nosic)|brasny na kolo'), None, None),
    ('svihadla', None, R(r'svihadl'), None),
    ('posilovaci-gumy', None, R(r'posilovac\w* (gum|pas)|odporov\w* gum|expander|(^|\W)o-?band|guma na cviceni|odporova guma|fitness guma|resistance band'), None),
    ('balancni-pomucky', None, R(r'balancn\w* (pol|podlozk|disk|cep|desk|kote|pomuck)|(^|\W)bosu|balance (board|pad)'), None),
    # ---- v3: merino first (the material beats the garment type), then the new product types ----
    ('merino-ponozky', None, R(r'merino\w*.*(ponozk|podkolenk)|(ponozk|podkolenk)\w*.*merino'), None),
    ('merino-pradlo', None, R(r'merino\w*.*(spodk|slip|boxerk|legin|spodni|kalhotk|podprsenk|pradl)|(spodk|slip|boxerk|legin|spodni pradl|kalhotk|podprsenk)\w*.*merino'), None),
    ('merino-mikiny', None, R(r'merino\w*.*(mikin|svetr|pulovr|fleece|bund|vest|kardigan)|(mikin|svetr|pulovr|bund|vest)\w*.*merino'), None),
    ('merino-doplnky', None, R(r'merino\w*.*(cepic|celenk|nakrcnik|satek|rukavic|kukl|buff|kulich)|(cepic|celenk|nakrcnik|rukavic|kukl|buff|kulich)\w*.*merino'), None),
    ('merino-tricka', None, R(r'merino'), None),
    ('lezecke-sedaky-a-pomucky', None, R(r'lezeck\w* (sedak|prilb|vest)|horolezeck\w* (sedak|prilb)|sedak.*lez|(^|\W)magnezi|lezeck\w* chyt|chyty (na|pro) lez|jistic|slaňov|slanov|brzda na lano'), None),
    ('lezecka-lana-a-karabiny', None, R(r'karabin|ferrat|(^|\W)lano(\W|$)|dynamick\w* lan|lezeck\w* lan|expreska|expresk|smyce|slaneni|ferratov'), None),
    ('lezecke-boty', None, R(r'lezecky|lezecke (bot|obuv)|(^|\W)lezecky(\W|$)(?!.*(sedak|prilb|lano|batoh|vest))|climbing shoe'), None),
    ('lezecke-boty', R(r'lezeni.*(boty|lezecky)|lezecke boty'), None, None),
    ('skolni-batohy', None, R(r'skoln\w* batoh|studentsk\w* batoh|batoh (do|na) skol|(^|\W)baagl|skolni aktovk|aktovk'), None),
    ('tasky-pres-rameno', None, R(r'(pres|na) rameno|dokladovk|crossbody|ledvink|bedern\w* (taska|pas)|taska na (pas|rameno)|sling bag|messenger'), None),
    ('plastenky', None, R(r'plastenk|(^|\W)ponc(o|a)|pláštěnk|rain ?poncho'), None),
    ('kombinezy', None, R(r'kombinez|overal|zimni set|lyzarsk\w* (set|souprav)|detsk\w* (set|souprav).*zimn|rampacs|romp'), None),
    # sneakers, not tents
    ('tenisky', None, R(r'stan smith'), None),
    # tent types (title rules, strongest signal first); each needs a tent word so poles, pegs and shoes never match
    ('detske-stany', None, R(r'^(?=.*(^|\W)(stan|stany|stanu|stanem|stanov\w*|tent)(\W|$)).*?(?:(detsk\w*|hrac\w*|pro deti)\W+(\w+\W+){0,3}stan|stan\w*\W+(\w+\W+){0,3}(detsk|hrac|pro deti))'), None),
    ('rybarske-doplnky', None, R(r'(kapr\w*|rybar\w*|bivvy)\W+(\w+\W+){0,3}(stolek|table|zidl\w*|kreslo|lehatko|postel|vozik)'), None),
    ('rybarske-stany', None, R(r'^(?=.*(^|\W)(stan|stany|stanu|stanem|stanov\w*|tent)(\W|$)).*?(?:(rybar\w*|kapr\w*|karp\w*|bivvy|biwy|bivak\w*)\W+(\w+\W+){0,4}(stan|bivak|bivvy)|(stan|bivak\w*)\W+(\w+\W+){0,4}(kapr|rybar|rybolov)|^(bivak|bivvy|biwy))'), None),
    ('tipi-a-lavvu', None, R(r'(^|\W)(tipi|tee-?pee|lavvu|laavu)(\W|$)'), None),
    ('pristresky-a-party-stany', None, R(r'party\W+stan|stan\W+party|(event|party|garden|zahradn\w*) shelter|(^|\W)(pavilon|pavilion|gazebo|altan)\w*|stanov\w* prist\w+|(^|\W)pristresek|sun ?shelter|slunecn\w* (stan|pristresek)'), None),
    ('pop-up-a-plazove-stany', None, R(r'^(?=.*(^|\W)(stan|stany|stanu|stanem|stanov\w*|tent)(\W|$)).*?(?:pop.?up|samorozkl\w*|instantn\w*|2 seconds|fast ?pitch|quick ?(up|pitch)|plaz\w*\W+(\w+\W+){0,2}stan|beach\W+(\w+\W+){0,2}(tent|stan)|stan\W+(\w+\W+){0,2}(plaz|beach))'), None),
    ('expedicni-stany', None, R(r'^(?=.*(^|\W)(stan|stany|stanu|stanem|stanov\w*|tent)(\W|$)).*?(?:4 ?(season|sezon)|ctyr ?sezon\w*|four ?season|expedic\w*|(extreme|horsk\w*|vysokohorsk\w*)\W+(\w+\W+){0,3}stan|stan\W+(\w+\W+){0,3}(extreme|expedic))'), None),
    ('rodinne-stany', None, R(r'^(?=.*(^|\W)(stan|stany|stanu|stanem|stanov\w*|tent)(\W|$)).*?(?:(^|\D)([4-9]|1[0-2])\s?(os\w*|p|person\w*|mistn\w*|-mistn\w*)(\W|$)|(^|\W)[4-9]p(\W|$)|rodinn\w*|family|tunel\w*|kopulov\w* stan\W+.*([4-9]|ctyr|sest))'), None),
    ('turisticke-stany', None, R(r'^(?=.*(^|\W)(stan|stany|stanu|stanem|stanov\w*|tent)(\W|$)).*?(?:trek\w*|turist\w*|hiking|backpack\w*|ultra ?light|(^|\W)ul\W+stan|stan\W+ul(\W|$)|(^|\W)[1-3]\s?(os\w*|p|person\w*|mistn\w*)(\W|$)|(^|\W)[1-3]p(\W|$)|dvou\w*|jednomist\w*|dvoumist\w*|tri ?mist\w*|\w*mistny\W+stan|outdoor\w*\W+stan)'), None),
    ('strechni-stany', None, R(r'stresn\w* stan|autostan|predstan|stan (na|k) (auto|streche)|dodavk\w* stan|(^|\W)napin\w* predstan'), None),
    ('detske-spacaky', None, R(r'detsk\w* (spaci pyt|spacak)|spacak.*dit|spacak.*detsk'), None),
    ('kajaky-a-cluny', None, R(r'kajak|kanoe|(^|\W)(nafukovaci )?clun|(^|\W)raft(\W|$)|pagaj|(^|\W)vesl(o|a)(\W|$)'), None),
    ('plovaci-vesty', None, R(r'plovac\w* vest|zachrann\w* vest|plovouc\w* vest|vesta (do|na) vod|life ?jacket'), None),
    ('elektrokolobezky', None, R(r'elektrick\w* kolobez|elektrokolobez|e-?scooter|elektro ?kolobez'), None),
    ('freestyle-kolobezky', None, R(r'freestyle kolobez|stunt (scooter|kolobez)|trick\w* kolobez'), None),
    ('discgolf', None, R(r'discgolf|disc golf|frisbee|letajici talir|aerobie|(^|\W)disk na (golf|frisbee)'), None),
    ('brankarske-rukavice', None, R(r'brankarsk\w* rukavic|rukavice brankar|goalkeeper glove'), None),
    ('fotbalove-chranice-a-stulpny', None, R(r'fotbalov\w* (chranic|stulpn)|stulpn|chranic\w* holeni.*fotbal|holenni chranic.*fotbal'), None),
    ('fotbalove-mice', None, R(r'fotbalov\w* (\w+ )?mic|mic (na|pro) (fotbal|futsal)|futsalov\w* mic|replik\w* mic'), None),
    ('florbalove-hole', None, R(r'florbalov\w* (hul|hole)|florbalka|hul\w* (na )?florbal|florbal\w* hul'), None),
    ('basketbalove-mice', None, R(r'basketbalov\w* (\w+ )?(mic|kos|desk)|mic (na|pro) basket|basketbalovy kos'), None),
    ('volejbalove-mice', None, R(r'volejbalov\w* (\w+ )?(mic|sit)|mic (na|pro) volejbal|volejbalov\w* sit|beach ?volley'), None),
    # racket sports before the generic "tenis" / "ostatni micove sporty"
    ('padel', None, R(r'padel|padelov'), None),
    ('squash', None, R(r'squash'), None),
    ('ragby-a-americky-fotbal', None, R(r'ragby|rugby|americk\w* fotbal'), None),
    ('baseball-a-softball', None, R(r'baseball\w* (palk|mic|rukavic|helm)|(palk|mic|rukavic)\w* (na )?(baseball|softball)|softball(?!.*(trick|mikin))'), None),
    ('hazena', R(r'^hazena'), None, None),
    ('hazena', None, R(r'(^|\W)hazenk\w*(?!.*(bot|obuv|tenisk))|hazen\w* (mic|branka|lepidl|pryskyric|sit)|(mic|branka|lepidlo|pryskyrice) \w*hazen'), None),
    # horse riding (Decathlon paths carry the sport as well)
    ('jezdecke-helmy', None, R(r'jezdeck\w* (prilb|helm)'), None),
    ('jezdecka-obuv', None, R(r'jezdeck\w* (vysok\w* )?(bot|obuv|cizm|polobot)|chapsy|(^|\W)chaps(\W|$)|jodhpur\w* bot'), None),
    ('jezdecke-kalhoty', None, R(r'rajtk|jezdeck\w* (kalhot|legin|breech)|jodhpur'), None),
    ('vybaveni-pro-kone', R(r'jezdectvi|(^|\W)kone(\W|$)|(^|\W)poni'), R(r'(^|\W)(podbrisnik|uzd[ay]|uzdecka|sedlo|sedlov\w*|trmen\w*|ohlavk?\w*|kopytn\w*|nauznik|hrebel\w*|pachov\w*|derka|kropenat|martingal|otepe?|ohlavka|vodici)'), None),
    ('vybaveni-pro-kone', None, R(r'(pro|na|pod) (kone|koni|poni)|pro koně|jezdeck\w* (sedl|uzd|derk|podbrisn)'), None),
    ('jezdecke-obleceni', None, R(r'jezdeck\w* (obleceni|polo|bund|vest|tricko|mikin|rukavic|ponozk|sako|soupr)'), None),
    ('jezdecka-obuv', R(r'jezdectvi.*(perka|chapsy|jezdecke boty|jezdecka obuv)'), None, None),
    ('jezdecke-obleceni', R(r'jezdectvi > jezdci > (jezdecke obleceni|obleceni)'), None, None),
    ('vybaveni-pro-kone', R(r'jezdectvi > (kone|pece o kone)'), None, None),
    ('jezdecke-doplnky', R(r'^jezdectvi'), R(r'^(?!.*(sedlo na|kolo|bike)).*'), None),
    # golf
    ('golfove-micky', None, R(r'golfov\w* mic|micky? (na )?golf|golf\w* (micky|ball)'), None),
    ('golfove-tasky-a-voziky', None, R(r'golfov\w* (bag|vak|task|voz|stojan)|(vozik|bag)\w* (na )?golf'), None),
    ('golfove-hole', None, R(r'golfov\w* (hul|dreve|zelezo|zeleza|putter|driver|wedge|set hul)|(^|\W)putter(\W|$)|golf\w* .*(wedge|driver)'), None),
    ('golfove-obleceni-a-obuv', None, R(r'golf\w* (polo|obleceni|bund|kalhot|sukn|obuv|bot|rukavic|cepice|ksiltovk)|(obuv|bot|rukavic|cepic)\w* (na )?golf'), None),
    ('golfove-hole', R(r'^golf > golfove (hole|sety)|golfove hole a sety'), None, None),
    ('golfove-micky', R(r'^golf > golfove micky|golfove micky'), None, None),
    ('golfove-tasky-a-voziky', R(r'^golf > golfove (tasky|voziky|bagy)|voziky'), R(r'golf'), None),
    ('golfove-obleceni-a-obuv', R(r'^golf > golfove (obleceni|obuv)'), None, None),
    ('golfove-doplnky', R(r'^golf'), None, None),
    ('golfove-doplnky', None, R(r'golf'), None),
    # dance, gymnastics, yoga
    ('tanecni-obleceni', None, R(r'tanecn\w* (obleceni|kalhot|top|sukn|trikot|saty)|baletn\w* (sukyn|sukn|trikot|obleceni|saty|top|bluz|tricko|kalhot|legin|body|pulover|svetr)|trikot(?!.*(dres|fotbal|hokej))|sukynk'), None),
    ('baletni-obuv', None, R(r'balet\w* (bot|obuv|piskot|cvick|bacor|pantof)|piskoty|ballet (shoe|slipper)'), None),
    ('tanecni-obuv', None, R(r'tanecn\w* (bot|obuv|tenisk)|(jazz|latin|street|hip.?hop) ?(shoe|dance|bot|obuv)'), None),
    ('pilates-pomucky', None, R(r'gymnastick\w* mic(?!.*(moderni|rytmick))|fitball|overball|balancni mic'), None),
    ('gymnasticke-pomucky', None, R(r'gymnastick\w* (pomuck|cvick|bot|stuh|kruh|ram|podlozk|pas|kladin)|mic (na|pro) (moderni )?gymnastik|kladina|cvicky(\W|$)|rytmick\w* gymnast|(^|\W)stuha(\W|$)|team ?gym'), None),
    ('meditace', None, R(r'medita|zafu|(^|\W)bolster'), None),
    ('jogove-pomucky', None, R(r'jogov\w* (blok|cihl|popruh|pas|kolo|valec|ručnik|rucnik|poduska)|popruh na jogu|(^|\W)yoga (block|strap|bolster|wheel)'), None),
    ('pilates-pomucky', None, R(r'pilates(?!\W*(leginy|kalhot|top|podprsenk|obleceni|tricko))|reformer|pilates ring|magick\w* kruh|overball'), None),
    # running specials
    ('bezecke-vesty-a-batohy', None, R(r'(bezeck|trailov|running|trail)\w* (vest|batoh|pack)|hydratacn\w* vest|bezecka vesta|vesta (na|pro) beh'), None),
    ('bezecke-opasky', None, R(r'(bezeck|running)\w* (opasek|ledvin)|opasek (na|pro) beh|pouzdro (na|pro) (telefon|mobil).*(beh|pas|paz)|bezecka ledvinka'), None),
    ('triatlon', None, R(r'triatlon|trisuit|tri.?suit'), None),
    ('atletika', None, R(r'atletick|hrot(y|u)? (na|pro) atlet|diskarsk|vrhac|ostep|atletik|start(ovaci)? blok|vrhac\w* (mic|kou)'), None),
    # hunting
    ('lovecke-obleceni', R(r'myslivost > myslivecke obleceni|myslivecke obleceni'), None, None),
    ('lovecke-obleceni', None, R(r'^(?!.*(nastrah|trpytk|prut|navijak|ryb)).*(lovec\w* (\w+ )?(obleceni|bund|kalhot|bot|obuv|vest|rukavic|cepic|kosil|tricko|triko|svetr|mikin|ponozk|kabat)|kamuflaz|maskovac|myslivecke? (obleceni|tricko|kosil|mikin|svetr|bund|kalhot))'), None),
    ('lovecke-vybaveni', R(r'^myslivost'), None, None),
    ('lovecke-vybaveni', None, R(r'^(?!.*(nastrah|trpytk|prut|navijak|ryb|kapr|splavk|mor)).*(lovec|myslivec|(^|\W)posed(\W|$)|nastrazn\w* (zver|zvere)|zverin)'), None),
]

# catch-alls by the shop's path only: last, so that a title that names clothing / shoes / a specific product type wins
LAST_RULES = [
    ('cyklo-prislusenstvi', R(r'cyklo prislusenstvi|cyklistika > prislusenstvi|cyklo|cyklistika'), None, None),
    ('outdoor-doplnky', R(r'^outdoor|sporty > outdoor|do prirody|otuzov'), None, None),
    ('fitness-pomucky', R(r'^fitness|posilovani|drobny fitness|pomucky na cviceni'), None, None),
    ('ostatni-micove-sporty', None, R(r'(^|\W)mic(e)?(\W|$)|softball'), R(r'^$|sport|mic')),
    # shop paths of whole categories whose product titles do not name the type (measured on the unmapped list of the 1. 11. build)
    ('sipkove-doplnky', R(r'^(letky|nasadky|hroty|pouzdra na sipky|barely|stonky|sipky > (letky|nasadky|hroty))|pouzdra na sipky'), None, None),
    ('sipkove-terce', R(r'^(terce|stojany na terce)|sipky > terce'), None, None),
    ('sportovni-kratasy', R(r'kratasy'), None, None),
    ('sportovni-rukavice', R(r'(^|> )rukavice$|rukavice a nakrcniky > rukavice|nakrcniky a rukavice > rukavice'), None, None),
    ('ostatni-micove-sporty', R(r'sportovni vybaveni > mice'), None, None),
    ('tenisky', R(r'boty > multifunkcni sportovni obuv'), None, None),
    ('sportovni-spodni-pradlo', R(r'spodni pradlo|boxerky|slipy'), None, None),
    ('turisticke-batohy', R(r'turisticke batohy|krosny'), None, None),
    ('mestske-batohy', R(r'(^|> )batohy$'), None, None),
    ('chranice-a-helmy', R(r'> helmy$'), None, None),
    ('lyzarske-doplnky', R(r'lyzarske hole|sjezdove lyzovani > lyzarske hole'), None, None),
    ('salova-obuv', R(r'volejbalove boty|salove boty|halove boty'), None, None),
    ('tenisky', R(r'chuze > obuv|obuv a doplnky na chuzi|> boty na chuzi'), None, None),
    ('cyklo-dily', R(r'cykl\w* komponent'), None, None),
    ('skateboardy', R(r'skate'), None, None),
    ('sportovni-tasky', R(r'tasky a kufry'), None, None),
    ('fotbal', R(r'^fotbal > vybaveni pro hrace'), None, None),
    ('fitness-pomucky', R(r'sporty > fitness > (cvicebni pomucky|fitness rukavice, opasky)|pomucky na domaci cviceni'), None, None),
]
RULES = TOP_RULES + [(slug, p, t, g) for slug, p, t, g in rules()] + LAST_RULES
# Evaluation order (title-audit of 1. 11.: 24 000 products named one thing and filed under another — "mikina" under "Bundy" because the shop's
# path says "Bundy a mikiny"): 1) rules that name a specific product type in the title, 2) the shop's own path, 3) generic title words
# ("bunda", "kalhoty", "boty", "taška") that only decide when nothing more specific did.
GENERIC = {'tenisky', 'sportovni-bundy-jaro-podzim', 'sportovni-kalhoty', 'sportovni-tricka', 'sportovni-vesty', 'sportovni-rukavice',
           'chranice-a-helmy', 'ostatni-micove-sporty', 'sportovni-tasky', 'mestske-batohy', 'hry-na-zahradu', 'outdoor-doplnky'}
PASS_A = [r for r in RULES if r[2] is not None and r[0] not in GENERIC]
PASS_B = [r for r in RULES if r[2] is None and r[1] is not None and r[0] not in GENERIC]
PASS_C = [r for r in RULES if r[0] in GENERIC or (r[1] is None and r[2] is None)]
ORDERED = PASS_A + PASS_B + PASS_C
for slug, *_ in RULES:
    assert slug in BY_SLUG, slug

# clothing / shoes categories (gender matters, fashion shops only with a sport brand)
APPAREL_ROOTS = {'sportovni-obleceni', 'sportovni-obuv'}


def section(slug):
    t = BY_SLUG[slug]
    ski_wear = slug == 'lyzarske-obleceni'
    while t[3]:
        t = BY_SLUG[t[3]]
        ski_wear = ski_wear or t[1] == 'lyzarske-obleceni'
    # ski clothing sits in the winter section for the visitor but is still clothing for vetoes, price floors and fashion rules
    return 'sportovni-obleceni' if ski_wear and t[1] == 'zimni-sporty' else t[1]


# Marketplace sellers stuff their titles with the category they want to rank for ("Zimní boty Atomic … + vázání" = skis, "Kalhoty Lymfodrenážní
# přístroj", "Trička … sauna"). In clothing / footwear / nutrition / fishing a title that also names another kind of product is not ours.
VETO_WEAR = re.compile(r'(^|\W)(sauna|sudov\w*|trikolk\w*|tri kolk\w*|elektrick\w*|elektro\w*|skutr\w*|motor\w*|sedac\w*|zahradn\w*|nabytek|pohovk\w*|lehatk\w*|zidl\w*|lavic\w*|sonar|plotter|lednic\w*|solarn\w*|panel|masazn\w* (pistol|pristroj)|theragun|lymfodren\w*|pressoterap\w*|therapy|trenazer\w*|rotoped\w*|kulecnik\w*|stul|stoly|stolek|narty|wiazani\w*|skis|skins|vazani|lyze|lyzi|sada lyz\w*|set lyz\w*|gw|strechni box|stresni box|box na|nosic\w*|zavazec\w*|bait boat|clun|kajak|paddleboard|stan|spacak|karimatk\w*|matrac\w*|hamak|hodinky|telefon|kamera|dalekohled|svitiln\w*|nabijec\w*|powerbank|20\d\d ?/ ?20?\d\d|(mi|x|nx|spx|sl|gs|fr|lz) ?1[0-4]|and (x|mi) ?\d+|revoshock|redster|hero elite|freebird|vazani)(\W|$)')
VETO_NUTR = re.compile(r'(panel|therapy|terapi|pistol|pristroj|theragun|masazn|lampa|termoterap|hodinky|vaha|trenazer|rotoped|elektrick|stul|sauna)')
VETO_FISH = re.compile(r'(^|\W)(lednic\w*|solarn\w*|panel|kamera|dron\w*)(\W|$)')
# brand-less fashion shops keep an item only with a word that is about sport itself ("Kira Sport Sandal" is a handbag-maker's model name)
SPORT_STRONG = re.compile(r'(funkcni|bezeck|beh(\W|$)|trenink|fitness|outdoor|treking|trek|lyz|ski(\W|$)|snowboard|cyklo|cyklist|termo|thermo|merino|softshell|fleece|flis|gore|dri.?fit|climalite|run(\W|ning)|training|yoga|joga|tenis|fotbal|basket|volejbal|hokej|plav|swim|hike|hiking|trail|protein|kreatin|bcaa|gainer|aminokyselin|syrovatk|izolat|pre-?workout|spalovac)')


def vetoed(slug, t):
    if re.search(r'(^|\W)(kesi|wloski)(\W|$)', t):  # fashion brand (wide trousers, dresses "s vazani" = ties), never sport gear
        return True
    root = section(slug)
    if root in ('sportovni-obleceni', 'sportovni-obuv', 'merino'):
        return bool(VETO_WEAR.search(t))
    if root == 'sportovni-vyziva':
        return bool(VETO_NUTR.search(t))
    if root == 'rybareni':
        return bool(VETO_FISH.search(t))
    return False


# ---- complete bikes vs. bike parts: "Gripy … na horské kolo" is a part, "Horské kolo GK2 26"" is a bike ----
BIKE_HEAD = re.compile(r'^(?:\w+[ -]){0,4}?(kolo|kola|elektrokolo|elektrokola|e-?bike|ebike|bicykl\w*|odrazedlo|odrazedla|trikolka)(?=\W|$)')
BIKE_ACC_PREP = re.compile(r'(?:^|\W)(na|pro|ke|k|do|od|pod|u|za|s) (?:\w+ ){0,2}(kolo|kola|kol|elektrokol\w*|bike|bicykl\w*|mtb)(?=\W|$)')
BIKE_PART_FIRST = re.compile(r'^(gripy|grip|plast|plaste|duse|sedlo|sedla|retez|retezy|prehazovack\w*|kazeta|kliky|klika|pedal\w*|brzd\w*|riditk\w*|predstavec|vidlic\w*|kryt|potah|nabijec\w*|baterie|blatnik\w*|zvonek|svetl\w*|kosik|nosic|tretry|ponozky|kratasy|dres|bunda|helma|prilba|rukavic\w*|obuv|boty|bryle|zamek|pumpa|tasky|brasna|motor|chranic|napinak|rafek|naboj|osa|lanko|sada|sedacka|vozik|stojan|navleky|kalhoty|tricko|vesta|cepice|nakrcnik|opasek|lahev|kosik|zrcatko|spojka|vidlice|servisni|nastroj|sada)(?=\W|$)')
BIKE_EXERCISE = re.compile(r'(posilovac\w*|domaci|treninkov\w*|fitness|spinning\w*|magnetick\w*|vzduchov\w*|stacionarn\w*|rehabilita\w*|pedalov\w*) (kolo|kola|bike|trenazer\w*)|rotoped|ergometr|airbike|air bike|cyklotrenazer|(^|\W)spinning(\W|$)|veloergometr|kolo.*(hms|insportline|trenazer)')
BIKE_CARE = re.compile(r'(^|\W)(mazivo|mazadl\w*|olej|cistic\w*|vosk(?!a)|wax|lubrik\w*|lube|lubricant|degreaser|sampon|sprej|odmastovac|chain)(\W|$)')
BIKE_PART_ANY = re.compile(r'(retez|retezy|clanku|clanek|cep|kazeta|prehazovack|pedal|brzdov|desticky|navaz|rafek|naboj|lanko|bowden|sedlovk|riditk|predstavec|baterie|nabijec|motor)')
BIKE_PATH = re.compile(r'(^|> )((horska|silnicni|gravel\w*|trekingova|mestska|detska|elektricka|elektrick\w*|skladaci|cross\w*|bmx)\s+)?(kola|jizdni kola|elektrokola|odrazedla)(\W|$)')
BIKE_PATH_NO = re.compile(r'prislusenstvi|komponent|dily|oblecen|obuv|tretry|helm|bryle|doplnk|servis|udrzba|naradi|tasky|svetl|zamk|pumpy')


HEAD_SLUG = {'bunda': 'sportovni-bundy-jaro-podzim', 'bundy': 'sportovni-bundy-jaro-podzim', 'mikina': 'mikiny', 'mikiny': 'mikiny', 'tricko': 'sportovni-tricka',
             'trika': 'sportovni-tricka', 'triko': 'sportovni-tricka', 'kalhoty': 'sportovni-kalhoty', 'rukavice': 'sportovni-rukavice', 'vesta': 'sportovni-vesty'}
HEAD_NOUN = re.compile(r'^(?:(?:pansk\w*|damsk\w*|detsk\w*|divci|chlapeck\w*|juniorsk\w*|unisex\w*|zimni|sportovni|funkcni|lehk\w*|dlouh\w*|kratk\w*) ){0,3}(' + '|'.join(HEAD_SLUG) + r')(?= )')


def _first(rules, p, t, g):
    for slug, rp, rt, rg in rules:
        if rp is not None and not rp.search(p):
            continue
        if rt is not None and not rt.search(t):
            continue
        if rg is not None and not rg.search(g):
            continue
        return slug
    return None


def _family(slug):
    """The level-2 ancestor ("sportovni-bundy" for all jackets), so that subtypes of one garment compare equal."""
    t = BY_SLUG[slug]
    chain = [t[1]]
    while t[3]:
        t = BY_SLUG[t[3]]
        chain.append(t[1])
    return chain[-2] if len(chain) > 1 else chain[0]


def bike_rule(p, t):
    """→ bike slug or None. Title decides first (head noun "kolo" within the first words, not an accessory phrase), the shop's path second."""
    if BIKE_PART_FIRST.search(t) or BIKE_ACC_PREP.search(t) or BIKE_EXERCISE.search(t) or BIKE_CARE.search(t) or 'gotu kola' in t:
        return None                      # "Gotu Kola" is a herb (food supplement), not a bike
    head = BIKE_HEAD.search(t)
    if head and head.group(1) in ('ebike', 'e-bike', 'bicykl') and BIKE_PART_ANY.search(t) and not re.search(r'(^|\W)(kolo|kola|elektrokolo)(\W|$)', t):
        return None                      # "Shimano řetěz SH CNE6070 E-BIKE …" is a chain for e-bikes
    pathy = BIKE_PATH.search(p) and not BIKE_PATH_NO.search(p)
    if not head and not pathy:
        return None
    if re.search(r'elektr|e-?bike|ebike|bosch|(^|\W)ep\d|pedelec', t) or (p and re.search(r'elektrokola|elektricka kola', p)):
        return 'elektrokola'
    if re.search(r'detsk|divci|chlapeck|junior|odrazedl|(^|\W)(12|14|16)("| palc| col)|do ?(10|12) let', t) or re.search(r'detska kola|odrazedla', p):
        return 'detska-kola'
    if re.search(r'horsk|mtb|celoodpruz|enduro|fatbike|dirt|downhill|freeride', t) or re.search(r'horska kola', p):
        return 'horska-kola'
    if re.search(r'silnicn|gravel|aero|triatlon|crossov|cyklokros', t) or re.search(r'silnicni kola|gravel', p):
        return 'silnicni-a-gravel-kola'
    if re.search(r'treking|mestsk|damsk|pansk|skladac|city|cross|retro|holandsk', t) or re.search(r'trekingova|mestska|skladaci', p):
        return 'trekingova-kola'
    return 'jizdni-kola'


def _fashion(slug, t, p):
    return slug not in ('sportovni-sukne-a-saty', 'kosile') and bool(FASHION.search(t) or FASHION.search(p)) and not SPORTY.search(t)


# Sub-categories of the cycling sections, decided from the title AFTER the section is known (no cycling word needed in the title:
# the feed path already said "cycling"). First match wins; no match keeps the section.
REFINE = {
    # --- bikes (3. 11. 2026). The non-bike rules come first (None = not sold here, a slug = it belongs elsewhere): the bike section had wheels,
    # holders, scooters, a tractor wheel and a gym machine in it because of the word "kolo". Then bike types by words and by known models.
    'jizdni-kola': [
        (None, r'malotraktor|kultivator|na karu|box pro psy|obal pro lahev|jeraby?\b'),
        ('kolobezky', r'kolobezk'), (None, r'bohuzel|rehabilita|cvicebn|kompresn|regeneracn|nafukovac|plazov|hrac[ií] kolo|proleze|bolero|instantni napoj|armadni|pryzov|poloos|eliptick|indorov|brisnich|rough ride|aqua back|palm kola'), ('energeticke-gely-a-tycinky', r'cokolad'), ('pilates-pomucky', r'jogov'), ('posilovaci-stroje', r'multipress|(^|\W)cyklo[pn]\b|atlasov'), ('fitness-pomucky', r'hula ?hoop'), ('pilates-pomucky', r'kolo jogy'),
        ('tenisky', r'adidas campus'),
        ('ebike-baterie', r'baterie'), ('cyklo-nosice-na-auto', r'nosic'),
        ('cyklo-prislusenstvi', r'drzak|stojan|nastenn|plachta|ochran\w* ramu|pasku ramu|chranic retezu|silikon|ochranna paska|snimac|merici|adapter|uchyt|zavazadlov|vak transport|cycplus|powermet|trenazer|podpora kola|handbike|prislusenstvi kolo'),
        ('cyklo-svetla', r'svetl[oa](\W|$)|svetel|osvetlen'),
        ('cyklo-dily', r'zaplet|naplet|(^|\W)kolo (zadni|predni)|(predni|zadni) kolo|ozubene kolo|spojka retezu|(^|\W)retez|(^|\W)(kmc|sram|roval)(\W|$)|rafek|nabojov|nahradni (kolo|predni|zadni)|upgrade kit|(^|\W)\d+-kolo|bafang|(^|\W)(fsa|sunrace)(\W|$)|prevodnik|pavouk|elektronicka sada|stahovak|guidon'),
        ('fitness-pomucky', r'podsedlove|lifespan|rotoped'),
        ('elektrokola', r'elektr|e-?bike|ebike|turbo (levo|kenevo|vado|como|tero|creo)'),
        ('skladaci-kola', r'skladac'), ('bmx-a-dirt-kola', r'(^|\W)(bmx|dirt)(\W|$)|pump ?track|freestyle'),
        ('detska-kola', r'(^|\W)(dino|toimsa|volare|casadei|early rider|beany|rascal|huffy|galaxy (neptun|early bird))(\W|$)|canull (16|20|24)|author (cosmic|record|simplex|smart|stylo|ultrasonic)|royal ?baby|capitan|detsk|junior|odrazedl'),
        ('fatbiky', r'fat ?bike|fatbike|tlust'),
        ('gravel-kola', r'gravel|grave\b|checkpoint|checkmate|checkout|diverge|crux|grevil|cyklokros|xplr'),
        ('silnicni-kola', r'silnicn|(^|\W)road|domane|madone|emonda|tarmac|roubaix|allez|aethos|pinarello|(^|\W)f ?series'),
        ('horska-kola', r'horsk|mtb|celoodpruz|enduro|downhill|supercaliber|procaliber|trek fuel|fuel ex|top fuel|slash|marlin|roscoe|stumpjumper|rockhopper|chisel|author (a-matrix|limit|vertigo|solution|impulse|horizon|aura|thema|kinetic|spirit|stratos|grand)|leader fox (mxc|jasper|factor)|storm \d+ shark|canull (26|27|29)|stevens tonga|mayo 29|apache hupahu'),
        ('krosova-kola', r'(^|\W)(kros|cross)|krosov|sirrus|trek fx|author airline'),
        ('trekingova-kola', r'treking|trekov|cestovn|mestsk|city|holandsk|retro|damsk|lady|author (gloria|linea|bello|classic|pegas|voyage|outset|rival|versus)|leader fox (toscana|ferrara|esent)'),
    ],
    'horska-kola': [('fatbiky', r'fat ?bike|fatbike|tlust'), ('celoodpruzena-horska-kola', r'celoodpruz|full ?susp|dualn|(^|\W)(fuel ex|top fuel|slash|spark|epic|stumpjumper)(\W|$)')],
    'silnicni-a-gravel-kola': [('krosova-kola', r'crossov|krosov'), ('gravel-kola', r'gravel|grave\b|checkpoint|checkmate|checkout|diverge|crux|grevil|cyklokros'), ('silnicni-kola', r'.')],
    'trekingova-kola': [('damska-kola', r'damsk|lady|zensk|women'), ('krosova-kola', r'(^|\W)(kros|cross)|krosov|sirrus|trek fx'),
                        ('mestska-kola', r'mestsk|city|holandsk|retro|dojizd|urban|author (gloria|linea|bello|classic|pegas)|leader fox (toscana|ferrara)')],
    'detska-kola': [(None, r'trasne'), ('kolobezky', r'kolobezk'), ('cyklisticke-helmy', r'^helma'), ('odrazedla', r'odrazedl|balance bike|balancni kolo'), ('detske-trikolky', r'trikolk|tricycle|(^|\W)trike(\W|$)'), ('detska-kola-12-14-palcu', r'(^|\W)(10|12|14)(\W|$)'), ('detska-kola-16-palcu', r'(^|\W)16(\W|$)'),
                    ('detska-kola-20-palcu', r'(^|\W)20(\W|$)'), ('detska-kola-24-palcu', r'(^|\W)24(\W|$)')],
    # e-bikes: out-of-section parts first, then by type; the umbrella "Trekingová a městská" splits into two
    'elektrokola': [
        ('elektrokolobezky', r'kolobezk|e-?scooter'), ('ebike-baterie', r'^(nahradni )?baterie|baterie specialized|nabijec'), ('cyklo-svetla', r'svetlo|spanninga|knog'),
        ('cyklo-dily', r'(^|\W)retez(\W|$)|(^|\W)connex|(^|\W)(fsa|sunrace)(\W|$)|prevodnik|pavouk|elektronicka sada|(^|\W)\d+-kolo|arcore'), ('cyklo-prislusenstvi', r'stojanek|stojan|drzak|montazni stojan|additive'),
        ('detska-elektrokola', r'juniorsk|detsk'), ('damska-elektrokola', r'damsk|lady|zensk|women|pro zeny|(^|\W)(viola|ardea|bellis|salvia|tilia)(\W|$)'),
        ('nakladni-elektrokola', r'cargo|nakladn'), ('fatbike-elektrokola', r'fat ?bike|fatbike|tlust|fat-?tire|[x×] ?[34]([.,]\d)?\b'),
        ('skladaci-elektrokola', r'skladac|sklopn|folding|kompaktn|prenosn|dvoumist|osszecsukhato|(^|\W)(dyu|t14|ep-?2|p20|f20|f26)(\W|$)'),
        ('horska-elektrokola', r'horsk|mtb|enduro|fuel|trail|fully|terenn|celoodpruz|plne odpruz|dualn|levo|kenevo|supercaliber|(^|\W)e-?mtb|(^|\W)(m20|l20|cabro)'),
        ('silnicni-a-gravel-elektrokola', r'gravel|silnicn|road|creo'),
        ('trekingova-elektrokola', r'treking|trekov|cross|krosov|touring|cestovn|vado|tero|sirrus|(^|\W)x-?rider|28 ?(palc|\"|’|”)|devron|corwin'),
        ('mestska-elektrokola', r'mestsk|city|dojizd|urban|holandsk|(^|\W)como(\W|$)'),
    ],
    'trekingova-a-mestska-elektrokola': [('mestska-elektrokola', r'mestsk|city|dojizd|urban|holandsk|retro'), ('trekingova-elektrokola', r'.')],
    'cyklisticke-helmy': [('detske-cyklohelmy', r'detsk|junior|(^|\W)kids?(\W|$)|dite|deti|disney|youth|(^|\W)(boy|girl)'), ('mtb-a-integralni-helmy', r'mtb|integraln|enduro|downhill|full ?face|(^|\W)(trail|bmx)(\W|$)'),
                          ('silnicni-cyklohelmy', r'silnic|(^|\W)road|aero|gravel|time trial'), ('mestske-cyklohelmy', r'mestsk|(^|\W)(city|urban)|komut|commut')],
    'cyklisticke-obleceni': [('cyklisticke-rukavice', r'rukavic'), ('cyklisticke-ponozky', r'ponozk'), ('cyklisticke-navleky', r'navlek|rukavy|nohavice|nastehny|rukaviky'),
                             ('cyklisticke-bundy-a-vesty', r'bund|(^|\W)vest|plastenk|pelerin|softshell|vetrovk'), ('cyklisticke-kratasy-a-kalhoty', r'kratas|sortk|kalhot|traky|(^|\W)bib|kolenovk'),
                             ('cyklisticke-dresy', r'(^|\W)dres')],
    # hockey: what is left in the generic section is sorted by type (feed paths are not needed for these words); misfiled skirts leave
    'hokej': [('pozemni-hokej', r'pozemn|field hockey|(^|\W)fh ?\d|hockey field'), ('sportovni-sukne-a-saty', r'(^|\W)(sukn\w*|skort|saty)(\W|$)'),
              ('brusle', r'krasobrusl|roztahovac|kacenk|(damsk|divci|chlapec)\w* brusl|rekreacn'),
              ('hokejove-suveniry-a-karty', r'karty|prives|minipuk|mini hokejov|mini ice|mini hockey|suvenyr|sberatel|figurk|plysov|hrnek|polstar'),
              ('hokejove-brankarske-vybaveni', r'goalie|brankar|lapak|vyrazec|goal pad'),
              ('hokejove-pasky-a-doplnky', r'paska|(^|\W)tape|vosk|wax|tkanick|snerovadl|omotavk|brousek|ostric|(^|\W)laces?(\W|$)|chranic\w* brusl|protektor'),
              ('hokejove-brusle', r'brusl|skates?(\W|$)'), ('hokejove-helmy-a-mrizky', r'helm|prilb|mrizk|vizir|kosik|visor|(^|\W)cage|maska'),
              ('hokejove-puky-a-branky', r'(^|\W)puk|brank|passer|passing|radar|tren|rebound|shooting|cvic|(^|\W)net(\W|$)|(^|\W)mini|dryland'),
              ('hokejove-cepele-a-nasady', r'cepel|blade|nasad|shaft'),
              ('hokejove-chranice', r'chranic|shin|ramen|girdle|kalhot|pants|loket|nahrdeln|rukavic|glove|suspens|pant cover|holen|elbow|(^|\W)pad(s)?(\W|$)|kolen'),
              ('hokejove-tasky', r'taska|tasky|batoh|(^|\W)bag|backpack|(^|\W)vak|kapsa|obal'),
              ('hokejove-dresy-a-obleceni', r'dres|replik|jersey|mikin|tricko|triko|bunda|cepice|ksiltovk|ponozk|podkolen|ribano|teplak|kratas|stulp|leginy|kosile|tilko|souprav')],
    'cyklo-prislusenstvi': [('cyklisticke-bryle', r'bryl'), ('cyklo-chranice', r'chranic|protektor|kolenn|loketn|brneni'),
                            ('cyklo-lahve-a-drzaky', r'lahev|lahve|bidon|kosik na lahev|drzak\w* \w*\s?(telef|mobil)'), ('cyklo-zvonky-a-zrcatka', r'zvonek|zvonky|klakson|zrcatk')],
}
# wheels, tyres, lights and small parts that the shops (and some machine-translated French titles: "Horský bicykl Gurpil … Tubeless") list as "bicykl/kolo":
# they leave every bike type for the parts / accessories sections
_PARTS = r'tubeless|(^|\W)(pneu|roue)(\W|$)|pneumatik|gurpil|atran ?velo|(kenda|maxxis|pirelli|panaracer|schwalbe|continental)(\W|$)|zaplet|naplet|(^|\W)(zadni|predni) kolo|guidon|(^|\W)zipp(\W|$)|menic|rdrx'
_ACC = r'drzak|stojan|trojnoz|uchyt|pouzdro|blatnik|adapter|comboloc|ovladac|patka|kryt na motor|vodici retezu|(^|\W)packa|svetl[oa](\W|$)|lumen|(^|\W)lux(\W|$)|osvetlen|kryt|potah|(^|\W)kos(\W|$)|taska|vozik|kocarek|meric|zavesn'
for _k in ('horska-kola', 'silnicni-a-gravel-kola', 'trekingova-kola', 'detska-kola'):
    REFINE[_k][0:0] = [('cyklo-dily', _PARTS), ('cyklo-prislusenstvi', _ACC)]
# ---- winter sports (3. 11. 2026): clothing first (a jacket with "snowboard" in the title is a jacket), then the hardware by type ----
_SKI_WORDS = r'lyzarsk|lyzar|snowboard|(^|\W)ski(\W|$)|skialp|bezk|bezeck\w* lyz'
_WAX = r'vosk|(^|\W)wax|klister|hotbox|stoupaci pasta|^(?!.*(lyze|lyzi|vazani|hole|boty|rukavic|bunda|kalhot)).*(^|\W)(toko|swix|vauhti|holmenkol|rode|briko|skigo)(\W|$)|brusny|pilnik|hrany (na|pro)|mazani|skrabk|kartac|(^|\W)(fart|cire)(\W|$)|zakladni .*skluznic'
_BAG = r'(^|\W)(vak|vaky|task\w*|batoh\w*|obal|pouzdr\w*|bag)(\W|$)'
_WINTER_WEAR = [
    ('snowboardove-chranice', r'chranic|paterak|(^|\W)(impact|protector)|ochranne (sortky|kalhot)'),
    ('lyzarske-kombinezy', r'kombinez|overal'),
    ('lyzarske-bundy', r'bund|anorak|parka|(^|\W)(vesta|vesty)(\W|$)|jacket'),
    ('lyzarske-kalhoty', r'kalhot|(^|\W)traky|nohavice|pants'),
    ('lyzarske-termopradlo', r'termopradl|termo (tric|trik|kalh|spod|set|sada)|funkcni (pradl|tric|trik|spod|set|sada)|spodni pradlo|(^|\W)(merino|base ?layer)|komplet termo|(^|\W)spodky(\W|$)'),
    ('lyzarske-ponozky', r'ponozk|podkolenk|(^|\W)socks?(\W|$)'),
    ('lyzarske-rukavice', r'rukavic|palcak|(^|\W)gloves?(\W|$)|(^|\W)mitt|(^|\W)(mufle|mufl\w*|ganty)(\W|$)'),
    ('lyzarske-cepice-a-nakrcniky', r'cepic|celenk|nakrcnik|(^|\W)kukl|satek|ksiltovk|(^|\W)(beanie|beany|neck)(\W|$)'),
    ('mikiny', r'mikin|hoodie|svetr'),
    ('sportovni-tricka', r'(^|\W)(tricko|trika|triko|tricka)(\W|$)'),
]
_SKI_HEAD = r'(nakrcnik|kukl|celenk|cepic|(^|\W)satek|buff|(^|\W)beanie).*(' + _SKI_WORDS + r')|(' + _SKI_WORDS + r').*(nakrcnik|kukl|celenk|cepic|(^|\W)satek|buff|(^|\W)beanie)'
_SKI_GEAR_COMMON = [('lyzarske-helmy', r'helm|prilb'), ('lyzarske-bryle', r'(^|\W)bryle|goggle|zorn'), ('lyzarske-vosky', _WAX)]
REFINE.update({
    'sjezdove-lyze': _WINTER_WEAR + _SKI_GEAR_COMMON + [
        ('bezecke-boty', r'(boty|obuv).*kolecko\w* lyz|kolecko\w* lyz.*(boty|obuv)'),
        ('lyzarske-doplnky', r'sportube|popruh|zamek na lyz|stojan|sverak|drzak|(^|\W)hroty|edge tuner|edger|thermo belt|(^|\W)belt(\W|$)'),
        ('bezecke-lyze', r'kolecko\w* lyz|roller ?ski'),
        ('lyzarske-boty', r'(lyzarsk|sjezdov)\w* bot|lyzaky|(^|\W)(ski|skiing) boots?|(lyzarsk|sjezdov)\w* obuv'),
        ('lyzarske-hole', r'(^|\W)(hul\w*|hole|poles?)(\W|$)'),
        ('lyzarske-vaky-a-tasky', _BAG),
        ('lyzarske-vazani', r'^(?!.*(lyze|lyzi|\+|(^|\W)set(\W|$)|komplet)).*(vazani|binding)'),
        ('detske-lyze', r'detsk|junior|(^|\W)jr(\W|$)|(^|\W)kids?(\W|$)|(^|\W)(boy|girl)s?(\W|$)'),
        ('lyze-komplety', r'\+|vazani|(^|\W)set(\W|$)|komplet|binding'),
    ],
    'snowboarding': _WINTER_WEAR + _SKI_GEAR_COMMON + [
        ('snowboardove-chranice', r'chranic|paterak|(^|\W)(impact|protector)'),
        ('snowboardova-vazani', r'^(?!.*\+)(vazani|(snowboardov\w* )?vazani|bindings?)|^(?!.*(snowboard \w+ \d{3}|\+)).*(vazani|binding)'),
        ('snowboardove-boty', r'snowboardov\w* bot|(^|\W)(boty|boot|boots)(\W|$)'),
        ('lyzarske-vaky-a-tasky', _BAG),
        ('snowboardy', r'snowboard|(^|\W)board(\W|$)|prkno|deska'),
    ],
    'bezecke-lyzovani': _WINTER_WEAR + _SKI_GEAR_COMMON + [
        ('lyzarske-hole', r'(^|\W)(hul\w*|hole|poles?)(\W|$)'),
        ('lyzarske-vaky-a-tasky', _BAG),
        ('bezecke-boty', r'bezeck\w* bot|boty na bezk|(^|\W)(boty|boot|boots)(\W|$)|(^|\W)(sns|nnn)\w* bot'),
        ('bezecke-vazani', r'^(?!.*(lyze|lyzi|\+|(^|\W)set(\W|$)|komplet)).*(vazani|binding|(^|\W)(prolink|turnamic)(\W|$))'),
        ('bezecke-lyze', r'lyze|lyzi|(^|\W)(skate|classic|combi|mohero|twin skin)(\W|$)|(^|\W)bezky(\W|$)'),
    ],
    'skialpinismus': _WINTER_WEAR + _SKI_GEAR_COMMON + [
        ('lyzarske-hole', r'(^|\W)(hul\w*|hole|poles?)(\W|$)'),
        ('lyzarske-vaky-a-tasky', _BAG),
        ('skialpove-lyze', r'lyze|lyzi|(^|\W)(set|komplet)(\W|$)'),
        ('skialpove-pasy', r'stoupac|(^|\W)(skins?|pasy)(\W|$)'),
        ('skialpove-boty', r'(^|\W)(boty|bota|boot|boots)(\W|$)|skialpov\w* bot'),
        ('skialpove-vazani', r'vazani|binding'),
    ],
    'lyzarske-doplnky': [(None, r'vazani\w* (vzadu|na zadech|v pase|na boku)|s vazanim (vzadu|na zadech)|kesi wloski|plus size|viskoz|tencel|teplakov|(^|\W)(polski|gap)(\W|$)')] + _WINTER_WEAR + [
        ('lyzarske-vosky', _WAX),
        ('lyzarske-vaky-a-tasky', _BAG),
        ('lyzarske-helmy', r'helm|prilb'), ('lyzarske-bryle', r'(^|\W)bryle|goggle'),
        ('lyzarske-hole', r'(^|\W)(hul\w*|hole|poles?)(\W|$)'),
        ('bezecke-vazani', r'(vazani|binding).*(bezeck|bezk|nnn|sns|prolink|turnamic)|(bezeck|bezk|nnn|sns|prolink|turnamic).*(vazani|binding)'),
        ('skialpove-vazani', r'(vazani|binding).*(skialp|tlt|tech|pin|touring)|(skialp|dynafit|tlt|kingpin|speed turn).*(vazani|binding)'),
        ('snowboardova-vazani', r'(vazani|binding).*snowboard|snowboard.*(vazani|binding)|(^|\W)(jones|flow|union)(\W|$).*(vazani|binding)'),
        ('lyzarske-vazani', r'vazani|binding'),
    ],
    'sportovni-rukavice': [('lyzarske-rukavice', _SKI_WORDS + r'|palcak')],
    'termopradlo': [('lyzarske-termopradlo', _SKI_WORDS)],
    'cepice-a-celenky': [('lyzarske-cepice-a-nakrcniky', _SKI_HEAD)],
    'nakrcniky-a-satky': [('lyzarske-kalhoty', r'(' + _SKI_WORDS + r').*kalhot|kalhot.*(' + _SKI_WORDS + r')'), ('lyzarske-bundy', r'(' + _SKI_WORDS + r').*bund|bund.*(' + _SKI_WORDS + r')'), ('lyzarske-cepice-a-nakrcniky', _SKI_HEAD)],
    'kombinezy': [('lyzarske-kombinezy', _SKI_WORDS)],
    'brusle': [
        (None, r'puncoch|ponozk|kalhot|saty|sukn'),
        ('hokejove-brusle', r'hokej|hockey|(^|\W)(bauer|ccm|jetspeed|tacks)(\W|$)'),
        ('krasobruslarske-brusle', r'krasobrusl|figure|(^|\W)(jackson|risport|edea|graf)(\W|$)'),
        ('rekreacni-brusle', r'brusl|skates?(\W|$)|(^|\W)ice(\W|$)'),
    ],
})

# Winter leaf categories: items the broader rules left in the wrong leaf (audit 3. 11. 2026)
REFINE['lyzarske-boty'] = [
    ('bezecke-boty', R(r'fischer (xc|otx|bcx|travers|rc\d? ?(classic|skate|combi|ws)|speedmax)|(^|\W)(skol|alpina) |(^|\W)nordic(\W|$)')),
    ('skialpove-boty', R(r'transalp|(^|\W)(touring|skitour)(\W|$)')),
    ('lyzarske-vaky-a-tasky', R(r'(^|\W)(batoh|taska)(\W|$)|heatbag')),
]
REFINE['lyzarske-bundy'] = [
    (None, R(r'(^|\W)(kesi|wloski)(\W|$)')),
    ('lyzarske-termopradlo', R(r'spodni termo|termokalhot|spodni (kalhot|tricko)')),
    ('snowboardove-chranice', R(r'polstrovan\w* lyzarsk\w* pas|(^|\W)pas (na|pro) ')),
]
REFINE['lyzarske-kalhoty'] = [
    (None, R(r'(^|\W)(kesi|wloski)(\W|$)')),
    (None, R(r'magnum')),
    ('lyzarske-termopradlo', R(r'spodni tricko|spodni (kalhot|pradl)|dlouhy rukav')),
]
REFINE['lyzarske-termopradlo'] = [
    (None, R(r'teplomer')),
    ('lyzarske-bundy', R(r'(^|\W)bund')),
    ('lyzarske-rukavice', R(r'rukavic')),
]
REFINE['lyzarske-vosky'] = [
    ('lyzarske-vaky-a-tasky', R(r'bottlebag|vak na (bezky|lyze)|(^|\W)taska(\W|$)')),
    ('lyzarske-doplnky', R(r'podpera|upinac')),
]
REFINE['lyzarske-vazani'] = [
    (None, R(r'(^|\W)(kesi|wloski)(\W|$)|(^|\W)(saty|kratasy)(\W|$)')),
]
REFINE['lyze-komplety'] = [
    (None, R(r'(^|\W)(kesi|wloski)(\W|$)')),
]
REFINE['detske-lyze'] = [
    ('lyzarske-cepice-a-nakrcniky', R(r'(^|\W)(beany|beanie)(\W|$)')),
]
# Sleds and bobsleds: drop food (cocoa / soy "boby"), hats and polos named "Bob", shoes of the Skechers "Bob" line, slippers called "Sane"
REFINE['sane-a-boby'] = [
    (None, R(r'kakao|sojov|edamame|fazol|klobouk|(^|\W)polo(\W|$)|(^|\W)(cepic\w*|ksiltovk\w*|kulich)(\W|$)')),
    ('pantofle-a-zabky', R(r'pantofl|(^|\W)aquos(\W|$)')),
    ('tenisky', R(r'skechers|tenisk|(^|\W)bbk(\W|$)|b\.?cute|(^|\W)boty(\W|$)')),
    ('fitness-pomucky', R(r'zatez\w* sane|sled ?(v2|master)|sledmaster|xt3|odporov\w*,? (rychlostn|silov)|hiit|postroj\w* ')),
]
# Audit 3. 11. 2026: snowboardy / lyzarske-bryle / spaci-pytle (boots, socks, lenses, liners, fishing bed systems filed in the main category)
REFINE['snowboardy'] = [
    ('zimni-obuv', r'(^|\W)ecco(\W|$)'),
    ('lyzarske-ponozky', r'ponozk|socks?(\W|$)|(^|\W)smartwool(\W|$)'),
    ('sane-a-boby', r'kluzak|skyboard|(^|\W)sanky|(^|\W)bob(\W|$)'),
    ('snowboardova-vazani', r'^(?!.*(\+|(^|\W)set(\W|$)|komplet|snowboard \w+ \d{3})).*(vazani|binding)'),
    ('snowboardove-boty', r'^(?!.*(\+|(^|\W)set(\W|$)|komplet|vazani)).*(obuv|(^|\W)(boty|bota|boot|boots)(\W|$)|(^|\W)boa(\W|$))'),
    ('snowboardove-sety', r'^(?!.*bez vazani).*(\+|(^|\W)(set|komplet|package)(\W|$)|s vazanim|vazani)'),
]
REFINE['lyzarske-bryle'] = [
    ('sportovni-bryle', r'(^|\W)laceto(\W|$)|slunecn\w* fotochrom'),
    ('nahradni-zorniky', r'^(?!.*(lyzarske|snowboardove|sjezdove) bryle .*(zornik|sklo|lens|cocka)).*(nahradni|vymenn\w* (zornik|sklo|skla|cocky)|pouzdro na|(^|\W)lens case|zornik\w* (do|k|pro)|(^|\W)zornik(\W|$)|(^|\W)sp lens)'),
]
REFINE['spaci-pytle'] = [
    (None, r'pro (miminko|miminka|novorozen|batol)|muselin|sleepee'),
    ('rybarske-spacaky', r'lehatk\w*|bedchair|bed syste|sleep(ing)? syste|luzko se spacak|(^|\W)(trakker|giants fishing|jrc|prologic|gardner|delphin|mikado)(\W|$)|rybar|carp|(^|\W)fox (?!outdoor)'),
    ('vlozky-do-spacaku', r'(^|\W)(vlozk\w*|liner\w*)(\W|$)|spacakov\w* prikryvk|(obal|vak|taska)\w* (na|do|pro) (spac|spaci)|kompres\w* (obal|vak)|storage bag|obal na spaci|(^|\W)tyvek|bivy|(^|\W)siet\w* skladovaci|skladovaci obal'),
    ('detske-spacaky', r'(^|\W)(detsk\w*|junior\w*|jr|kids?|deti|dite)(\W|$)'),
    ('perove-spacaky', r'perov|(^|\W)down(\W|$)|(^|\W)peri(\W|$)'),
    ('dekove-spacaky', r'dekov|(^|\W)deka(\W|$)|spacak s prehozem'),
]
REFINE['jizdni-kola'][0:0] = [('cyklo-dily', _PARTS), ('cyklo-prislusenstvi', _ACC)]
# ---- 11. 11. 2026 content gap (reports/sporteka/content-gap-2026-11.md): demand that had no category of its own ----
_FIT_FOOD = (r'(arasidov|orisk|mandlov|kesu|liskooris|pistaciov)\w* (maslo|krem)|maslo z (arasidu|mandli|kesu)|proteinov\w* (kase|palacink|pudink|krem|pomazank|chlebic|testovin|wafl)|'
             r'(palacink|pancake|wafl)\w*.*(mix|smes)|(ovesn|proteinov)\w* kase|sirup (bez|0|zero)|(zero|0 ?kcal|nizkokaloric)\w* sirup|rizov\w* (chlebic|plack)|fit (sirup|omack|dresink)')
for _parent, _rules in {
    'kardio-trenazery': [('rotopedy', r'rotoped|spinning|ergometr|air ?bike|cyklotrenazer'), ('behaci-pasy', r'bezeck\w* pas|chodic\w* pas|treadmill|walking ?pad'),
                         ('elipticke-trenazery', r'eliptick|crosstrainer|cross trainer'), ('veslovaci-trenazery', r'veslovac|(^|\W)rower(\W|$)')],
    'masazni-pomucky': [('masazni-pistole', r'masazn\w* pistol|massage gun')],
    'vitaminy-a-mineraly': [('omega-3', r'omega.?3|rybi olej|rybi tuk'), ('horcik', r'horcik|magnesium|magnesia|magnezium')],
    'ostatni-doplnky-stravy': [('ashwagandha', r'ashwagandh')],
    'barefoot-obuv': [('ponozkoboty', r'ponozkobot|skinners|fivefingers|five fingers')],
    'posilovaci-stroje': [('posilovaci-lavice', r'lavic|(^|\W)bench(\W|$)')],
    'sportovni-hodinky': [('chytre-hodinky', r'chytr\w* hodink|smart ?watch|fitness naramek|chytry naramek|(^|\W)(apple watch|amazfit|huawei watch|fitbit|galaxy watch)')],
    'obleceni-bojove-sporty': [('kimona', r'kimono|judogi|karategi|dobok|(^|\W)gi (pro|bjj)|bjj gi')],
}.items():
    REFINE.setdefault(_parent, [])[0:0] = _rules
# ---- 16. 11. 2026 January wave: own loop, the parents above keep their rules (a repeated dict key would replace them) ----
for _parent, _rules in {
    'sane-a-boby': [('kluzaky-na-snih', r'kluzak|klouzak|snezn\w* talir|(^|\W)talir na snih|snow ?(rocket|tube)|lopat\w* (na|k) (sjezd|klouz)')],
    'posilovaci-stroje': [('posilovaci-veze', r'^(?!.*(kladk|lank|madl|nahradn|prislusenstv|tyc k)).*(posilovac\w* vez|multistanic|multipos|posilovac\w* stanic|multifunkcni posilovac)')],
    'pilates-pomucky': [('gymnasticke-mice', r'gymnast\w* mic|fit ?ball|gym ?ball|balancn\w* mic|rehabilitac\w* mic|overbal|(^|\W)mic (na|pro) (cviceni|sezeni)|sedaci mic|swiss ?ball')],
    'fitness-pomucky': [('gymnasticke-mice', r'gymnast\w* mic|fit ?ball|gym ?ball|balancn\w* mic|rehabilitac\w* mic|overbal|sedaci mic|swiss ?ball')],
    'gymnasticke-pomucky': [('gymnasticke-mice', r'gymnast\w* mic|fit ?ball|gym ?ball|balancn\w* mic|overbal')],
    'cinky-a-kotouce': [('zatezove-vesty', r'zatez\w* vest|weight ?vest')],
    'funkcni-trenink': [('zatezove-vesty', r'zatez\w* vest|weight ?vest')],
    'aminokyseliny-bcaa': [('glutamin', r'^(?!.*(bcaa|eaa|2:1:1|4:1:1)).*glutamin')],
    'vitaminy-a-mineraly': [('vitamin-d', r'^(?!.*(omega|rybi)).*(vitamin d(\d|\W|$)|(^|\W)d3(\W|$)|cholekalciferol)'), ('vitamin-c', r'vitamin c(\W|$)|kyselin\w* askorb'), ('zinek', r'^(?!.*(magnes|horcik|kolagen|multivit)).*(^|\W)(zinek|zinku|zinc)(\W|$)')],
    'energeticke-gely-a-tycinky': [('fit-potraviny', _FIT_FOOD)],
    'proteiny': [('fit-potraviny', _FIT_FOOD)],
    'proteinove-tycinky-a-snacky': [('fit-potraviny', _FIT_FOOD)],
    'sportovni-vyziva': [('fit-potraviny', _FIT_FOOD)],
}.items():
    REFINE.setdefault(_parent, [])[0:0] = _rules
# ---- 16. 11. 2026 January wave 2: own loop again (inserted in front of the older rules of the same parent) ----
_ELEKTRO = r'^(?!.*(bcaa|eaa|aminokysel|protein|kolagen|collagen|kreatin|creatin|gainer)).*(elektrolyt|electrolyt|salt ?(caps|tabs|stick)|soln\w* tablet|(^|\W)sul\w* v tablet)'
_MULTIVIT = r'^(?!.*(protein|gainer|pro psy|pro kone|pro kocky|(^|\W)psy(\W|$))).*(multi.?vit|multi.?mineral|vitaminov\w* a mineraln\w* komplex)'
_KARNITIN = r'karnitin|carnitin|carnipure'
_PROBIO = r'probiot|lactobacil|bifidobakter|bifidobacter|(^|\W)lacto\w* (rhamnos|acidoph)'
_TRIBULUS = r'tribulus|kotvicn'
_KURKUMA = r'kurkum|curcum|turmeric'
_GREENS = r'^(?!.*(cloud|versa|bot[ay]|obuv|tenisk|trick|mikin)).*(spirulin|chlorell|super ?greens|(^|\W)greens(\W|$)|mlad\w* (jecmen|psenice)|barley grass|zelen\w* (superfood|smoothie|jecmen))'
_SEJKR = r'^(?!.*(trick|triko|trika|mikin|kosil|cepic|ponoz|svetr|chrastit|termolah|termosk|ice shaker|(^|\W)nba(\W|$)|\+ ?(sejkr|shaker)|protein\w* \d)).*(sejkr|shaker|(^|\W)mixer (na|pro) protein|smart ?shake)'
_BOSU = r'^(?!.*(balance ball|(^|\W)mic(\W|$))).*((^|\W)bosu(\W|$)|half ?ball|balancn\w* (podlozk|polokoul|cock|disk|polstar|vankus)|balance (pad|trainer|disc|cushion)|senzomotor\w* (podlozk|cock|disk|polstar)|dynair)'
_MEDBAL = r'^(?!.*(stojan|drzak|regal|grip|sedl)).*(medicinbal|medicine ?ball|slam ?ball|wall ?ball|(^|\W)med ?ball)'
_ZEBRINY = r'^(?!.*(triko|tricko|mikin|divci|chlapeck)).*(zebrin|ribstol|swedish ladder|stall bars)'
_STOJAN = r'^(?!.*(drep|squat|power ?rack|klec|bench|lavic|medicinbal|kolo|bike)).*((stojan|regal|drzak|vesak)\w* (na |pro )?(\w+ )?(cink|jednoruc|kotouc|kettlebel|os[auy]?(\W|$)|zavazi)|dumbbell rack|plate (tree|rack)|toast rack)'
_REFLEX = r'^(?!.*(polokosil|tricko|triko|bunda|kalhot|pro psa|psi|canihunt)).*(reflexn\w* vest|hi-?vis\w* vest|vest\w* (s )?reflex|bezpecnostn\w* vest|vystrazn\w* vest)'
_KUKLA = r'^(?!.*(neopren|potap|freediv|spearfish)).*((^|\W)kukl[ayu]?(\W|$)|balaclava)'
_PATER = r'chranic\w* (pater|zad)|(^|\W)pater\w* chranic|back protector|spine protector|back ?pro(\W|$)'
_IMPREG = r'^(?!.*(s impregnac|impregnovan)).*(impregnac|nikwax|grangers|tx\.? ?direct|(^|\W)proof (spray|sprej)|water ?proof(ing)? spray)'
for _parent, _rules in {
    'iontove-napoje': [('elektrolyty', _ELEKTRO)],
    'aminokyseliny-bcaa': [('elektrolyty', _ELEKTRO), ('l-karnitin', _KARNITIN)],
    'energeticke-gely-a-tycinky': [('elektrolyty', _ELEKTRO)],
    'vitaminy-a-mineraly': [('multivitaminy', _MULTIVIT), ('probiotika', _PROBIO), ('spirulina-chlorella', _GREENS),
                            ('tribulus', _TRIBULUS), ('kurkuma', _KURKUMA)],
    'spalovace-tuku': [('l-karnitin', _KARNITIN)],
    'ostatni-doplnky-stravy': [('elektrolyty', _ELEKTRO), ('multivitaminy', _MULTIVIT), ('l-karnitin', _KARNITIN),
                               ('probiotika', _PROBIO), ('tribulus', _TRIBULUS), ('kurkuma', _KURKUMA), ('spirulina-chlorella', _GREENS)],
    'sportovni-vyziva': [('elektrolyty', _ELEKTRO), ('multivitaminy', _MULTIVIT), ('l-karnitin', _KARNITIN),
                         ('probiotika', _PROBIO), ('tribulus', _TRIBULUS), ('kurkuma', _KURKUMA), ('spirulina-chlorella', _GREENS), ('sejkry', _SEJKR)],
    'lahve-a-termosky': [('sejkry', _SEJKR)],
    'fitness-pomucky': [('sejkry', _SEJKR), ('balancni-podlozky-bosu', _BOSU), ('medicinbaly', _MEDBAL), ('stojany-na-cinky', _STOJAN)],
    'balancni-pomucky': [('balancni-podlozky-bosu', _BOSU)],
    'pilates-pomucky': [('balancni-podlozky-bosu', _BOSU), ('medicinbaly', _MEDBAL)],
    'funkcni-trenink': [('medicinbaly', _MEDBAL), ('zebriny', _ZEBRINY)],
    'hrazdy-a-bradla': [('zebriny', _ZEBRINY)],
    'posilovaci-stroje': [('zebriny', _ZEBRINY)],
    'gymnasticke-pomucky': [('zebriny', _ZEBRINY)],
    'cinky-a-kotouce': [('stojany-na-cinky', _STOJAN)],
    'kettlebelly': [('stojany-na-cinky', _STOJAN)],
    'sportovni-vesty': [('reflexni-vesty', _REFLEX)],
    'bezecke-vesty-a-batohy': [('reflexni-vesty', _REFLEX)],
    'nakrcniky-a-satky': [('kukly', _KUKLA)],
    'lyzarske-cepice-a-nakrcniky': [('kukly', _KUKLA)],
    'merino-doplnky': [('kukly', _KUKLA)],
    'termopradlo': [('kukly', _KUKLA)],
    'chranice-a-helmy': [('chranice-pater', _PATER)],
    'snowboardove-chranice': [('chranice-pater', _PATER)],
    'cyklo-chranice': [('chranice-pater', _PATER)],
    'lyzarske-doplnky': [('chranice-pater', _PATER)],
    'doplnky-k-obuvi': [('impregnace', _IMPREG)],
    'outdoor-doplnky': [('impregnace', _IMPREG)],
    'kempingove-doplnky': [('impregnace', _IMPREG)],
}.items():
    REFINE.setdefault(_parent, [])[0:0] = _rules
# ---- 16. 11. 2026 November wave 3: own loop again ----
_KSILT = r'^(?!.*(kulich|celenk|zimni cepic|beanie|stojan|drzak|swim|plavec|koupac)).*(ksilt|snapback|baseball ?cap|trucker|dad ?hat|(^|\W)(\w+ )?cap(\W|$)|(^|\W)(9fifty|9forty|59fifty|39thirty))'
_SOUPR = r'^(?!.*(lyzar|termo|plavk|pyzam|spodn|nepromok|do deste|rybar|cyklo|dres|brankar|kimon|neopren|kridl|postroj|comfort light|chranic|track ?suit (trouser|pant|bottom|jacket|top))).*(teplakov\w* soupr|soupr\w* teplak|track ?suit|jogging ?suit|(teplakov|sportovn|bavlnen)\w* (komplet|set)(\W|$))'
_SOUPR_ANY = _SOUPR[:-1] + r'|(^|\W)souprav[ay]?(\W|$))'
_CROP = r'^(?!.*(legin|legging|kalhot|kratas|short|sukn)).*((^|\W)crop(ped)?(\W|$)|crop.?top)'
_LEDV = r'ledvin|waist ?bag|belt ?bag|hip ?(bag|pack)|bum ?bag|fanny'
_TERMOHRN = r'^(?!.*(vicko|nahradn|cistic)).*(termohrn|termo ?hrn|thermo ?mug|travel ?mug|(^|\W)tumbler|termo\w* (na kav|hrnek|pohar)|(hrnek|pohar)\w* (termo|thermo|s dvojit))'
_SAMONAF = r'samonafuk|self.?inflat'
_MATRAC = r'^(?!.*(chranic|pump|lepen|opravn|zaplat|samonafuk|self.?inflat|karimat)).*(nafukovac\w* (matrac|lehat|lehatk|postel|kreslo|sedack)|matrac\w* (nafuk|do vody|k vode|plazov)|(^|\W)air ?bed|velurov\w* matrac|lehatk\w* (do|na) vod|plazov\w* matrac|(^|\W)matrace(\W|$))'
_TEJP = r'^(?!.*etape).*(kinesio|kinezio|kineziolog|tejp|(^|\W)(sport|athletic|kinesiology|k)[ -]?tape(\W|$)|leukotape)'
_PEROV = r'^(?!.*(vest|kalhot|spacak|bot[ay]|rukavic|cepic|ponoz)).*(perov\w* (bund|kabat|parka|mikin)|(^|\W)perovk|(^|\W)down (jacket|hoody|hoodie|parka|coat)|(bund|kabat)\w* (s )?(perov|perim|z peri))'
_SOFTKAL = r'softshell\w* (kalhot|nohavic|pants)|kalhot\w* (z )?softshell'
_NOTEBOOK = r'notebook|laptop|macbook'
_JEDNOD = r'^(?!.*(divc|detsk|chlapec|pansk|junior|kids|girl|boy|panove|zebrovan)).*(jednodiln|one.?piece|(^|\W)swimsuit|celoplav|plavky celo)'
_DVOUD = r'^(?!.*(divc|detsk|chlapec|pansk|junior|kids|girl|boy)).*(dvoudiln|bikin|tankin|two.?piece|(^|\W)(plavk\w* )?(horni|spodni) dil|plavkov\w* (podprsenk|kalhotk))'
_TURF = r'^(?!.*(kratas|short|shrt|tric|tee|dres|ponoz|chranic|mikin|kalhot|bund)).*(^|\W)(turf\w*|tf|tt)(\W|$)'
_STEPPER = r'stepper|(^|\W)stepr'
_KOMPRES = r'^(?!.*((^|\W)(ruc|paz|arm)\w*(\W|$)|kryo|reboot|pneumat)).*(kompresn\w* (ponoz|podkol|navlek|stulp|lytk|nadkol)|compression (sock|sleeve|calf)|(ponoz|podkolen|navlek)\w* kompres)'
_ARGININ = r'^(?!.*(pre.?workout|predtrenink|(^|\W)pump)).*(arginin|citrulin|citrullin|(^|\W)aakg(\W|$))'
_DRZMOB = r'(drzak|uchyt|pouzdr|obal|brasn|kryt)\w* (na |pro )?(mobil|telefon|smartphone|iphone)|(phone|mobile|smartphone) ?(mount|holder|case|bag)|quad ?lock|sp ?connect|(^|\W)fidlock vacuum'
_PIKNIK = r'piknik|picnic'
_ZIDLE = r'^(?!.*(stul|stol(ek|ky|y)?(\W|$)|table)).*(zidl|kresl|stolick|sedatk|sedak|chair|stool|lehatk|lehatk)'
_STUL = r'(^|\W)(stul|stol|stolek|stolky|stoly|table)(\W|$)'
_KEMPNAB = r'kempingov|campingov|camping|skladac|turistick|outdoorov'
_BALDESKA = r'balancn\w* desk|balance ?board|wobble ?board|(^|\W)(rola ?bola|rolla ?bolla)|indo ?board|surf ?trainer|(^|\W)rocker ?board'
_MMA = r'(^|\W)(mma|ufc|grappling)(\W|$)'
for _parent, _rules in {
    'cepice-a-celenky': [('ksiltovky', _KSILT)],
    'teplaky': [('teplakove-soupravy', _SOUPR_ANY)],
    'mikiny': [('teplakove-soupravy', _SOUPR)],
    'soupravy': [('teplakove-soupravy', _SOUPR_ANY)],
    'tilka': [('crop-topy', _CROP)],
    'sportovni-tricka': [('crop-topy', _CROP)],
    'tasky-pres-rameno': [('ledvinky', _LEDV)],
    'sportovni-tasky': [('ledvinky', _LEDV)],
    'skolni-batohy': [('ledvinky', _LEDV)],
    'vareni-v-prirode': [('termohrnky', _TERMOHRN)],
    'kempingove-nadobi': [('termohrnky', _TERMOHRN)],
    'lahve-a-termosky': [('termohrnky', _TERMOHRN)],
    'outdoor-doplnky': [('termohrnky', _TERMOHRN), ('piknikove-deky', _PIKNIK)],
    'karimatky-a-matrace': [('samonafukovaci-karimatky', _SAMONAF), ('nafukovaci-matrace', _MATRAC)],
    'nafukovaci-hracky': [('samonafukovaci-karimatky', _SAMONAF), ('nafukovaci-matrace', _MATRAC)],
    'plavecke-pomucky': [('nafukovaci-matrace', _MATRAC)],
    'bandaze-a-ortezy': [('kompresni-ponozky', _KOMPRES), ('tejpy', _TEJP)],
    'prvni-pomoc': [('tejpy', _TEJP)],
    'zimni-bundy': [('perove-bundy', _PEROV)],
    'sportovni-bundy-jaro-podzim': [('perove-bundy', _PEROV)],
    'sportovni-bundy': [('perove-bundy', _PEROV)],
    'outdoorove-kalhoty': [('softshellove-kalhoty', _SOFTKAL)],
    'sportovni-kalhoty': [('softshellove-kalhoty', _SOFTKAL)],
    'mestske-batohy': [('batohy-na-notebook', _NOTEBOOK)],
    'batohy': [('batohy-na-notebook', _NOTEBOOK)],
    'plavky': [('jednodilne-plavky', _JEDNOD), ('dvoudilne-plavky', _DVOUD)],
    'damske-plavky': [('jednodilne-plavky', _JEDNOD), ('dvoudilne-plavky', _DVOUD)],
    'kopacky': [('turfy', _TURF)],
    'kardio-trenazery': [('steppery', _STEPPER)],
    'sportovni-ponozky': [('kompresni-ponozky', _KOMPRES)],
    'merino-ponozky': [('kompresni-ponozky', _KOMPRES)],
    'aminokyseliny-bcaa': [('arginin-a-citrulin', _ARGININ)],
    'ostatni-doplnky-stravy': [('arginin-a-citrulin', _ARGININ)],
    'sportovni-vyziva': [('arginin-a-citrulin', _ARGININ)],
    'cyklo-lahve-a-drzaky': [('drzaky-na-mobil-na-kolo', _DRZMOB)],
    'cyklo-riditka': [('drzaky-na-mobil-na-kolo', _DRZMOB)],
    'cyklo-tasky-a-nosice': [('drzaky-na-mobil-na-kolo', _DRZMOB)],
    'cyklo-prislusenstvi': [('drzaky-na-mobil-na-kolo', _DRZMOB)],
    'kempingove-doplnky': [('piknikove-deky', _PIKNIK), ('kempingove-zidle', rf'^(?=.*({_KEMPNAB})).*' + _ZIDLE[_ZIDLE.index('(zidl'):]),
                           ('kempingove-stoly', rf'^(?=.*({_KEMPNAB})).*{_STUL}')],
    'kempingovy-nabytek': [('kempingove-stoly', _STUL), ('kempingove-zidle', _ZIDLE)],
    'balancni-pomucky': [('balancni-desky', _BALDESKA)],
    'fitness-pomucky': [('balancni-desky', _BALDESKA)],
    'boxerske-rukavice': [('mma-rukavice', _MMA)],
    'sportovni-rukavice': [('mma-rukavice', rf'^(?=.*(rukav|glove)).*{_MMA}')],
    'obleceni-bojove-sporty': [('mma-rukavice', rf'^(?=.*(rukav|glove)).*{_MMA}')],
}.items():
    REFINE.setdefault(_parent, [])[0:0] = _rules
# ---- 16. 11. 2026 November wave 4: own loop again ----
_NOTSHOE = r'^(?!.*(bot[ay]?(\W|$)|tenisk|obuv|brusl|cepic|kulich|pantof|skechers|bbk|sneaker|ponoz|rukavic|mikin|bund|kalhot|trick)).*'
_BOBY = r'^(?!.*(marley|edamame|soj|s okraji|fazol|flexfit|klobouk|bucket|dres|kakao|(^|\W)polo(\W|$)))' + _NOTSHOE + r'((^|\W)(bob|boby|bobik|bobek)(\W|$)|snow ?bob|s volantem|ridit\w* (bob|sane)|kluzak s volant)'
_SANKY = _NOTSHOE + r'(sank[ya]?(\W|$)|sanek|(^|\W)sane(\W|$)|saních|sanich|rohat\w* sane|drevene sane|skladac\w* sane|sled(ge)?(\W|$))'
_WHEY = r'^(?!.*(tyc|bar(\W|$)|susenk|cookie|wafl|pudink|kase|palacink|sejkr|shaker|clear whey hydrate)).*(whey|syrovatk)'
_VEGAN = r'^(?!.*(tyc|bar(\W|$)|susenk|cookie|wafl)).*(vegan\w* protein|protein\w* vegan|rostlinn\w* protein|plant ?(based )?protein|hrachov\w* protein|(sojov|ryzov|konopn|dyn)\w* protein|vegan (blend|protein))'
_ZIP = r'^(?!.*(vest|bund|kalhot|teplak|souprav)).*(na zip|full.?zip|(^|\W)fz(\W|$)|zip hood|zip(ova|ove|ovou)? mikin|mikin\w* (s )?zip)'
_KAPUCE = r'^(?!.*(vest|bund|kalhot|teplak|souprav|bez kapuc)).*(s kapuc|kapuci|hood(ie|y)?(\W|$)|hooded|(^|\W)hd(\W|$))'
_JEDNORUC = r'^(?!.*(stojan|drzak|regal|osa|osy|kotouc|zavazi|kettlebel)).*(jednoruc|dumbbell|(hexagon|neopren|vinyl|chrom|gumov|nakladac|stavitel)\w* cink|cink\w* (hexagon|neopren|vinyl|nakladac|stavitel)|(^|\W)par cinek|(^|\W)\d+ ?x ?\d+ ?kg cink)'
_KOLENO = r'^(?!.*(kotnik|zapest|loket|ramen|kycl|bederni|zad)).*((ortez|bandaz|navlek|chranic|stabilizator|nakolenik)\w* (na |pro )?(kolen|kolen[ou]|koleno)|kolenn\w* (ortez|bandaz|chranic|navlek)|nakolenik|knee (brace|sleeve|support|pad|guard))'
_KOTNIK = r'^(?!.*(kolen|zapest|loket)).*((ortez|bandaz|stabilizator|navlek|chranic)\w* (na |pro )?(kotnik|hlezn)|kotnikov\w* (ortez|bandaz)|ankle (brace|support|sleeve))'
_CESTOVNI = r'^(?!.*(ledvin|pres rameno|crossbody|kosmetick|toaletn|organizer)).*(cestovn\w* (tas|vak|batoh)|duffel|duffle|weekender|travel ?bag|(^|\W)base camp duffel|kufr|na kolecka|trolley)'
_FOTBDRES = r'^(?!.*(cykl|iihf|nhl|nba|nfl|mlb|hokej|basket|(^|\W)tas|(^|\W)vak|batoh|mic|ball|ponoz|stulp|chranic|kratas|short|bund|mikin|teplak|kalhot|cepic|saly|brankar)).*(fotbal\w* dres|dres\w* fotbal|football (jersey|shirt)|(home|away|third) (jersey|shirt|kit|dres)|(domaci|venkovni|hostujic)\w* dres|replica|(^|\W)(ac milan|ac sparta|sk slavia|real madrid|barcelona|manchester|liverpool|arsenal|chelsea|juventus|bayern|psg|inter) )'
_BOXERKY = r'^(?!.*(kalhotk|plavk|plavec|aquashort|swim|plavani|tanga|sport bra|podprsenk)).*(boxerk|boxer(s|ky)?(\W|$)|trenk|(^|\W)trunks?(\W|$)|boxer brief|briefs?(\W|$)|slip(y)? pansk|pansk\w* slip)'
_KALHOTKY = r'^(?!.*(plavk|swim|boxer|trenk|pansk)).*(kalhotk|tanga|(^|\W)string(\W|$)|brazilk|hipster|(^|\W)bikini brief|damsk\w* slip|slip(y)? damsk)'
_PENNY = r'penny ?board|pennyboard|(^|\W)penny(\W|$)|plastov\w* (skate|board)|mini ?cruiser|fish ?board|(^|\W)(22|27)("| ?palc)'
_KOS = r'^(?!.*(mic(\W|$)|ball(\W|$)|dres|bot[ay]|tric|sit na mic)).*(basketbal\w* kos(e|u|i|em|ich)?(\W|$)|kos (na )?basket|(^|\W)kos s desk|basketbal\w* (desk|konstrukc|stojan|sit(\W|$)|obruc)|basketball (hoop|system|board|stand|ring|net)|streetbal\w* kos|(^|\W)obruc (na )?basket)'
for _parent, _rules in {
    'sane-a-boby': [('boby', _BOBY), ('sanky', _SANKY)],
    'zimni-sporty': [('boby', _BOBY)],
    'proteiny': [('veganske-proteiny', _VEGAN), ('whey-proteiny', _WHEY)],
    'sportovni-vyziva': [('veganske-proteiny', _VEGAN)],
    'mikiny': [('mikiny-na-zip', _ZIP), ('mikiny-s-kapuci', _KAPUCE)],
    'cinky-a-kotouce': [('jednorucni-cinky', _JEDNORUC)],
    'bandaze-a-ortezy': [('ortezy-na-kotnik', _KOTNIK), ('ortezy-na-koleno', _KOLENO)],
    'chranice-a-helmy': [('ortezy-na-koleno', r'^(?=.*(kolen|knee)).*(chranic|nakolenik|pad|guard)')],
    'volejbal': [('ortezy-na-koleno', r'^(?=.*(kolen|knee)).*(chranic|nakolenik|pad|guard)')],
    'sportovni-tasky': [('cestovni-tasky', _CESTOVNI)],
    'dresy': [('fotbalove-dresy', _FOTBDRES)],
    'sportovni-spodni-pradlo': [('boxerky', _BOXERKY), ('kalhotky', _KALHOTKY)],
    'merino-pradlo': [('boxerky', _BOXERKY), ('kalhotky', _KALHOTKY)],
    'skateboardy': [('pennyboardy', _PENNY)],
    'basketbalove-mice': [('basketbalove-kose', _KOS)],
    'basketbal': [('basketbalove-kose', _KOS)],
}.items():
    REFINE.setdefault(_parent, [])[0:0] = _rules
# ---- 17. 11. 2026 November wave 5: own loop ----
_SNEHULE = r'^(?!.*(ponoz|navlek|vlozk|impregn|tkanick|kalhot|bund|rukavic|cepic|kombinez)).*(snehul|snow ?boots?(\W|$)|(^|\W)apres|moon ?boot)'
_CARGO = r'^(?!.*(kratk\w* kalhot|kratas|short|bermud|3/4|sukn|bund|mikin|bike|nakladn|kolo(\W|$))).*(cargo|kapsac)'
_ZATEPL = r'^(?!.*(ponoz|merino)).*((zateplen|termo|thermo|fleece|flis|zimn|warm|hrejiv)\w* legin|legin\w* (zateplen|termo|thermo|fleece|s flisem|zimn)|(thermal|winter|warm|fleece) (tights?|leggings?))'
_VLOZKY = r'^(?!.*(spacak|helm|prilb|kalhot|bund|rukavic|batoh|bryl)).*(vlozk\w* do (bot|obuv)|(^|\W)vlozky(\W|$)|stelk|insoles?(\W|$)|(^|\W)footbed)'
_RUCNIK = r'^(?!.*(vesak|drzak|hacek|(^|\W)tas|task|dek[ay]|stan(\W|$)|lehatk|zidl|kresl|ponc)).*(rucnik|osusk|towel)'
_PAPUCE = r'^(?!.*(plaz|bazen|do vody|sprch|crocs|zabk|sandal|(^|\W)slides?(\W|$))).*(papuc|domac\w* (obuv|pantof|bot)|backor|bacor|slippers?(\W|$)|na doma)'
_PINGSTUL = r'^(?!.*((^|\W)sit(\W|$)|sitk|obal|potah|kryci|plachta|kryt|palk|mick|robot|sada)).*((pingpong|ping pong|ping-pong)\w* stul|stoln\w* tenis\w* stul|stul\w* (na |pro )?(ping|stoln\w* tenis)|table tennis table)'
_VALEC = r'^(?!.*(inline|brusl|kolecka|kolo(\W|$)|skate|kolobez|lozisk|ab roller|ab wheel|posilovac\w* kol)).*(masazn\w* (valec|valce|valecek|roller|tyc)|foam ?roll|(^|\W)roller(\W|$)|valec na (masaz|cviceni)|fasci\w* (valec|roller)|blackroll)'
_BUZOLA = r'^(?!.*(pouzdr|podper|kresadl|klip|hodink|watch|cyklopocit|dalekohled)).*(buzol|(^|\W)kompas)'
_NEOPREN = r'^(?!.*(rukavic|kukl|oblek|vest|tricko|kratas|kalhot|bund)).*(neopren\w* (ponoz|bot|obuv|botick|capack|navlek|sock|boot)|(ponoz|bot|botick|sock|boot)\w* .*neopren|(^|\W)neo(prene)? (socks?|boots?)(\W|$))'
_ESUS = r'(^|\W)esus|mess ?tins?(\W|$)|(^|\W)kotlik'
for _parent, _rules in {
    'zimni-obuv': [('snehule', _SNEHULE)],
    'barefoot-obuv': [('snehule', _SNEHULE), ('domaci-pantofle', r'papuc|na doma|domac\w* (obuv|pantof|bot)')],
    'sportovni-kalhoty': [('cargo-kalhoty', _CARGO)],
    'outdoorove-kalhoty': [('cargo-kalhoty', _CARGO)],
    'teplaky': [('cargo-kalhoty', _CARGO)],
    'leginy': [('zateplene-leginy', _ZATEPL)],
    'doplnky-k-obuvi': [('vlozky-do-bot', _VLOZKY)],
    'plazove-doplnky': [('rucniky', _RUCNIK)],
    'hygiena-a-repelenty': [('rucniky', _RUCNIK)],
    'outdoor-doplnky': [('rucniky', _RUCNIK), ('buzoly-a-kompasy', _BUZOLA)],
    'pantofle-a-zabky': [('domaci-pantofle', _PAPUCE)],
    'stolni-tenis': [('pingpongove-stoly', _PINGSTUL)],
    'masazni-pomucky': [('masazni-valce', _VALEC)],
    'fitness-pomucky': [('masazni-valce', _VALEC)],
    'joga-a-podlozky': [('masazni-valce', _VALEC)],
    'pilates-pomucky': [('masazni-valce', _VALEC)],
    'dalekohledy-a-kompasy': [('buzoly-a-kompasy', _BUZOLA)],
    'obuv-do-vody': [('neoprenove-boty-a-ponozky', _NEOPREN)],
    'sportovni-ponozky': [('neoprenove-boty-a-ponozky', _NEOPREN)],
    'neopreny': [('neoprenove-boty-a-ponozky', _NEOPREN)],
    'kempingove-nadobi': [('esusy', _ESUS)],
    'vareni-v-prirode': [('esusy', _ESUS)],
    'lovecke-vybaveni': [('esusy', _ESUS)],
    'lovecke-obleceni': [('esusy', _ESUS)],
}.items():
    REFINE.setdefault(_parent, [])[0:0] = _rules
# ---- 17. 11. 2026 November wave 6: own loop (first = prepended before the older rules of the parent, last = appended after them) ----
_AKUPRES = r'^(?!.*(sprej|cistic|vlozk|stelk|do bot|(^|\W)mic(ek|ky)?(\W|$)|valec|naramk|ponoz)).*(akupres|akupunkt\w* (podlozk|sad|polstar)|fakirsk\w* (podlozk|lozk)|shakti|spike ?mat)'
_CHODPAS = r'^(?!.*(podlozk\w* pod|olej|maziv|silikon|kryt|dalkov\w* ovlad)).*(walking ?pad|chodic\w* pas|chodic\w* a bezeck\w* pas|bezeck\w* a chodic\w* pas|pas pod stul|under ?desk)'
_AIRTRACK = r'^(?!.*((^|\W)(pumpa|kompresor|lepidlo|zaplat)\w* (na|pro|k)\W)).*(air ?track|air ?floor|air ?spot|zinenk)'
_PROSIV = r'^(?!.*((^|\W)vest[ay]?(\W|$)|gilet|kalhot|rukavic|cepic|sukn|kombinez|spacak|dek[ay]|(^|\W)bot[ya]?(\W|$))).*(prosivan|quilted|(^|\W)puffer|(^|\W)quilt\w* (jacket|bund))'
_NEPRKAL = (r'^(?!.*(kratas|short|bund|jacket|rukavic|ponoz|navlek|sukn|kombinez|lyzar|(^|\W)ski(\W|$)|snowboard|softshell)).*('
            r'(nepromokav\w*|do deste|(^|\W)rain(\W|$)|waterproof|gore.?tex|(^|\W)gtx(\W|$)|h2no|dryvent|precip)\W.{0,30}(kalhot|pants|trousers)'
            r'|(kalhot|pants|trousers)\w*\W.{0,40}(nepromokav|do deste|(^|\W)rain(\W|$)|waterproof|gore.?tex|(^|\W)gtx(\W|$))|prekalhot|overpants)')
_SNBBUNDA = r'^(?!.*(kalhot|pants|rukavic|cepic|kukl|batoh|helm|bryl)).*(snowboard\w* (bund|jacket|anorak)|(bund|jacket|anorak)\w*\W.{0,30}snowboard)'
_SNBKAL = r'^(?!.*(bund|jacket|rukavic|kratas|short)).*(snowboard\w* (kalhot|pants)|(kalhot|pants)\w*\W.{0,30}snowboard)'
_NAVLEKBOT = (r'^(?!.*(neck|nakrcn|(^|\W)krk|tube|rukav|rukou|nohavic|kolen|(leg|arm) ?warm|zapest|nesmek|spike)).*('
              r'(navlek|navleky)\w*\W(na |pres )?(bot|obuv|tretr)|(^|\W)gamas|(^|\W)kamas|(^|\W)gaiters?(\W|$)|shoe ?covers?|overshoes?|turistick\w* navlek)')
_FOTBRANKA = (r'^(?!.*(brankar|rukavic|dres|kalhot|mikin|tricko|chranic|hokej|florbal)).*((fotbal\w*|futsal\w*)\W.{0,20}bran(k|e|y)'
              r'|bran(k\w*|y) (na|pro) (fotbal|futsal|minifotbal)|football goal|(^|\W)bran(ka|ky|ek)(\W|$))')
_MOSKYT = r'^(?!.*(spacak|repelent|sprej|hamak|hammock)).*(moskyt|mosquito ?net|sit\w* proti (hmyz|komar))'
_CHLTASKA = (r'^(?!.*((^|\W)box(\W|$)|autochlad|kompresor|chladnic|vlozk|nahradn)).*(chladic\w* (task|batoh|vak)|termotask|termo task'
             r'|obedov\w* task|task\w* na (jidlo|obed|svacin)|lunch ?bag|cooler ?bag|soft ?cooler|chladic\w* batoh)')
_HOKRUK = r'^(?!.*(brankar|lapack|vyrazeck|blokar|(^|\W)potah)).*(rukavic|gloves?(\W|$))'
_ZUBY = r'^(?!.*(sprej|desinf|cistic|pouzdr|krabick|(^|\W)box na)).*(chranic\w* (na )?(zub|chrup)|mouth ?guard|gum ?shield|(^|\W)mouthpiece)'
_OTUZ = (r'^(?!.*(neopren|rukavic|ponoz|(^|\W)bot[ya]?(\W|$)|teplomer|(^|\W)kryt|(^|\W)vik(o)?(\W|$)|plachta|chladic\w* jednot|filtr|cerpadl|podlozk|naparov|ohrivac)).*('
         r'otuzov\w* (kad|vana|vanu|sud|bazen|nadob)|ice ?bath|ice ?tub|icetub|cold ?plunge|ledov\w* (lazen|kad|vana)|ochlazovac\w* (kad|kruh|vana))')
_JOGABLOK = r'^(?!.*((^|\W)sada|(^|\W)set(\W|$)|podlozk\w* (a|\+))).*((jog\w*|yog\w*|pilates\w*) (blok|kostk|cihl|block|brick)|(blok|kostk|cihl)\w* (na|pro) (jog|yog|pilat)|yoga ?blocks?|jogablok)'
_KOTOUC = (r'^(?!.*((^|\W)pil[ay](\W|$)|kotoucov\w* pil|brzd|rotor|cykl|disc ?brake|stojan|(^|\W)strom|(^|\W)drzak|jednoruc|kettlebel)).*(kotouc|bumper ?plates?|olympijsk\w* (talir|osa|tyc)'
           r'|talir\w* (na|zavazi)|zavazi\w* talir|(^|\W)osa (na cink|olymp|ez|rovna|k cink)|(^|\W)ez osa|vzperack\w* tyc|tyc na kotouc|olympic bar)')
_ZAVAZI = r'(zavazi|zatez\w*)\W(na\W)?(nohy|kotnik|zapest|ruce)|ankle ?weights?|wrist ?weights?|(^|\W)manzet\w* se zatez'
_FERRATA = r'^(?!.*((^|\W)(mtb|kolo|bike)(\W|$)|rock ?shox|(^|\W)fox(\W|$)|kosil)).*ferrat'
_FERRBOOT = r'^(?=.*ferrat)(?=.*((^|\W)(bot[ya]?|obuv)(\W|$)|hanwag))'   # Hanwag Ferrata II / Loap Ferrat are boots
_SHIN_BOJ = r'(chranic\w* holen|shin ?guard).*(venum|bushido|dbx|(^|\W)mma(\W|$)|muay|thai|kickbox|leone|rdx|outshock|fairtex|twins)|(venum|bushido|dbx|(^|\W)mma(\W|$)|muay|thai|kickbox|leone|rdx|outshock|fairtex|twins).*(chranic\w* holen|shin ?guard)'
_SHIN_SKATE = r'(chranic\w* holen|shin).*(triple eight|skate|whip|kolobez|brusl)|(triple eight|skate|kolobez|brusl).*(chranic\w* holen|shin)'
_SHIN = r'chranic\w* holen|shin ?guard|(^|\W)stulpn'
for _parent, _pre, _post in [
    ('masazni-pomucky', [('akupresurni-podlozky', _AKUPRES)], []),
    ('fitness-pomucky', [('akupresurni-podlozky', _AKUPRES), ('chodici-pasy', _CHODPAS), ('airtracky-a-zinenky', _AIRTRACK),
                         ('otuzovaci-kade', _OTUZ), ('joga-bloky', _JOGABLOK), ('zavazi-na-kotniky', _ZAVAZI)], []),
    ('joga-a-podlozky', [('akupresurni-podlozky', _AKUPRES), ('joga-bloky', _JOGABLOK)], []),
    ('behaci-pasy', [('chodici-pasy', _CHODPAS)], []),
    ('kardio-trenazery', [('chodici-pasy', _CHODPAS)], []),
    ('posilovaci-stroje', [('chodici-pasy', _CHODPAS)], []),
    ('funkcni-trenink', [('airtracky-a-zinenky', _AIRTRACK), ('zavazi-na-kotniky', _ZAVAZI)], []),
    ('pilates-pomucky', [('airtracky-a-zinenky', _AIRTRACK), ('joga-bloky', _JOGABLOK)], []),
    ('gymnasticke-pomucky', [('airtracky-a-zinenky', _AIRTRACK)], []),
    ('zimni-bundy', [], [('snowboardove-bundy', _SNBBUNDA), ('prosivane-bundy', _PROSIV)]),   # péřové first (older rule)
    ('sportovni-bundy-jaro-podzim', [('prosivane-bundy', _PROSIV)], []),
    ('outdoorove-kalhoty', [('nepromokave-kalhoty', _NEPRKAL)], []),
    ('sportovni-kalhoty', [('snowboardove-kalhoty', _SNBKAL), ('nepromokave-kalhoty', _NEPRKAL)], []),
    ('lyzarske-bundy', [], [('snowboardove-bundy', _SNBBUNDA)]),        # after the kesi / termoprádlo vetoes
    ('lyzarske-kalhoty', [], [('snowboardove-kalhoty', _SNBKAL)]),
    ('doplnky-k-obuvi', [('navleky-na-boty', _NAVLEKBOT)], []),
    ('outdoor-doplnky', [('navleky-na-boty', _NAVLEKBOT), ('otuzovaci-kade', _OTUZ)], []),
    ('trekova-obuv', [('navleky-na-boty', _NAVLEKBOT)], []),
    ('lyzarske-doplnky', [('navleky-na-boty', _NAVLEKBOT)], []),
    ('cyklisticke-navleky', [('navleky-na-boty', _NAVLEKBOT)], []),
    ('fotbal', [('chranice-bojove-sporty', _SHIN_BOJ), ('chranice-a-helmy', _SHIN_SKATE), ('fotbalove-chranice-a-stulpny', _SHIN),
                ('fotbalove-branky', _FOTBRANKA)], []),
    ('hygiena-a-repelenty', [('moskytiery', _MOSKYT)], []),
    ('chladici-boxy', [('chladici-tasky', _CHLTASKA)], []),
    ('lahve-a-termosky', [('chladici-tasky', _CHLTASKA)], []),
    ('tasky-pres-rameno', [('chladici-tasky', _CHLTASKA)], []),
    ('hokejove-chranice', [('hokejove-rukavice', _HOKRUK)], []),
    ('chranice-bojove-sporty', [('chranice-zubu', _ZUBY)], []),
    ('chranice-a-helmy', [('chranice-zubu', _ZUBY)], []),
    ('ragby-a-americky-fotbal', [('chranice-zubu', _ZUBY)], []),
    ('bazeny', [('otuzovaci-kade', _OTUZ)], []),
    ('jogove-pomucky', [('joga-bloky', _JOGABLOK)], []),
    ('boxovaci-pytle', [('joga-bloky', _JOGABLOK)], []),
    ('cinky-a-kotouce', [('zavazi-na-kotniky', _ZAVAZI)], [('kotouce-na-cinky', _KOTOUC)]),   # stojany / jednoruční first
    ('lezecka-lana-a-karabiny', [('zimni-obuv', r'(?=.*ferrat)(?=.*zimn\w* bot)'), ('trekova-obuv', _FERRBOOT), ('via-ferrata', _FERRATA)], []),
    ('horolezectvi', [('zimni-obuv', r'(?=.*ferrat)(?=.*zimn\w* bot)'), ('trekova-obuv', _FERRBOOT), ('via-ferrata', _FERRATA)], []),
    ('lezecke-sedaky-a-pomucky', [('zimni-obuv', r'(?=.*ferrat)(?=.*zimn\w* bot)'), ('trekova-obuv', _FERRBOOT), ('via-ferrata', _FERRATA)], []),
    ('cyklo-vidlice-a-tlumice', [('zimni-obuv', r'(?=.*ferrat)(?=.*zimn\w* bot)'), ('trekova-obuv', _FERRBOOT), ('via-ferrata', _FERRATA)], []),
    ('cyklo-brzdy', [('zimni-obuv', r'(?=.*ferrat)(?=.*zimn\w* bot)'), ('trekova-obuv', _FERRBOOT), ('via-ferrata', _FERRATA)], []),
]:
    REFINE.setdefault(_parent, [])[0:0] = _pre
    REFINE[_parent].extend(_post)
# ---- 18. 11. 2026 November wave 7: own loop (pre = before the older rules of the parent, post = after them) ----
_LANO = r'^(?!.*(svihad|tazn|odtah|vlek\w*|na pradlo|skakac|batt?le ?rope|posilov|(^|\W)smyck|ferrat|lonz|splhac|trenink\w* lan|triceps|bushido|(^|\W)dbx(\W|$)|kladk|(^|\W)jut)).*((^|\W)lan[oa](\W|$)|(^|\W)ropes?(\W|$)|repsnur)'
_KARABINA = r'^(?!.*(hrnek|hrnk|(^|\W)set(\W|$)|ferrat|lonz|obratlik|swivel|eggsnap|privesek|klicenk|(^|\W)task|tastick|kolecka|reflexn)).*(karabin|carabiner)'
_CEPIN = r'^(?!.*(pouzdr|chranic\w* (hrot|spic)|(^|\W)obal|nesmek)).*(cepin|ice ?axe|(^|\W)macky(\W|$)|stoupac\w* zelez|crampons?(\W|$))'
_TARP = r'^(?!.*((^|\W)stan(\W|$)|kolik|(^|\W)napinak|kolobez|motork|(^|\W)auto(\W|$)|kol[ao](\W|$))).*((^|\W)tarp|(^|\W)celta|placht\w* (na|pro|nad) (kemp|stan|hamak)|hamak\w* placht|rain ?fly)'
_KOSMET = r'^(?!.*(batoh|krem|sampon|(^|\W)gel(\W|$)|mydl)).*(toaletn\w* (task|pouzdr|tastick)|kosmetick\w* (task|pouzdr|tastick|kufrik)|neceser|wash ?bag|toiletry)'
_DRYVAK = r'^(?!.*(spacak|(^|\W)stan(\W|$)|mobil|telefon|smartphone|phone)).*(dry ?bag|drybag|dry ?sack|vodotesn\w* (vak|pytel|batoh)|nepromokav\w* (vak|pytel)|lodni vak|vodack\w* (vak|batoh|barel|sud)|roll ?top (vak|bag))'
_KLADKA = r'^(?!.*(cyklo|(^|\W)kol[ao](\W|$)|bike|retez|lanovk|horolez|lezec|zachran|kladkostroj|kladk\w* (na|pro) (lan|kladkostr))).*(kladk|lat ?pull|kabelov\w* (stroj|crossover)|cable ?crossover)'
_FILTR = r'^(?!.*(kavov|(^|\W)kav[ay](\W|$)|bazen|akvari|prach|vzduch|uv filtr|objektiv|cerpadl)).*(filtr\w* (na|pro) vod|vodni filtr|lifestraw|sawyer|katadyn|filtracn\w* (lahev|lahv|brck|slamk)|tablet\w* (na|pro) (cisteni|dezinfekci|upravu) vod|grayl|befree)'
_HYDROVAK = r'^(?!.*(batoh|(^|\W)vest[ay]?(\W|$)|ledvin)).*(hydrovak|hydratacn\w* vak|hydrapak|widepac|rezervoar|vak\w* na vodu|(^|\W)bladder|water ?reservoir|soft ?flask)'
_TERMOJIDLO = r'^(?!.*(hrnek|hrnk|lahev|lahv|na piti|kava|uzaver|(^|\W)vick|pouzdr|nahradn|tesneni)).*(termosk\w* na (jidlo|polevk|obed)|jidelni termosk|food ?jar|food ?container|food ?flask|termo\w* (box|nadob|obedar|jidlonosic)\w* na jidlo|termoobedar|jidlonosic)'
_HRUDNI = r'^(?!.*podprsenk).*(hrudni pas|snimac\w* (tepu|srdecn)|pulsmetr|heart ?rate (monitor|sensor|strap)|(^|\W)hrm[ -]?(pro|dual|run|fit)|polar h(9|10)(\W|$))'
_NEPRPONOZ = r'((nepromokav|vodeodoln|waterproof)\w*\W.{0,25}(ponoz|socks?(\W|$))|(ponoz|socks?(\W|$))\w*\W?.{0,25}(nepromokav|vodeodoln|waterproof)|(dexshell|sealskinz).*(sock|ponoz))'
_BRASNA = r'^(?!.*(batoh|kosik|stojan|kolobez|chladic|(^|\W)lahv|drzak (na )?(mobil|telefon))).*(brasn|podsedlov|(task|vak|bag)\w* (na ram|pod sedlo|na riditk|na nosic|na predstavec)|frame ?bag|saddle ?bag|handlebar ?bag|top ?tube|bikepacking|pannier|seat ?pack|cyklistick\w* task|(^|\W)zadni task|task\w* na kolo)'
_KOSIK = r'^(?!.*(lahv|lahev|bidon|(^|\W)drzak (na )?lahv|sroub|uchyt)).*(kosik|basket)'
_CYKLOBATOH = r'^(?!.*(ledvin|(^|\W)vak na vodu)).*((cyklo|cyklistick|bike|mtb|enduro)\w*\W.{0,15}(batoh|backpack)|(batoh|backpack)\w*\W.{0,20}(na kolo|cyklo|cyklisti|(^|\W)bike|mtb|enduro)|(^|\W)evoc|deuter (trans alpine|bike|race|attack))'
_REFORMER = r'reformer'
_SUSPENZOR = r'suspenzor|(^|\W)jock ?straps?(\W|$)|chranic\w* (rozkrok|genital|slabin)|groin ?(guard|protector)'
_NORDIC = r'nordic ?walk|(^|\W)nw (hul|hol)'
_SOLAR = r'solarn|solar ?(panel|charger|power)'
_VIBRA = r'vibracn\w* (plosin|desk|stroj|trenaz)|vibration ?plate|vibro ?plosin|power ?plate'
_TRX = r'^(?!.*(task|bund|park[ay]?(\W|$)|kalhot|(^|\W)bot[ya]?(\W|$)|seno|adidas|kopack|(^|\W)tf(\W|$)|vintage)).*(zavesn\w* (posilov\w* )?(system|trenaz|popruh|pas)|(^|\W)trx(\W|$)|suspension ?train|sling ?train)'
_POTITKO = r'potitk|potni pask|sweat ?bands?(\W|$)|wrist ?bands?(\W|$)'
_PETANQ = r'p[e]tanq|petank|petang|boccia|(^|\W)boules?(\W|$)|(^|\W)bocce'
_VYHRIV = r'vyhrivan|heated (gloves?|socks?|vest|jacket)'
_PREDSTAN = r'predstan|stan (k|ke|za|na) aut|autostan|markyz|zadni stan|(^|\W)awning'
for _parent, _pre, _post in [
    ('lezecka-lana-a-karabiny', [], [('horolezecka-lana', _LANO), ('karabiny', _KARABINA)]),   # after the ferrata rules
    ('horolezectvi', [('cepiny-a-macky', _CEPIN)], [('horolezecka-lana', _LANO), ('karabiny', _KARABINA)]),
    ('skialpinismus', [('cepiny-a-macky', _CEPIN)], []),
    ('kempingove-nadobi', [], [('karabiny', r'^(?!.*(hrnek|hrnk|esus|nadob|kotlik)).*karabin')]),
    ('stanove-doplnky', [('strechni-stany', _PREDSTAN), ('tarpy', _TARP)], []),
    ('outdoor-doplnky', [('tarpy', _TARP), ('kosmeticke-tasky', _KOSMET), ('nepromokave-vaky', _DRYVAK), ('filtry-na-vodu', _FILTR)], []),
    ('sportovni-tasky', [('kosmeticke-tasky', _KOSMET), ('nepromokave-vaky', _DRYVAK), ('hydrovaky', _HYDROVAK)], []),
    ('cestovni-tasky', [('kosmeticke-tasky', _KOSMET)], []),
    ('mestske-batohy', [('kosmeticke-tasky', _KOSMET), ('cyklisticke-batohy', _CYKLOBATOH)], []),
    ('hygiena-a-repelenty', [('kosmeticke-tasky', _KOSMET), ('filtry-na-vodu', _FILTR)], []),
    ('kempingove-doplnky', [('nepromokave-vaky', _DRYVAK)], []),
    ('paddleboardy', [('nepromokave-vaky', _DRYVAK)], []),
    ('posilovaci-stroje', [('posilovaci-kladky', _KLADKA)], []),
    ('fitness-pomucky', [('posilovaci-kladky', _KLADKA), ('vibracni-plosiny', _VIBRA), ('zavesne-systemy-trx', _TRX)], []),
    ('lahve-a-termosky', [('filtry-na-vodu', _FILTR), ('hydrovaky', _HYDROVAK), ('termosky-na-jidlo', _TERMOJIDLO)], []),
    ('vareni-v-prirode', [('filtry-na-vodu', _FILTR)], []),
    ('sportovni-hodinky', [('hrudni-pasy', _HRUDNI)], []),
    ('cyklo-prislusenstvi', [('hrudni-pasy', _HRUDNI)], []),
    ('sportovni-ponozky', [('vyhrivane-obleceni', _VYHRIV), ('nepromokave-ponozky', _NEPRPONOZ)], []),
    ('cyklo-tasky-a-nosice', [('cyklisticke-batohy', _CYKLOBATOH), ('kosiky-na-kolo', _KOSIK), ('brasny-na-kolo', _BRASNA)], []),
    ('cyklo-riditka', [('kosiky-na-kolo', _KOSIK)], []),
    ('pilates-pomucky', [('pilates-reformery', _REFORMER)], []),
    ('chranice-bojove-sporty', [('suspenzory', _SUSPENZOR)], []),
    ('hokejove-chranice', [('suspenzory', _SUSPENZOR)], []),
    ('trekove-hole', [('nordic-walking-hole', _NORDIC)], []),
    ('powerbanky-a-nabijeni', [('solarni-nabijecky', _SOLAR)], []),
    ('masazni-pomucky', [('vibracni-plosiny', _VIBRA)], []),
    ('posilovaci-gumy', [('vibracni-plosiny', _VIBRA), ('zavesne-systemy-trx', _TRX)], []),
    ('funkcni-trenink', [('zavesne-systemy-trx', _TRX)], []),
    ('cepice-a-celenky', [('vyhrivane-obleceni', _VYHRIV), ('potitka', _POTITKO)], []),
    ('hry-na-zahradu', [('petanque', _PETANQ)], []),
    ('sportovni-rukavice', [('vyhrivane-obleceni', _VYHRIV)], []),
    ('lyzarske-rukavice', [('vyhrivane-obleceni', _VYHRIV)], []),
    ('sportovni-vesty', [('vyhrivane-obleceni', _VYHRIV)], []),
    ('sportovni-bundy-jaro-podzim', [('vyhrivane-obleceni', _VYHRIV)], []),
    ('zimni-bundy', [('vyhrivane-obleceni', _VYHRIV)], []),
]:
    REFINE.setdefault(_parent, [])[0:0] = _pre
    REFINE[_parent].extend(_post)
# ---- 19. 11. 2026 November wave 8 ----
_VOLEJBOTY = (r'^(?!.*(ponoz|chranic|kolen|bandaz|rukav|mic|sit(\W|$)|dres|kratas|tricko|taska)).*(volejbal\w* (boty|obuv|tenisk)|(boty|obuv|tenisky)\w*\W.{0,25}volejbal'
              r'|metarise|hyperset|sky elite|beyond ff|netburner|wave momentum|wave lightning|wave dimension|wave luminous|upcourt|gel-rocket|gel rocket)')
_BOXBOTY = r'^(?!.*(rukavic|bandaz|helm|tricko|kratas|ponoz|taska)).*(boxersk\w* (boty|obuv)|zapasnick\w* (boty|obuv)|boxing shoes?|wrestling shoes?|hyperko|machomai|(^|\W)inflict|(^|\W)tawa(\W|$)|ringside.*(boty|shoe)|everlast elite)'
for _parent, _pre, _post in [
    ('volejbal', [('volejbalova-obuv', _VOLEJBOTY)], []),
    ('fitness-pomucky', [('posilovaci-kolecka', r'^(?!.*(kolobez|brusl|vozik|nahradn)).*(posilovac\w* kolec|kolecko na (cviceni|posilovani|bricho)|ab ?wheel|ab ?roller|bricni kolec)')], []),
    ('funkcni-trenink', [('posilovaci-kolecka', r'posilovac\w* kolec|ab ?wheel|ab ?roller|kolecko na (cviceni|bricho)')], []),
    ('salova-obuv', [('volejbalova-obuv', _VOLEJBOTY)], []),
    ('tenisky', [('volejbalova-obuv', _VOLEJBOTY), ('boxerske-boty', _BOXBOTY)], []),
    ('treninkova-obuv', [('boxerske-boty', _BOXBOTY)], []),
    ('obleceni-bojove-sporty', [('boxerske-boty', _BOXBOTY)], []),
    ('bojove-sporty', [('boxerske-boty', _BOXBOTY)], []),
]:
    REFINE.setdefault(_parent, [])[0:0] = _pre
    REFINE[_parent].extend(_post)
REFINE['cyklo-prislusenstvi'].append(('cyklo-stojany-a-drzaky', r'stojan|drzak\w* (na )?(kol|bicykl)|nastenn|zavesn\w* (na )?kol|zavesen\w* na kolo'))
REFINE = {k: [(c, re.compile(r)) for c, r in v] for k, v in REFINE.items()}


def refine(slug, title):
    """→ the specific sub-category of a cycling section for this title (folded or not), the section itself, or None when the product
    does not belong in the shop at all (a rule target of None). Two levels: a bike first lands in its type, the type may split further."""
    t = fold(title)
    for _ in range(3):
        nxt = slug
        for child, rx in REFINE.get(slug, ()):
            if rx.search(t):
                nxt = child
                break
        if nxt is None or nxt == slug:
            return nxt
        slug = nxt
    return slug


# A shop path that says footwear ("Dámské > Boty > Tenisky") keeps the item in footwear: a title word must not turn a shoe into a polo shirt
# ("Polo Ralph Lauren Sayer" → polokosile, 3 200 Spartoo rows). Only when the path alone also resolves to footwear.
FOOT_PATH = re.compile(r'(^|\W)(boty|obuv|tenisky|sandaly|pantofle|kopacky|sneakers|bota)(\W|$)')


def categorize(path, title, gpc=''):
    slug, fashion = _categorize(path, title, gpc)
    if slug and section(slug) == 'sportovni-obleceni' and FOOT_PATH.search(fold(path)):
        alt, alt_fashion = _categorize(path, '', gpc)
        if alt and section(alt) == 'sportovni-obuv':
            slug, fashion = alt, alt_fashion
    return (refine(slug, title) if slug else slug), fashion


def _categorize(path, title, gpc=''):
    """→ (slug, fashion_flag). fashion_flag = the item is a generic apparel type that needs a sport brand/sport word."""
    p, t, g = fold(path), fold(title), fold(gpc)
    p = re.sub(r'^home > (?=sporty > )', '', p)   # Exisport's tree root is "Home > Sporty"; EXCLUDE drops the word home (home decor)
    if EXCLUDE.search(p) or EXCLUDE.search(t):
        return None, False
    b = bike_rule(p, t)
    if b:
        return b, False
    if 'stan smith' in t:        # Adidas sneakers, not tents (they sat in /stany/ because of the word "stan")
        return 'tenisky', _fashion('tenisky', t, p)
    cand = _first(PASS_A, p, t, g)
    if cand is None:
        # a type noun at the head of the title ("Bunda Kilpi …", "Pánské tričko …") beats a shop path of another family ("Mikiny a bundy"),
        # but never a more specific path of the same family (a winter jacket stays a winter jacket)
        hm = HEAD_NOUN.search(t)
        pb = _first(PASS_B, p, t, g)
        if hm:
            hs = HEAD_SLUG[hm.group(1)]
            if pb is None or _family(pb) != _family(hs):
                cand = hs
    if cand is not None:
        if vetoed(cand, t):
            return None, False
        return cand, _fashion(cand, t, p)
    for slug, rp, rt, rg in ORDERED:
        if rp is not None and not rp.search(p):
            continue
        if rt is not None and not rt.search(t):
            continue
        if rg is not None and not rg.search(g):
            continue
        if rp is None and rt is None and rg is None:
            continue
        if vetoed(slug, t):
            return None, False
        return slug, _fashion(slug, t, p)
    return None, False


GENDER_RULES = [
    ('deti', R(r'(^|\W)(deti|detsk\w*|divc\w*|chlapec\w*|chlapeck\w*|junior\w*|kids?|boys?|girls?|kojenec\w*|youth|jr)(\W|$)')),
    ('zeny', R(r'(^|\W)(zeny|damsk\w*|women\w*|woman|wmns|female|lady|ladies)(\W|$)')),
    ('muzi', R(r'(^|\W)(muzi|pansk\w*|men|mens|male)(\W|$)')),
]
# Answear's whole path is "Ona" / "On" / "Dítě" ("On" is also a shoe brand, so only as the path's first segment)
PATH_GENDER = [('zeny', R(r'^ona(\W|$)')), ('muzi', R(r'^on(\W|$)')), ('deti', R(r'^dite(\W|$)'))]


def gender(path, title, sex=''):
    """muzi | zeny | deti | unisex | '' (unknown)."""
    t, p = fold(title), fold(path)
    for g, rx in GENDER_RULES:
        if rx.search(t):
            return g
    for g, rx in GENDER_RULES + PATH_GENDER:
        if rx.search(p):
            return g
    s = (sex or '').lower()
    return {'male': 'muzi', 'female': 'zeny', 'unisex': 'unisex', 'kids': 'deti'}.get(s, '')


# sport (Decathlon first_sport) → default category when nothing more specific matched; apparel words go to the clothing one
SPORT_DEFAULT = {
    'jezdectvi': ('jezdecke-doplnky', 'jezdecke-obleceni'), 'drezura': ('jezdecke-doplnky', 'jezdecke-obleceni'),
    'vsestranna jizda na koni': ('jezdecke-doplnky', 'jezdecke-obleceni'), 'vyjizdky na koni': ('jezdecke-doplnky', 'jezdecke-obleceni'),
    'parkurove skakani': ('jezdecke-doplnky', 'jezdecke-obleceni'), 'western': ('jezdecke-doplnky', 'jezdecke-obleceni'),
    'golf': ('golfove-doplnky', 'golfove-obleceni-a-obuv'),
    'lov drobne zvere': ('lovecke-vybaveni', 'lovecke-obleceni'), 'lov velke zvere': ('lovecke-vybaveni', 'lovecke-obleceni'),
    'lov': ('lovecke-vybaveni', 'lovecke-obleceni'), 'pozorovani prirody': ('dalekohledy-a-kompasy', 'lovecke-obleceni'),
    'lov na polozenou': ('rybarske-doplnky', 'rybarske-obleceni'), 'lov s nastrahou': ('rybarske-doplnky', 'rybarske-obleceni'),
    'kaprarina': ('rybarske-doplnky', 'rybarske-obleceni'), 'rybolov z lodi': ('rybarske-doplnky', 'rybarske-obleceni'),
    'rybolov': ('rybarske-doplnky', 'rybarske-obleceni'), 'prutovy rybolov': ('rybarske-doplnky', 'rybarske-obleceni'),
    'joga': ('jogove-pomucky', 'sportovni-kalhoty'), 'pilates': ('pilates-pomucky', 'sportovni-kalhoty'),
    'balet': ('baletni-obuv', 'tanecni-obleceni'), 'soudoby tanec': ('tanecni-obuv', 'tanecni-obleceni'), 'tanec': ('tanecni-obuv', 'tanecni-obleceni'),
    'team gym': ('gymnasticke-pomucky', 'tanecni-obleceni'), 'sportovni gymnastika': ('gymnasticke-pomucky', 'tanecni-obleceni'),
    'rytmicka gymnastika': ('gymnasticke-pomucky', 'tanecni-obleceni'), 'cviceni pro nejmensi': ('gymnasticke-pomucky', 'tanecni-obleceni'),
    'padel': ('padel', 'padel'), 'squash': ('squash', 'squash'),
    'triatlon': ('triatlon', 'triatlon'),
    'bodybuilding': ('ostatni-doplnky-stravy', None), 'kulturistika': ('ostatni-doplnky-stravy', None),
}
APPAREL_NATURE = re.compile(r'(^|\W)(polo|tricko|triko|mikin|bund|kalhot|rajtk|legin|ponozk|rukavic|vest|sukn|saty|kratas|kombinez|souprav|top(\W|$)|body|dres|cepic|svetr|kosil)')
# shoe nature words of a sport → the shoe category of that sport
SPORT_SHOE = {'padel': 'padel', 'tenis': 'tenisova-obuv', 'volejbal': 'salova-obuv', 'kruhovy trenink': 'treninkova-obuv',
              'kardio trenink': 'treninkova-obuv', 'telocvik': 'treninkova-obuv', 'bodybuilding': 'treninkova-obuv', 'fitness': 'treninkova-obuv',
              'soudoby tanec': 'tanecni-obuv', 'balet': 'baletni-obuv', 'sportovni chuze': 'tenisky', 'beh': 'silnicni-bezecke-boty',
              'silnicni beh': 'silnicni-bezecke-boty', 'trailovy beh': 'trailove-boty', 'florbal': 'salova-obuv', 'basketbal': 'basketbalova-obuv'}
SHOE_NATURE = re.compile(r'^(sportovni obuv|tenisky|obuv|boty)$')


def categorize_ctx(path, title, gpc='', sport='', nature='', own=True):
    """categorize() plus the sport / product nature of feeds that carry them (Decathlon): → (slug, fashion_flag)."""
    sp, na = fold(sport).strip(), fold(nature).strip()
    if not own:
        return categorize(path, title, gpc)       # marketplace sellers fill sport/nature at random (Skechers boots as "riding boots")
    if sp in SPORT_SHOE and SHOE_NATURE.match(na):
        return (None if vetoed(SPORT_SHOE[sp], fold(title)) else SPORT_SHOE[sp]), False
    r = categorize(path, title, gpc)
    if r[0] and sp in SPORT_DEFAULT and section(r[0]) == 'sportovni-obleceni' and SPORT_DEFAULT[sp][1] not in (None, 'sportovni-kalhoty'):
        return SPORT_DEFAULT[sp][1], False          # a riding polo / golf shirt belongs to the sport, not to the generic shirts
    if r[0] or not (sp or na):
        return r
    r = categorize(f'{sp} > {na}', f'{title} {nature}', gpc)
    if r[0]:
        return r
    if sp in SPORT_DEFAULT:
        gen, app = SPORT_DEFAULT[sp]
        if gen == 'ostatni-doplnky-stravy' and not re.search(r'doplnek|protein|syrovatk|izolat|kreatin|aminokys|vitamin|vyziv|tycink', na + ' ' + fold(title)):
            return None, False
        pick = app if app and APPAREL_NATURE.search(na) else gen
        return (None if vetoed(pick, fold(title) + ' ' + na) else pick), False
    return None, False
