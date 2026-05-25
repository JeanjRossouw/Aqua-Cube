#!/usr/bin/env python3
"""Patch AquaCube_08_Akwa_Products with real pricing from Akwa_Cost_Prices_FINAL."""
import csv
import os

CSV_DIR = "/tmp/aqua-shopify"
PRICE_CSV = "/root/.claude/uploads/2bb4a821-069e-4dd1-88bc-b658a0330e6f/a2bdb53a-Akwa_Cost_Prices_FINAL.csv"
IN_CSV = os.path.join(CSV_DIR, "AquaCube_08_Akwa_Products_SHOPIFY_COLLECTIONS.csv")
OUT_CSV = os.path.join(CSV_DIR, "AquaCube_08_Akwa_Products_SHOPIFY_COLLECTIONS_PRICED.csv")

# Load pricing data
pricing = {}
with open(PRICE_CSV, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        sku = (row.get("SKU") or "").strip()
        if not sku:
            continue
        cost_incl = (row.get("Cost_Incl_VAT") or "").strip()
        selling = (row.get("Selling_Price_30pct_Markup") or "").strip()
        map_price = (row.get("Akwa_MAP_Price") or "").strip()
        pricing[sku] = {
            "cost": cost_incl,
            "price": selling,
            "map": map_price,
            "name": (row.get("Product_Name") or "").strip(),
        }

# Patch File 8
patched = 0
flagged = []
rows_out = []
with open(IN_CSV, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        sku = (row.get("SKU") or "").strip()
        p = pricing.get(sku)
        if not p:
            flagged.append((sku, "no pricing data found", row.get("Title", "")))
            rows_out.append(row)
            continue

        # Skip rows with N/A pricing (FG0302)
        if p["price"].upper() in ("N/A", "NA", ""):
            flagged.append((sku, "price is N/A in pricing file", p["name"]))
            rows_out.append(row)
            continue

        try:
            price_f = float(p["price"])
            cost_f = float(p["cost"])
        except ValueError:
            flagged.append((sku, f"non-numeric price/cost: {p['price']}/{p['cost']}", p["name"]))
            rows_out.append(row)
            continue

        row["Price"] = f"{price_f:.2f}"
        row["Cost per item"] = f"{cost_f:.2f}"

        # Compare-at price: use MAP only if valid AND > selling price; else clear
        row["Compare-at price"] = ""
        if p["map"] and p["map"].upper() not in ("N/A", "NA"):
            try:
                map_f = float(p["map"])
                if map_f > price_f:
                    row["Compare-at price"] = f"{map_f:.2f}"
            except ValueError:
                pass

        patched += 1
        rows_out.append(row)

# Write output
with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows_out)

print(f"Patched: {patched} / {len(rows_out)} products")
print(f"Flagged (still need attention): {len(flagged)}")
for sku, reason, name in flagged:
    print(f"  {sku}: {reason}  ({name})")
print(f"\nOutput: {OUT_CSV}")
