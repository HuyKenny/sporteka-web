// "Shrnutí nabídky" on a product page: a few sentences written only from our own data (price history, the product's
// place among the category's prices, shop spread, sizes only one shop has). The shop's description below it is the
// same text on every price comparison site; this block is what the page adds (Google core update 11/2026: feed
// catalogues read as scaled content). A sentence is printed only when the data support it — no filler.
import { cena, cislo, datum, esc } from './format';
import { shopName } from './shops';

type Point = { day: string; min_price: number };
type OfferLite = { domain: string; price: number; stock: number; sizes?: string };

const sizesOf = (o: OfferLite) => { try { return o.sizes ? (JSON.parse(o.sizes) as string[]) : []; } catch { return []; } };
const daysBetween = (a: string, b: string) => Math.round((Date.parse(b) - Date.parse(a)) / 86400_000);
const short = (iso: string) => datum(iso).replace(/\s\d{4}$/, '');   // "3. 11."

export interface SummaryInput {
  name: string;
  offers: OfferLite[];
  history: Point[];
  today: string;                      // YYYY-MM-DD of the data
  cat?: { name: string; slug: string; prices: Float64Array | null; guide: boolean } | null;
}

/** Sentences as HTML (escaped). Empty when there is nothing worth saying. */
export function productSummary(x: SummaryInput): string[] {
  const out: string[] = [];
  const live = x.offers.filter((o) => o.price > 0);
  if (!live.length) return out;
  const inStock = live.filter((o) => o.stock !== -1);
  const cur = Math.min(...(inStock.length ? inStock : live).map((o) => o.price));

  // 1. price history over the last 90 days (a weekly point per change)
  const from = new Date(Date.parse(x.today) - 90 * 86400_000).toISOString().slice(0, 10);
  const h = x.history.filter((p) => p.day >= from && p.min_price > 0);
  if (h.length >= 2) {
    const span = daysBetween(h[0]!.day, x.today);
    const lo = h.reduce((a, b) => (b.min_price < a.min_price ? b : a));
    const hi = h.reduce((a, b) => (b.min_price > a.min_price ? b : a));
    const spread = hi.min_price - lo.min_price;
    if (span >= 14 && spread / hi.min_price >= 0.03) {
      if (cur <= lo.min_price + 0.5) {
        out.push(`Aktuální cena ${cena(cur)} je nejnižší za posledních ${cislo(span)} dní, kdy cenu sledujeme. Nejvýš byla ${cena(hi.min_price)} (${short(hi.day)}).`);
      } else if (cur >= hi.min_price - 0.5) {
        out.push(`Cena je teď nejvyšší za posledních ${cislo(span)} dní. Nejlevněji jsme produkt viděli za ${cena(lo.min_price)} (${short(lo.day)}), takže se vyplatí sledovat slevy.`);
      } else {
        out.push(`Za posledních ${cislo(span)} dní se nejnižší cena pohybovala mezi ${cena(lo.min_price)} a ${cena(hi.min_price)}; teď je ${cena(cur)}.`);
      }
    } else if (span >= 28) {
      out.push(`Cena se za posledních ${cislo(span)} dní prakticky nezměnila, drží se kolem ${cena(cur)}.`);
    }
  }

  // 2. the product's place among the prices of its main category
  const ps = x.cat?.prices;
  if (x.cat && ps && ps.length >= 20) {
    let below = 0;
    while (below < ps.length && ps[below]! < cur) below++;
    const pct = Math.round((below / ps.length) * 100);
    const median = ps[Math.floor(ps.length / 2)]!;
    const cat = `<a href="/${x.cat.slug}/">${esc(x.cat.name)}</a>`;
    if (pct <= 25) out.push(`V kategorii ${cat} patří k levnější čtvrtině: dražších je ${100 - pct} % z ${cislo(ps.length)} modelů (polovina stojí víc než ${cena(median)}).`);
    else if (pct >= 75) out.push(`V kategorii ${cat} patří k dražší čtvrtině: levnějších je ${pct} % z ${cislo(ps.length)} modelů, polovina stojí do ${cena(median)}.`);
    else out.push(`Cenou je ve středu kategorie ${cat}: polovina z ${cislo(ps.length)} modelů stojí do ${cena(median)}.`);
  }

  // 3. shop spread and sizes only one shop has
  const shops = [...new Set(live.map((o) => o.domain))];
  if (shops.length > 1) {
    const max = Math.max(...live.map((o) => o.price));
    const diff = max - cur;
    const sells = shops.length < 5 ? `Prodávají ho ${shops.length} obchody` : `Prodává ho ${shops.length} obchodů`;
    if (diff >= 1) out.push(`${sells}; mezi nejlevnější a nejdražší nabídkou je rozdíl ${cena(diff)} (${Math.round((diff / max) * 100)} %).`);
    else out.push(`${sells} za stejnou cenu, rozhoduje tedy doprava a dostupnost velikostí.`);
    // sizes only one shop has — only among shops that label sizes the same way (≥ 2 sizes in common with every other
    // shop), otherwise "36S" vs "36 short" or "S/35-38" vs "EU 39–42" would read as different sizes
    const norm = (s: string) => s.toLowerCase().replace(/^eu\s*/, '').replace(/\s+/g, '');
    const lists = new Map<string, Map<string, string>>();
    for (const o of live) for (const s of sizesOf(o)) { if (!lists.has(o.domain)) lists.set(o.domain, new Map()); lists.get(o.domain)!.set(norm(s), s); }
    const doms = [...lists.keys()];
    const comparable = doms.length >= 2 && doms.every((a) => doms.every((b) => a === b || [...lists.get(a)!.keys()].filter((k) => lists.get(b)!.has(k)).length >= 2));
    if (comparable) {
      let said = 0;
      for (const d of doms) {
        const ss = [...lists.get(d)!].filter(([k]) => doms.every((o) => o === d || !lists.get(o)!.has(k))).map(([, s]) => s);
        if (ss.length && ss.length <= 6 && said < 2) { said++; out.push(`${ss.length === 1 ? 'Velikost' : 'Velikosti'} ${esc(ss.join(', '))} ${ss.length === 1 ? 'má' : 'mají'} skladem jen ${esc(shopName(d))}.`); }
      }
    }
  }

  // 4. the category's buying guide
  if (out.length && x.cat?.guide) out.push(`Nevíte, co při výběru sledovat? Přečtěte si <a href="/${x.cat.slug}/#pruvodce">průvodce kategorií ${esc(x.cat.name)}</a>.`);
  return out;
}
