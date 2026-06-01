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
Recreate the Claude-on-web environment with a network policy that allows at minimum:
- `akwa.co.za` (supplier — our own supplier, permission given)
- `chihiros.com` / `chihirosaquaticstudio.com` (Chihiros = "Shaquero")
- `zetlight.com` (Zetlight = "Z Lite")
- manufacturer sites as needed: `dymax.com`, `dophin*.com`, `tropica.com`,
  `dennerle.com`, `hikariusa.com`, `nt-labs.co.uk`, `bubblemagus.com`, `maxspect.com`

**Why this unlocks scale:** most of these are Shopify or structured sites. For any Shopify
store, `‹domain›/products.json?limit=250&page=N` returns **full descriptions + every image
URL** as JSON — so enrichment becomes a deterministic map, not manual copy-paste.
(Confirmed akwa.co.za is Shopify-based; `/products.json` is the target once allowlisted.)

### Terminology confirmed with user
- **"Z Lite" = Zetlight** ✓ (vendor in catalog)
- **"Shaquero" = Chihiros** ✓ (vendor in catalog)

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

### Phase 0 — Internal fixes (no network needed) ✅ can start anytime
- [ ] Fix mis-typed Hikari foods (Aquatic Plant → Fish Food) + strip false "live plant" text
- [ ] Audit other vendor/type mismatches via ShopifyQL/GraphQL
- [ ] Normalize obviously-wrong boilerplate where vendor/type contradicts it

### Phase 1 — Navigation (no network needed) ✅ can start anytime
- [ ] Create per-supplier **Lights** sub-collections (tags already exist)
- [ ] Build **LIGHTS ▾** dropdown (pilot)
- [ ] Roll out remaining category dropdowns (Filtration, Pumps, CO2, Plants, Food, …)
- [ ] Clean up mislabeled legacy menu items ("Voonline & Crash", "DR Tank", bare
      `/collections` links)

### Phase 2 — Enrichment (REQUIRES network access) ⏸ blocked until env recreated
- [ ] Allowlist supplier domains; pull `/products.json` feeds
- [ ] Match supplier products → our products by SKU / title / barcode
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
- [ ] Verify network access by fetching `https://akwa.co.za/products.json?limit=1`.
- [ ] Dymax collection (`/collections/dymax`, smart, 119 products) + nav link already done.
- [ ] Resume at Phase 0/1 (no-network work) regardless, then Phase 2 once allowlisted.
