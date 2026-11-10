import { getEnv } from './server/env';

/** "Now" for anything printed into a page. The static snapshot pins it to the catalogue day (--var DATA_DAY:YYYY-MM-DD)
 *  so the same data renders the same bytes and only really changed pages are uploaded. */
export function renderNow(): number {
  const d = (getEnv() as { DATA_DAY?: string }).DATA_DAY;
  return d && /^\d{4}-\d{2}-\d{2}$/.test(d) ? Date.parse(d + 'T12:00:00Z') : Date.now();
}
