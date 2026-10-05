"""Phase 3: build data/recurrence.json and notes/comparison.md from data/elements.json.
Unit of analysis = (product_group, page_type): a product's weekly design and its daily design are separate examples;
several images of the same product + page type count once.  Own Hobonichi pages are reported separately, not counted."""
import json, os, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); sys.path.insert(0, HERE)
import taxonomy as T
from commentary import COMMENTARY

imgs = {i['file']: i for i in json.load(open(f'{ROOT}/data/images.json'))['images']}
el = json.load(open(f'{ROOT}/data/elements.json'))
units = defaultdict(set)
for f, i in imgs.items():
    if not i['is_own']: units[(i['page_type'], i['product_group'])].add(f)
N = {pt: sum(1 for k in units if k[0] == pt) for pt in ('weekly', 'daily')}
def tier(n, of):
    if of == 0 or n == 0: return None
    p = n / of
    return 'Core' if p >= 0.5 else 'Common' if p >= 0.25 else 'Niche'
RANK = {'Core': 3, 'Common': 2, 'Niche': 1, None: 0}
def label(u): return f"{u[1]} [{', '.join(sorted(units[u], key=lambda s: int(s.split('.')[0])))}]"

pres = defaultdict(lambda: defaultdict(set))                          # element -> pt -> units
vpres = defaultdict(lambda: defaultdict(lambda: defaultdict(set)))    # element -> group -> pt -> units
vnames = defaultdict(lambda: defaultdict(set)); own = defaultdict(list); hob = {}
for pt, P in el['pages'].items():
    for z, Z in P['zones'].items():
        for e, E in Z['elements'].items():
            for v in E['variants']:
                hob[e] = (v['hobonichi_overlap'], v['hobonichi_note'])
                if v['is_own']: own[e].append(v['id']); continue
                u = (pt, v['product_group']); pres[e][pt].add(u); vpres[e][v['variant_group']][pt].add(u); vnames[e][v['variant_group']].add(v['variant_name'])

out = {'meta': dict(unit='(product_group, page_type)', examples_counted={k: N[k] for k in N}, examples_total=sum(N.values()),
        tier_rule='Core: in >=50% of that page type\'s examples; Common: 25-49%; Niche: <25%. Overall tier = best of the two page types.',
        caveat='Many source images are marketing shots showing only part of a page, so every count is a floor.',
        units={pt: [label(u) for u in sorted(units) if u[0] == pt] for pt in N}), 'elements': {}}
for e, d in T.ELEMENTS.items():
    c = {pt: dict(n=len(pres[e][pt]), of=N[pt], pct=round(100 * len(pres[e][pt]) / N[pt]), units=[label(u) for u in sorted(pres[e][pt])]) for pt in N}
    tw, td = tier(c['weekly']['n'], N['weekly']), tier(c['daily']['n'], N['daily'])
    ov = tw if RANK[tw] >= RANK[td] else td
    vs = []
    for g, byp in vpres[e].items():
        vc = {pt: dict(n=len(byp[pt]), of=N[pt], units=[label(u) for u in sorted(byp[pt])]) for pt in N}
        tot = sum(vc[pt]['n'] for pt in N)
        vs.append(dict(variant_group=g, example_variant_names=sorted(vnames[e][g]), counts=vc, total=tot,
                       tier={pt: tier(vc[pt]['n'], N[pt]) for pt in N}))
    vs.sort(key=lambda v: -v['total'])
    for i, v in enumerate(vs): v['rank_in_element'] = i + 1
    out['elements'][e] = dict(label=d['label'], zone=d['zone'], counts=c, tier=dict(weekly=tw, daily=td, overall=ov),
        overall=dict(n=c['weekly']['n'] + c['daily']['n'], of=N['weekly'] + N['daily']),
        variants=vs, hobonichi=dict(overlap=hob.get(e, (d['hobonichi_overlap'], d['hobonichi_note']))[0], note=hob.get(e, (d['hobonichi_overlap'], d['hobonichi_note']))[1],
        on_users_hobonichi_pages=bool(own[e]), user_pages_variant_ids=own[e]), commentary=COMMENTARY[e],
        input_style=d['input_style'], draw_effort=d['draw_effort'], daily_effort=d['daily_effort'], skip_tolerance=d['skip_tolerance'])
