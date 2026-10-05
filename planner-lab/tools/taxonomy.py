"""Controlled vocabulary for the element hierarchy.

Page type -> Zone -> Element -> Variant.  Zones and elements are fixed here so
that nothing gets flattened or invented silently.  Per-variant overrides are
applied in the entries files.

skip_tolerance: high = forgiving if a day is missed, low = looks broken / guilt-inducing.
draw_effort / daily_effort: 1 (light) .. 3 (heavy).
Hobonichi notes are from general knowledge of the Techo (daily page with time
axis, monthly calendar, grid paper, a printed quote) and are UNVERIFIED until
photos of the user's own Hobonichi pages are added.
"""
ZONES = ["header", "plan", "schedule", "track", "reflect", "capture", "decorative"]
PAGE_TYPES = ["weekly", "daily", "other"]
INPUT_STYLES = ["checkbox", "write-in line", "color-in", "scale/rating", "free space", "time grid"]

def E(zone, label, inp, draw, daily, skip, hob, hob_note, adhd, sens):
    return dict(zone=zone, label=label, input_style=inp, draw_effort=draw, daily_effort=daily,
                skip_tolerance=skip, hobonichi_overlap=hob, hobonichi_note=hob_note,
                adhd_notes=adhd, sensory_notes=sens)

