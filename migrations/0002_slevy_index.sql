-- /slevy/: every discounted product by discount; the partial index keeps the page cheap (no scan of the 300 000 products)
CREATE INDEX IF NOT EXISTS idx_products_slevy ON products (disc_pct DESC, id DESC) WHERE status = 'publish' AND in_stock = 1 AND disc_pct >= 10 AND disc_pct <= 85;
