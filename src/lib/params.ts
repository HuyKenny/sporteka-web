// Product parameters as the site shows and filters them (written by scripts/katalog.py into product_params):
//   pro   = Pánské / Dámské / Dětské / Unisex (from the shop's category path, the title or the feed's gender)
//   velikost = normalised size (scripts/velikosti.py): XS…XXXL, "EU 42", "128 cm", "4 let"
//   sezona / material / objem / osoby = read from the titles (scripts/parametry.py)
//   barva = one of ~14 base colours (feed colour or title)
export const PARAM_ORDER = ['pro', 'velikost', 'sezona', 'material', 'objem', 'osoby', 'delka', 'flex', 'teplota', 'vypln', 'typ', 'tvar', 'profil', 'tuhost', 'uroven', 'filtr', 'zip', 'vaha', 'vlastnost', 'membrana', 'barva'] as const;
export type ParamKey = (typeof PARAM_ORDER)[number];
export const PARAM_LABEL: Record<ParamKey, string> = { pro: 'Pro koho', velikost: 'Velikost', sezona: 'Sezóna', material: 'Materiál a technologie', objem: 'Objem', osoby: 'Počet osob', delka: 'Délka', flex: 'Tuhost (flex)', teplota: 'Teplota použití', vypln: 'Výplň', tvar: 'Tvar', profil: 'Profil prkna', tuhost: 'Tuhost prkna', uroven: 'Úroveň jezdce', filtr: 'Kategorie filtru', zip: 'Zip', vaha: 'Hmotnost', vlastnost: 'Vlastnosti', typ: 'Typ a použití', membrana: 'Vodní sloupec', barva: 'Barva' };
/** Values whose natural order is not alphabetical or numeric. */
export const VALUE_ORDER: Partial<Record<ParamKey, string[]>> = {
  teplota: ['Letní (nad 10 °C)', 'Přechodový (0 až 10 °C)', 'Zimní (−10 až 0 °C)', 'Extrémní (pod −10 °C)'],
  vaha: ['do 700 g', '700–1 200 g', '1,2–2 kg', 'nad 2 kg'],
  tuhost: ['Měkká', 'Střední', 'Tuhá'],
  uroven: ['Začátečník', 'Pokročilý', 'Expert / závodní'],
  filtr: ['S0 (čiré, noc a mlha)', 'S1 (zataženo)', 'S2 (proměnlivo)', 'S3 (slunečno)', 'S4 (ledovec)'],
  sezona: ['Letní', 'Třísezónní', 'Zimní'],
};
export const BUCKETS: Partial<Record<ParamKey, Array<[string, string, number, number]>>> = {};

/** ASCII slug of a parameter value for URLs (?p_pro=damske). */
export const valueSlug = (v: string) => v.normalize('NFKD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');

export function paramText(_key: ParamKey, values: string[]): string {
  return values.join(', ');
}

const LETTERS = ['XXXS', 'XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL', '4XL', '5XL', '6XL'];
/** Natural order of normalised sizes (same as scripts/velikosti.py size_key): letters, EU numbers, heights, ages. */
export function sizeRank(s: string): number {
  const i = LETTERS.indexOf(s);
  if (i >= 0) return i;
  let m = /^EU (\d+(?:\.\d)?)(?: ([12])\/3)?/.exec(s);
  if (m) return 100 + Number(m[1]) + (m[2] ? Number(m[2]) / 3 : 0);
  m = /^(\d+)(?:–\d+)? cm$/.exec(s);
  if (m) return 1000 + Number(m[1]);
  m = /^(\d+)(?:–\d+)? (let|měsíců)$/.exec(s);
  if (m) return (m[2] === 'měsíců' ? 2000 : 3000) + Number(m[1]);
  return 50;
}

/** Natural order of the filters whose values are numbers in words ("do 20 l" < "20–30 l" < "55 l a více", "1 osoba" < "2 osoby" < "5 a více osob"). */
export function numRank(label: string): number {
  if (/^do /.test(label)) return 0;
  const m = /(\d+)/.exec(label);
  return m ? Number(m[1]) : 999;
}
