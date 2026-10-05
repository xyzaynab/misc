"""Build data/elements.json and catalog/ crops from entries_*.py files.

Usage: python3 tools/build.py [--qa DIR]   (QA writes bbox overlays to DIR)
Each entries file defines REGIONS {img: (x0,y0,x1,y1,mode)} and ENTRIES {img: [(element, variant_name, bbox, description, overrides)]}.
Footprint is approximate dots at 5 mm pitch: a portrait page is 28x42 dots; a spread (or landscape sheet) is 56x42.
"""
import glob, importlib, json, os, sys
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import taxonomy as T
import variant_groups as VG

imgs = {int(i['file'].split('.')[0]): i for i in json.load(open(f'{ROOT}/data/images.json'))['images']}
REGIONS, ENTRIES = {}, {}
for f in sorted(glob.glob(f'{HERE}/entries_*.py')):
    m = importlib.import_module(os.path.basename(f)[:-3])
    REGIONS.update(m.REGIONS); ENTRIES.update(m.ENTRIES)

KEYMAP = dict(draw='draw_effort', daily='daily_effort', skip='skip_tolerance', inp='input_style',
              hob='hobonichi_overlap', hob_note='hobonichi_note', adhd='adhd_notes', sens='sensory_notes')

def footprint(box, region):
    rx0, ry0, rx1, ry1, mode = region
    s = (28 if mode == 'portrait' else 56) / (rx1 - rx0)
    w = max(2, round((box[2] - box[0]) * s)); h = max(2, round((box[3] - box[1]) * s))
    return [w, h]

tree = {}; n_total = 0; names = {}; ungrouped = set()
qa_dir = sys.argv[sys.argv.index('--qa') + 1] if '--qa' in sys.argv else None
for n in sorted(ENTRIES):
    info = imgs[n]; im = Image.open(f"{ROOT}/{info['path']}").convert('RGB')
    qa = ImageDraw.Draw(im) if qa_dir else None
    for seq, (el, vname, box, desc, ov) in enumerate(ENTRIES[n], 1):
        d = T.ELEMENTS[el]; zone = d['zone']; pt = info['page_type']
        vid = f"e{n:02d}_{seq:02d}"
        rel = f"catalog/{pt}/{zone}/{el}/{vid}.png"
        os.makedirs(f"{ROOT}/catalog/{pt}/{zone}/{el}", exist_ok=True)
        x0, y0, x1, y1 = box
        Image.open(f"{ROOT}/{info['path']}").convert('RGB').crop((max(0,x0),max(0,y0),min(im.width,x1),min(im.height,y1))).save(f"{ROOT}/{rel}")
        vg, matched = VG.group(el, vname)
        if not matched: ungrouped.add((el, vname))
        v = dict(id=vid, source_image=info['path'], crop_path=rel, crop_box=list(box),
                 page_type=pt, zone=zone, element=el, variant_name=vname, variant_group=vg, description=desc,
                 input_style=d['input_style'], footprint_dots=footprint(box, REGIONS[n]),
                 draw_effort=d['draw_effort'], daily_effort=d['daily_effort'], skip_tolerance=d['skip_tolerance'],
                 hobonichi_overlap=d['hobonichi_overlap'], hobonichi_note=d['hobonichi_note'] + ' (unverified)',
                 adhd_notes=d['adhd_notes'], sensory_notes=d['sensory_notes'],
                 product_group=info['product_group'], duplicate_of_image=info.get('duplicate_of'))
        for k, val in ov.items():
            if k == 'adhd+': v['adhd_notes'] += ' ' + val
            elif k == 'sens+': v['sensory_notes'] += ' ' + val
            else: v[KEYMAP[k]] = val
        tree.setdefault(pt, {'zones': {}})['zones'].setdefault(zone, {'elements': {}})['elements'].setdefault(el, {'label': d['label'], 'variants': []})['variants'].append(v)
        names.setdefault((el, vname), set()).add(n); n_total += 1
        if qa:
            qa.rectangle(box, outline=(255, 0, 255), width=3); qa.text((x0 + 4, y0 + 4), f"{seq}", fill=(255, 0, 255))
    if qa_dir:
        os.makedirs(qa_dir, exist_ok=True); im.save(f"{qa_dir}/{n}.png")
meta = dict(hierarchy=['page_type', 'zone', 'element', 'variant'], zones=T.ZONES, input_styles=T.INPUT_STYLES,
            rubric=dict(draw_effort='1-3 time to hand-draw', daily_effort='1-3 daily fill-in load',
                        skip_tolerance='high = forgiving if a day is skipped; low = looks broken/guilt-inducing',
                        footprint_dots='approx width x height in dots at 5 mm pitch; portrait page 28x42, spread 56x42',
                        hobonichi_overlap='general knowledge only; unverified until user supplies Hobonichi photos'),
            images_covered=sorted(ENTRIES), variant_count=n_total)
json.dump(dict(meta=meta, pages=tree), open(f'{ROOT}/data/elements.json', 'w'), indent=1, ensure_ascii=False)
print(n_total, 'variants from', len(ENTRIES), 'images')
print(len(ungrouped), 'single-style variants use their own name as group')
for (el, vn), s in sorted(names.items()): print(f"  {el} :: {vn}  [{','.join(map(str,sorted(s)))}]")