json.dump(out, open(f'{ROOT}/data/recurrence.json', 'w'), indent=1, ensure_ascii=False)

# ---- markdown
Z = T.ZONES; E = out['elements']
def line(e):
    x = E[e]; return f"{x['label']} ({x['counts']['weekly']['n']}/{N['weekly']} weekly, {x['counts']['daily']['n']}/{N['daily']} daily)"
md = ["# Comparison and recommendations (Phase 3)", "",
 "How the elements recur across the examples, which variants win, and which book each belongs in. Numbers come from `data/recurrence.json`; the commentary is judgement.", "",
 "## How this was counted", "",
 f"- **Examples counted: {sum(N.values())}** ({N['weekly']} weekly, {N['daily']} daily). An example is a product's weekly design or its daily design. Several images of the same product and page type count once (so 12 and 15, and 18 and 19, each count once).",
 "- A product shown as both weekly and daily counts in both (for example the Habit/ANT journal: images 23 and 24).",
 "- **Tiers:** Core = in 50% or more of that page type's examples. Common = 25-49%. Niche = under 25%. An element's overall tier is its best tier across weekly and daily.",
 "- **Counts are floors.** Many images are marketing shots showing part of a page, so an element may exist where I did not see it.",
 "- Your own Hobonichi pages (images 25, 26) are not counted as examples; they are used to verify overlap.", "",
 "## Tier summary", ""]
for pt in ('weekly', 'daily'):
    md.append(f"### {pt.capitalize()} ({N[pt]} examples)"); md.append("")
    for t in ('Core', 'Common'):
        es = sorted([e for e in E if E[e]['tier'][pt] == t], key=lambda e: -E[e]['counts'][pt]['n'])
        md.append(f"- **{t}:** " + (', '.join(f"{E[e]['label']} ({E[e]['counts'][pt]['n']})" for e in es) or 'none'))
    nn = sorted([e for e in E if E[e]['tier'][pt] == 'Niche'], key=lambda e: -E[e]['counts'][pt]['n'])
    md.append(f"- **Niche:** " + ', '.join(f"{E[e]['label']} ({E[e]['counts'][pt]['n']})" for e in nn)); md.append("")
md += ["## Leading variants of the most recurring elements", "", "Per element, the variant style used by the most examples (weekly + daily).", ""]
core_all = sorted([e for e in E if E[e]['tier']['overall'] in ('Core',)], key=lambda e: -E[e]['overall']['n'])
com_all = sorted([e for e in E if E[e]['tier']['overall'] == 'Common'], key=lambda e: -E[e]['overall']['n'])
for e in core_all + com_all:
    vs = E[e]['variants'][:4]
    md.append(f"- **{E[e]['label']}**: " + '; '.join(f"{v['variant_group']} ({v['total']})" for v in vs))
