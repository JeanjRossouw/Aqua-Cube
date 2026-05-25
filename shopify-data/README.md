# Shopify Data — AquaCube

Working data + helper scripts for migrating the 389-product catalog to the live `aquacubesa.co.za` Shopify store.

## Folder layout

```
shopify-data/
├── csv/                                                       # outputs ready for Shopify import
│   ├── AquaCube_08_Akwa_Products_SHOPIFY_COLLECTIONS_PRICED.csv  # File 8 with pricing patched (52/53 priced; FG0302 needs SKU verify)
│   ├── akwa_image_manifest.csv                                   # 53 Akwa products → local JPG filenames (fill Image Src after upload)
│   ├── akwa_image_bulk_update_TEMPLATE.csv                       # Shopify import format (placeholder URLs; regenerate after upload)
│   ├── non_akwa_image_search.csv                                 # 336 products × Bing + Google search links (manual image pick)
│   └── non_akwa_image_bulk_update_TEMPLATE.csv                   # blank Image Src column to paste picks into
│
├── scripts/                                                   # Python tools to regenerate the CSVs
│   ├── validate.py                                               # validate all 8 SHOPIFY_COLLECTIONS.csv files
│   ├── patch_akwa_prices.py                                      # apply pricing to File 8 from supplier sheet
│   ├── build_akwa_image_csv.py                                   # build/finalize Akwa image bulk-update CSV
│   └── build_non_akwa_image_links.py                             # generate Bing/Google links for non-Akwa products
│
└── docs/                                                      # human-readable reports
    ├── VALIDATION_SUMMARY.md                                     # CSV validation findings
    ├── AKWA_PRICING_SUMMARY.md                                   # what the pricing patch did
    ├── AKWA_IMAGE_WORKFLOW.md                                    # 4-step guide to live Akwa images
    └── validation_report.txt                                     # full per-row validation output
```

## Workflow order

1. **Imported** the 8 SHOPIFY_COLLECTIONS CSVs (Files 1–7 as-is; File 8 use the `_PRICED` version)
2. **Upload** the 53 Akwa JPGs listed in `akwa_image_manifest.csv` to Shopify Files
3. **Regenerate** `akwa_image_bulk_update_TEMPLATE.csv` with real CDN URLs:
   ```bash
   python3 scripts/build_akwa_image_csv.py final --cdn-base "https://cdn.shopify.com/s/files/1/<your-ids>/files"
   ```
4. **Import** the regenerated CSV in Shopify (Products → Import, overwrite same handle ✅)
5. **Pick images** for the 336 non-Akwa products using `non_akwa_image_search.csv` (Bing + Google links)
6. **Build** the non-Akwa bulk update CSV by pasting picks into the `Chosen_Image_URL` column → produce final CSV → import

## Outstanding items

- **FG0302** (FULLGAIN FLAT LED 18W 60cm) — confirm correct SKU with Akwa, add cost, rerun `patch_akwa_prices.py`
- **"Backgrounds" collection** (48 products) — listed in CSV but not in setup doc's 19-collection list. Verify it exists in Shopify admin or rename.
