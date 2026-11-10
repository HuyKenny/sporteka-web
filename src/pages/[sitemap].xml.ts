// Sitemap files (product-sitemapN, category-sitemap, brand-sitemap, page-sitemap), built from D1 (lib/sitemap.ts).
import type { APIRoute } from 'astro';
import { getEnv } from '../lib/server/env';
import { sitemapFile } from '../lib/sitemap';

export const prerender = false;
const NAME = /^(page-sitemap|category-sitemap|brand-sitemap|product-sitemap\d{1,3})$/;
export const GET: APIRoute = async ({ params }) => {
  const name = String(params.sitemap ?? '');
  const xml = NAME.test(name) ? await sitemapFile(getEnv().DB, name) : null;
  if (!xml) return new Response('Not found', { status: 404, headers: { 'content-type': 'text/plain; charset=utf-8' } });
  return new Response(xml, { headers: { 'content-type': 'application/xml; charset=UTF-8', 'x-robots-tag': 'noindex, follow' } });
};
