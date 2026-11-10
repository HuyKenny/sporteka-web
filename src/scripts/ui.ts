// Small progressive enhancements (the site works without JS): mega menu, collapsed intro, mobile filters, filter
// auto-submit, gallery, sticky price bar, search suggestions (/api/suggest).
// (Document | HTMLElement roots; the Workers type library shadows the DOM ParentNode type)
type Root = { querySelector: Document['querySelector']; querySelectorAll: Document['querySelectorAll'] };
const $ = <T extends Element = HTMLElement>(s: string, r: Root = document) => r.querySelector<T>(s);
const $$ = <T extends Element = HTMLElement>(s: string, r: Root = document) => [...r.querySelectorAll<T>(s)];
const desktop = () => matchMedia('(min-width: 1000px)').matches;

// mega menu: close on the × (mobile), outside click and Escape; no page scroll behind the full-screen menu
const mm = $<HTMLDetailsElement>('.mm');
if (mm) {
  mm.addEventListener('toggle', () => document.body.classList.toggle('bez-scroll', mm.open && !matchMedia('(min-width: 900px)').matches));
  document.addEventListener('click', (e) => {
    const t = e.target as Element;
    if (t.closest('[data-zavrit]') || (mm.open && !t.closest('.mm'))) mm.open = false;
  });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') mm.open = false; });
  // the category tree is not in every page's HTML: fetched once from /kategorie/ on first open (hover/focus prefetch)
  const slot = $('[data-menu]', mm);
  let loading: Promise<void> | null = null;
  const load = () => loading ??= fetch(slot!.dataset.menu!).then((r) => r.text()).then((t) => {
    const tree = new DOMParser().parseFromString(t, 'text/html').querySelector('main .mm-strom');
    if (tree) slot!.replaceWith(tree);
  }).catch(() => { loading = null; });
  if (slot) {
    mm.addEventListener('toggle', () => { if (mm.open) void load(); });
    mm.querySelector('summary')?.addEventListener('pointerenter', () => void load(), { once: true });
  }
}

// category intro: three lines + "Více"
// (collapsed by the server only when the text is long — no layout reads on load)
for (const b of $$<HTMLButtonElement>('[data-vice]')) {
  const el = b.previousElementSibling;
  if (!el) continue;
  b.addEventListener('click', () => { const o = el.classList.toggle('je-zav'); b.textContent = o ? 'Zobrazit více' : 'Zobrazit méně'; b.setAttribute('aria-expanded', String(!o)); });
}

// filters: bottom sheet on mobile; values of one name joined by commas (?znacka=a,b); desktop submits on change
const fl = $<HTMLFormElement>('form.fl');
// the static export filters and sorts in the browser (./filtry.ts) — the server used to answer the query string
if (fl && document.documentElement.dataset.static === '1' && location.search) void import('./filtry').then((m) => m.run(fl));
if (fl) {
  const open = (o: boolean) => { fl.classList.toggle('je-otevreno', o); document.body.classList.toggle('bez-scroll', o); };
  $$('[data-filtry]').forEach((b) => b.addEventListener('click', () => open(true)));
  $$('[data-filtry-zavrit]', fl as unknown as Root).forEach((b) => b.addEventListener('click', () => open(false)));
  fl.addEventListener('submit', (e) => {
    e.preventDefault();
    const fd = new FormData(fl);
    const sp = new URLSearchParams();
    for (const [k, v] of fd.entries()) {
      const s = String(v).trim();
      if (!s) continue;
      sp.set(k, sp.has(k) ? sp.get(k) + ',' + s : s);
    }
    location.href = fl.action.split('?')[0] + (sp.toString() ? '?' + sp.toString().replace(/%2C/g, ',') : '');
  });
  fl.addEventListener('change', (e) => { if (desktop() && ['checkbox', 'radio'].includes((e.target as HTMLInputElement).type)) fl.requestSubmit(); });
}

// gallery thumbnails
const main = $<HTMLImageElement>('.ga__m img');
for (const b of $$<HTMLButtonElement>('.ga__t button')) {
  b.addEventListener('click', () => {
    if (!main) return;
    main.src = b.dataset.src!; main.srcset = b.dataset.srcset ?? '';
    $$('.ga__t button').forEach((x) => x.setAttribute('aria-current', String(x === b)));
  });
}

// sticky price bar once the main CTA scrolled away (mobile)
const bar = $('.lista'), cta = $('.pb__cta');
if (bar && cta && 'IntersectionObserver' in window) {
  new IntersectionObserver(([en]) => bar.classList.toggle('je-videt', !en!.isIntersecting && en!.boundingClientRect.top < 0)).observe(cta);
}

