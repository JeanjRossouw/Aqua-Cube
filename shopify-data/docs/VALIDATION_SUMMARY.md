# AquaCube Shopify CSV Validation — Summary

**Files validated:** 8
**Total products:** 389
**Errors:** 0
**Real issues found:** 2 (see below)

---

## ✅ What's clean

| Check                                  | Result |
|----------------------------------------|--------|
| Required columns present (all 8 files) | ✅ Pass |
| Handle format (lowercase + hyphens)    | ✅ Pass |
| SKU uniqueness within file             | ✅ Pass |
| SKU uniqueness across all 8 files      | ✅ Pass |
| Handle uniqueness across all 8 files   | ✅ Pass |
| Status values valid                    | ✅ Pass (all `Active`) |
| Pricing formula compliance             | ✅ Pass (files 1–7 match `Cost × 1.15 × 1.30`) |
| Numeric fields (price, cost, inventory)| ✅ Pass |

All 389 products have valid Shopify-importable structure.

---

## ⚠️ Real issues (2)

### Issue 1 — File 8 (Akwa) has no pricing
All **53 Akwa products** have `Price = 0` and `Cost per item = 0`.

Importing these as-is would make them free.

**Fix options:**
- Set prices in the CSV before import (apply same `Cost × 1.15 × 1.30` formula)
- Or import with placeholder cost & set prices via Shopify bulk editor after

### Issue 2 — `Continue selling when out of stock = "DENY"` (cosmetic)
All 389 rows use uppercase `"DENY"`. Shopify accepts this (case-insensitive) so import will work, but Shopify's docs spell it lowercase `"deny"`. **Not blocking** — flagged only for consistency.

---

## 📊 Catalog breakdown

### Per file
| # | File                                  | Products |
|---|---------------------------------------|---------:|
| 1 | Lighting_CO2                          | 36       |
| 2 | Pumps_Flow                            | 55       |
| 3 | Filtration_Accessories                | 66       |
| 4 | Decorations_Ornaments                 | 38       |
| 5 | Hardscape_Decorations                 | 78       |
| 6 | DR_Tank_Fertilizers                   | 29       |
| 7 | Voonline_Crash_Accessories            | 34       |
| 8 | Akwa_Products (no pricing yet)        | 53       |
|   | **Total**                             | **389**  |

### Collections (19 distinct)
58 Lighting · 55 Pumps & Filters · 48 Backgrounds · 38 Decorations · 34 Hardscape · 33 Filtration · 29 Water Treatment · 16 Maintenance · 12 Accessories · 11 Plants · 10 Substrate · 9 Tanks · 9 Heaters · 8 Aeration · 6 CO2 & Dosing · 6 Breeding · 4 Food · 2 Feeding · 1 Water Testing

> **Note:** Setup doc claims 19 collections including "Backgrounds" but doc lists "Tanks, Heaters, Maintenance, Aeration, Food, Feeding, Water Treatment, Water Testing, Accessories, Breeding" — these all match the CSV data. **"Backgrounds" appears in CSVs but is NOT in the doc's 19-collection list.** Worth a quick sanity check on collection naming in Shopify admin.

### Vendors (13 distinct)
135 Aquatic · 53 Akwa · 47 SYAquarium · 37 Sobo · 29 DRTank · 28 Voonline · 25 Chihiros · 13 BubbleMagus · 10 Zetlight · 5 Jebao · 5 Crash · 1 Aquapro · 1 Aquamaster

---

## 🚀 Recommended next steps

1. **Get Akwa pricing** — add Cost values to File 8 and recompute Price (×1.15 ×1.30).
2. **Sanity-check "Backgrounds" collection** — confirm it exists in Shopify admin or rename it in CSVs.
3. **Import order:** Files 1–7 are import-ready right now. Hold File 8 until pricing is added.
4. **Image work (separate task):** Akwa images mapping & non-Akwa image search links.

---

*Full per-row report saved as `validation_report.txt`*
