import { isStatic } from './server/env';

/** Shop exit link: /go/<slug>/ (logged redirect) on the SSR site; the stored affiliate URL itself in the static
 *  snapshot (no Worker runs there). The target is used byte for byte — signed network links must not be re-encoded. */
export function goHref(goSlug: string | null | undefined, target: string | null | undefined, ctx: string): string {
  if (isStatic() && target && /^https:\/\//.test(target)) return target;
  return `/go/${goSlug}/?ctx=${ctx}`;
}
