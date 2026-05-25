# Aqua Cube — Shopify Theme

Liquid theme converted from the static `index.html` / `products.html` / `cart.html` site at the repo root. Drops into Shopify and uses the live product catalog (389 SKUs across 19 collections) from your CSV imports.

---

## What's inside

```
shopify-theme/
├── layout/theme.liquid              # main HTML shell (one place for <head>, header/footer groups)
├── templates/
│   ├── index.json                   # homepage (Hero + Trust bar + Featured + Categories + About + Newsletter + Contact)
│   ├── product.json                 # PDP
│   ├── collection.json              # collection listing
│   ├── list-collections.json        # /collections index
│   ├── cart.json                    # cart page
│   ├── search.json                  # search results
│   ├── page.json                    # generic CMS pages (About, Contact, etc.)
│   └── 404.liquid
├── sections/
│   ├── header.liquid + header-group.json   # inline search + cart + linklist menu
│   ├── footer.liquid + footer-group.json
│   ├── hero.liquid                          # heading + subheading + CTA (route picker) + image
│   ├── trust-bar.liquid                     # 4-up icon row (shipping/secure/expertise/returns)
│   ├── featured-collection.liquid
│   ├── categories.liquid                    # 4-up category grid with built-in SVG icons or custom images
│   ├── about.liquid                         # heading + stats blocks
│   ├── newsletter.liquid                    # email signup (Shopify customer form, tagged "newsletter")
│   ├── contact.liquid                       # Shopify {% form 'contact' %}
│   ├── main-product.liquid                  # PDP body + breadcrumbs + JSON-LD
│   ├── main-collection.liquid               # paginated product grid + sort + breadcrumbs
│   ├── main-list-collections.liquid
│   ├── main-cart.liquid                     # cart line items + Shopify checkout
│   ├── main-page.liquid
│   └── main-search.liquid
├── snippets/
│   ├── product-card.liquid
│   ├── breadcrumbs.liquid                   # auto-detects template context
│   ├── product-schema.liquid                # JSON-LD for SEO / rich results
│   ├── category-icon.liquid                 # dispatcher for built-in SVGs
│   ├── icon-aquariums.liquid                # original SVGs from static site
│   ├── icon-filters.liquid
│   ├── icon-lighting.liquid
│   └── icon-decorations.liquid
├── assets/
│   ├── style.css                    # original site CSS + Shopify-specific additions
│   ├── global.js                    # mobile menu + gallery thumb swap
│   ├── logo.svg
│   └── hero-aquarium.svg
├── config/
│   ├── settings_schema.json         # theme editor schema (colours, logo, social)
│   └── settings_data.json
└── locales/
    └── en.default.json
```

---

## How to install

### Option 1 — Zip upload (easiest, no CLI)
1. From the repo root: `cd shopify-theme && zip -r ../aqua-cube-theme.zip .`
2. Shopify admin → **Online Store → Themes → Add theme → Upload zip**
3. Click **Customize** to set colours / logo / menu
4. Click **Publish** when ready

### Option 2 — Shopify CLI (recommended for development)
```bash
npm install -g @shopify/cli @shopify/theme
cd shopify-theme
shopify theme dev --store aquacubesa.co.za     # live-reload preview
shopify theme push                              # upload as unpublished
shopify theme push --live                       # replace live theme (CAREFUL)
```

---

## After install — Shopify admin checklist

1. **Navigation** (Online Store → Navigation)
   - Create a `main-menu` linklist with: Home, Products (links to `/collections/all` or `/collections`), About (page), Contact (page)
   - Create a `footer` linklist with the same items

2. **Pages** (Online Store → Pages)
   - Create **About** page (URL handle `about`)
   - Create **Contact** page (URL handle `contact`)

3. **Collections** — these should already exist from your CSV imports:
   - tanks, filtration, lighting, decorations, etc.

4. **Theme settings** (Customize)
   - Upload logo + favicon
   - Set social URLs
   - Pick the homepage featured collection (e.g. "Featured" or "Lighting")

5. **Featured collection** — create a Shopify collection called "Featured" and tag your hero products with `featured` so they auto-populate, OR pick any existing collection.

---

## Notes / decisions

- **Categories section** on the homepage links to the `tanks`, `filtration`, `lighting`, `decorations` collections by default. The 4 inline SVG icons from the static site aren't included in defaults — upload your own icon images per category card in the theme editor, OR paste the original SVG markup into the `icon_svg` block setting.
- **Cart** uses Shopify's native cart form. "Checkout" submits to Shopify's hosted checkout (PayFast goes here once configured).
- **Pricing** is `Cost × 1.30` as established by the CSV import work — no theme code changes needed.
- **Contact form** uses Shopify's `{% form 'contact' %}` — submissions go to the store's owner email (set under Settings → General).
- **Search** is not wired up (no search-results template yet). Easy to add later.

---

## Local preview

Liquid can't render outside Shopify, so you can't view this in a browser as-is. Either:
- Use `shopify theme dev` (CLI) for live preview against a real store
- Upload as an unpublished theme and use **Customize → Preview**

The old static site (`/index.html` etc.) at the repo root still works as a design reference.
