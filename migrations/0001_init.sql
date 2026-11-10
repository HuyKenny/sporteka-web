-- sporteka.cz — initial schema (31. 10. 2026). Derived from apps/sporteka (eroka → sporteka lineage) without the
-- WordPress leftovers. The catalogue is built on the Pi (scripts/katalog.py keeps a local SQLite mirror and pushes only
-- changed rows); the web Worker only reads, except the click log.

-- every root URL /<slug>/: product, category or static page (facet landings live in facet_pages)
CREATE TABLE slugs (
  slug TEXT PRIMARY KEY,
  kind TEXT NOT NULL CHECK (kind IN ('product','category','post','page','postcat')),
  ref_id INTEGER NOT NULL
) STRICT, WITHOUT ROWID;

CREATE TABLE products (
  id INTEGER PRIMARY KEY,
  slug TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'publish',       -- publish | retired (no offer for 60 days → 301 to its category)
  short_html TEXT NOT NULL DEFAULT '',
  desc_html TEXT NOT NULL DEFAULT '',
  image TEXT NOT NULL DEFAULT '',
  images TEXT NOT NULL DEFAULT '',              -- JSON list of up to 5 gallery URLs (one shop's extra photos)
  ean TEXT NOT NULL DEFAULT '',
  primary_cat INTEGER NOT NULL DEFAULT 0,
  brand_id INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  noindex INTEGER NOT NULL DEFAULT 0,
  seo_title TEXT NOT NULL DEFAULT '',
  seo_desc TEXT NOT NULL DEFAULT '',
  source TEXT NOT NULL DEFAULT '',              -- cj:<advertiserId> of the shop the product was created from
  -- denormalised from active offers (katalog.py)
  min_price REAL NOT NULL DEFAULT 0,
  max_price REAL NOT NULL DEFAULT 0,
  offer_count INTEGER NOT NULL DEFAULT 0,
  shop_count INTEGER NOT NULL DEFAULT 0,
  best_offer_id INTEGER NOT NULL DEFAULT 0,
  best_domain TEXT NOT NULL DEFAULT '',
  disc_pct INTEGER NOT NULL DEFAULT 0,
  in_stock INTEGER NOT NULL DEFAULT 0,
  pop INTEGER NOT NULL DEFAULT 0,
  last_offer_at TEXT NOT NULL DEFAULT ''
) STRICT;
CREATE INDEX idx_products_ean ON products(ean) WHERE ean <> '';
CREATE INDEX idx_products_pop ON products(status, pop DESC);

-- category membership copied to every ancestor (a listing = one index range); sort keys duplicated from products
CREATE TABLE cat_products (
  cat_id INTEGER NOT NULL,
  created_at TEXT NOT NULL,
  product_id INTEGER NOT NULL,
  direct INTEGER NOT NULL DEFAULT 0,            -- 1 main category, 0 ancestor
  min_price REAL NOT NULL DEFAULT 0,
  pop INTEGER NOT NULL DEFAULT 0,
  disc INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (cat_id, created_at, product_id)
) STRICT, WITHOUT ROWID;
CREATE INDEX idx_cat_products_product ON cat_products(product_id);
CREATE INDEX idx_cp_price ON cat_products(cat_id, min_price);
CREATE INDEX idx_cp_pop ON cat_products(cat_id, pop DESC);
CREATE INDEX idx_cp_disc ON cat_products(cat_id, disc DESC, pop DESC);

CREATE TABLE brand_products (
  brand_id INTEGER NOT NULL,
  created_at TEXT NOT NULL,
  product_id INTEGER NOT NULL,
  PRIMARY KEY (brand_id, created_at, product_id)
) STRICT, WITHOUT ROWID;
CREATE INDEX idx_brand_products_product ON brand_products(product_id);

CREATE TABLE categories (
  id INTEGER PRIMARY KEY,
  slug TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  parent INTEGER NOT NULL DEFAULT 0,
  description_html TEXT NOT NULL DEFAULT '',
  second_html TEXT NOT NULL DEFAULT '',
  guide_html TEXT NOT NULL DEFAULT '',
  faq_json TEXT NOT NULL DEFAULT '',
  menu_order INTEGER NOT NULL DEFAULT 0,
  count_direct INTEGER NOT NULL DEFAULT 0,
  count_total INTEGER NOT NULL DEFAULT 0,
  noindex INTEGER NOT NULL DEFAULT 0,
  seo_title TEXT NOT NULL DEFAULT '',
  seo_desc TEXT NOT NULL DEFAULT '',
  seo_robots TEXT NOT NULL DEFAULT ''
) STRICT;
CREATE INDEX idx_categories_parent ON categories(parent);

CREATE TABLE brands (
  id INTEGER PRIMARY KEY,
  slug TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  description_html TEXT NOT NULL DEFAULT '',
  second_html TEXT NOT NULL DEFAULT '',
  faq_json TEXT NOT NULL DEFAULT '',
  seo_title TEXT NOT NULL DEFAULT '',
  seo_desc TEXT NOT NULL DEFAULT '',
  count INTEGER NOT NULL DEFAULT 0,
  noindex INTEGER NOT NULL DEFAULT 0
) STRICT;

-- one row per shop and product; size/colour variants of the shop are folded into it (sizes = JSON list in stock)
CREATE TABLE offers (
  id INTEGER PRIMARY KEY,
  product_id INTEGER NOT NULL,
  feed TEXT NOT NULL,                  -- cj:<advertiserId>
  unique_id TEXT NOT NULL,             -- item group id in the shop's feed
  title TEXT NOT NULL DEFAULT '',
  domain TEXT NOT NULL DEFAULT '',
  price REAL NOT NULL DEFAULT 0,
  price_old REAL NOT NULL DEFAULT 0,
  currency TEXT NOT NULL DEFAULT 'CZK',
  target_url TEXT NOT NULL,            -- final affiliate URL, returned byte for byte by /go/
  orig_url TEXT NOT NULL DEFAULT '',
  stock INTEGER NOT NULL DEFAULT 1,    -- 1 in stock, 0 unknown, -1 out of stock
  ean TEXT NOT NULL DEFAULT '',
  img TEXT NOT NULL DEFAULT '',
  sizes TEXT NOT NULL DEFAULT '',      -- JSON list of sizes in stock
  variants INTEGER NOT NULL DEFAULT 1,
  delivery_price REAL,
  extra TEXT NOT NULL DEFAULT '',
  go_slug TEXT,
  updated_at TEXT NOT NULL,
  active INTEGER NOT NULL DEFAULT 1,
  content_hash TEXT NOT NULL DEFAULT ''
) STRICT;
CREATE INDEX idx_offers_product ON offers(product_id, active, price);
CREATE UNIQUE INDEX idx_offers_key ON offers(feed, unique_id);
CREATE UNIQUE INDEX idx_offers_go ON offers(go_slug) WHERE go_slug IS NOT NULL;

CREATE TABLE product_params (
  product_id INTEGER NOT NULL,
  key TEXT NOT NULL,
  value TEXT NOT NULL,
  PRIMARY KEY (product_id, key, value)
) STRICT, WITHOUT ROWID;
CREATE INDEX idx_pp_kv ON product_params(key, value, product_id);

CREATE TABLE product_keys (
  key TEXT PRIMARY KEY,
  product_id INTEGER NOT NULL
) STRICT, WITHOUT ROWID;
CREATE INDEX idx_product_keys_product ON product_keys(product_id);

CREATE TABLE price_history (
  product_id INTEGER NOT NULL,
  day TEXT NOT NULL,
  min_price REAL NOT NULL,
  PRIMARY KEY (product_id, day)
) STRICT, WITHOUT ROWID;

-- static pages (o-nas, podminky …) and later the guides; same shape as eroka/sporteka
CREATE TABLE posts (
  id INTEGER PRIMARY KEY,
  type TEXT NOT NULL CHECK (type IN ('post','page')),
  slug TEXT NOT NULL,
  title TEXT NOT NULL,
  content_html TEXT NOT NULL DEFAULT '',
  excerpt TEXT NOT NULL DEFAULT '',
  published_at TEXT NOT NULL,
  modified_at TEXT NOT NULL,
  cat_id INTEGER NOT NULL DEFAULT 0,
  image TEXT NOT NULL DEFAULT '',
  image_card TEXT NOT NULL DEFAULT '',
  image_alt TEXT NOT NULL DEFAULT '',
  image_w INTEGER NOT NULL DEFAULT 0,
  image_h INTEGER NOT NULL DEFAULT 0,
  author TEXT NOT NULL DEFAULT '',
  noindex INTEGER NOT NULL DEFAULT 0,
  seo_title TEXT NOT NULL DEFAULT '',
  seo_desc TEXT NOT NULL DEFAULT '',
  seo_robots TEXT NOT NULL DEFAULT '',
  ld_json TEXT NOT NULL DEFAULT '',
  status TEXT NOT NULL DEFAULT 'publish',
  UNIQUE (type, slug)
) STRICT;
CREATE INDEX idx_posts_type_date ON posts(type, status, published_at DESC);
CREATE TABLE post_categories (
  id INTEGER PRIMARY KEY,
  slug TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  description TEXT NOT NULL DEFAULT '',
  count INTEGER NOT NULL DEFAULT 0
) STRICT;

CREATE TABLE facet_pages (
  id INTEGER PRIMARY KEY,
  slug TEXT NOT NULL UNIQUE,
  base_slug TEXT NOT NULL,
  qs TEXT NOT NULL,
  h1 TEXT NOT NULL,
  seo_title TEXT NOT NULL,
  seo_desc TEXT NOT NULL,
  intro_html TEXT NOT NULL DEFAULT '',
  second_html TEXT NOT NULL DEFAULT '',
  faq_json TEXT NOT NULL DEFAULT '',
  keyword TEXT NOT NULL DEFAULT '',
  volume INTEGER NOT NULL DEFAULT 0,
  min_products INTEGER NOT NULL DEFAULT 5,
  total INTEGER NOT NULL DEFAULT 0,
  noindex INTEGER NOT NULL DEFAULT 0,
  updated_at TEXT NOT NULL DEFAULT ''
) STRICT;
CREATE INDEX facet_pages_base ON facet_pages (base_slug);

CREATE TABLE redirects (
  from_path TEXT PRIMARY KEY,
  to_path TEXT NOT NULL,
  status INTEGER NOT NULL DEFAULT 301
) STRICT, WITHOUT ROWID;

CREATE TABLE clicks (
  id INTEGER PRIMARY KEY,
  offer_id INTEGER NOT NULL,
  product_id INTEGER NOT NULL,
  domain TEXT NOT NULL,
  context TEXT NOT NULL DEFAULT 'go',
  ip_hash TEXT NOT NULL DEFAULT '',
  clicked_at TEXT NOT NULL
) STRICT;
CREATE INDEX idx_clicks_time ON clicks(clicked_at);

CREATE TABLE site_cache (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL,
  updated_at TEXT NOT NULL
) STRICT, WITHOUT ROWID;

-- contentless_delete: katalog.py removes a product by rowid without knowing its old text
CREATE VIRTUAL TABLE product_fts USING fts5(name, brand, content='', contentless_delete=1, tokenize = 'unicode61 remove_diacritics 2');
