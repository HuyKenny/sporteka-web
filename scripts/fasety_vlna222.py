"""sporteka.cz — facet landing wave 222 (22. 11. 2026): SERP tuning of the 22 shoe-model landings of wave 175a–d. The TOP 10 of every model
phrase is a listing (Top4running "… | 27 Produktů", Heureka "… od 2 699 Kč", Footshop "Sleva až 45 %") or a guide (best4run), so the title
keeps the model first, adds the live product count (%pocet%, filled at render time) and says it is a guide: "<model> – 73 produktů a průvodce
výběrem". Descriptions end with the same count. Nike Metcon gets the questions of its "People also ask"."""
import copy

import fasety_vlna175a as A
import fasety_vlna175b as B
import fasety_vlna175c as C
import fasety_vlna175d as D

NEW = {}
for _m in (A, B, C, D):
    for _slug, _e in _m.NEW.items():
        e = copy.deepcopy(_e)
        name = e['title'].split(':')[0].strip()
        e['title'] = f'{name} – %pocet% a průvodce výběrem'
        NEW[_slug] = e

NEW['nike-metcon']['faq'] = list(NEW['nike-metcon']['faq']) + [
    ('Co znamená Metcon?',
     'Název vychází ze zkratky metabolic conditioning, tedy intenzivního funkčního tréninku. Nike Metcon je řada tréninkových bot určených původně pro crossfit: stabilní podrážka pro zvedání a lehčí část pro skoky a lana.'),
    ('Jak poznat padělek bot Nike?',
     'Kupujte u ověřených obchodů, které uvádějí kód modelu, a porovnejte jej s kódem na štítku uvnitř boty. Podezřele nízká cena, nekvalitní šití a chybějící krabice nebo štítek jsou varovné signály. Neověřitelné inzeráty se vyhněte.'),
    ('Je Nike lepší než Adidas?',
     'Obecně neplatí. Značky mají odlišný střih a řady, záleží na sportu a tvaru chodidla. Pro zvedání a funkční trénink rozhoduje stabilní podrážka, přilnavost a sedí-li bota. Vždy porovnejte konkrétní modely a vyzkoušejte velikost.'),
]
