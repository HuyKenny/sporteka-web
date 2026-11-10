// Section icons (own monoline sprite public/a/s2.svg, 48 px grid): every category inherits the icon of its section,
// a subcategory falls back to its nearest ancestor that has one.
import type { Cat } from './db';

/** Trail-marker colour per section (Czech hiking signs: red, blue, green, yellow) — the colour stripe of tiles and headings. */
export const SECTIONS: Array<{ slug: string; icon: string; label: string; mark: 'r' | 'b' | 'g' | 'y' }> = [
  { slug: 'sportovni-obleceni', icon: 'obleceni', label: 'Oblečení', mark: 'r' },
  { slug: 'sportovni-obuv', icon: 'obuv', label: 'Obuv', mark: 'b' },
  { slug: 'outdoor', icon: 'outdoor', label: 'Outdoor', mark: 'g' },
  { slug: 'kemping', icon: 'kemping', label: 'Kemping', mark: 'y' },
  { slug: 'rybareni', icon: 'ryby', label: 'Rybaření', mark: 'g' },
  { slug: 'lov-a-priroda', icon: 'lov', label: 'Lov a příroda', mark: 'y' },
  { slug: 'cyklistika', icon: 'cyklistika', label: 'Cyklistika', mark: 'r' },
  { slug: 'kolobezky-a-brusle', icon: 'kolecka', label: 'Kolečka', mark: 'y' },
  { slug: 'zimni-sporty', icon: 'zima', label: 'Zimní sporty', mark: 'b' },
  { slug: 'vodni-sporty', icon: 'voda', label: 'Voda a plavání', mark: 'b' },
  { slug: 'fitness', icon: 'fitness', label: 'Fitness', mark: 'g' },
  { slug: 'beh', icon: 'beh', label: 'Běh a atletika', mark: 'b' },
  { slug: 'joga-a-pilates', icon: 'joga', label: 'Jóga a pilates', mark: 'y' },
  { slug: 'tanec-a-gymnastika', icon: 'tanec', label: 'Tanec a gymnastika', mark: 'r' },
  { slug: 'sportovni-vyziva', icon: 'vyziva', label: 'Sportovní výživa', mark: 'r' },
  { slug: 'micove-sporty', icon: 'mice', label: 'Míčové sporty', mark: 'y' },
  { slug: 'bojove-sporty', icon: 'box', label: 'Bojové sporty', mark: 'r' },
  { slug: 'golf', icon: 'golf', label: 'Golf', mark: 'b' },
  { slug: 'jezdectvi', icon: 'jezdectvi', label: 'Jezdectví', mark: 'g' },
  { slug: 'volny-cas', icon: 'hry', label: 'Hry a volný čas', mark: 'g' },
];
/** The 13 strongest sections: shown in the header strip and the mega menu; the rest sits under "Další kategorie". The homepage tiles take the first 12. */
export const TOP: string[] = ['sportovni-obleceni', 'sportovni-obuv', 'outdoor', 'kemping', 'cyklistika', 'zimni-sporty', 'fitness', 'sportovni-vyziva',
  'micove-sporty', 'vodni-sporty', 'rybareni', 'kolobezky-a-brusle', 'bojove-sporty'];
/** Icons of well-known subcategories (sprite ids in /a/s2.svg); everything else inherits the section icon. */
const SUB: Record<string, string> = {
  'stany': 'stan', 'stanove-kolky': 'stan', 'stanove-doplnky': 'stan', 'turisticke-stany': 'stan', 'rodinne-stany': 'stan', 'pop-up-a-plazove-stany': 'stan', 'tipi-a-lavvu': 'stan', 'expedicni-stany': 'stan', 'pristresky-a-party-stany': 'stan', 'rybarske-stany': 'stan', 'detske-stany': 'stan', 'strechni-stany': 'stan', 'trekingova-a-mestska-elektrokola': 'kolo', 'horska-elektrokola': 'kolo', 'skladaci-elektrokola': 'kolo', 'nakladni-elektrokola': 'kolo', 'skladaci-kola': 'kolo', 'bmx-a-dirt-kola': 'kolo', 'odrazedla': 'kolo', 'detske-cyklohelmy': 'helma', 'mtb-a-integralni-helmy': 'helma', 'silnicni-cyklohelmy': 'helma', 'mestske-cyklohelmy': 'helma', 'cyklisticke-bryle': 'bryle', 'cyklisticke-rukavice': 'bunda', 'cyklisticke-dresy': 'bunda', 'cyklisticke-kratasy-a-kalhoty': 'bunda', 'cyklisticke-bundy-a-vesty': 'bunda', 'cyklisticke-navleky': 'ponozka', 'cyklo-lahve-a-drzaky': 'lahev', 'cyklo-chranice': 'helma', 'cyklisticke-ponozky': 'ponozka', 'sportovni-bundy': 'bunda', 'lyzarske-bundy': 'bunda', 'cyklisticke-helmy': 'helma', 'lyzarske-helmy': 'helma',
  'trekove-hole': 'hole', 'lahve-a-termosky': 'lahev', 'sportovni-hodinky': 'hodinky', 'cyklo-computery': 'hodinky', 'sportovni-bryle': 'bryle', 'lyzarske-bryle': 'bryle',
  'plavecke-bryle': 'bryle', 'cinky-a-kotouce': 'cinka', 'sportovni-ponozky': 'ponozka', 'cepice-a-celenky': 'cepice', 'plavecke-cepice': 'cepice', 'bezecka-obuv': 'bezecka',
  'plavky': 'plavky', 'jizdni-kola': 'kolo', 'elektrokola': 'kolo', 'sjezdove-lyze': 'lyze', 'bezecke-lyzovani': 'lyze', 'skialpinismus': 'lyze', 'proteiny': 'proteiny', 'gainery': 'proteiny',
};
const BY_SLUG = new Map(SECTIONS.map((s) => [s.slug, s]));

/** Section of a category (own or of the nearest ancestor), or null. */
export function section(slug: string, tree?: { byId: Map<number, Cat>; bySlug: Map<string, Cat> }) {
  let c = tree?.bySlug.get(slug);
  if (!c) return BY_SLUG.get(slug) ?? null;
  const seen = new Set<number>();
  while (c && !seen.has(c.id)) {
    seen.add(c.id);
    const hit = BY_SLUG.get(c.slug);
    if (hit) return hit;
    c = tree?.byId.get(c.parent);
  }
  return null;
}
/** Icon id in /a/s2.svg for a category, or null. */
export function catIcon(slug: string, tree?: { byId: Map<number, Cat>; bySlug: Map<string, Cat> }): string | null {
  return SUB[slug] ?? section(slug, tree)?.icon ?? null;
}
