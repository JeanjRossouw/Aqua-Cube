# Aqua Cube — Full Catalog Enrichment & Navigation Plan

**Store:** Aquacube (`aquacube-6.myshopify.com` / `r6cvc5-bk.myshopify.com`)
**Prepared:** 2026-06-01
**Status:** Plan approved (full catalog). Execution pending network-enabled environment.

---

## 1. Goal (what the user asked for)

1. **Fix vague/wrong product info** — current descriptions are auto-generated boilerplate
   and in places factually wrong. Replace with precise, accurate descriptions sourced from
   the supplier/manufacturer.
2. **Carousels** — add multiple images per product (currently 1 image each).
3. **Category → supplier dropdowns** — e.g. *Lights ▸ Chihiros / Zetlight / Dophin / …*
   so customers can browse by what they're actually looking for.

---

## 2. Catalog snapshot (live counts, 2026-06-01)

- **3,238 products** total — **1,006 active**, **1,902 draft**, **330 archived**
- **27 vendors**, **70 product types**, ~250 `Collection: *` tags already in place

### Products per vendor

| Vendor | Count | | Vendor | Count |
|---|--:|---|---|--:|
| Aqua Cube (house/akwa) | 2,587 | | Dennerle | 24 |
| Hikari | 93 | | Isopods/Sun Sun | 20 |
| Dophin | 88 | | Kaiser Aquatics | 17 |
| Dymax | 86 | | Waterlife | 16 |
| Sobo | 58 | | Grech | 12 |
| Tropica | 58 | | Bioloark | 11 |
| NT Labs | 34 | | Maxspect | 11 |
| Bubble-Magus | 27 | | ADA | 9 |
| Chihiros | 26 | | Aquapro | 9 |
| Sun Sun | 20 | | Zetlight | 9 |
| Hygger | 8 | | Voonline | 8 |
| Antopie | 6 | | Resun | 6 |
| Deebow | 5 | | JBL | 2 |
| Qanvee | 7 | | Aim | 1 |

> **Note:** "Aqua Cube" vendor (2,587) is the house label covering most rebadged stock.
> Real enrichment value is concentrated in the **branded** lines (Hikari, Dophin, Dymax,
> Chihiros, Zetlight, Tropica, Dennerle, NT Labs, Bubble-Magus, Maxspect, Bioloark…).

### Products per category (by `Collection:` tag)

| Category | Count | Category | Count |
|---|--:|---|--:|
| Filtration | 544 | Water Treatment | 101 |
| Plants | 274 | Accessories | 95 |
| Fish Food | 257 | Paludariums | 71 |
| Lighting | 250 | CO₂ / Dosing | 66 |
| Maintenance | 161 | Heaters | 64 |
| Hardscape | 142 | Decorations | 58 |
| Pumps & Flow | 137 | Substrate | 21 |
| Aquariums | 125 | Isopods | 21 |
| | | Protein Skimmers | 21 |

---

## 3. Known data-quality bugs (fixable WITHOUT external access)

These are wrong in the current data and can be corrected immediately from internal logic:

1. **Mis-typed Hikari foods** — multiple Hikari **fish foods** have
   `productType = "Aquatic Plant"` and a description reading
   *"…is a live aquatic plant ready to bring colour, oxygen and natural cover…"*
   → Should be `Fish Food`. Affects a chunk of the 93 Hikari items.
2. **Boilerplate everywhere** — virtually all active products share one of two template
   blurbs ("part of the Aqua Cube range…" / "live aquatic plant…") with no real specs.
3. **Single image** — every product has exactly 1 image; carousels need 2+.

