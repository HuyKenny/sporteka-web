// Listing filters and sort of the static export (no server): /_f/<listing>/a.json holds the filter attributes of the
// listing's most popular products (scripts/staticky.py build_filters), the cards come in files of 100 (<n>.json).
// Runs only when the URL carries a filter, a sort or ?strana= — the plain listing is the static HTML itself.
import { card, esc, type Card } from './hledat';

type Row = [number, number, number | number[], number, number, number, number[]];
interface Data { n: number; c: number; b: string[]; s: string[]; p: string[]; r: Row[] }
const PER = 24;
const TOP = 6000;
const memo = new Map<string, Promise<unknown>>();
const get = <T>(u: string): Promise<T | null> => {
  if (!memo.has(u)) memo.set(u, fetch(u).then((r) => (r.ok ? r.json() : null)).catch(() => null));
  return memo.get(u) as Promise<T | null>;
};
const list = (v: string | null) => (v ?? '').split(',').map((x) => x.trim().toLowerCase()).filter(Boolean);
const num = (v: string | null) => (v && /^\d+$/.test(v.trim()) ? Number(v) : undefined);
const produktu = (n: number) => (n === 1 ? 'produkt' : n >= 2 && n <= 4 ? 'produkty' : 'produktů');

/** listing key of this page + the fixed query of a facet landing */
async function listing(): Promise<{ key: string; fixed: URLSearchParams } | null> {
  const path = decodeURIComponent(location.pathname).replace(/page\/\d+\/$/, '');
  const m = /^\/znacka\/([^/]+)\/$/.exec(path);
  if (m) return { key: `b/${m[1]}`, fixed: new URLSearchParams() };
  if (path === '/slevy/') return { key: 'slevy', fixed: new URLSearchParams() };
  const slug = /^\/([^/]+)\/$/.exec(path)?.[1];
  if (!slug) return null;
  const land = await get<{ k: string; q: string }>(`/_f/l/${slug}.json`);
  if (land) return { key: land.k, fixed: new URLSearchParams(land.q) };
  return { key: `c/${slug}`, fixed: new URLSearchParams() };
}

