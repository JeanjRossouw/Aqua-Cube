# Supplier data drop-zone

Put supplier catalog exports here and the Phase 2 session will read them
locally — no network access required.

## Accepted
- Shopify CSV export (Products → Export → CSV) — e.g. `akwa-products.csv`
- products.json saved from a logged-in browser — e.g. `akwa-products.json`
- Any spec sheet / price list (CSV/XLSX/JSON) with at least: SKU or title, description,
  and image URL(s).

## Why this works without network
Shopify imports product images **server-side from a URL**. So even though the build
sandbox can't browse the web, as long as a row gives a public image URL
(e.g. an https://cdn.shopify.com/... link), carousels can still be built.

## Naming
`‹brand›-products.csv` / `‹brand›-products.json` (e.g. `dymax-products.csv`).
