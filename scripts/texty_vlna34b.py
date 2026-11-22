"""sporteka.cz — wave 34b (22. 11. 2026): SERP tuning of the wave 33/34 categories after the Ahrefs TOP 10 of their head phrases
(reports/sporteka/gap/serp-2026-11-22.md). Titles lead with the phrase and end with %pocet% (the listing's product count, filled when the
page is rendered — Heureka and Top4running do the same), descriptions end with %od% (cheapest price, dropped when unknown), and the FAQ gets
the "People also ask" questions the TOP 10 shows. Everything else stays as written in the wave 33/34 files this patches.
General information only; medical wording stays hedged."""
import copy

import texty_vlna33a as A
import texty_vlna33b as B
import texty_vlna34a as C

NEW = {}


def _patch(src, slug, title, desc, faq=()):
    e = copy.deepcopy(src.NEW[slug])
    e['title'], e['desc'] = title, desc
    have = {q for q, _ in e['faq']}
    e['faq'] = list(e['faq']) + [(q, a) for q, a in faq if q not in have]
    NEW[slug] = e


_patch(C, 'ortezy-na-zapesti', 'Ortézy na zápěstí: bandáže, dlahy, gym | %pocet%',
       'Ortézy a bandáže na zápěstí: elastické, neoprenové i dlahové. Velikost, levá a pravá ruka, kdy k lékaři. Srovnání obchodů %od%', [
    ('Kdy mám nárok na ortézu od pojišťovny?',
     'Zdravotnické prostředky, které předepíše lékař, může částečně hradit zdravotní pojišťovna. Podmínky a výše úhrady závisí na typu pomůcky a pojišťovně, proto se zeptejte lékaře nebo ve výdejně. Sportovní bandáže z e-shopu se zpravidla nehradí.'),
    ('Čím zpevnit zápěstí?',
     'Při cvičení stačí elastická nebo neoprenová bandáž, při vzpírání tahové pásky. Po úrazu zápěstí zpevňuje ortéza s dlahou, tu ale volte po radě lékaře nebo fyzioterapeuta. Bandáž zápěstí zpevní, nenahradí vyšetření.'),
    ('Co dělat, když mě bolí zápěstí?',
     'Bolest po pádu, otok, necitlivost prstů nebo bolest, která budí v noci a nepolevuje, patří k lékaři. U bolesti po zátěži pomáhá odpočinek a omezení pohybu, který bolest spouští. Ortéza zápěstí podpoří, příčinu ale neřeší.'),
    ('Na co je dobrá ortéza na zápěstí?',
     'Zpevňuje a zahřívá zápěstí, omezuje krajní pohyby a při zátěži zlepšuje pocit stability. Používá se při cvičení s činkami, v raketových sportech, při lezení i po lékařem doporučené fixaci. Nelepí zlomeninu ani nevyléčí zranění.')])

_patch(C, 'ortezy-na-loket', 'Ortézy na loket a tenisový loket | %pocet%',
       'Ortézy na loket a tenisový loket: pásky, neopren a návleky. Jak vybrat velikost a kam pásek nasadit. Srovnání obchodů %od%', [
    ('Jak správně nasadit ortézu na loket?',
     'Návlek natáhněte na paži tak, aby střed ortézy seděl na loketním kloubu. Pásek na tenisový loket se nasazuje na předloktí těsně pod loket podle návodu výrobce. Nemá škrtit, prsty nesmí mravenčit ani bělat.'),
    ('Jak funguje ortéza na tenisový loket?',
     'Pásek rozloží tlak z úponu svalů na větší plochu předloktí a tím zmírní zátěž bolestivého místa. Neoprenový návlek navíc zahřívá. Výrobci popisují podporu a úlevu při pohybu, ortéza ale potíže sama neléčí.'),
    ('Jak se léčí zánět v lokti?',
     'Léčbu určuje lékař nebo fyzioterapeut podle příčiny, obvykle jde o odlehčení, úpravu zátěže a cvičení. Ortéza může při pohybu podpořit loket. Pokud bolest trvá déle než pár týdnů, přichází po úrazu nebo s otokem, nenechávejte ji bez vyšetření.'),
    ('Jakou ortézu na tenisový loket zvolit?',
     'Při sportu s opakovaným úchopem (tenis, padel, golf, lezení) bývá praktický pásek na předloktí. Pro zahřátí a celkovou oporu kloubu zvolte neoprenový nebo elastický návlek. Rozhoduje obvod paže a pohodlí při pohybu.')])

_patch(A, 'volejbalova-obuv', 'Volejbalové boty: halová obuv | %pocet%',
       'Volejbalové boty do haly: nízké i mid, guma bez šmouh, tlumení dopadu a boční opora. Velikosti a srovnání více obchodů %od%', [
    ('Jaké boty jsou vhodné na volejbal?',
     'Do haly halová obuv s gumovou podrážkou, která nešmouhá, s tlumením pod patou a boční oporou. Běžecká bota je pro skoky a výpady měkká a nestabilní. Venku na písku se hraje naboso nebo v ponožkách na písek.')])

_patch(A, 'boxerske-boty', 'Boxerské boty a zápasnická obuv | %pocet%',
       'Boxerské boty a zápasnická obuv: tenká podrážka, split sole, opora kotníku. Jak vybrat velikost. Srovnání více obchodů %od%')

_patch(B, 'posilovaci-kolecka', 'Posilovací kolečka na břicho | %pocet% a návod',
       'Posilovací kolečka (ab wheel): jednoduchá, dvojitá, s pružinou i 3v1. Jak cvičit rollout, kolik opakování a jak vybrat. Srovnání obchodů %od%', [
    ('Co posiluje posilovací kolečko?',
     'Hlavně střed těla: přímý a šikmé břišní svaly, které při rolloutu drží bedra. Zapojuje se i hluboký stabilizační systém, ramena a široký sval zádový. Je to cvik na sílu trupu, tuk na břiše nespálí.'),
    ('Jak často a kolik minut denně cvičit s kolečkem?',
     'Začátečníkovi stačí dvě až tři krátké série týdně s odpočinkem mezi nimi, ne každý den. Počítejte kvalitní opakování, ne minuty. Zvyšujte rozsah pohybu a počet postupně a končete dřív, než se prohnou záda.'),
    ('Jaký je nejlepší posilovač břišních svalů?',
     'Jeden nejlepší neexistuje. Kolečko, prkno, visy na hrazdě nebo cviky s míčem trénují břicho jinak a dobře se kombinují. Vybírejte podle úrovně, technika a postupné zvyšování zátěže je důležitější než pomůcka.')])
