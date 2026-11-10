// Shop display names (offers only carry the domain), brand colours (stripe on shop tiles) and full logos
// (public/a/ob/<domain>.webp + src/data/shop-logos.json; without a logo the name is set in the display font).
import logos from '../data/shop-logos.json';
const NAMES: Record<string, string> = {
  'sportisimo.cz': 'Sportisimo', 'bezvasport.cz': 'Bezvasport', 'answear.cz': 'Answear', 'footshop.cz': 'Footshop', '4camping.cz': '4camping',
  'd-sport.cz': 'D-Sport', 'azfishing.cz': 'AZfishing', 'hs-sport.cz': 'Hs-sport', 'insportline.cz': 'inSPORTline', 'swimaholic.cz': 'Swimaholic',
  '2sport.cz': '2sport', 'e-sportshop.cz': 'E-sportshop', 'skinners.cz': 'Skinners', 'decathlon.cz': 'Decathlon',
  'e-sipky.cz': 'E-šipky',
  'allegro.cz': 'Allegro',
  'bauerhockey.cz': 'Bauerhockey',
  'lekarna.cz': 'Lékárna.cz',
  'forsize.cz': 'Forsize',
  'militarysklad.cz': 'Militarysklad',
  'naboso.cz': 'NaBOSo',
  'newbalance.cz': 'New Balance',
  'benu.cz': 'Benu',
  'naturalprotein.cz': 'NaturalProtein',
  'nejlevnejsiprotein.cz': 'Nejlevnější protein',
  'nutriheads.cz': 'Nutriheads',
  'shapenbarefoot.com': 'Shapen Barefoot',
  'fanda-nhl.cz': 'Fanda-NHL',
  'acrasport.cz': 'Acrasport',
  'footballtime.cz': 'FootballTime',
  'gigamat.cz': 'Gigamat',
  'shopcom.cz': 'Shopcom',
  'm1sport.cz': 'M1sport',
  'marrko.cz': 'Marrko',
  'sunshop.cz': 'Sunshop',
  'merinoobchod.cz': 'Merinoobchod',
  'st-potapeni.cz': 'ST-potapeni',
  'olpran.cz': 'Olpran',
  'springos.cz': 'Springos',
  'relaxworld.cz': 'Relaxworld',
  'trailstore.cz': 'TrailStore',
  'nejoutdoor.cz': 'Nejoutdoor',
  'ppb-pohary.cz': 'ppb-pohary',
  'merinoshop.cz': 'Merinoshop',
  'bscom.cz': 'Bscom',
  'sachasport.cz': 'Sachasport',
  'kokiskashop.cz': 'Kokiskashop',
  'outdoormarket.cz': 'OutdoorMarket',
  'stretchfit.cz': 'Stretchfit',
  'swix.cz': 'Swix',
  'sorrygravity.cz': 'SorryGravity',
  'pepebike.cz': 'Pepebike',
  'eleven-sportswear.cz': 'Eleven-sportswear',
  'honzovy-longboardy.cz': 'Honzovy-longboardy',
  'procamping.cz': 'Procamping',
  'spartoo.cz': 'Spartoo',
  'isostar.cz': 'Isostar',
  'outdoorshops.cz': 'Outdoorshops',
};
export const shopName = (domain: string) => NAMES[domain] ?? domain;
const COLORS: Record<string, string> = {
  'sportisimo.cz': '#E30613', 'bezvasport.cz': '#00A3E0', 'answear.cz': '#111111', 'footshop.cz': '#111111', '4camping.cz': '#F39200',
  'd-sport.cz': '#E2001A', 'azfishing.cz': '#2E7D32', 'hs-sport.cz': '#0B4EA2', 'insportline.cz': '#E30613', 'swimaholic.cz': '#00A7C4',
  '2sport.cz': '#F7931E', 'e-sportshop.cz': '#1E5A43', 'skinners.cz': '#2B2B2B', 'decathlon.cz': '#0082C3',
};
/** Bump when a logo file is replaced: /a/* is cached for 30 days by browsers and the edge. */
const LOGO_V = 7;
export const shopColor = (domain: string) => COLORS[domain] ?? '#1E5A43';

/** Full logo with a display size of similar visual weight (width grows with √ aspect ratio), or null. */
export function shopLogo(domain: string): { src: string; w: number; h: number } | null {
  const d = (logos as unknown as Record<string, [number, number]>)[domain];
  if (!d) return null;
  const r = d[0] / d[1];
  let h = Math.sqrt(3600 / r), w = h * r;
  if (w > 132) { w = 132; h = w / r; }
  if (h > 40) { h = 40; w = h * r; }
  return { src: `/a/ob/${domain.replace(/\./g, '-')}.webp?v=${LOGO_V}`, w: Math.round(w), h: Math.round(h) };
}
