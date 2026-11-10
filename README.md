# sporteka.cz

Srovnávač cen sportovního a outdoorového vybavení. Od 9. 11. 2026 **statický web**: ~820 tis. stránek ve Workerech
`sporteka-s00…s14` (jen statické soubory, bez skriptu), obrázky přes Worker `sporteka-img` (R2).

Celý týdenní cyklus běží v GitHub Actions (`.github/workflows/tyden.yml`):

| Krok | Co dělá | Skript |
|---|---|---|
| data | stáhne feedy obchodů (CJ, Decathlon, XML feedy, Allegro), postaví katalog a přírůstkově aktualizuje jeho kopii | `cj-stahni.py`, `decathlon-stahni.py`, `xml-feedy-stahni.py`, `cj-allegro.py`, `katalog.py build` + `update` |
| web | z kopie katalogu vykreslí změněné stránky (Astro SSR lokálně přes `wrangler dev`), nahraje je do shardů, ohlásí IndexNow a zkontroluje živý web | `staticky.py weekly`, `indexnow.py`, `staticky_audit.py` |

Pondělí = data + web, ostatní dny jen dokončení webu, když se předchozí běh nevešel do časového limitu.

**Bezpečnost (repo je veřejné):** klíče jsou jen v GitHub secrets a do kroků se předávají jako proměnné prostředí;
stav mezi běhy (kopie katalogu, stav nasazení, poslední feedy) je v release `state` zašifrovaný AES-256 (`scripts/state.sh`,
klíč `STATE_KEY`); každý běh pouští gitleaks nad historií a `scripts/verify_no_secrets.py`; workflow se spouští jen
plánem nebo ručně, nikdy z pull requestu.

Lokálně (vývoj šablon): `pnpm install`, `pnpm build`, náhled `pnpm preview`.
