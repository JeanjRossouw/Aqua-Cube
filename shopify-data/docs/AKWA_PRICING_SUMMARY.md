# File 8 (Akwa) — Pricing Patch Complete

## Result
- **52 / 53 products priced** using `Cost_Incl_VAT × 1.30 = Selling Price` (matches Files 1–7 formula)
- **11 products** have a `Compare-at price` set from Akwa MAP (creates a visible "sale" strikethrough)
- **1 product flagged** for manual review: `FG0302` — FULLGAIN FLAT LED 18W 60cm (marked "CHECK SKU" in pricing file, price = N/A)

## Pricing-formula clarification
Setup doc said `(Cost × 1.15 VAT) × 1.30 markup = Price`, but the actual stored pattern in **all 8 files** is `Cost × 1.30 = Price`. The 1.15 VAT is already baked into the stored `Cost per item` value. No discrepancy — just doc wording was misleading.

## Compare-at price (MAP) products
| SKU      | Price (R) | MAP (R) | Savings |
|----------|----------:|--------:|--------:|
| FG0300   | 447.01    | 618.95  | 28%     |
| FG0301   | 581.99    | 805.85  | 28%     |
| FG0303   | 867.62    | 1201.30 | 28%     |
| FG0304   | 1047.40   | 1450.25 | 28%     |
| GRC0001  | 112.94    | 156.40  | 28%     |
| GRC0002  | 133.35    | 184.65  | 28%     |
| MAG0001  | 128.87    | 178.45  | 28%     |
| MAG0002  | 195.10    | 270.15  | 28%     |
| MAG0003  | 233.37    | 323.15  | 28%     |
| SCR0001  | 70.12     | 97.10   | 28%     |

## Action required from you
1. **FG0302** — confirm correct SKU with Akwa (pricing file note says "CHECK SKU"), then either patch the CSV manually or send updated pricing.
2. Import the new file: `AquaCube_08_Akwa_Products_SHOPIFY_COLLECTIONS_PRICED.csv`

## All 8 files now import-ready
| # | File                                  | Products | Status |
|---|---------------------------------------|---------:|--------|
| 1 | Lighting_CO2                          | 36       | ✅ Ready |
| 2 | Pumps_Flow                            | 55       | ✅ Ready |
| 3 | Filtration_Accessories                | 66       | ✅ Ready |
| 4 | Decorations_Ornaments                 | 38       | ✅ Ready |
| 5 | Hardscape_Decorations                 | 78       | ✅ Ready |
| 6 | DR_Tank_Fertilizers                   | 29       | ✅ Ready |
| 7 | Voonline_Crash_Accessories            | 34       | ✅ Ready |
| 8 | Akwa_Products **(_PRICED.csv)**       | 52 + 1 TBD | ⚠️ FG0302 needs SKU check |
