# Maison Miette — storefront

A lightweight, static landing page for **Maison Miette**: one-of-one handmade couture for 11½″ fashion dolls. No build step — plain HTML, CSS and JavaScript.

## Structure

```
maison-miette/
├── index.html              # the page
├── css/style.css           # all styling
├── js/products-data.js     # the 6 pieces — edit prices, photos, links, sold-out here
├── js/app.js               # rendering + nav + form behaviour
└── images/products/        # drop product photos here (see below)
```

## Run it

It's static — just open `index.html` in a browser, or serve the folder:

```bash
cd maison-miette
python3 -m http.server 8000   # then visit http://localhost:8000
```

## Manage the shop

Everything you'll touch lives in **`js/products-data.js`**:

- **Add a photo** — drop a file into `images/products/` and point the piece's `image`
  field at it (e.g. `images/products/rosalind.jpg`). Until a photo exists, the card
  shows an elegant monogram placeholder automatically.
- **Mark a piece sold** — set `soldOut: true`. The card greys out and the button
  reads *Sold out*. (These are one-of-one, so this happens once per piece.)
- **Buy links** — each `url` opens the live Shopify product page. The handles are
  best-guesses; confirm each in Shopify admin (Products → a product → **View**) and
  update if it differs.

## Hosting

Drop the folder on any static host — GitHub Pages, Netlify, Vercel, Cloudflare Pages.
For GitHub Pages, point it at `/maison-miette/` (or move the contents to the repo root).