// search suggestions (the static export searches its JSON index in the browser: ./hledat.ts, loaded on first use)
const STATIC = document.documentElement.dataset.static === '1';
const SEARCH = STATIC ? '/hledat/' : '/';
if (STATIC && location.pathname === '/' && new URLSearchParams(location.search).has('s')) location.replace('/hledat/' + location.search);
if (STATIC && document.getElementById('hl')) void import('./hledat').then((m) => m.searchPage());
const esc = (s: string) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]!));
interface Sug { cats: Array<{ u: string; n: string; c: number }>; brands: Array<{ u: string; n: string; c: number }>; products: Array<{ u: string; n: string; p: string; i: string }> }
for (const input of $$<HTMLInputElement>('input[data-suggest]')) {
  const box = input.closest('.hs')?.querySelector<HTMLElement>('.hs__s');
  if (!box) continue;
  let timer = 0, seq = 0, idx = -1;
  const links = () => $$<HTMLAnchorElement>('a', box as unknown as Root);
  const hide = () => { box.hidden = true; idx = -1; };
  const render = (d: Sug, q: string) => {
    let h = '';
    if (d.cats.length) h += '<div class="hs__h">Kategorie</div>' + d.cats.map((c) => `<a href="${esc(c.u)}" role="option"><span>${esc(c.n)}</span><span class="hs__c">${c.c}</span></a>`).join('');
    if (d.brands.length) h += '<div class="hs__h">Značky</div>' + d.brands.map((c) => `<a href="${esc(c.u)}" role="option"><span>${esc(c.n)}</span><span class="hs__c">${c.c}</span></a>`).join('');
    if (d.products.length) h += '<div class="hs__h">Produkty</div>' + d.products.map((p) => `<a href="${esc(p.u)}" role="option">${p.i ? `<img src="${esc(p.i)}" alt="" width="40" height="40" loading="lazy">` : ''}<span>${esc(p.n)}</span><span class="hs__c">${esc(p.p)}</span></a>`).join('');
    if (!h) { hide(); return; }
    h += `<a href="${SEARCH}?s=${encodeURIComponent(q)}" role="option"><b>Všechny výsledky pro „${esc(q)}“</b></a>`;
    box.innerHTML = h; box.hidden = false; idx = -1;
  };
  input.addEventListener('input', () => {
    clearTimeout(timer);
    const q = input.value.trim();
    if (q.length < 2) { hide(); return; }
    timer = window.setTimeout(async () => {
      const my = ++seq;
      try {
        if (STATIC) {
          const d = await (await import('./hledat')).suggest(q);
          if (my === seq) render(d, q);
          return;
        }
        const r = await fetch('/api/suggest?q=' + encodeURIComponent(q));
        if (r.ok && my === seq) render(await r.json() as Sug, q);
      } catch { /* offline */ }
    }, 160);
  });
  input.addEventListener('keydown', (e) => {
    const l = links();
    if (box.hidden || !l.length) return;
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault();
      idx = (idx + (e.key === 'ArrowDown' ? 1 : -1) + l.length) % l.length;
      l.forEach((a, i) => a.setAttribute('aria-selected', String(i === idx)));
    } else if (e.key === 'Enter' && idx >= 0) { e.preventDefault(); location.href = l[idx]!.href; }
    else if (e.key === 'Escape') hide();
  });
  document.addEventListener('click', (e) => { if (!(e.target as Element).closest('.hs')) hide(); });
}

// Promile calculator of /alkohol-kalkulacka/ (WordPress mu-plugin ah_claude_promile_form, v2.0): the form is part of the
// article HTML, the calculation ran from a footer script. Widmark: r man 0.68 / woman 0.55, elimination 0.15 ‰ per hour.
(() => {
  const f = document.getElementById('ah-promile') as HTMLFormElement | null;
  const out = document.getElementById('ah-promile-out');
  if (!f || !out) return;
  f.removeAttribute('onsubmit');
  f.addEventListener('submit', (e) => e.preventDefault());
  const el = (n: string) => f.elements.namedItem(n) as HTMLInputElement | null;
  const num = (n: string) => { const v = parseFloat(String(el(n)?.value ?? '').replace(',', '.')); return Number.isFinite(v) && v > 0 ? v : 0; };
  const fmt = (x: number) => x.toFixed(2).replace('.', ',');
  const hrs = (x: number) => { let h = Math.floor(x), m = Math.round((x - h) * 60); if (m === 60) { h++; m = 0; } return h + ' h' + (m ? ' ' + m + ' min' : ''); };
  const calc = () => {
    const r = parseFloat((f.querySelector('input[name=sex]:checked') as HTMLInputElement | null)?.value ?? '0.68');
    const kg = num('kg') || 80;
    let g = 0;
    f.querySelectorAll<HTMLInputElement>('input[data-g]').forEach((i) => { g += num(i.name) * parseFloat(i.getAttribute('data-g') ?? '0'); });
    g += num('cml') * num('cpct') / 100 * 0.789;
    if (g <= 0) { out.className = 'ahp-out'; out.innerHTML = 'Zadejte, co jste vypili — výsledek se spočítá hned.'; return; }
    const peak = g / (kg * r), t = num('h'), now = Math.max(0, peak - 0.15 * t), left = Math.max(0, now / 0.15);
    const clock = new Date(Date.now() + left * 3600000).toLocaleString('cs-CZ', { weekday: 'long', hour: '2-digit', minute: '2-digit' });
    out.className = 'ahp-out ' + (now > 0 ? 'warn' : 'ok');
    out.innerHTML = 'Čistý alkohol: <b>' + Math.round(g) + ' g</b> · nejvyšší hladina cca <b>' + fmt(peak) + ' ‰</b>'
      + '<strong class="big">Teď máte cca ' + fmt(now) + ' ‰</strong>'
      + (now > 0 ? 'Na 0,00 ‰ budete zhruba za <b>' + hrs(left) + '</b> (kolem: ' + clock + '). Do té doby neřiďte.'
        : 'Podle výpočtu by alkohol měl být odbouraný. Odhad je ale jen orientační — pokud jste pili hodně nebo nedávno, raději ještě počkejte.');
  };
  f.addEventListener('input', calc);
  f.addEventListener('change', calc);
  calc();
})();