ELEMENTS = {
 # ---- header
 "date_header": E("header","Date header","write-in line",1,1,"high","full","Printed on every Hobonichi page.",
    "Cheap anchor; one line, no decision needed.","Predictable position; very low noise."),
 "week_header": E("header","Week header (date range / week number)","write-in line",1,1,"high","full","Weeks/Techo print week range and week number.",
    "Set once per spread; makes the page findable later.","Quiet, fixed position."),
 "focus_theme": E("header","Weekly/daily focus, theme or intention","write-in line",1,1,"high","none","No dedicated field.",
    "One short phrase is a good re-entry cue after a skipped stretch.","Minimal."),
 "quote_mantra": E("header","Quote or mantra","write-in line",2,1,"high","partial","Techo prints a daily quote; no personal mantra field.",
    "Optional; copying a quote each day becomes a chore.","Calm if short; text-heavy if long."),
 "month_year_strip": E("header","Month / day-of-month strip","color-in",2,1,"high","full","Hobonichi has monthly calendars and date tabs.",
    "Orients you but is fiddly to draw; one mark per page.","Colour-coded versions add noise; plain is better."),
 "weekday_circles": E("header","Weekday circles (M T W T F S S)","color-in",1,1,"high","partial","Dated pages already show the weekday.",
    "One tap to say which day it is; useful for undated pages.","Tiny, regular, quiet."),
 # ---- plan
 "top_priorities": E("plan","Top priorities (1-3)","write-in line",1,2,"high","partial","Not printed; users write them into the free grid.",
    "Capping at 3 limits overwhelm; blank lines don't read as failure.","Few lines = low density."),
 "focus_box": E("plan","Single focus box","free space",1,1,"high","none","No dedicated field.",
    "One thing only; very ADHD-friendly if kept to one line.","One open box; clear edge."),
 "todo_list": E("plan","To-do list","checkbox",2,2,"medium","partial","Free grid is used for lists; no printed to-do.",
    "Long lists breed overwhelm; unfilled checkboxes pile up guilt.","Many repeated lines/boxes add visual noise."),
 "secondary_tasks": E("plan","Secondary tasks (do later / other / everything else)","checkbox",2,2,"high","none","No dedicated field.",
    "Gives a parking spot so the priority list stays short.","Boxes are clearly separate from priorities."),
 "weekly_goals": E("plan","Weekly goals","write-in line",1,1,"high","none","No dedicated field.",
    "Set once a week; low daily load.","Few lines."),
 "focus_areas": E("plan","Focus-area task lists","checkbox",3,2,"medium","none","No dedicated field.",
    "Good for project grouping but many lists to maintain.","Multi-column dense grid: high visual noise."),
 "one_three_five": E("plan","1-3-5 task ladder (1 focus, 3 support, 5 tiny)","checkbox",3,3,"low","none","No dedicated field.",
    "Strong structure but heavy daily asks; looks very empty if skipped.","Dense, many icons and zones."),
 "not_to_do": E("plan","Not-to-do list","checkbox",1,1,"high","none","No dedicated field.",
    "Optional guard-rail list; can be skipped.","Small box."),
 "event_organizer": E("plan","Event / date table","write-in line",2,1,"high","partial","Monthly calendar and week pages cover dates.",
    "Writing each event once is easy; skipping is harmless.","Two-column table, clear grid."),
 "appointments": E("plan","Appointments (time + write-in)","write-in line",1,1,"high","full","Time axis / calendar covers appointments.",
    "Small list; only fills when needed.","Few lines."),
 "to_buy": E("plan","Shopping / to-buy list","checkbox",1,1,"high","none","Not printed; commonly kept in free notes.",
    "Capture list that doesn't need daily upkeep.","Simple box list."),
 "people_to_connect": E("plan","People to connect with","write-in line",2,1,"high","none","No dedicated field.",
    "Names rather than tasks lowers friction for reaching out; optional.","Small icons per row add noise; plain lines are enough."),
 "sorted_task_hub": E("plan","Sorted task hub (call / email / text / do soon ...)","checkbox",3,3,"low","none","No dedicated field.",
    "Reduces what-do-I-do-next, but 12 zones is a lot to fill.","Colour-coded grid is high noise; plain version better."),
 # ---- schedule
 "week_at_a_glance": E("schedule","Week at a glance (7-day layout)","free space",2,2,"medium","full","Weekly spread in Weeks/Cousin; Techo has week pages.",
    "Whole week visible at once; missing days leave blank boxes.","Clear day edges are good; many boxes can be busy."),
 "time_blocks": E("schedule","Time blocks / hourly schedule","time grid",2,3,"low","full","Techo daily page has a time axis.",
    "Blank hours feel like failure; high daily upkeep.","Ruled lines are calm; multiple columns less so."),
 "day_part_schedule": E("schedule","Day-part schedule (morning / afternoon / evening)","checkbox",2,2,"medium","partial","Time axis is finer; no day-part labels.",
    "Softer than hourly blocks; fewer decisions.","Section rules give clear zones."),
 "time_record": E("schedule","Time record (colour-in timeline)","color-in",2,2,"medium","full","Hobonichi time axis is used the same way.",
    "Done after the fact, so no planning pressure; can be skipped.","Needs a colour palette; plain pen shading works."),
 "monthly_calendar": E("schedule","Mini monthly calendar","free space",3,1,"high","full","Hobonichi has monthly spreads.",
    "Reference only; duplicate of Hobonichi.","Small grid text can be hard to read."),
 "clock_planner": E("schedule","Clock face planner","color-in",2,2,"medium","none","No dedicated field.",
    "Visual time awareness helps some; others find it fiddly.","Round shape breaks the grid."),
 # ---- track
 "habit_tracker": E("track","Habit tracker","checkbox",2,2,"medium","partial","Techo users add their own; not printed.",
    "Streak gaps feel punishing; weekly grids limit the damage.","Repeated boxes are regular but busy."),
 "mood_tracker": E("track","Mood tracker","scale/rating",2,1,"high","none","No dedicated field.",
    "Fast single mark; emotional check-in without writing.","Faces are quick; wheel versions are heavy."),
 "energy_tracker": E("track","Energy / battery tracker","scale/rating",1,1,"high","none","No dedicated field.",
    "One quick shaded bar; informs pacing.","Simple."),
 "productivity_rating": E("track","Productivity rating","scale/rating",1,1,"high","none","No dedicated field.",
    "Self-scoring productivity can feed guilt; keep optional.","Simple."),
 "water_tracker": E("track","Water tracker","color-in",1,1,"high","none","No dedicated field.",
    "Visible, easy wins; drops fill as you drink.","Row of icons, quiet."),
 "meals": E("track","Meals","write-in line",1,2,"high","none","Not printed; Techo users log food in the free grid.",
    "Useful for medication/eating reminders; skip is fine.","Four lines, calm."),
 "weather": E("track","Weather","scale/rating",1,1,"high","partial","Some Techo editions have a weather field.",
    "One circle; trivial.","Small icons, quiet."),
 "self_care_grid": E("track","Self-care icon grid","checkbox",3,2,"high","none","No dedicated field.",
    "Icons make it quick; drawing 12 icons is heavy.","Icon grid is busy; keep icons simple."),
 "health_fitness": E("track","Health / fitness / body check","checkbox",1,2,"high","none","No dedicated field.",
    "Short checklist (water, meds, move); good if kept to 3-4 items.","Small boxes."),
 "sleep_times": E("track","Sleep / wake times","write-in line",1,1,"high","partial","Techo time axis can show sleep.",
    "Two numbers a day.","Tiny."),
 # ---- reflect
 "gratitude": E("reflect","Gratitude","write-in line",1,1,"high","none","No dedicated field.",
    "Fast positive prompt; fine to skip.","Open lines are calm."),
 "wins": E("reflect","Wins / small wins","write-in line",1,1,"high","none","No dedicated field.",
    "Reward-focused; counters 'I did nothing'.","Few lines."),
 "highlight_of_day": E("reflect","Highlight / happy moment","write-in line",1,1,"high","none","No dedicated field.",
    "One line; easy to finish.","One box."),
 "lessons_learned": E("reflect","Lessons learned","write-in line",1,1,"high","none","No dedicated field.",
    "Can feel evaluative; keep optional.","Few lines."),
 "review_prompts": E("reflect","Review prompts (open questions)","write-in line",2,2,"medium","none","No dedicated field.",
    "Many prompts = high effort; one prompt is manageable.","Prompt text adds reading load."),
 "priority_review": E("reflect","Priority progress review","write-in line",1,1,"high","none","No dedicated field.",
    "Fast % check-in.","Simple."),
 "improve_next": E("reflect","Improve / continue-or-change next","write-in line",1,1,"high","none","No dedicated field.",
    "Forward-looking; avoids blame.","Few lines."),
 "challenge": E("reflect","Intentional challenge","write-in line",1,1,"high","none","No dedicated field.",
    "One optional challenge a week; low load.","One box."),
 "end_of_day_check": E("reflect","End-of-day assessment","checkbox",1,1,"high","none","No dedicated field.",
    "Three kind options only (no 'failed'); safe if skipped.","Three boxes."),
 "reward": E("reflect","Reward","write-in line",1,1,"high","none","No dedicated field.",
    "Pairs effort with a payoff; strong for ADHD motivation if the reward is concrete.","One line."),
 "tomorrow_first_step": E("reflect","Tomorrow's first step","write-in line",1,1,"high","none","No dedicated field.",
    "Great for starting again after a gap.","Single line."),
 "feelings_check": E("reflect","Feelings check-in","scale/rating",1,1,"high","none","No dedicated field.",
    "Name an emotion with one circle.","Faces/words in a row."),
 "leave_behind": E("reflect","Leave behind / release","write-in line",1,1,"high","none","No dedicated field.",
    "Optional venting spot.","Small box."),
 "identity_statement": E("reflect","Identity / intention statement","write-in line",1,1,"high","none","No dedicated field.",
    "Short, set once and reused.","Simple."),
 "mood_impact": E("reflect","What impacted my mood","write-in line",2,1,"high","none","No dedicated field.",
    "Weekly sorting task; good pattern-finding, heavy if every day.","Three columns, clear edges."),
 "life_area_goals": E("reflect","Goals by life area","write-in line",2,1,"high","none","No dedicated field.",
    "Six boxes can overwhelm; pick 2-3.","Boxed layout, moderately busy."),
 "resistance_check": E("reflect","Resistance / ANTs-and-PETs check","write-in line",2,2,"medium","none","No dedicated field.",
    "Therapy-style prompts; heavy daily asks.","Text-dense."),
 # ---- capture
 "brain_dump": E("capture","Brain dump","free space",1,1,"high","partial","Free grid can be used as a brain dump.",
    "Fast, no sorting; forgiving.","Open box, quiet."),
 "notes": E("capture","Notes / free space","free space",1,1,"high","full","Grid / free pages in Hobonichi.",
    "Catch-all; reduces pressure on other zones.","Ruled or dotted = calm."),
 # ---- decorative
 "color_key": E("decorative","Colour key / legend","color-in",1,1,"high","none","No dedicated field.",
    "Cuts decisions by pre-assigning meaning; needs 3 pens.","Adds colour; keep to 2-3."),
 "banner": E("decorative","Banner / ribbon label","write-in line",1,1,"high","none","No dedicated field.",
    "Decorative; purely cosmetic.","Keep subtle."),
}

# Verified from the user's own Hobonichi photos (images 25, 26): element -> (overlap, note)
VERIFIED_HOB = {
 "date_header": ("full", "Printed date box on every day: month, big day number, weekday tab (Sunday in a colour block), moon phase and day-of-year."),
 "week_header": ("full", "Weekly spread prints a month banner (year, month, big month name) and the week number."),
 "time_blocks": ("full", "Daily page has a vertical 24-hour axis (labelled every 3 h); weekly columns label every hour. Grid behind both."),
 "time_record": ("full", "The same 24-hour axis over a grid works for colouring time after the fact."),
 "appointments": ("full", "Time axis covers timed appointments."),
 "week_at_a_glance": ("full", "Weekly spread is seven vertical day columns, each with a 24-hour axis."),
 "monthly_calendar": ("full", "Mini month grid with the current week/day circled on both the daily and weekly pages."),
 "notes": ("full", "Whole writing area is a fine grid; free-write space is the default."),
 "quote_mantra": ("full", "A printed quote sits at the foot of each daily page (not user-written)."),
 "month_year_strip": ("partial", "Coloured month tabs on the page edge; no day-of-month strip."),
 "brain_dump": ("partial", "The open grid doubles as a brain dump."),
}
