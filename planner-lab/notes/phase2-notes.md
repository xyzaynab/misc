# Phase 2 notes: element extraction

Output: `data/elements.json` (nested page type > zone > element > variant), crops in `catalog/<page type>/<zone>/<element>/`.
Rebuild with `python3 tools/build.py` (needs Pillow). Element vocabulary lives in `tools/taxonomy.py`; per-image crops in `tools/entries_b*.py`.

## Counts
- 188 variants from 22 images (15.jpg skipped: duplicate Dashboard layout of 12.jpg).
- Weekly 74, daily 114 (see the file for zone splits).

## Fields
Each variant has the fields you asked for plus `variant_group` (the shared style used for recurrence counts in Phase 3), `crop_box`, `product_group`, and `hobonichi_note`.

## Caveats
- **Footprint** is approximate. A portrait page is taken as 28 x 42 dots (5.5 x 8.25 in at 5 mm). A two-page spread or a landscape sheet is scaled to 56 dots wide. Product images are not true size, so treat footprints as relative.
- **Efforts, skip tolerance and ADHD/sensory notes** are my judgement from the images, set per element with some per-variant overrides. They are not measured.
- **Hobonichi overlap** comes from general knowledge of the Techo/Weeks layout and is marked unverified until you add photos of your own pages to `examples/mine/`.
- **Crop quality:** 10.jpg is photographed at an angle, so its crops overlap neighbours slightly. 13.jpg is cut off at the right edge. 21.png is low resolution. Several single-line elements make thin crops.
- **Elements added within the existing hierarchy** (no new levels): `people_to_connect`, `reward`. No new zones or page types were added.
- 6/14/24 weekly review pages are tagged weekly with their review content in the reflect zone. 7.jpg is folded into weekly as agreed.
