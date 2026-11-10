// Unknown URL → the most relevant listing (27. 10. 2026). Words of the path (no diacritics, stop words, numbers) are
// compared by stems (no final vowels, 5 letters) with the names of indexable categories (≥ 5 products) and brands (≥ 3 products):
// score = IDF of the matched stems − half the IDF of the candidate's name stems missing from the URL, so "cerny-vibrator"
// lands on Vibrátory rather than Černé body. A clear match → 301 there (dispatch.ts), otherwise the page stays 404.
import { brandList, catTree } from './db';

const STOP = new Set(['pro', 'and', 'the', 'for', 'with', 'eroticke', 'eroticky', 'eroticka', 'erotic', 'erotik', 'erotika', 'sex', 'sexy',
  'shop', 'eshop', 'levne', 'levny', 'levna', 'cena', 'ceny', 'recenze', 'nejlepsi', 'koupit', 'prodej', 'www', 'html', 'page', 'null',
  'stock', 'tag', 'kategorie', 'produkt', 'product', 'znacka', 'brand', 'novinky', 'akce', 'sleva', 'zdarma', 'dalsi']);
const fold = (t: string) => t.normalize('NFKD').replace(/[̀-ͯ]/g, '').toLowerCase();
export const stems = (t: string) => [...new Set(fold(t).split(/[^a-z0-9]+/).filter((w) => w.length >= 3 && !/\d/.test(w) && !STOP.has(w)).map(stem))];
// Czech endings: drop trailing vowels, then the first 5 letters (maska/masky → mask, černý/černé → cern, korzety → korze)
function stem(w: string) { return w.replace(/[aeiouy]+$/, '').slice(0, 5) || w.slice(0, 5); }

/** stems of category names (rum, whisk, gin, vodk…): a brand matched only through them (Presidente Rum for "rum-do-caje") is no match, the category is */
let catStems = new Set<string>();
interface Doc { to: string; name: string[]; all: Set<string>; n: number; brand: boolean; generic?: boolean }
let memo: { at: number; docs: Doc[]; idf: Map<string, number> } | null = null;

async function index(db: D1Database) {
  if (memo && Date.now() - memo.at < 600_000) return memo;
  const [tree, brands] = await Promise.all([catTree(db), brandList(db)]);
  const docs: Doc[] = [];
  for (const c of tree.byId.values()) {
    if (c.noindex || c.count_total < 5) continue;
    const name = stems(c.name);
    docs.push({ to: `/${c.slug}/`, name, all: new Set([...name, ...stems(c.slug)]), n: c.count_total, brand: false });
  }
  for (const b of brands.byId.values()) {
    if (b.count < 3 || b.slug === 'ostatni') continue;
    const name = stems(b.name);
    if (name.length) docs.push({ to: `/znacka/${b.slug}/`, name, all: new Set([...name, ...stems(b.slug)]), n: b.count, brand: true });
  }
  catStems = new Set(docs.filter((d) => !d.brand).flatMap((d) => d.name));
  const df = new Map<string, number>();
  for (const d of docs) for (const s of d.all) df.set(s, (df.get(s) ?? 0) + 1);
  const idf = new Map([...df].map(([s, k]) => [s, Math.log(docs.length / k)]));
  // brands named like a category ("Latex") are ordinary words: the category answers them better
  const catNames = new Set(docs.filter((d) => !d.brand).map((d) => d.name.join(' ')));
  for (const d of docs) if (d.brand && catNames.has(d.name.join(' '))) d.generic = true;
  memo = { at: Date.now(), docs, idf };
  return memo;
}

/** Best listing for an unknown path (words joined from its segments), or null. */
export async function guessListing(db: D1Database, words: string): Promise<string | null> {
  const want = stems(words);
  if (!want.length) return null;
  const { docs, idf } = await index(db);
  let best: { to: string; score: number; n: number } | null = null;
  for (const d of docs) {
    let hit = 0;
    for (const s of want) if (d.all.has(s) && !(d.brand && catStems.has(s))) hit += idf.get(s) ?? 0;
    if (!hit) continue;
    let miss = 0;
    for (const s of d.name) if (!want.includes(s)) miss += idf.get(s) ?? 0;
    // brands win ties (an old product URL starts with its brand: lelo-sona-2 → Lelo, not Sono)
    const bonus = !d.brand ? 0 : d.generic ? -0.5 : d.all.has(want[0]!) ? 0.5 * (idf.get(want[0]!) ?? 0) : 0.1;
    const score = hit - miss / 2 + bonus + Math.log10(d.n) / 10;
    if (!best || score > best.score) best = { to: d.to, score, n: d.n };
  }
  return best && best.score >= 1.2 ? best.to : null;
}
