#!/usr/bin/env python3
"""Validate Shopify product CSVs for AquaCube."""
import csv
import os
import re
import sys
from collections import defaultdict, Counter

CSV_DIR = "/tmp/aqua-shopify"

# Shopify's standard product CSV required columns
REQUIRED_COLS = [
    "Title", "URL handle", "Status", "SKU", "Price", "Inventory quantity",
    "Vendor", "Collections",
]

# Valid values per Shopify spec
VALID_STATUS = {"active", "draft", "archived"}
VALID_PUBLISHED = {"TRUE", "FALSE", "true", "false", ""}
VALID_TAX = {"TRUE", "FALSE", "true", "false", ""}
VALID_REQ_SHIP = {"TRUE", "FALSE", "true", "false", ""}
VALID_GIFT = {"TRUE", "FALSE", "true", "false", ""}
VALID_CONT_SELL = {"TRUE", "FALSE", "true", "false", "deny", "continue", ""}

HANDLE_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

files = sorted(f for f in os.listdir(CSV_DIR) if f.endswith("_SHOPIFY_COLLECTIONS.csv"))

global_skus = defaultdict(list)        # sku -> [(file, row#, title)]
global_handles = defaultdict(list)     # handle -> [(file, row#, title)]
all_collections = Counter()
all_vendors = Counter()
all_statuses = Counter()

report = []
total_rows = 0
total_errors = 0
total_warnings = 0


def log(msg):
    report.append(msg)
    print(msg)


for fname in files:
    path = os.path.join(CSV_DIR, fname)
    log(f"\n{'=' * 78}")
    log(f"FILE: {fname}")
    log(f"{'=' * 78}")

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames or []

        # Required columns
        missing_cols = [c for c in REQUIRED_COLS if c not in cols]
        if missing_cols:
            log(f"  [ERROR] Missing required columns: {missing_cols}")
            total_errors += 1
        else:
            log(f"  [OK] All required columns present")

        rows = list(reader)
        log(f"  Rows: {len(rows)}")
        total_rows += len(rows)

        local_skus = Counter()
        local_handles = Counter()
        errors = 0
        warnings = 0

        for i, row in enumerate(rows, start=2):  # row 2 = first data row
            title = (row.get("Title") or "").strip()
            handle = (row.get("URL handle") or "").strip()
            sku = (row.get("SKU") or "").strip()
            price = (row.get("Price") or "").strip()
            cost = (row.get("Cost per item") or "").strip()
            inv = (row.get("Inventory quantity") or "").strip()
            status = (row.get("Status") or "").strip()
            published = (row.get("Published on online store") or "").strip()
            vendor = (row.get("Vendor") or "").strip()
            collections = (row.get("Collections") or "").strip()
            charge_tax = (row.get("Charge tax") or "").strip()
            req_ship = (row.get("Requires shipping") or "").strip()
            gift = (row.get("Gift card") or "").strip()
            cont_sell = (row.get("Continue selling when out of stock") or "").strip()

            # Required field checks
            if not title:
                log(f"  [ERROR] Row {i}: empty Title")
                errors += 1
            if not handle:
                log(f"  [ERROR] Row {i}: empty URL handle (title={title!r})")
                errors += 1
            elif not HANDLE_RE.match(handle):
                log(f"  [ERROR] Row {i}: invalid handle format {handle!r} (must be lowercase, alphanumeric + hyphens)")
                errors += 1
            if not sku:
                log(f"  [ERROR] Row {i}: empty SKU (title={title!r})")
                errors += 1
            if not price:
                log(f"  [ERROR] Row {i}: empty Price (title={title!r})")
                errors += 1
            else:
                try:
                    p = float(price)
                    if p <= 0:
                        log(f"  [WARN] Row {i}: Price={p} (zero or negative)")
                        warnings += 1
                except ValueError:
                    log(f"  [ERROR] Row {i}: Price not numeric: {price!r}")
                    errors += 1

            if cost:
                try:
                    c = float(cost)
                    if c <= 0:
                        log(f"  [WARN] Row {i}: Cost={c}")
                        warnings += 1
                    elif price:
                        try:
                            p = float(price)
                            # Expected: cost * 1.15 * 1.30 = price (within 1% tolerance)
                            expected = c * 1.15 * 1.30
                            if abs(p - expected) / expected > 0.02:
                                log(f"  [WARN] Row {i} ({sku}): price {p} doesn't match cost×1.15×1.30={expected:.2f}")
                                warnings += 1
                        except ValueError:
                            pass
                except ValueError:
                    log(f"  [ERROR] Row {i}: Cost not numeric: {cost!r}")
                    errors += 1

            if inv:
                try:
                    int(float(inv))
                except ValueError:
                    log(f"  [ERROR] Row {i}: Inventory quantity not numeric: {inv!r}")
                    errors += 1

            # Enumerated values
            if status and status.lower() not in VALID_STATUS:
                log(f"  [ERROR] Row {i}: invalid Status {status!r} (must be active/draft/archived)")
                errors += 1
            if published and published not in VALID_PUBLISHED:
                log(f"  [WARN] Row {i}: unusual Published value {published!r}")
                warnings += 1
            if charge_tax and charge_tax not in VALID_TAX:
                log(f"  [WARN] Row {i}: unusual Charge tax value {charge_tax!r}")
                warnings += 1
            if req_ship and req_ship not in VALID_REQ_SHIP:
                log(f"  [WARN] Row {i}: unusual Requires shipping value {req_ship!r}")
                warnings += 1
            if gift and gift not in VALID_GIFT:
                log(f"  [WARN] Row {i}: unusual Gift card value {gift!r}")
                warnings += 1
            if cont_sell and cont_sell not in VALID_CONT_SELL:
                log(f"  [WARN] Row {i}: unusual Continue selling value {cont_sell!r}")
                warnings += 1

            if not vendor:
                log(f"  [WARN] Row {i}: empty Vendor")
                warnings += 1
            if not collections:
                log(f"  [WARN] Row {i}: empty Collections (won't appear in any collection)")
                warnings += 1

            # Tracking
            if sku:
                local_skus[sku] += 1
                global_skus[sku].append((fname, i, title))
            if handle:
                local_handles[handle] += 1
                global_handles[handle].append((fname, i, title))

            for c in [x.strip() for x in collections.split(",") if x.strip()]:
                all_collections[c] += 1
            if vendor:
                all_vendors[vendor] += 1
            if status:
                all_statuses[status] += 1

        # Local dupes
        for sku, count in local_skus.items():
            if count > 1:
                log(f"  [ERROR] Duplicate SKU within file: {sku!r} ({count}×)")
                errors += 1
        for h, count in local_handles.items():
            if count > 1:
                log(f"  [ERROR] Duplicate handle within file: {h!r} ({count}×)")
                errors += 1

        log(f"  Summary: {errors} errors, {warnings} warnings")
        total_errors += errors
        total_warnings += warnings

