import type { APIRoute } from 'astro';
import { getEnv } from '../../lib/server/env';
import { handleGo } from '../../lib/server/go';

export const prerender = false;
export const GET: APIRoute = ({ params, request, locals }) => handleGo(params.slug, request, getEnv(), (p) => locals.cfContext?.waitUntil(p));
