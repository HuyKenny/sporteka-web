// Formatting helpers shared by templates (Czech typography: non-breaking spaces in numbers and before "Kč").
export const NBSP = ' ';

export function cislo(n: number | string | null | undefined): string {
  return Math.round(Number(n) || 0).toString().replace(/\B(?=(\d{3})+(?!\d))/g, NBSP);
}
export function cena(n: number | string | null | undefined): string {
  return cislo(n) + NBSP + 'Kč';
}
/** 1 produkt, 2–4 produkty, 5+ produktů (erk_produktu) */
export function produktu(n: number): string {
  return n === 1 ? 'produkt' : n >= 2 && n <= 4 ? 'produkty' : 'produktů';
}
export function eshopu(n: number): string {
  return n === 1 ? 'eshopu' : 'eshopů';
}
export function datum(iso: string | null | undefined): string {
  const m = /^(\d{4})-(\d{2})-(\d{2})/.exec(String(iso ?? ''));
  return m ? `${Number(m[3])}. ${Number(m[2])}. ${m[1]}` : '';
}
export function esc(s: string): string {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}
/** Decode the HTML entities WordPress leaves in titles (&#8211; …) for plain-text contexts. */
export function decode(s: string | null | undefined): string {
  return String(s ?? '')
    .replace(/&#(\d+);/g, (_, n) => String.fromCodePoint(Number(n)))
    .replace(/&#x([0-9a-f]+);/gi, (_, n) => String.fromCodePoint(parseInt(n, 16)))
    .replace(/&nbsp;/g, NBSP).replace(/&quot;/g, '"').replace(/&#039;|&apos;/g, "'").replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&');
}
/** wp_strip_all_tags + whitespace collapse (what Rank Math does for %excerpt% / %term_description%). */
export function stripTags(html: string | null | undefined): string {
  return decode(String(html ?? '').replace(/<(script|style)\b[\s\S]*?<\/\1>/gi, '').replace(/<[^>]+>/g, '')).replace(/\s+/g, ' ').trim();
}
/** Plain text cut at a word boundary (cards, blog listing). Rank Math descriptions are NOT cut — use stripTags. */
export function excerpt(html: string | null | undefined, max = 160): string {
  const t = stripTags(html);
  if (t.length <= max) return t;
  const cut = t.slice(0, max + 1);
  const i = cut.lastIndexOf(' ');
  return (i > 80 ? cut.slice(0, i) : t.slice(0, max)).replace(/[\s,;:–-]+$/, '');
}

/** Subset of WordPress wptexturize() for displayed titles (Czech quotes „…“, en dash, ellipsis, apostrophe). Rank Math
 *  titles/descriptions use the raw text, H1 and listings the texturized one — both are kept so parity holds. */
export function texturize(s: string): string {
  return s
    .replace(/(\d)''/g, '$1“').replace(/(\d)"/g, '$1″').replace(/(\d)x(\d)/g, '$1×$2')
    .replace(/(^|[\s(\[])"(?=\S)/g, '$1„').replace(/"/g, '“')
    .replace(/(\d)'(?=\s|$)/g, '$1′').replace(/(\d)'/g, '$1’')
    .replace(/(\w)'(\w)/g, '$1’$2').replace(/(\w)'(?=\s)/g, '$1‘')
    .replace(/ - /g, ' – ').replace(/ -- /g, ' — ')
    .replace(/\.\.\./g, '…');
}

/** Comment HTML from WordPress (originally visitor input): only p, br, b/strong, i/em and plain http(s) links survive. */
export function safeCommentHtml(html: string): string {
  return String(html ?? '')
    .replace(/<(script|style|iframe|object|embed|svg|math)\b[\s\S]*?<\/\1\s*>/gi, '')
    .replace(/<\/?([a-z0-9]+)([^>]*)>/gi, (tag, name: string, attrs: string) => {
      const n = name.toLowerCase();
      const close = tag.startsWith('</');
      if (['p', 'br', 'b', 'strong', 'i', 'em'].includes(n)) return close ? `</${n}>` : `<${n}>`;
      if (n === 'a') {
        if (close) return '</a>';
        const href = /href\s*=\s*["']?(https?:\/\/[^"'\s>]+)/i.exec(attrs)?.[1];
        return href ? `<a href="${esc(decode(href))}" rel="nofollow ugc noopener" target="_blank">` : '<a>';
      }
      return '';
    });
}
