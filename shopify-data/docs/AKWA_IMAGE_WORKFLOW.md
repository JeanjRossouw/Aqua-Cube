# Akwa Image Mapping — Workflow Guide

## What you have now

| File | Purpose |
|------|---------|
| `akwa_image_manifest.csv` | Cross-reference: 53 products ↔ local JPG filenames ↔ blank "paste URL here" column |
| `akwa_image_bulk_update.csv` | Final Shopify import CSV (currently has placeholder URLs — needs real Shopify CDN URLs) |
| `build_akwa_image_csv.py` | Generator script — run again after you have real URLs |

Both CSVs have **53 rows**, one per Akwa product. SKU coverage = 100%.

---

## The 3-step process to live images

### Step 1 — Upload the 53 Akwa JPGs to Shopify Files

You only need to upload **53 of the 5,910** extracted images — the specific ones listed in `akwa_image_manifest.csv` column "Image File (local)".

In Shopify admin: **Settings → Files → Upload files** → drag the 53 JPGs.

> Don't upload all 5,910 — most aren't mapped to products. Filter the extracted ZIP first.

### Step 2 — Get your Shopify CDN base URL

After upload, click any uploaded file in **Settings → Files**. Its URL looks like:
```
https://cdn.shopify.com/s/files/1/0123/4567/files/akwa_img-041.jpg
```

Your **CDN base** is everything before `/akwa_img-041.jpg`:
```
https://cdn.shopify.com/s/files/1/0123/4567/files
```

### Step 3 — Generate the final CSV with real URLs

```bash
python3 build_akwa_image_csv.py final \
  --cdn-base "https://cdn.shopify.com/s/files/1/0123/4567/files"
```

This writes `akwa_image_bulk_update.csv` with proper CDN URLs.

### Step 4 — Import to Shopify

In Shopify admin: **Products → Import → Add file** → choose `akwa_image_bulk_update.csv` → **Overwrite existing products with same handle** = ✅

Shopify matches by `Handle` and updates the `Image Src` / `Image Alt Text` / `Image Position` columns only.

---

## Alternative: Filename-to-URL JSON map

If your CDN URLs don't follow the simple `base/filename.jpg` pattern (e.g. Shopify added hash suffixes), make a JSON map and use `--url-map`:

```json
{
  "akwa_img-041.jpg": "https://cdn.shopify.com/s/files/1/0123/4567/files/akwa_img-041_8a3b.jpg",
  "akwa_img-042.jpg": "https://cdn.shopify.com/s/files/1/0123/4567/files/akwa_img-042_2cf1.jpg"
}
```

Then run:
```bash
python3 build_akwa_image_csv.py final --url-map shopify_cdn_urls.json
```

---

## Notes

- **Alt text** is auto-filled with each product's Title (good for SEO + accessibility).
- **Image Position = 1** for all — these are the primary product images. If you add more images per product later, increment Position.
- **Handle** matches your `AquaCube_08_Akwa_Products_SHOPIFY_COLLECTIONS_PRICED.csv` exactly — no manual reconciliation needed.
- **53 image files total to upload** (listed in `Image File (local)` column of manifest).
