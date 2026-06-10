#!/usr/bin/env python3
"""
Build Shopify bulk image-update CSV for the 53 Akwa products.

Usage:
  # Step 1: produce manifest (no CDN URLs yet)
  python3 build_akwa_image_csv.py manifest

  # Step 2: after uploading JPGs to Shopify Files, generate final CSV
  python3 build_akwa_image_csv.py final --cdn-base "https://cdn.shopify.com/s/files/1/0XXX/XXXX/files"

  # Step 3 (alternative): generate from a CDN URL map (filename -> URL) JSON
  python3 build_akwa_image_csv.py final --url-map shopify_cdn_urls.json
"""
import argparse
import csv
import json
import os
import sys

CSV_DIR = "/tmp/aqua-shopify"
MAPPING = os.path.join(CSV_DIR, "Akwa_Image_Mapping_with_Title.csv")
FILE8 = os.path.join(CSV_DIR, "AquaCube_08_Akwa_Products_SHOPIFY_COLLECTIONS.csv")


def load_mapping():
    """Join Akwa mapping with File 8 to get handles + titles."""
    with open(FILE8, newline="", encoding="utf-8") as f:
        file8 = {r["SKU"]: r for r in csv.DictReader(f)}

    with open(MAPPING, newline="", encoding="utf-8") as f:
        mapping = list(csv.DictReader(f))

    joined = []
    for m in mapping:
        sku = m["SKU"].strip()
        p = file8.get(sku)
        if not p:
            print(f"  [WARN] SKU {sku} not in File 8", file=sys.stderr)
            continue
        joined.append({
            "SKU": sku,
            "Handle": p["URL handle"].strip(),
            "Title": p["Title"].strip(),
            "Image_File": m["Image_File"].strip(),
            "Alt_Text": p["Title"].strip(),  # use product title as alt text
        })
    return joined


def write_manifest(rows):
    """Manifest CSV — you upload images, then fill Image Src column."""
    path = os.path.join(CSV_DIR, "akwa_image_manifest.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Handle", "Image File (local)", "Image Src (PASTE CDN URL HERE)", "Image Alt Text", "Image Position", "SKU", "Title"])
        for r in rows:
            w.writerow([r["Handle"], r["Image_File"], "", r["Alt_Text"], "1", r["SKU"], r["Title"]])
    print(f"Wrote manifest: {path}")
    print(f"  {len(rows)} rows. Fill the 'Image Src' column with CDN URLs after uploading to Shopify Files.")


def write_final(rows, cdn_base=None, url_map=None):
    """Final Shopify bulk import CSV using product CSV format."""
    path = os.path.join(CSV_DIR, "akwa_image_bulk_update.csv")
    skipped = 0
    written = 0
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        # Minimal Shopify Product CSV header for image update
        w.writerow(["Handle", "Image Src", "Image Position", "Image Alt Text"])
        for r in rows:
            if url_map:
                src = url_map.get(r["Image_File"], "")
            elif cdn_base:
                src = f"{cdn_base.rstrip('/')}/{r['Image_File']}"
            else:
                src = ""
            if not src:
                skipped += 1
                continue
            w.writerow([r["Handle"], src, "1", r["Alt_Text"]])
            written += 1
    print(f"Wrote final bulk CSV: {path}")
    print(f"  {written} rows written, {skipped} skipped (no URL).")
    print(f"  Import this in Shopify admin: Products > Import")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["manifest", "final"])
    ap.add_argument("--cdn-base", help="Shopify CDN base URL (everything before /<filename>.jpg)")
    ap.add_argument("--url-map", help="JSON file mapping local filename -> Shopify CDN URL")
    args = ap.parse_args()

    rows = load_mapping()
    if args.mode == "manifest":
        write_manifest(rows)
    else:
        url_map = None
        if args.url_map:
            with open(args.url_map) as f:
                url_map = json.load(f)
        if not (args.cdn_base or url_map):
            ap.error("--cdn-base or --url-map required for 'final' mode")
        write_final(rows, cdn_base=args.cdn_base, url_map=url_map)


if __name__ == "__main__":
    main()
