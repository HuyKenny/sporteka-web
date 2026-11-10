// Search of the static export (no server): /_s/n.json = category + brand names, /_s/t/<2 letters>.json = known words
// with that start ([word, products], most frequent first), /_s/w/<word>.json = the 48 most popular products whose name
// has the word (cards, see src/pages/api/static-cards.ts). Words are folded like the index (scripts/staticky.py fold()).
export type Card = [number, string, string, string, string, number, number, number];
type Name = [string, string, number];

export const fold = (t: string) => t.normalize('NFKD').replace(/[̀-ͯ]/g, '').toLowerCase();
export const words = (q: string) => fold(q).split(/[^a-z0-9]+/).filter((w) => w.length > 1).slice(0, 5);

const memo = new Map<string, Promise<unknown>>();
function get<T>(u: string): Promise<T | null> {
  if (!memo.has(u)) memo.set(u, fetch(u).then((r) => (r.ok ? r.json() : null)).catch(() => null));
  return memo.get(u) as Promise<T | null>;
}

/** Index words for one typed word: the word itself when known, plus (while typing) the most frequent continuations. */
async function tokens(w: string, typing: boolean): Promise<string[]> {
  const list = (await get<Array<[string, number]>>(`/_s/t/${w.slice(0, 2)}.json`)) ?? [];
  const exact = list.some(([t]) => t === w);
  const more = list.filter(([t]) => t !== w && t.startsWith(w)).map(([t]) => t);
  return exact ? [w, ...(typing ? more.slice(0, 2) : [])] : more.slice(0, typing ? 3 : 2);
}

export async function search(q: string, typing: boolean, limit: number) {
  const ws = words(q);
  if (!ws.length) return { ws, cats: [] as Name[], brands: [] as Name[], items: [] as Card[] };
  const namesP = get<{ c: Name[]; b: Name[] }>('/_s/n.json');
  const toks = (await Promise.all(ws.map((w, i) => tokens(w, typing && i === ws.length - 1)))).flat();
  const lists = await Promise.all([...new Set(toks)].map((t) => get<Card[]>(`/_s/w/${t}.json`)));
  // union in popularity order, then keep the cards whose name has the most typed words
  const seen = new Map<number, { c: Card; rank: number; hits: number }>();
  for (const l of lists) (l ?? []).forEach((c, i) => {
    const prev = seen.get(c[0]);
    if (prev) { prev.rank = Math.min(prev.rank, i); return; }
    const n = fold(c[2]);
    seen.set(c[0], { c, rank: i, hits: ws.filter((w) => n.includes(w)).length });
  });
  const all = [...seen.values()];
  const best = Math.max(0, ...all.map((x) => x.hits));
  const items = all.filter((x) => x.hits === best && best > 0).sort((a, b) => a.rank - b.rank).slice(0, limit).map((x) => x.c);
  const names = (await namesP) ?? { c: [], b: [] };
  const hit = (n: string) => { const f = fold(n); return ws.every((w) => f.includes(w)); };
  return { ws, cats: names.c.filter((x) => hit(x[1])), brands: names.b.filter((x) => hit(x[1])), items };
}

export const esc = (s: string) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]!));
const cislo = (n: number) => n.toLocaleString('cs-CZ');

/** Product card like src/components/Karta.astro (links to the product page; the shop link lives there). */
export function card(c: Card, i: number): string {
  const [, slug, name, price, img, shops, disc, stock] = c;
  const href = `/${encodeURIComponent(slug)}/`;
  return `<li><article class="k"><div class="k__img">${img ? `<img src="${esc(img)}" alt="${esc(name)}" width="240" height="240" loading="${i < 4 ? 'eager' : 'lazy'}" decoding="async">` : ''}`
    + `${disc >= 10 ? `<span class="k__s">−${disc} %</span>` : ''}</div><h3 class="k__n"><a href="${href}">${esc(name)}</a></h3>`
    + (price ? `<p class="k__p num"><span>${esc(price)}</span></p><p class="k__m"><span class="${stock ? 'dot' : 'dot dot--no'}"></span>${shops > 1 ? `v ${shops} obchodech` : 'v 1 obchodě'}</p>` : '<p class="k__m">Teď není v nabídce</p>')
    + `<a class="btn ${shops > 1 ? 'btn--o' : 'btn--g'} k__b" href="${href}" tabindex="-1">${shops > 1 ? 'Porovnat ceny' : 'Zobrazit'}</a></article></li>`;
}

/** /hledat/?s= */
export async function searchPage(): Promise<void> {
  const box = document.getElementById('hl');
  if (!box) return;
  const q = (new URLSearchParams(location.search).get('s') ?? '').trim().slice(0, 100);
  const input = document.querySelector<HTMLInputElement>('#hs-q');
  if (input && q) input.value = q;
  if (!q) return;
  document.title = `Hledání: ${q} | Sporteka`;
  document.getElementById('hl-h')!.textContent = `Výsledky hledání: ${q}`;
  box.innerHTML = '<p class="prazdno">Hledám…</p>';
  const r = await search(q, false, 48);
  const pk = document.getElementById('hl-pk')!;
  const tiles = [...r.cats.slice(0, 6).map(([u, n, c]) => `<li><a href="${esc(u)}"><span>${esc(n)} <small>${cislo(c)}</small></span></a></li>`),
    ...r.brands.slice(0, 6).map(([u, n, c]) => `<li><a href="${esc(u)}"><span>Značka ${esc(n)} <small>${cislo(c)}</small></span></a></li>`)];
  pk.innerHTML = tiles.join('');
  pk.hidden = !tiles.length;
  if (r.items.length) document.getElementById('hl-n')!.textContent = `${r.items.length >= 48 ? 'nejoblíbenějších ' : ''}${r.items.length} produktů`;
  box.innerHTML = r.items.length ? `<ul class="g">${r.items.map(card).join('')}</ul>`
    : `<p class="prazdno">${tiles.length ? 'Produkty podle názvu jsme nenašli, zkuste kategorii nebo značku nahoře.' : 'Nic jsme nenašli. Zkuste jiné slovo nebo vyberte kategorii v menu.'}</p>`;
}

/** Header suggestions in the shape of /api/suggest. */
export async function suggest(q: string) {
  const r = await search(q, true, 6);
  return {
    cats: r.cats.slice(0, 4).map(([u, n, c]) => ({ u, n, c })),
    brands: r.brands.slice(0, 3).map(([u, n, c]) => ({ u, n, c })),
    products: r.items.map((c) => ({ u: `/${c[1]}/`, n: c[2], p: c[3], i: c[4] })),
  };
}
