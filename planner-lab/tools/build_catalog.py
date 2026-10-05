"""Build site/catalog.html (self-contained: data and crops embedded) from data/elements.json + data/recurrence.json.
Also writes a fragment (no doctype/head/body) for publishing as an Artifact."""
import base64, io, json, os, sys
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); sys.path.insert(0, HERE)
import taxonomy as T
el = json.load(open(f'{ROOT}/data/elements.json')); rec = json.load(open(f'{ROOT}/data/recurrence.json'))

def img_uri(path, maxw=760):
    im = Image.open(f'{ROOT}/{path}').convert('RGB')
    if im.width > maxw: im = im.resize((maxw, max(1, round(im.height * maxw / im.width))), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'WEBP', quality=80, method=4)
    return 'data:image/webp;base64,' + base64.b64encode(b.getvalue()).decode(), im.width, im.height

rank = {(e, v['variant_group']): v['rank_in_element'] for e, x in rec['elements'].items() for v in x['variants']}
variants = []
for pt, P in el['pages'].items():
    for z, Z in P['zones'].items():
        for e, E in Z['elements'].items():
            for v in E['variants']:
                tier = rec['elements'][e]['tier'][pt]
                name = v['variant_name']
                uri, iw, ih = img_uri(v['crop_path'])
                variants.append(dict(id=v['id'], pt=pt, zone=z, el=e, name=name, desc=v['description'], img=uri, iw=iw, ih=ih,
                    fp=v['footprint_dots'], draw=v['draw_effort'], daily=v['daily_effort'], skip=v['skip_tolerance'], input=v['input_style'],
                    hob=v['hobonichi_overlap'], hobnote=v['hobonichi_note'], adhd=v['adhd_notes'], sens=v['sensory_notes'], own=v['is_own'],
                    src=v['source_image'].split('/', 1)[1] if '/' in v['source_image'] else v['source_image'], tier=tier,
                    rank=rank.get((e, v['variant_group']), 99),
                    hay=' '.join([name, v['description'], E['label'], v['adhd_notes'], v['sensory_notes'], v['input_style'], v['variant_group']]).lower()))
R = {e: dict(label=x['label'], c={pt: dict(n=x['counts'][pt]['n'], of=x['counts'][pt]['of']) for pt in ('weekly', 'daily')},
             tier={pt: x['tier'][pt] for pt in ('weekly', 'daily')}, hob=x['hobonichi']['overlap']) for e, x in rec['elements'].items()}
data = dict(variants=variants, rec=R, meta=dict(n=rec['meta']['examples_counted'], zones=T.ZONES, input_styles=T.INPUT_STYLES, elements=len(R)))
blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
tpl = open(f'{HERE}/site_template_catalog.html').read().replace('__DATA__', blob)
head, rest = tpl.split('</style>\n', 1)
full = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        + head + '</style>\n</head>\n<body>\n' + rest + '\n</body>\n</html>\n')
open(f'{ROOT}/site/catalog.html', 'w').write(full)
frag = os.environ.get('FRAG')
if frag: open(frag, 'w').write(tpl)
print(len(variants), 'variants;', round(len(full) / 1e6, 2), 'MB')