md += ["", "## Element by element", "", "Each entry: what it is for, the best variant for you, pros and cons, ADHD fit, sensory fit, and which book it belongs in. Tier shown for weekly / daily.", ""]
for z in Z:
    es = [e for e in E if E[e]['zone'] == z]
    if not es: continue
    md.append(f"### {z.capitalize()}"); md.append("")
    for e in sorted(es, key=lambda e: -E[e]['overall']['n']):
        x = E[e]; c = x['commentary']; h = x['hobonichi']
        md += [f"#### {x['label']}", f"*Tier: weekly {x['tier']['weekly'] or 'n/a'}, daily {x['tier']['daily'] or 'n/a'}. Seen in {x['counts']['weekly']['n']}/{N['weekly']} weekly and {x['counts']['daily']['n']}/{N['daily']} daily examples. Draw effort {x['draw_effort']}/3, daily effort {x['daily_effort']}/3, skip tolerance {x['skip_tolerance']}.*", "",
               f"- **For:** {c['purpose']}", f"- **Best variant for you:** {c['best']}", f"- **Pros:** {c['pros']}", f"- **Cons:** {c['cons']}",
               f"- **ADHD fit:** {c['adhd']}", f"- **Sensory fit:** {c['sensory']}",
               f"- **Belongs in:** {c['home'].capitalize()}. {c['home_note']} (Hobonichi overlap: {h['overlap']}.)", ""]
md += ["## Which book: the short version", "",
 "**Already in your Hobonichi (do not redraw):** " + ', '.join(E[e]['label'] for e in E if E[e]['hobonichi']['overlap'] == 'full' and '(verified' in E[e]['hobonichi']['note']) + ".", "",
 "**Natural homes for the notebook** (not printed in the Hobonichi): top priorities, to-do list, habit tracker, wins, brain dump, mood/energy/water trackers, weekly review prompts, gratitude, tomorrow's first step.", "",
 "## Starter set (my suggestion, not a decision)", "",
 "Built mostly from Core and Common elements, and kept off anything the Hobonichi already prints (hours, calendar, date box). Everything is small enough to draw in a few minutes with a pen and ruler.", "",
 "### Weekly spread (two facing pages, 56 x 42 dots)", "",
 "1. **Week header + one weekly focus line** (week header and focus line; Core and Common). One line each, set once.",
 "2. **Top 3 priorities** (Core): three numbered lines.",
 "3. **Weekly to-do parking list** (to-do list, Common): 5-6 checkbox lines.",
 "4. **Habit tracker** (Core weekly): 2-3 habit rows by 7 day boxes. Weekly grids stay forgiving if days are missed.",
 "5. **Wins + next week** (wins and improve-next, Common): a small wins box and one \"what to continue or change\" line.",
 "6. **Dotted free space** (notes, Core): leave a block of plain dots, no boxes.",
 "",
 "Skip: the day-by-day hour columns (your Hobonichi already does this), the mini calendar and the printed date box.", "",
 "### Daily page (one page, 28 x 42 dots)", "",
 "1. **Date line** (small; skip it if you already date the page in the Hobonichi).",
 "2. **Top 3 priorities** (Core): three numbered lines.",
 "3. **Other tasks** (secondary tasks, Common): 4-5 checkbox lines.",
 "4. **Brain dump / free space** (Core): the largest block, plain dots.",
 "5. **One win or highlight + tomorrow's first step** (Common/Niche): two single lines at the foot, a gentle restart cue after a skipped day.",
 "",
 "Skip: hour blocks (Hobonichi), printed quote (Hobonichi), mini calendar.", "",
 "### Optional add-ons (pick 2-3)", "",
 "- **Mood face or energy bar** (one mark, no writing).",
 "- **Water drops** (a row of 8, easy wins).",
 "- **Reward line** (pairs a priority with a concrete payoff).",
 "- **Meds/body check** (3-4 tiny boxes) if reminders help.", "",
 "### Why these", "",
 "- **Forgiving of skipped days:** blank lines and open dotted space do not look broken; there is no hourly grid to leave empty and no streak chart that punishes a gap.",
 "- **Fast to set up:** about eight ruled lines and one grid per page.",
 "- **Low visual noise (sensory):** no colour coding or icons required; clear edges between zones; one idea per zone.",
 "- **Hobonichi split:** the Hobonichi keeps time, dates and the calendar; the notebook holds intentions, tasks, trackers and reflection.", ""]
open(f'{ROOT}/notes/comparison.md', 'w').write('\n'.join(md))
print('ok', N, len(md), 'lines')