# Cross-file checks
log(f"\n{'=' * 78}")
log("CROSS-FILE CHECKS")
log(f"{'=' * 78}")

cross_sku_dupes = {s: locs for s, locs in global_skus.items() if len(locs) > 1}
cross_handle_dupes = {h: locs for h, locs in global_handles.items() if len(locs) > 1}

if cross_sku_dupes:
    log(f"  [ERROR] {len(cross_sku_dupes)} SKU(s) appear in multiple files:")
    for sku, locs in list(cross_sku_dupes.items())[:20]:
        log(f"    {sku}:")
        for fn, r, t in locs:
            log(f"      {fn}:{r}  {t}")
    if len(cross_sku_dupes) > 20:
        log(f"    ... and {len(cross_sku_dupes) - 20} more")
    total_errors += len(cross_sku_dupes)
else:
    log("  [OK] No cross-file SKU duplicates")

if cross_handle_dupes:
    log(f"  [ERROR] {len(cross_handle_dupes)} handle(s) appear in multiple files:")
    for h, locs in list(cross_handle_dupes.items())[:20]:
        log(f"    {h}:")
        for fn, r, t in locs:
            log(f"      {fn}:{r}  {t}")
    total_errors += len(cross_handle_dupes)
else:
    log("  [OK] No cross-file handle duplicates")

# Catalog summary
log(f"\n{'=' * 78}")
log("CATALOG SUMMARY")
log(f"{'=' * 78}")
log(f"  Total products: {total_rows}")
log(f"  Distinct collections referenced: {len(all_collections)}")
for col, n in all_collections.most_common():
    log(f"    {n:>4}  {col}")
log(f"  Distinct vendors: {len(all_vendors)}")
for v, n in all_vendors.most_common():
    log(f"    {n:>4}  {v}")
log(f"  Status distribution:")
for s, n in all_statuses.most_common():
    log(f"    {n:>4}  {s}")

log(f"\n{'=' * 78}")
log(f"TOTAL: {total_errors} errors, {total_warnings} warnings across {len(files)} files / {total_rows} products")
log(f"{'=' * 78}")

# Write report file
with open(os.path.join(CSV_DIR, "validation_report.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(report))

sys.exit(0 if total_errors == 0 else 1)
