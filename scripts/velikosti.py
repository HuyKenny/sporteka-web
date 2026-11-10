#!/usr/bin/env python3
"""sporteka.cz — one size notation for the whole site (EU).

    norm_sizes(raw_sizes, kind) -> sorted list of display strings   (kind: 'shoe' | 'apparel' | 'other')
    python3 scripts/velikosti.py                                    # self-test on real feed patterns

Feeds give 5 000+ spellings ("45 (UK 11)", "EUR 39 1/3", "2XL", "122/128", "5 roky / 110 cm", "NO SIZE" …).
Output vocabulary: letters "XXS … 4XL", "S/M"; shoes "EU 42", "EU 42.5", "EU 40 2/3"; adult numeric clothing "EU 38";
kids "128 cm" / "122–128 cm" (height) or "4 let" / "18 měsíců" (age only); other units ("12 kg", "82 mm", "25 ″") kept tidy.
One-size markers (NO SIZE, UNI, OS …) are dropped; a bare 3–15 on shoes is UK/US without a unit → dropped (better nothing than wrong).
"""
import re

ONE_SIZE = re.compile(r'^(osfm|os \(uni\)|no ?size|uni|one ?size|onesize|os|jednotn[áa] velikost|jedna velikost|sans taille|tu|t\.?u\.?|n/?a|-|univerz[áa]ln[ií]|bez velikosti|standard)$', re.I)
LETTER_FIX = {'2XS': 'XXS', '3XS': 'XXXS', '2XL': 'XXL', '3XL': 'XXXL', 'XXXS': 'XXXS', 'SM': 'S', 'MD': 'M', 'LG': 'L', 'XLG': 'XL', 'XXLG': 'XXL', 'SMALL': 'S', 'MEDIUM': 'M', 'LARGE': 'L'}
LETTERS = ['XXXS', 'XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL', '4XL', '5XL', '6XL']
LETTER = re.compile(r'^(?:[2-6]?X?[SL]|XXXS|XXS|XXL|XXXL|M|S|L|XL|[4-6]XL)$')
DASH = '–'
THIRDS = {'1/3': '1/3', '2/3': '2/3'}


def _letters(u):
    u = LETTER_FIX.get(u, u)
    return u if u in LETTERS else None


def _letter_combo(u):
    parts = re.split(r'\s*/\s*', u)
    if 2 <= len(parts) <= 2 and all(_letters(p) for p in parts):
        return '/'.join(_letters(p) for p in parts)
    return None


