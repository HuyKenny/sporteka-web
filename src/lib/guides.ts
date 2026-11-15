// Seasonal buying guides (Kenny 16. 11. 2026, the January wave): hand-written pages at /<slug>/ with the top products of
// the categories they talk about. Texts live in src/texts/pruvodce.json (no catalogue build, the fast texts deploy);
// katalog.py reserves their slugs like the facet landings' (a product must not take /domaci-posilovna/).
import guides from '../texts/pruvodce.json';

export interface GuideSection {
  h2: string;
  html: string;
  /** category slug whose most popular products are shown under the section */
  cat?: string;
  /** how many products (default 4) */
  n?: number;
}
export interface Guide {
  h1: string;
  seo_title: string;
  seo_desc: string;
  /** short name for links and the breadcrumb */
  name: string;
  intro_html: string;
  sections: GuideSection[];
  faq_json?: string;
  /** ISO date of the last real edit */
  updated: string;
  /** category slugs that link back to this guide (besides the ones its sections show) */
  cats?: string[];
}

export const GUIDES = guides as unknown as Record<string, Guide>;

/** Guides that talk about a category (or one of its ancestors): links on the category page. */
export function guidesFor(catSlugs: string[]): Array<{ slug: string; name: string }> {
  const want = new Set(catSlugs);
  return Object.entries(GUIDES)
    .filter(([, g]) => [...(g.cats ?? []), ...g.sections.map((s) => s.cat ?? '')].some((c) => want.has(c)))
    .map(([slug, g]) => ({ slug, name: g.name }));
}
