"""Canonical variant groups so recurrence can be counted across images.

variant_name keeps the specific way one example draws an element; variant_group is the
shared style it falls under.  Rules are (substring of variant_name, group); first match wins.
Anything unmatched falls back to its own variant_name (and is reported by build.py).
"""
RULES = {
 'appointments': [('', 'time + write-in lines')],
 'banner': [('', 'colour label tab')],
 'brain_dump': [('ruled', 'ruled lines'), ('', 'open box with label')],
 'date_header': [('stacked', 'stacked DD / MM / YY boxes'), ('', 'date write-in line')],
 'end_of_day_check': [('kind options', 'three kind options'), ('', 'pre-sleep ritual line')],
 'energy_tracker': [('5-segment', 'segment bar to colour'), ('', 'notes by time of day')],
 'focus_box': [('goals', 'dotted goal lines'), ('', 'single titled box')],
 'focus_theme': [('sentence', 'sentence starter / frame'), ('goal-for', 'boxed goal line'), ('', 'short write-in line')],
 'gratitude': [('tick-box', 'tick-box checklist'), ('numbered', 'numbered lines'), ('', 'boxed list')],
 'habit_tracker': [('9 primary habits', 'named rows x 7-day dots / circles'), ('7 dots', 'named rows x 7-day dots / circles'),
                   ('secondary', 'secondary habits + reflection line'), ('checklist', 'checklist panels'),
                   ('tick column', 'rows with tick column (no days)'), ('', 'named rows x 7-day checkboxes')],
 'health_fitness': [('', 'short checkbox list')],
 'highlight_of_day': [('one line', 'one line'), ('', 'boxed')],
 'identity_statement': [('', 'prompted open box')],
 'improve_next': [('checkbox', 'checkbox rows'), ('two-column', 'two-column went well | improve'), ('open', 'open box'), ('', 'ruled lines')],
 'lessons_learned': [('checkbox', 'checkbox / numbered lines'), ('numbered', 'checkbox / numbered lines'), ('', 'open box')],
 'meals': [('single', 'single line'), ('', 'per-meal fields')],
 'month_year_strip': [('plain', 'plain strip'), ('', 'colour-coded strip')],
 'mood_tracker': [('wheel', 'circular wheel'), ('colour boxes', 'colour boxes + faces'), ('single face', 'single face'), ('', 'open band')],
 'notes': [('ruled', 'ruled page / lines'), ('dotted', 'dotted free space'), ('boxed', 'boxed area'), ('', 'unlined area')],
 'one_three_five': [('focus', '1 focus task'), ('support', '3 support tasks'), ('', '5 tiny wins')],
 'people_to_connect': [('', 'short list')],
 'priority_review': [('', 'score / percent field')],
 'productivity_rating': [('total', 'total time'), ('', 'open score row')],
 'quote_mantra': [('banner', 'banner affirmation'), ('title bar', 'banner affirmation'), ('', 'printed quote')],
 'resistance_check': [('', 'ANT / resistance prompts')],
 'review_prompts': [('two-column', 'two-column prompt'), ('ruled lines', 'prompt + ruled lines'), ('', 'prompt + open space')],
 'secondary_tasks': [('sub-steps', 'tasks with sub-steps + icons'), ('optional extras', 'optional numbered extras'), ('', 'checkbox / dotted lines')],
 'time_blocks': [('hour labels', 'hour-ruled lines'), ('time |', 'time | task | tick table'), ('vertical', 'vertical checkbox column'), ('', 'flexible time column')],
 'to_buy': [('', 'checkbox list')],
 'todo_list': [('numbered morning', 'routine lines + completed boxes'), ('bullet', 'bullet / numbered lines'), ('numbered', 'bullet / numbered lines'),
               ('', 'checkbox / circle lines')],
 'tomorrow_first_step': [('', 'labelled dotted line')],
 'top_priorities': [('5 numbered', '5+ numbered / bullet lines'), ('6 bullet', '5+ numbered / bullet lines'),
                    ('checkbox', '3 checkbox lines'), ('circle', '3 checkbox lines'),
                    ('time field', 'priority box with time'), ('two open', 'two open columns'), ('yellow panel', 'panel with rating icons + reward'),
                    ('numbered', '3 numbered lines')],
 'water_tracker': [('', 'row of drops / circles')],
 'week_at_a_glance': [('header', 'day boxes with header bars'), ('ruled', 'ruled day columns'), ('', 'stacked day rows')],
 'week_header': [('title only', 'title only'), ('WEEK n', 'title only'), ('date range', 'printed date range + week number'),
                 ('month/month', 'printed date range + week number'), ('', 'title + write-in date')],
 'weekday_circles': [('circles', 'letters over circles'), ('', 'letters only')],
 'weekly_goals': [('', '3 numbered lines')],
 'wins': [('checkbox', 'checkbox rows'), ('box', 'open / tinted box'), ('', 'numbered lines')],
}

def group(element, variant_name):
    for sub, g in RULES.get(element, []):
        if sub in variant_name:
            return g, True
    return variant_name, False