def norm_one(raw, kind):
    s = re.sub(r'\s+', ' ', (raw or '').replace('\xa0', ' ')).strip()
    s = re.split(r'\s*,\s*(?=\d)', s)[0] if re.search(r'cm\s*,\s*\d', s, re.I) else s
    s = re.sub(r'^EUR?\s+EU\s+', '', s, flags=re.I)
    m_eu = re.search(r'(?:^|/)\s*EU\s*(\d{2}(?:[.,]5)?(?:\s[12]/3)?)\s*$', s, re.I) if re.search(r'\b(UK|US)\b', s, re.I) else None
    if m_eu:                                   # "UK 11 / EU 46" → the EU part
        s = m_eu.group(1)
    if not s or ONE_SIZE.match(s):
        return None
    u = s.upper()
    if re.match(r'^[A-Z]{1,3}\s*-\s*[A-Z]{1,3}$', u):
        u = u.replace(' ', '').replace('-', '/')
    y = re.match(r'^Y(XS|S|SM|M|MD|L|LG|XL|XXL)$', u)               # youth sizes (hockey, bike)
    if y:
        return 'Y' + {'SM': 'S', 'MD': 'M', 'LG': 'L'}.get(y.group(1), y.group(1))
    m = re.match(r'^\(\s*\d+\s*[-–]\s*\d+\s*\)\s*([A-Z0-9]{1,4})$', u)      # "(34-37) S" (hockey socks/gloves): the letter is what matters
    if m:
        u = m.group(1)
        s = u
    if _letters(u):
        return _letters(u)
    if _letter_combo(u):
        return _letter_combo(u)
    # drop the "(UK 11 / FR 42 …)" tail; "5 roky / 110 cm" keeps its height part
    b = re.sub(r'\s*\((?:UK|US|FR|DE|IT|JP|CM|CN|MX)[^)]*\)', '', s, flags=re.I).strip()
    bu = b.upper()
    h = re.search(r'(\d{2,3})\s*(?:[-–/]\s*(\d{2,3}))?\s*cm\b', b, re.I)
    if h and kind != 'other' and 50 <= int(h.group(1)) <= 200 and (re.match(r'^\d{2,3}\s*([-–/]\s*\d{2,3})?\s*cm', b, re.I) or re.search(r'let|rok', b, re.I)):
        lo, hi = h.group(1), h.group(2)
        return f'{lo}{DASH}{hi} cm' if hi else f'{lo} cm'
    a = re.match(r'^(\d{1,2})(?:\s*[-–]\s*(\d{1,2}))?\s*(let|l|roky|rok|yrs|yr|y|years?)\b', bu, re.I)
    if a:
        return f'{a.group(1)}{DASH + a.group(2) if a.group(2) else ""} let'
    mo = re.match(r'^(\d{1,2})(?:\s*[-–]\s*(\d{1,2}))?\s*(m|měs\w*|mes\w*|months?)\b', b, re.I)
    if mo:
        return f'{mo.group(1)}{DASH + mo.group(2) if mo.group(2) else ""} měsíců'
    # kids heights "122/128", "122-128", single 3-digit
    r = re.match(r'^(\d{3})\s*[/\-–]\s*(\d{3})$', b)
    if r and 50 <= int(r.group(1)) <= 200 and kind != 'other':
        return f'{r.group(1)}{DASH}{r.group(2)} cm'
    if re.match(r'^\d{3}$', b) and kind == 'apparel' and 50 <= int(b) <= 200:
        return f'{b} cm'
    # numeric: everything "EU"; halves written "42 1/2" or "42.5"
    num = re.match(r'^(?:EUR?\s*)?(\d{2})(?:[.,](5)|\s+1/2)?(?:\s*([12]/3))?$', bu)
    if num:
        n = int(num.group(1))
        half = bool(re.search(r'[.,]5$|\s1/2$', bu))
        frac = ' ' + num.group(3) if num.group(3) else ('.5' if half else '')
        if kind == 'shoe' and 16 <= n <= 50:
            return f'EU {n}{frac}'
        if kind in ('apparel', 'other') and not frac:
            if 30 <= n <= 62:
                return f'EU {n}'
            if kind == 'apparel' and 62 < n <= 98:
                return f'{n} cm'                      # baby heights 68 … 98
        if kind == 'other' and frac and 30 <= n <= 50:
            return f'EU {n}{frac}'
    rng = re.match(r'^(?:EUR?\s*)?(\d{2})\s*[/\-–]\s*(\d{2})$', bu)       # shoes "39/41", socks "35/38"
    if rng and 16 <= int(rng.group(1)) <= 50 and int(rng.group(2)) > int(rng.group(1)) and kind in ('shoe', 'apparel', 'other'):
        return f'EU {rng.group(1)}{DASH}{rng.group(2)}'
    if re.match(r'^\d{1,2}([.,]5)?$', bu):
        return None                      # UK/US without a unit
    # other: keep units tidy
    u2 = re.sub(r'\s*([A-Z]+|["″”])$', lambda m: ' ' + ('″' if m.group(1) in ('"', '″', '”') else m.group(1).lower()), bu) if re.match(r'^\d+([.,]\d+)?\s*(CM|MM|KG|G|L|ML|M|"|″|”)$', bu) else None
    if u2:
        return u2.replace(',', '.')
    lit = re.match(r'^(\d+(?:[.,]\d+)?)\s*LITR\w*$', bu)
    if lit:
        return f'{lit.group(1).replace(",", ".")} l'
    return b if len(b) <= 14 else None


FILTER_OK = re.compile(r'^(XXXS|XXS|XS|S|M|L|XL|XXL|XXXL|[4-6]XL|Y?[A-Z]{1,3}/[A-Z]{1,3}|Y(XS|S|M|L|XL|XXL)|EU [\d. /]+(–\d+)?|\d+(–\d+)? cm|\d+(–\d+)? (let|měsíců))$')


def filterable(v):
    """Only the clean vocabulary becomes a filter value (offers.sizes keeps everything for display: "90 capsules", "12 OZ" …)."""
    return bool(FILTER_OK.match(v))


def size_key(s):
    if s in LETTERS:
        return (0, LETTERS.index(s), 0.0, s)
    m = re.match(r'^EU (\d+(?:\.\d)?)(?: ([12])/3)?', s)
    if m:
        return (1, float(m.group(1)) + (int(m.group(2)) / 3 if m.group(2) else 0), 0.0, s)
    m = re.match(r'^(\d+)(?:–(\d+))? cm$', s)
    if m:
        return (2, int(m.group(1)), 0.0, s)
    m = re.match(r'^(\d+)(?:–\d+)? (let|měsíců)$', s)
    if m:
        return (3 if m.group(2) == 'měsíců' else 4, int(m.group(1)), 0.0, s)
    if '/' in s:
        return (0, 50, 0.0, s)
    m = re.match(r'^(\d+(?:\.\d+)?)', s)
    return (5, float(m.group(1)) if m else 0.0, 0.0, s)


def norm_sizes(raws, kind, limit=40):
    out = []
    for raw in raws:
        for part in re.split(r',(?=\s*\d)', raw) if ',' in raw and re.search(r'\d–\d+\s*cm,\d', raw) else [raw]:
            v = norm_one(part, kind)
            if v:
                out.append(v)
    return sorted(set(out), key=size_key)[:limit]


