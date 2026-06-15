# Akwa duplicate-product merge plan

Generated from a live bulk scan of all 3,238 products. Full row-by-row plan: `akwa_duplicate_merge_plan.csv`.

## Headline
- **139 SKUs** exist on more than one product -> **154 redundant records**, every one vendor **"Aqua Cube"**.
- Keepers: **85 active + 53 draft** (the proper catalogue product; usually the real brand-vendor twin).

## What 'archive the duplicate' actually touches
- **127 are ALREADY archived** -> no action, they're effectively merged out already.
- **27 are still live duplicates** = the real cleanup (24 draft, 3 active).

## ⚠ Review before archiving
- **3 ACTIVE duplicates** (customer-facing) flagged for archive:
    - `AFM0103` — "Akwa Activated Carbon" (keeper: a different product, same SKU)
    - `LED0010` — "Led Light 5W (White & Blue)" (keeper: a different product, same SKU)
    - `LED0011` — "Led Light 5W (Multi Colour)" (keeper: a different product, same SKU)
- **0 of the live duplicates have inventory > 0** — archiving would strand that stock; transfer/verify first.

## Recommended tiers
1. **Safe now (24):** draft duplicates with 0 inventory — archive immediately, zero customer/stock impact.
2. **Confirm (3 – overlap aside):** active duplicates + any with inventory.
3. **Already archived (127):** optionally delete later to fully declutter; not urgent.

_Keeper chosen by: status (Active>Draft>Archived) -> has image -> inventory -> oldest. Adjust any row in the CSV before executing._
