// Hand-written facet-landing texts (src/texts/fasety.json, written by scripts/fasety_vlna*.py → scripts/fasety-export.py).
// A landing without such a text is thin (the generated template): it stays reachable but noindex, out of the sitemap and out of
// the category's list of related listings, until its text exists (Kenny 11. 11. 2026 — more landings, only good ones indexed).
import facetTexts from '../texts/fasety.json';

export interface FacetText { seo_title?: string; seo_desc?: string; description_html?: string; guide_html?: string; faq_json?: string }
export const FACET_TEXTS = facetTexts as unknown as Record<string, FacetText>;
export const hasFacetText = (slug: string): boolean => !!FACET_TEXTS[slug]?.guide_html;