SHOE_CATS = {'sportovni-obuv', 'lyzarske-boty', 'brusle', 'inline-brusle', 'cyklisticka-obuv', 'kopacky', 'obuv-do-vody', 'snowboardove-boty',
             'jezdecka-obuv', 'baletni-obuv', 'tanecni-obuv', 'lezecke-boty', 'bezecke-boty', 'skialpove-boty', 'krasobruslarske-brusle', 'rekreacni-brusle', 'hokejove-brusle'}
APPAREL_CATS = {'sportovni-obleceni', 'cyklisticke-obleceni', 'obleceni-bojove-sporty', 'rybarske-obleceni', 'neopreny', 'plavky', 'dresy', 'termopradlo',
                'jezdecke-obleceni', 'jezdecke-kalhoty', 'tanecni-obleceni', 'lovecke-obleceni', 'merino', 'kombinezy', 'lyzarske-obleceni'}


def kind_of(cat_slug, ancestors):
    """ancestors: slugs from the category up to its root (inclusive)."""
    chain = set(ancestors) | {cat_slug}
    if chain & SHOE_CATS:
        return 'shoe'
    if chain & APPAREL_CATS:
        return 'apparel'
    return 'other'


if __name__ == '__main__':
    T = [
        ('45 (UK 11)', 'shoe', 'EU 45'), ('UK 11 / EU 46', 'apparel', 'EU 46'), ('UK 8 / EU 42', 'shoe', 'EU 42'), ('EUR 27', 'shoe', 'EU 27'), ('EUR 39 1/3', 'shoe', 'EU 39 1/3'), ('40 2/3 (UK 7)', 'shoe', 'EU 40 2/3'),
        ('40.5 (UK 7)', 'shoe', 'EU 40.5'), ('38,5', 'shoe', 'EU 38.5'), ('9.5', 'shoe', None), ('10', 'shoe', None), ('28 (UK 11C)', 'shoe', 'EU 28'),
        ('39/41 (UK 5.5/7)', 'shoe', 'EU 39–41'), ('NO SIZE', 'shoe', None), ('UNI', 'other', None), ('OS', 'apparel', None), ('One Size', 'other', None),
        ('2XL', 'apparel', 'XXL'), ('xxl', 'apparel', 'XXL'), ('3XL', 'apparel', 'XXXL'), ('2XS', 'apparel', 'XXS'), ('S/M', 'apparel', 'S/M'), ('l/xl', 'other', 'L/XL'),
        ('38 (UK 28 / DE 36)', 'apparel', 'EU 38'), ('48 (UK 32 / FR 42)', 'apparel', 'EU 48'), ('122/128', 'apparel', '122–128 cm'), ('122-128', 'apparel', '122–128 cm'),
        ('5 roky / 110 cm', 'apparel', '110 cm'), ('4 let', 'apparel', '4 let'), ('3-4 let', 'apparel', '3–4 let'), ('2Yrs', 'apparel', '2 let'), ('3Y', 'apparel', '3 let'),
        ('18-24m', 'apparel', '18–24 měsíců'), ('24-36 měsíců', 'apparel', '24–36 měsíců'), ('59cm', 'other', '59 cm'), ('12kg', 'other', '12 kg'), ('25"', 'other', '25 ″'),
        ('(34-37) S', 'apparel', 'S'), ('35/38', 'apparel', 'EU 35–38'), ('sm', 'apparel', 'S'), ('S-M', 'apparel', 'S/M'), ('EUR EU M', 'apparel', 'M'), ('ymd', 'apparel', 'YM'), ('OSFM', 'apparel', None), ('EUR 42 1/2', 'shoe', 'EU 42.5'), ('113-122cm 5-6L', 'apparel', '113–122 cm'), ('141–150cm,10–11L', 'apparel', '141–150 cm'), ('86', 'apparel', '86 cm'), ('42', 'other', 'EU 42'), ('7', 'other', None), ('82 mm', 'other', '82 mm'), ('9 LITRŮ', 'other', '9 l'), ('164', 'apparel', '164 cm'), ('Jedna velikost', 'other', None),
        ('23g', 'other', '23 g'), ('5', 'apparel', None), ('M', 'shoe', 'M'),
    ]
    bad = 0
    for raw, kind, want in T:
        got = norm_one(raw, kind)
        if got != want:
            bad += 1
            print('FAIL', repr(raw), kind, 'got', repr(got), 'want', repr(want))
    print('multi:', norm_sizes(['131–140cm,8–9L'], 'apparel'), norm_sizes(['M', 'S', '2XL', 'L', 'XL', 'NO SIZE'], 'apparel'), norm_sizes(['44', '38 (UK 5)', '40.5', '39 1/3'], 'shoe'))
    print('OK' if not bad else f'{bad} failures')
