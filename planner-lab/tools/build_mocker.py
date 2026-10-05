"""Build data/templates.json and site/mocker.html (self-contained) from elements.json, recurrence.json and templates.py."""
import json, os, statistics as st, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); sys.path.insert(0, HERE)
import taxonomy as T
from templates import TEMPLATES
el = json.load(open(f'{ROOT}/data/elements.json')); rec = json.load(open(f'{ROOT}/data/recurrence.json'))
vs = {}
for pt, P in el['pages'].items():
    for z, Z in P['zones'].items():
        for e, E in Z['elements'].items():
            for v in E['variants']:
                if not v['is_own']: vs.setdefault((e, v['variant_group']), []).append(v)
groups = []
for (e, g), lst in vs.items():
    r = rec['elements'][e]; v0 = lst[0]; key = f'{e}|{g}'
    rv = next((x for x in r['variants'] if x['variant_group'] == g), None)
    frm = {pt: dict(n=rv['counts'][pt]['n'], of=rv['counts'][pt]['of']) for pt in ('weekly', 'daily') if rv and rv['counts'][pt]['n']}
    groups.append(dict(id=key, element=e, el_label=r['label'], zone=r['zone'], group=g, names=sorted({v['variant_name'] for v in lst}),
        seen=frm, tier=r['tier'], draw=round(st.median(v['draw_effort'] for v in lst)), daily=round(st.median(v['daily_effort'] for v in lst)),
        skip=v0['skip_tolerance'], input=v0['input_style'], hob=v0['hobonichi_overlap'], hobnote=v0['hobonichi_note'],
        adhd=v0['adhd_notes'], sens=v0['sensory_notes'], fp=[int(st.median(v['footprint_dots'][0] for v in lst)), int(st.median(v['footprint_dots'][1] for v in lst))],
        home=r['commentary']['home'], home_note=r['commentary']['home_note'], t=TEMPLATES[key]))
order = {z: i for i, z in enumerate(T.ZONES)}
groups.sort(key=lambda g: (order[g['zone']], g['element'], g['group']))
json.dump({k: v for k, v in TEMPLATES.items()}, open(f'{ROOT}/data/templates.json', 'w'), indent=1, ensure_ascii=False)
data = dict(groups=groups, meta=dict(zones=T.ZONES, n=rec['meta']['examples_counted']))
blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
tpl = open(f'{HERE}/site_template_mocker.html').read().replace('__DATA__', blob)
head, rest = tpl.split('</style>\n', 1)
full = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        + head + '</style>\n</head>\n<body>\n' + rest + '\n</body>\n</html>\n')
open(f'{ROOT}/site/mocker.html', 'w').write(full)
if os.environ.get('FRAG'): open(os.environ['FRAG'], 'w').write(tpl)
print(len(groups), 'groups;', round(len(full) / 1e3), 'KB')
