// data_version: bumped by the importer once a night (finalizeDay) and by POST /facets (site_cache), memoised 60 s. Part of every edge-cache key, so a price
// change is visible right after an import without purging.
import { getEnv } from './env';

let memo: { v: string; at: number } | null = null;
export async function dataVersion(): Promise<string> {
  if (memo && Date.now() - memo.at < 60_000) return memo.v;
  const row = await getEnv().DB.prepare("SELECT value FROM site_cache WHERE key='data_version'").first<{ value: string }>();
  memo = { v: row?.value ?? '0', at: Date.now() };
  return memo.v;
}
