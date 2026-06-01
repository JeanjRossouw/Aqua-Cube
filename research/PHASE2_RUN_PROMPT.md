# Phase 2 — Run Prompt (paste into the enrichment session)

> Goal: replace boilerplate descriptions + add carousel images on Aquacube
> (`aquacube-6`). ~1,006 active products. Full plan: `research/CATALOG_ENRICHMENT_PLAN.md`.

---

**Phase 2 — Enrich Aqua Cube products.**

Guardrails first: confirm the connected store is **Aquacube** via `get-shop-info`
before ANY write. Never call `switch-shop`. Validate every GraphQL mutation before
executing. Work in batches.

**Step 1 — establish a data source, in this order. Do NOT assume web access works.**
1. Local file: check `data/suppliers/*.csv` / `*.json` in the repo. If present, use it —
   no network needed.
2. Else try web: `curl https://www.akwa.co.za/products.json?limit=1` (akwa = distributor
   carrying all brands). Expect JSON.
3. Else per-brand sites: chihiros.com, zetlight.com, tropica.com, dennerle.com,
   hikariusa.com, ntlabs.co.uk, bubble-magus.net, maxspect.com, mydymax.com
4. If every external fetch returns `Host not in allowlist` or 403/404 → **STOP, tell the
   user, and use the data-file path (option 1).** Do not fabricate data.

**Step 2 — enrich.**
- Match supplier products → ours by **SKU → barcode → normalized title**.
- Bulk-replace `descriptionHtml` with real specs.
- Add extra images via `productCreateMedia` using public image URLs. NOTE: Shopify fetches
  these server-side, so this works even if the session can't reach the host — a public URL
  (e.g. cdn.shopify.com) is all that's needed.
- Prioritize branded lines: Hikari, Dophin, Dymax, Chihiros, Zetlight, Tropica, Dennerle,
  NT Labs, Bubble-Magus, Maxspect, Bioloark.
- Leave `vendor:"Aqua Cube"` rebadged R0.00 duplicates (no real tags) for separate cleanup.

**Step 3 — report.** Per batch: counts matched / updated / skipped, plus a sample to eyeball.

---

## If configuring an allowlisted environment, these are the hosts
```
www.akwa.co.za  akwa.co.za  cdn.shopify.com
chihiros.com  chihirosaquaticstudio.com  zetlight.com  tropica.com
dennerle.com  hikariusa.com  ntlabs.co.uk  bubble-magus.net  maxspect.com  mydymax.com
```

## Known gotcha (verified)
akwa.co.za 403s bots and its `/products.json` 404s. If web access is configured but still
blocked, fall back to the data-file path — that needs no network at all.

## Brand source sites (for reference / manual lookup — emails NOT verified)
Get contact emails from each brand's own contact page; do not trust any pre-filled list.
Chihiros · Zetlight · Tropica · Dennerle · Hikari · NT Labs · Bubble-Magus · Maxspect · Dymax
