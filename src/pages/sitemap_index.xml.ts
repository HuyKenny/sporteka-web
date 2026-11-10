import type { APIRoute } from 'astro';
import { getEnv } from '../lib/server/env';
import { sitemapIndex } from '../lib/sitemap';

export const prerender = false;
export const GET: APIRoute = async () => new Response(await sitemapIndex(getEnv().DB), { headers: { 'content-type': 'application/xml; charset=UTF-8', 'x-robots-tag': 'noindex, follow' } });
