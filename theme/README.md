# Maison Miette — Shopify theme (Online Store 2.0)

A custom, editorial OS 2.0 theme for **Maison Miette** — one-of-one handmade couture for fashion dolls. Built from scratch (no Dawn fork). Editorial, minimal, cream/blush palette, hairline borders, **no drop shadows**, generous whitespace.

> **Status: scaffold.** This is a faithful first pass built from the brand brief. The exact design tokens (the canonical `<style>` values in the prototype `README.md`) still need to be dropped in — see **Tuning to spec** below.

## Structure

```
layout/theme.liquid          <head>, fonts, CSS-variable tokens from settings, header/footer
sections/
  header.liquid              wordmark (theme setting) + menu + cart
  footer.liquid              block-based: brand / menu / newsletter / text
  hero.liquid                homepage hero
  meta-strip.liquid          hairline-divided marquee of short phrases
  atelier-intro.liquid       editorial intro prose
  collection-grid.liquid     featured collection on the homepage
  statement-band.liquid      blush quote band
  main-collection.liquid     shop page: category filter chips + grid + Sold state
  main-product.liquid        product: two-column gallery + reorderable info blocks
  spec list / price / buy    (blocks inside main-product)
  ethos-band.liquid          dark "why one of one" band (shared)
  more-from-atelier.liquid    related pieces on the product page
  main-cart / main-page / main-404
snippets/product-card.liquid  the reusable "1 of 1" card (Sold state)
templates/*.json             index, collection, product, cart, page, 404
config/settings_schema.json   Brand (wordmark), Colours, Layout
locales/en.default.json
assets/base.css, theme.js
```

## Run it

Requires the [Shopify CLI](https://shopify.dev/docs/themes/tools/cli):

```bash
cd theme
shopify theme dev --store yixwg3-3d.myshopify.com
```

This hot-reloads against your store's real products/collections. Or `shopify theme push --unpublished` to upload it as a draft theme you can preview from the admin.

## Key settings

- **Wordmark** — *Theme settings → Brand → Wordmark.* The displayed name (default `MIETTE`) is a single swappable setting, in both header and footer. The name isn't final by design.
- **Colours** — *Theme settings → Colours.* Every token (background, ink, blush, accent, hairline) is a setting and feeds the CSS variables in `theme.liquid`.
- Every section is configurable and reorderable in the theme editor (sections + blocks).

## Content hooks the theme expects

- **Style line** on cards / product page comes from a product metafield **`custom.style`** (text). If absent, it falls back to the product's first tag. Define it as a Shopify metafield to control it cleanly.
- **Sold out** is automatic: a product with 0 inventory and "deny when out of stock" shows the `Sold` state and a disabled buy button. (Your 6 pieces are already set up this way.)
- **Filter chips** on the shop page are built from product **type**. Set each product's *Type* (e.g. *Gown*, *Set*, *Dress*) to populate them.

## Tuning to spec

When you have the prototype `README.md` + `homepage.html / shop.html / product.html`:
1. Replace the colour defaults in `config/settings_schema.json` + `config/settings_data.json` with the canonical hex tokens.
2. Reconcile type scale / spacing in `assets/base.css` against the prototype `<style>` blocks.
3. Swap the Google Fonts link in `layout/theme.liquid` if the prototype uses different families.
4. Drop the studio photos onto the products (or as section images) in admin.

Nothing in the layout assumes specific token values — they all flow from settings/variables, so tuning is low-risk.