**Phase 0 quick win:** sweep for products whose description contains the "live aquatic
plant" template but whose vendor/type indicates food/equipment, and re-type + neutralize
the false text. (Doesn't need supplier data — just stops actively wrong claims.)

---

## 4. THE BLOCKER — supplier data access

The core mechanism (copy real descriptions + extra photos from Akwa / Zetlight / Chihiros)
**cannot run in the current environment.** Verified 2026-06-01:

- `akwa.co.za` → **HTTP 403 Forbidden** (bot-blocked)
- any other external host → **"Host not in allowlist"** (network policy blocks outbound web)

### Resolution (user chose: "Open network access")
Recreate the Claude-on-web environment with a network policy that **allowlists the supplier
domains**. Confirmed with user (2026-06-01): supplier sites are **public retail sites — no
login required**, so once the domains are reachable, data can be pulled directly.

**Primary target — `akwa.co.za`:** Akwa is Aqua Cube's **distributor** and carries all the
resold brands (Chihiros, Zetlight, Dophin, Dymax, etc.) in ONE Shopify catalog. So
`akwa.co.za/products.json?limit=250&page=N` is the single highest-value source — full
descriptions + every image URL for most of our catalog in one feed. **Allowlist this first.**

**Secondary (richer specs on premium lines):**
- `chihiros.com` / `chihirosaquaticstudio.com` (Chihiros = "Shaquero")
- `zetlight.com` (Zetlight = "Z Lite")
- `tropica.com`, `dennerle.com`, `hikariusa.com`, `nt-labs.co.uk`,
  `bubblemagus.com`, `maxspect.com`, `dymax.com`

**Why this unlocks scale:** Shopify stores expose `/products.json?limit=250&page=N` returning
**full descriptions + every image URL** as JSON — enrichment becomes a deterministic
SKU/title map, not manual copy-paste. (akwa.co.za confirmed Shopify-based.)

**First action in next session:** verify with `https://akwa.co.za/products.json?limit=1`.
If it returns JSON (not 403), network is open — proceed to Phase 2.

### Terminology confirmed with user
- **"Z Lite" = Zetlight** ✓ (vendor in catalog) — public site
- **"Shaquero" = Chihiros** ✓ (vendor in catalog) — public site
- All supplier sites are **public** (no dealer login needed)

---

## 5. Navigation redesign — Category → Supplier dropdowns

### Current main menu (flat, mostly pointing at bare `/collections`)
Home · Contact · Pumps & Flow · Lighting & CO2 · Filtration & Accessories ·
Decorations & Ornaments · Hardscape Decorations · DR Tank & Fertilizers ·
Voonline & Crash · Akwa Products · **Dymax** (added this session)

> Several items are mislabeled/placeholder ("Voonline & Crash", "DR Tank") and link to the
> generic `/collections` page rather than a real collection.

### Target structure (top categories, each with supplier sub-items)

```
LIGHTS ▾            FILTRATION ▾         PUMPS & FLOW ▾       CO2 & DOSING ▾
  Chihiros            Dophin               Sobo                 Dymax
  Zetlight            Sobo                 Dophin               Qanvee
  Dophin              Grech                Bubble-Magus         Bubble-Magus
  Dymax               Sun Sun              Maxspect             (Regulators/Diffusers
  Aim                 Qanvee               Resun                 as sub-groups)
  Bioloark            Bubble-Magus       
  Maxspect          
  (by water type:    AQUARIUMS ▾          PLANTS ▾             FISH FOOD ▾
   Freshwater/         Dymax                Tropica              Hikari
   Marine/Plant/       Resun                Dennerle             (by type:
   Terrarium)          (by size)            ADA                   pellets/flakes/
                                            (Live/Artificial)     frozen)

WATER CARE ▾         HARDSCAPE & DECOR ▾   MAINTENANCE ▾
  NT Labs              (Natural/Artificial)  (Tools/Media/Nets)
  Waterlife            ADA
  JBL                  Kaiser Aquatics
```

### Mechanism
- **Per-supplier sub-collections** as smart collections, rule = `TAG EQUALS
  "Collection: ‹Category›"` **AND** `VENDOR EQUALS "‹Supplier›"` (AND logic).
- Many supplier-light tags **already exist** (`Collection: Chihiros Lights`,
  `Collection: Zetlight Lights`, `Collection: Dophin Lights`, `Collection: Bioloark
  Lights`, `Collection: Aim Lights`, `Collection: Fullgain Lights`, `Collection: Ocean Max
  Lights`) — so the Lights dropdown can be built from existing data on day one.
- Build menu via `menuUpdate` (proven this session — preserves existing items, append-safe).

### Existing lighting collections (already live)
| Collection | Handle | Products |
|---|---|--:|
| Lighting (all) | `lighting` | 250 |
| Freshwater Lights | `lighting-freshwater` | 208 |
| Plant Lights | `lighting-plant` | 15 |
| Marine Lights | `lighting-marine` | 13 |
| Terrarium Lights | `lighting-terrarium` | 5 |
| Light Accessories | `lighting-accessories` | 4 |

Missing: **per-supplier** light collections (Chihiros, Zetlight, Dophin, …) — to create.

---

## 6. Execution phases

### Phase 0 — Internal fixes (no network needed)
- [x] **Fix mis-typed Hikari foods (Aquatic Plant → Fish Food)** — 14 products retyped
      2026-06-01 (Carnivor, Shrimp Cuisine, Algae Wafers, Food Sticks, Carnisticks, etc.)
- [ ] Strip false "live aquatic plant" sentence from those 14 (full food copy = Phase 2)
- [ ] Audit other vendor/type mismatches via ShopifyQL/GraphQL
      (15 total non-plant vendors were Plant-typed; 14 were Hikari, now fixed)
- [ ] Clean junk titles (e.g. "…- 1Kg R1,937.24 Retail Price Incl.: R1,937.25",
      trailing barcodes like "04205521102") — affects several Hikari + others
- [ ] Normalize obviously-wrong boilerplate where vendor/type contradicts it

### Phase 1 — Navigation (no network needed)
- [x] **Create per-supplier Lights sub-collections** (2026-06-01) — 8 smart collections:
      Chihiros (20) `chihiros-lights`, Dophin (17) `dophin-lights`,
      Zetlight (10) `zetlight-lights`, Bioloark (10) `bioloark-lights`,
      Ocean Max (7) `ocean-max-lights`, Aim (2) `aim-lights`,
      Fullgain (2) `fullgain-lights`, Akwa (2) `akwa-lights`
- [x] **Build LIGHTS ▾ dropdown** (2026-06-01) — replaced broken "Lighting & CO2"
      placeholder (was → bare `/collections`) with **Lights** → `/collections/lighting`,
      13 nested sub-items (8 suppliers + Freshwater/Plant/Marine/Terrarium/Accessories).
      Parent menu item id `780547588169`.
- [ ] Roll out remaining category dropdowns (Filtration, Pumps, CO2, Plants, Food, …)
- [ ] Clean up remaining mislabeled legacy menu items ("Voonline & Crash", "DR Tank
      & Fertilizers", "Decorations & Ornaments", etc. — all still → bare `/collections`)

**Lights dropdown is the proven pattern** — replicate for other categories:
1. confirm/create per-supplier smart collections (rule: TAG = "Collection: ‹Cat›" AND
   VENDOR = "‹Supplier›", or reuse existing supplier tags)
2. `menuUpdate` with nested `items` under the category parent (always pass back ALL
   existing top-level items with their ids to avoid wiping the menu)

### Phase 2 — Enrichment (REQUIRES network access) ⏸ blocked until env recreated

**ACTION (user chose 2026-06-01): recreate Claude-on-web env with allowlist.**
Add these to the environment's network allowlist (exact hosts; include `www.`):
```
www.akwa.co.za   akwa.co.za          ← PRIMARY (distributor, all brands, Shopify)
cdn.shopify.com                       ← image hosts (so image URLs are fetchable)
chihiros.com  chihirosaquaticstudio.com
zetlight.com
tropica.com  dennerle.com  hikariusa.com  nt-labs.co.uk
bubblemagus.com  maxspect.com  dymax.com
```

**⚠️ KNOWN GOTCHA (verified 2026-06-01):** akwa.co.za returns **HTTP 403 to bots** on the
normal product pages even from a browser UA. Allowlisting fixes the env wall, but the site's
own anti-bot may still 403. Mitigations to try, in order:
1. `/products.json?limit=250&page=N` — different code path, often NOT bot-blocked.
2. per-collection JSON: `/collections/‹handle›/products.json`
3. If both 403: fall back to **"Give me the data file"** — user exports akwa catalog CSV
   from Shopify admin, or saves products.json from their logged-in browser, into the repo.

Steps once reachable:
- [ ] Verify: fetch `https://www.akwa.co.za/products.json?limit=1` → expect JSON, not 403
- [ ] Page through `/products.json?limit=250&page=N` → build supplier catalog (title, vendor,
      type, body_html, images[], variants[].sku/barcode)
- [ ] Match supplier products → our products by SKU / barcode / title
- [ ] Bulk-update `descriptionHtml` with real specs (copyright OK — our suppliers)
- [ ] Append additional images → enable carousels (`productCreateMedia`)
- [ ] Prioritize branded lines first (Hikari, Dophin, Dymax, Chihiros, Zetlight,
      Tropica, Dennerle, NT Labs, Bubble-Magus, Maxspect, Bioloark)
- [ ] House "Aqua Cube" rebadged stock last (map to original manufacturer where known)

### Matching strategy (Phase 2 detail)
1. Primary key: **SKU** (most reliable across supplier ↔ our store)
2. Fallback: **barcode/EAN**, then normalized **title** fuzzy match
3. Unmatched → flagged report for manual review (don't guess on specs)

---

## 7. Scale & batching notes
- ~1,000 active products are the priority; 1,902 drafts can follow.
- Bulk edits run in batches (rate-limit aware). Validate every GraphQL op before executing.
- Each phase produces a before/after report; spot-check a sample per batch.

---

## 8. Session continuity checklist (READ FIRST in next session)
- [ ] Confirm connected store is **Aquacube** (`get-shop-info`) before ANY write —
      a prior session accidentally acted on a different store ("My Store 3").
- [ ] **Never** call `switch-shop` unless explicitly switching — it revokes the token.
- [ ] Verify network access by fetching `https://www.akwa.co.za/products.json?limit=1`
      → JSON = ready for Phase 2; 403/"Host not in allowlist" = still blocked (see §6 gotcha).
- [ ] Resume at Phase 2 (enrichment) — Phases 0 & 1-Lights already done (below).

### Done so far (live on Aquacube)
- Dymax smart collection `/collections/dymax` (119) + "Dymax" main-menu link.
- Phase 0: 14 mis-typed Hikari foods → Fish Food.
- Phase 1: 8 per-supplier Lights collections + **Lights ▾** dropdown
  (parent menu item `780547588169`, 13 sub-items).
- Remaining no-network work: category dropdowns for Filtration/Pumps/Plants/Food/CO2,
  and clean up dead menu links ("Voonline & Crash", "DR Tank & Fertilizers", etc.).