export async function run(form: HTMLFormElement): Promise<void> {
  const own = new URLSearchParams(location.search);
  own.delete('s');
  if (![...own.keys()].length) return;
  const at = await listing();
  if (!at) return;
  const data = await get<Data>(`/_f/${at.key}/a.json`);
  if (!data) return;
  const sp = new URLSearchParams(at.fixed);
  for (const [k, v] of own) sp.set(k, v);
  const sort = sp.get('orderby') ?? 'pop';
  const min = num(sp.get('min_price')), max = num(sp.get('max_price'));
  const brands = new Set(list(sp.get('znacka'))), shops = new Set(list(sp.get('obchod')));
  const stock = sp.get('skladem') === '1', disc = sp.get('sleva') === '1';
  const want = new Map<string, Set<string>>();
  for (const [k, v] of sp) if (k.startsWith('p_')) want.set(k.slice(2), new Set(list(v)));
  // parameter value index → "key=value"; per wanted key the matching indexes
  const wantIdx = [...want].map(([k, vals]) => new Set(data.p.flatMap((pv, i) => (vals.has(pv.slice(k.length + 1)) && pv.startsWith(k + '=') ? [i] : []))));
  const shopIdx = new Set(data.s.flatMap((d, i) => (shops.has(d) ? [i] : [])));
  let idx: number[] = [];
  data.r.forEach((r, i) => {
    if (min !== undefined && r[0] < min) return;
    if (max !== undefined && r[0] > max) return;
    if (brands.size && !brands.has(data.b[r[1]]!)) return;
    if (shopIdx.size && !(Array.isArray(r[2]) ? r[2] : [r[2]]).some((x) => shopIdx.has(x))) return;
    if (stock && r[3] !== 1) return;
    if (disc && !(r[4] > 0)) return;
    for (const s of wantIdx) if (!r[6].some((x) => s.has(x))) return;
    idx.push(i);
  });
  const R = data.r;
  if (sort === 'price') idx.sort((a, b) => (R[a]![0] || 1e9) - (R[b]![0] || 1e9) || a - b);
  else if (sort === 'price-desc') idx.sort((a, b) => R[b]![0] - R[a]![0] || a - b);
  else if (sort === 'disc') idx.sort((a, b) => R[b]![4] - R[a]![4] || a - b);
  else if (sort === 'date') idx.sort((a, b) => R[b]![5] - R[a]![5] || a - b);
  const pages = Math.max(1, Math.ceil(idx.length / PER));
  const page = Math.min(pages, Math.max(1, num(own.get('strana')) ?? 1));
  const shown = idx.slice((page - 1) * PER, page * PER);
  const chunks = await Promise.all([...new Set(shown.map((i) => Math.floor(i / data.c)))].map(async (n) => [n, await get<Card[]>(`/_f/${at.key}/${n}.json`)] as const));
  const byChunk = new Map(chunks);
  const cards = shown.map((i) => byChunk.get(Math.floor(i / data.c))?.[i % data.c]).filter((c): c is Card => !!c);

  // grid, count, pagination
  const grid = document.querySelector('.lv ul.g, .lv .prazdno');
  const html = cards.length ? `<ul class="g">${cards.map(card).join('')}</ul>` : '<p class="prazdno">Těmto filtrům nic neodpovídá. Zkuste některý zrušit.</p>';
  if (grid) grid.outerHTML = html;
  document.querySelector('.lv nav.str')?.remove();
  const capped = data.n >= TOP ? ` z ${TOP.toLocaleString('cs-CZ')} nejoblíbenějších` : '';
  const n = document.querySelector('.lh__n');
  if (n) n.textContent = `${idx.length.toLocaleString('cs-CZ')} ${produktu(idx.length)}${capped}`;
  const base = location.pathname.replace(/page\/\d+\/$/, '');
  const qs = (extra: Record<string, string | null>) => {
    const q = new URLSearchParams(own);
    for (const [k, v] of Object.entries(extra)) { if (v === null) q.delete(k); else q.set(k, v); }
    const s = q.toString().replace(/%2C/g, ',');
    return base + (s ? '?' + s : '');
  };
  if (pages > 1) {
    const show = [...new Set([1, 2, 3, pages - 2, pages - 1, pages, page - 2, page - 1, page, page + 1, page + 2])].filter((x) => x >= 1 && x <= pages).sort((a, b) => a - b);
    let h = '', prev = 0;
    for (const x of show) {
      if (prev && x - prev > 1) h += '<li><span>…</span></li>';
      h += x === page ? `<li><span aria-current="page">${x}</span></li>` : `<li><a href="${esc(qs({ strana: x > 1 ? String(x) : null }))}" rel="nofollow">${x}</a></li>`;
      prev = x;
    }
    document.querySelector('.lv ul.g, .lv .prazdno')?.insertAdjacentHTML('afterend', `<nav class="str" aria-label="Stránkování"><ul>${h}</ul></nav>`);
  }
  // sort tabs keep the filters
  for (const a of document.querySelectorAll<HTMLAnchorElement>('.rz a')) {
    const k = new URL(a.href).searchParams.get('orderby') ?? 'pop';
    a.href = qs({ orderby: k === 'pop' ? null : k, strana: null });
    if (k === sort) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
  }
  // the form shows the state (the static HTML has every box empty) + chips to remove a filter
  const chips: Array<[string, string]> = [];
  for (const el of form.querySelectorAll<HTMLInputElement>('input[name]')) {
    const v = el.value, name = el.name;
    const on = name === 'znacka' ? brands.has(v) : name === 'obchod' ? shops.has(v) : name === 'skladem' ? stock : name === 'sleva' ? disc
      : name.startsWith('p_') ? !!want.get(name.slice(2))?.has(v) : false;
    if (el.type === 'checkbox' || el.type === 'radio') {
      el.checked = on;
      if (on && !at.fixed.has(name)) {
        const label = el.closest('label')?.querySelector('span')?.textContent ?? v;
        const rest = list(own.get(name)).filter((x) => x !== v);
        chips.push([label, qs({ [name]: rest.length ? rest.join(',') : null, strana: null })]);
      }
    }
  }
  const fMin = form.querySelector<HTMLInputElement>('[name=min_price]'), fMax = form.querySelector<HTMLInputElement>('[name=max_price]');
  if (fMin && min !== undefined) fMin.value = String(min);
  if (fMax && max !== undefined) fMax.value = String(max);
  if (min !== undefined || max !== undefined) chips.unshift([`Cena ${min !== undefined ? 'od ' + min.toLocaleString('cs-CZ') : ''} ${max !== undefined ? 'do ' + max.toLocaleString('cs-CZ') : ''} Kč`, qs({ min_price: null, max_price: null, strana: null })]);
  if (sort !== 'pop' && !form.querySelector('input[name=orderby]')) form.insertAdjacentHTML('afterbegin', `<input type="hidden" name="orderby" value="${esc(sort)}">`);
  document.querySelector('.lv ul.ch')?.remove();
  if (chips.length) {
    const plain = base + (own.get('orderby') ? `?orderby=${encodeURIComponent(own.get('orderby')!)}` : '');
    document.querySelector('.lv .lt')?.insertAdjacentHTML('afterend', `<ul class="ch" aria-label="Aktivní filtry">${chips.map(([t, u]) => `<li><a href="${esc(u)}" rel="nofollow">${esc(t)} ×</a></li>`).join('')}<li><a class="ch__x" href="${esc(plain)}" rel="nofollow">Zrušit filtry</a></li></ul>`);
    const fb = document.querySelector('[data-filtry]');
    if (fb && fb.lastChild?.nodeType === 3) fb.lastChild.textContent = `Filtry (${chips.length})`;
  }
}
