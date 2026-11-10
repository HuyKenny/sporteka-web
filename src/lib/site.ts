// Site-wide constants and the JSON-LD base graph (Organization/WebSite).
export const BASE = 'https://sporteka.cz';
export const SITE_NAME = 'Sporteka';
/** GA4 measurement id — empty until the property exists (Base.astro then prints no tag). */
export const GA4_ID = 'G-M17T23654D';
/** Operator (same person as alkoholicky.cz); the home address is left out on purpose. */
export const OPERATOR = { name: 'Ha Duy Huy', ico: '07876823', email: 'info@sporteka.cz' };
export const LOGO_URL = BASE + '/a/logo-512.png';
/** Share image for pages without their own photo. */
export const OG_DEFAULT = BASE + '/a/og.png';
export const OG_HOME = OG_DEFAULT;
export const PER_PAGE = 24;
export const POSTS_PER_PAGE = 12;

/** Founder (Kenny's personal site huy.cz is the Person entity; same node on all his projects). */
export const FOUNDER = { '@type': 'Person', '@id': 'https://huy.cz/#kenny', name: 'Ha Duy Huy', alternateName: 'Kenny', url: 'https://huy.cz/', jobTitle: 'SEO konzultant' };

export function orgGraph(short = false, searchAction = false): unknown[] {
  return [
    short
      ? { '@type': 'Organization', '@id': BASE + '/#organization', name: 'Sporteka.cz', founder: FOUNDER }
      : {
        '@type': 'Organization', '@id': BASE + '/#organization', name: 'Sporteka.cz', url: BASE,
        logo: { '@type': 'ImageObject', '@id': BASE + '/#logo', url: LOGO_URL, contentUrl: LOGO_URL, caption: SITE_NAME, inLanguage: 'cs', width: '512', height: '512' },
        image: { '@id': BASE + '/#logo' },
        founder: FOUNDER,
      },
    {
      '@type': 'WebSite', '@id': BASE + '/#website', url: BASE, name: SITE_NAME, alternateName: 'Srovnávač cen sportovního vybavení', publisher: { '@id': BASE + '/#organization' }, inLanguage: 'cs',
      ...(searchAction ? { potentialAction: { '@type': 'SearchAction', target: BASE + '/?s={search_term_string}', 'query-input': 'required name=search_term_string' } } : {}),
    },
  ];
}

/** D1 keeps local (Europe/Prague) "Y-m-d H:i:s" → ISO with the Prague offset. */
export function isoPrague(local: string): string {
  const s = String(local || '').replace(' ', 'T').slice(0, 19);
  if (!/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$/.test(s)) return '';
  const d = new Date(s + 'Z');
  const name = new Intl.DateTimeFormat('en-US', { timeZone: 'Europe/Prague', timeZoneName: 'shortOffset' }).formatToParts(d).find((p) => p.type === 'timeZoneName')?.value ?? 'GMT+1';
  const m = /GMT([+-])(\d{1,2})/.exec(name);
  const off = m ? `${m[1]}${m[2]!.padStart(2, '0')}:00` : '+01:00';
  return s + off;
}
