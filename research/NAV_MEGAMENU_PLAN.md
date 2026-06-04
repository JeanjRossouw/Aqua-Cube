# Aqua Cube — Deep Megamenu + Shop by Brand — PLAN (review before theme edit)

**Date:** 2026-06-04  **Reference:** mcmerwe.co.za  **Decisions locked with user:**
linklist-driven megamenu · changes via `shopify-live` PR (user publishes) · Ocean Max + JBL
brand collections created · marine kept in catalog but OUT of nav.

## Already done (store-level, live now)
- Created smart brand collections **Ocean Max** (`ocean-max`, vendor=Ocean Max, ~19) and
  **JBL** (`jbl`, vendor=JBL, ~7), published to Online Store.
- **`brands` linklist → 34 items** (added Ocean Max, JBL alphabetically). Powers "Shop by Brand".
- NOTE: almost the entire category tree already exists as tag-driven smart collections (~140).

## The theme change (1 file: `sections/header.liquid` on `shopify-live`)
Replace the hard-coded flat links + 3 block dropdowns with a loop over `linklists.main-menu`.
- Lifts the **30-block cap** (linklists are uncapped) → full tree renders.
- **Reuses every existing class** (`ac-nav__drop/__trigger/__menu/__item`) so current styling,
  the mobile accordion JS (`global.js`), and the recent dropdown fixes keep working unchanged.
- Removes the **Marine** flat link (excluded) and the **Dymax** flat link (brand now under Shop by Brand).
- Content is then 100% managed in the Shopify Navigation editor (`main-menu`) → survives GitHub sync
  (linklists are not theme settings, so the sync-stripping gotcha doesn't apply).

Proposed `<ul class="ac-nav__links" id="NavMenu">` body:
```liquid
{%- for link in linklists.main-menu.links -%}
  {%- if link.links.size > 0 -%}
    <li class="ac-nav__drop" role="none">
      <button class="ac-nav__trigger" type="button" aria-haspopup="true" aria-expanded="false" role="menuitem">
        {{ link.title }} {% render 'icon-caret-down' %}
      </button>
      <div class="ac-nav__menu{% if link.links.size <= 6 %} ac-nav__menu--narrow{% endif %}" role="menu">
        {%- for child in link.links -%}
          <a href="{{ child.url }}" class="ac-nav__item" role="menuitem">
            <span class="ac-nav__item-txt"><span class="ac-nav__item-title">{{ child.title }}</span></span>
          </a>
        {%- endfor -%}
      </div>
    </li>
  {%- else -%}
    <li role="none">
      <a href="{{ link.url }}" class="ac-nav__link{% if link.current %} is-active{% endif %}" role="menuitem">{{ link.title }}</a>
    </li>
  {%- endif -%}
{%- endfor -%}
```
"Shop by Brand" = a top-level `main-menu` item (children = the 34 brands), rendered by the same
loop as a wide multi-column panel (CSS tweak: brand panel uses 3–4 columns).

## Final `main-menu` tree (13 branches → real collections; marine excluded; empties omitted)
1. **Aquariums & Stands** `/collections/aquariums` → Aquariums/Tanks `aquariums` · Aquarium Sets `pre-built-tanks` · Stands & Cabinets `stands-cabinets` · Mats & Foam `accessories-mats`
2. **Paludariums & Terrariums** `/collections/paludariums` → All Paludariums `paludariums` · Paludarium Plants `paludarium-plants` · Terrarium Lights `lighting-terrarium`  *(gaps: Terrarium/Paludarium Sets, Backgrounds — none/empty)*
3. **Filtration** `/collections/filtration` → Canister `filters-canister` · Hang-on-Back `filters-hob` · Internal/Submersible `filters-internal` · Sponge `filters-sponge` · Filter Media `filter-media` · UV `filters-uv`  *(gaps: Filter Spares, Surface Skimmers)*
4. **Pumps & Flow** `/collections/pumps-flow` → Air Pumps `air-pumps` · Water Pumps `pumps-water` · Wavemakers `pumps-wavemakers`
5. **Heating & Cooling** `/collections/heaters` → Heaters `heaters` · Chillers/Fans `pumps-chillers`  *(Thermometers folded into Heaters)*
6. **Lighting** `/collections/lighting` → Plant/Freshwater `lighting-freshwater` · Paludarium/Terrarium `lighting-terrarium` · Light Accessories `lighting-accessories`
7. **CO₂ Equipment** `/collections/co2` → Regulators `co2-regulators` · Diffusers `co2-diffusors` · Bottles `co2-bottles` · Drop Checkers `co2-drop-checkers` · Tubing & Accessories `co2-tubing`  *(gap: Bubble Counters)*
8. **Plants** `/collections/plants-moss` → Tropica `plants-tropica` · Moss `moss` · Paludarium Plants `paludarium-plants`  *(could add ADA/Dennerle/tech-levels — all exist)*
9. **Cleanup Crew** `/collections/cleanup-crew` → Isopods `isopods` · Springtails `springtails`
10. **Substrate & Hardscape** `/collections/hardscape-substrate` → Inert Gravel & Sand `substrate-inert` · Rocks & Wood `hardscape` · Decor `decor`  *(gap: Aquasoil/Plant Substrate — empty)*
11. **Water Care** `/collections/water-treatment` → Dechlorinators `water-dechlorinators` · Bacteria & Starters `water-bacteria` · Plant Fertilisers `plant-food` · Algae Treatments `water-algae` · Test Kits `test-kits`
12. **Food** `/collections/fish-food` → Fish Food `fish-food` · Pellets `food-pellets` · Flakes `food-flakes` · Frozen `food-frozen`
13. **Tools & Accessories** `/collections/accessories` → Scaping Tools `accessories-tools` · Airline/Hose `airline-hose` · Auto Feeders `accessories-feeders`
+ **Shop by Brand** → 34 brand collections (`brands` linklist).

## Open question — 13 top-level items is wide for desktop
Options: (a) keep 13 (condensed bar), (b) group to ~9 (combine CO₂ into Lighting, Heating into
Filtration/Pumps, etc.), (c) McMerwe-style fewer top items + big mega-panels. Default = keep 13.

## Next steps (after user OK)
1. Build the `main-menu` tree via API (linklist — reversible, previewable in Nav editor).
2. Open **DRAFT PR** on `shopify-live` with the `header.liquid` diff (+ small CSS for brand panel).
3. User reviews diff → merges → publishes "Aqua Cube 2026" (188936552521) to go live.
   (Reminder: the GitHub theme is currently UNPUBLISHED; a manual snapshot is live.)
