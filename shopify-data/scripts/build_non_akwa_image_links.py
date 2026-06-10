#!/usr/bin/env python3
"""Build image-search-link CSV for the 336 non-Akwa products.

For each product: SKU, Handle, Title, Vendor, Collection, Bing search URL, Google Images URL.
"""
import csv
import os
import urllib.parse

CSV_DIR = "/tmp/aqua-shopify"
MASTER = os.path.join(CSV_DIR, "AquaCube_Products_with_Image_URLs.csv")
OUT = os.path.join(CSV_DIR, "non_akwa_image_search.csv")

# Load Akwa SKUs to exclude
with open(os.path.join(CSV_DIR, "AquaCube_08_Akwa_Products_SHOPIFY_COLLECTIONS.csv")) as f:
    akwa_skus = {r["SKU"] for r in csv.DictReader(f)}

# Build a SKU -> (handle, vendor, collection) map from files 1-7
sku_info = {}
for fname in sorted(os.listdir(CSV_DIR)):
    if not fname.endswith("_SHOPIFY_COLLECTIONS.csv"):
        continue
    if fname.startswith("AquaCube_08"):
        continue
    with open(os.path.join(CSV_DIR, fname)) as f:
        for r in csv.DictReader(f):
            sku = r["SKU"].strip()
            if sku:
                sku_info[sku] = {
                    "handle": r["URL handle"].strip(),
                    "vendor": r["Vendor"].strip(),
                    "collections": r["Collections"].strip(),
                    "source": fname,
                }

# Load master + filter
with open(MASTER) as f:
    master = list(csv.DictReader(f))

rows_out = []
unmatched = []
for r in master:
    sku = r["SKU"].strip()
    if sku in akwa_skus:
        continue  # skip Akwa
    info = sku_info.get(sku)
    if not info:
        unmatched.append(sku)
        continue
    title = r["Title"].strip()
    # Augment search with vendor for better results
    q = urllib.parse.quote(f"{info['vendor']} {title}".strip())
    bing = f"https://www.bing.com/images/search?q={q}"
    google = f"https://www.google.com/search?tbm=isch&q={q}"
    rows_out.append({
        "SKU": sku,
        "Handle": info["handle"],
        "Title": title,
        "Vendor": info["vendor"],
        "Collections": info["collections"],
        "Bing_Image_Search": bing,
        "Google_Image_Search": google,
        "Chosen_Image_URL": "",  # for user to paste their pick
        "Source_File": info["source"],
    })

with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows_out[0].keys()))
    w.writeheader()
    w.writerows(rows_out)

print(f"Wrote: {OUT}")
print(f"  Rows: {len(rows_out)}  (target was 336)")
print(f"  Unmatched SKUs (in master but not in CSVs 1-7): {len(unmatched)}")
if unmatched[:5]:
    print(f"    examples: {unmatched[:5]}")

# Also build the bulk-import CSV stub (so once user fills "Chosen_Image_URL", they can import)
stub = os.path.join(CSV_DIR, "non_akwa_image_bulk_update_TEMPLATE.csv")
with open(stub, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Handle", "Image Src", "Image Position", "Image Alt Text"])
    for r in rows_out:
        w.writerow([r["Handle"], "", "1", r["Title"]])
print(f"  Stub for bulk import: {stub} (paste Image Src column from non_akwa_image_search.csv)")
