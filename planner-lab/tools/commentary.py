"""Per-element commentary for Phase 3 (judgement, not measurement).
Fields: purpose, best (variant_group or 'custom: ...'), pros, cons, adhd, sensory, home, home_note.
home: notebook | hobonichi | either.  The notebook extends the Hobonichi: it should not redraw what the
Hobonichi already prints (date box, hour axis, week columns, mini calendar, grid notes, quote)."""
C = lambda *a: dict(zip(['purpose','best','pros','cons','adhd','sensory','home','home_note'], a))
COMMENTARY = {
# header
'date_header': C('Says which day a page belongs to.','date write-in line','One line; findable later.','Needs writing every page.','Cheap anchor; no decision needed.','Fixed, quiet position.','either','Hobonichi prints a full date box. In the notebook keep it to one small line, or skip it on daily pages that pair with the Hobonichi date.'),
'week_header': C('Names the week (range and number).','custom: printed-style date range + week number','Makes a spread findable; set once per week.','Weekly numbers are fiddly to track by hand.','Once-a-week task, low load.','Quiet.','either','Hobonichi prints the month banner and week number. Notebook needs only a date range line.'),
'focus_theme': C('One short intention or theme for the week or day.','short write-in line','One line, no layout, easy re-entry cue after a gap.','Can feel vague if left unprompted.','Strong: one phrase, no sorting.','Minimal.','notebook','Hobonichi has no field for it.'),
'quote_mantra': C('A printed or written affirmation at the top.','banner affirmation','Sets tone; optional.','Copying a quote daily becomes a chore.','Optional only; fine to leave blank.','Calm if short.','either','Hobonichi already prints a daily quote. Skip in the notebook unless you want your own mantra.'),
'month_year_strip': C('Month/day orientation strip.','plain strip','Orients the page.','Fiddly to draw; the colour-coded versions are noisy.','One mark a day; low value.','Plain is calm; colour versions are busy.','hobonichi','Hobonichi has month tabs and calendars. Skip in the notebook.'),
'weekday_circles': C('Row of day letters to tick the current day.','letters over circles','Handy on undated pages.','Needless if you write the date.','Easy one-tap marker.','Tiny and regular.','either','Optional on daily pages; skip if the date is already written.'),
# plan
'top_priorities': C('Caps the day or week to a few must-dos.','3 numbered lines','Most common element; one tiny list; blank lines are neutral.','Three can still feel like three failures if all slip.','Core ADHD tool: small cap limits overwhelm.','Few lines, low density.','notebook','Hobonichi has no priority field.'),
'focus_box': C('A single "if only one thing" box.','single titled box','One box, one item.','Overlaps with top priorities.','Very friendly: choose one thing.','One open box with clear edge.','notebook','Use instead of, not as well as, top priorities if you want even less.'),
'todo_list': C('Open task list.','checkbox / circle lines','Familiar; flexible length.','Long lists breed overwhelm; unticked boxes pile up.','Keep to 5-6 lines so it never feels endless.','Many repeated lines add noise; use fewer lines.','notebook','Hobonichi grid works for lists but has no printed boxes.'),
'secondary_tasks': C('Parking spot for lower-priority tasks.','checkbox / dotted lines','Keeps priorities short.','Easy to ignore.','Helpful: lets you note it without committing.','Clearly separate from priorities.','notebook','No Hobonichi equivalent.'),
'weekly_goals': C('A few goals for the week.','3 numbered lines','Set once; short.','Overlaps top priorities.','Low daily load.','Few lines.','notebook','Use the weekly top-priorities list instead.'),
'focus_areas': C('Per-project or per-area task lists.','titled column with circle lines','Good for projects.','Many columns to maintain; heavy to draw.','Too much for most days.','Dense grid.','notebook','Only if you run several projects; otherwise skip.'),
'one_three_five': C('Structured daily ladder: 1 big, 3 medium, 5 small.','custom: a lighter version (1 focus + 3 + 5 plain lines, no icons)','Clear structure; tiny wins.','Heavy to draw and fill; empty looks like failure.','Powerful if it fits you; high risk of guilt on skipped days.','Icon strips are very busy.','notebook','Try a stripped-down version as an optional add-on.'),
'not_to_do': C('List of things to avoid today.','4 grey checkbox lines','Optional guard-rail.','Rarely used.','Optional.','Small box.','notebook','Optional add-on.'),
'event_organizer': C('Event/date table for the week.','custom: two-column event | date','Easy to scan.','Duplicates a calendar.','Easy; only fills when needed.','Clear grid.','hobonichi','Hobonichi week columns and calendar already carry events.'),
'appointments': C('Timed appointments.','time + write-in lines','Short, only when needed.','Duplicates the hour axis.','Quick.','Few lines.','hobonichi','The Hobonichi time axis covers it.'),
'to_buy': C('Shopping list.','checkbox list','Handy capture list.','Needs its own space.','Easy.','Simple.','notebook','Good dotted-page filler if wanted.'),
'people_to_connect': C('People to message or call.','short list','Names lower the barrier to reaching out.','Icon bullets are fiddly.','Nice optional prompt.','Plain lines are enough.','notebook','Optional add-on.'),
'sorted_task_hub': C('Twelve sorted zones (call, email, text, ...).','custom: 4 zones max','Reduces "what do I do next".','Twelve zones is too much to draw or fill.','High payoff but heavy; only if you like sorting.','Colour grid is busy.','notebook','Optional; consider a 4-zone mini version.'),
# schedule
'week_at_a_glance': C('Whole week visible at once.','day boxes with header bars','Clear day edges; whole week at a glance.','Seven boxes take much space.','Blank days read as neutral if no hours are printed.','Even boxes are calm.','hobonichi','Hobonichi weekly columns already do this with a 24-hour axis. Notebook could use only one-line day highlights.'),
'time_blocks': C('Plan or log the day by time.','custom: hobonichi hour axis','Strong for time awareness.','Blank hours feel like failure; heavy daily upkeep.','Risky for guilt when a day is skipped.','Ruled lines calm; multi-column dense.','hobonichi','Verified: your Hobonichi has the hour axis. Do not redraw it.'),
'day_part_schedule': C('Soft morning/afternoon/evening split.','morning / afternoon / evening / night circle lines','Gentler than hourly.','Still a lot of lines.','Better than hourly if you want some structure.','Section rules help.','either','Optional in the notebook if you want a softer structure than the Hobonichi axis.'),
'time_record': C('Colour in what actually happened.','vertical 24h timeline coloured with highlighters','No pre-planning pressure.','Needs highlighters.','Reflective, can be skipped.','Pastel bars; pen shading works.','hobonichi','Use the Hobonichi hour axis for this.'),
'monthly_calendar': C('Mini month for reference.','stacked mini month grids (Mon start)','Reference only.','Fiddly to draw.','No daily load.','Small text.','hobonichi','Hobonichi prints it. Skip.'),
'clock_planner': C('Clock face to shade blocks.','12-hour clock face to shade','Visual time awareness.','Round shape breaks the grid.','Helps some, fiddly for others.','Curved shape.','notebook','Optional curiosity.'),
# track
'habit_tracker': C('Weekly habit grid.','named rows x 7-day checkboxes','Most common tracker; weekly scope limits guilt.','Streak gaps can feel punishing; too many habits.','Keep to 2-3 habits.','Regular grid; fewer rows quieter.','notebook','Hobonichi has none printed.'),
'mood_tracker': C('Quick mood record.','single face','One mark, no writing.','Wheel is heavy.','Very friendly if one face.','Faces are quiet.','notebook','Optional add-on.'),
'energy_tracker': C('Daily energy level.','segment bar to colour','One quick shaded bar.','Needs a convention.','Informs pacing.','Simple.','notebook','Optional add-on.'),
'productivity_rating': C('Self-rating of the day.','open score row','Fast.','Can feed guilt.','Skip unless helpful.','Simple.','notebook','Skip by default.'),
'water_tracker': C('Water intake drops.','row of drops / circles','Easy wins.','Takes a little drawing.','Fun and fast.','Quiet row.','notebook','Optional add-on.'),
'meals': C('Meal log.','per-meal fields','Handy for eating/med reminders.','Another upkeep item.','Useful if meals slip; otherwise skip.','Simple lines.','notebook','Optional.'),
'weather': C('Weather icon row.','row of 5 weather icons','Trivial.','Low value.','Skip.','Quiet.','notebook','Skip.'),
'self_care_grid': C('Icon grid of self-care checks.','custom: 4 icons max','Quick ticks.','Drawing 12 icons is heavy.','Strong prompt; too many icons overwhelm.','Busy.','notebook','Optional; limit to 3-4 items.'),
'health_fitness': C('Short health/meds checklist.','short checkbox list','Visible reminder for meds, water, move.','Extra upkeep.','Good if it includes meds.','Small boxes.','notebook','Optional add-on.'),
'sleep_times': C('Sleep and wake times.','custom: two small boxes','Two numbers.','Another daily field.','Optional.','Tiny.','either','Hobonichi axis can show sleep; skip in notebook.'),
# reflect
'gratitude': C('Gratitude prompt.','boxed list','Fast positive.','Can feel forced.','Optional.','Open lines calm.','notebook','Optional.'),
'wins': C('Record small wins.','numbered lines','Counters "I did nothing".','Hard when mood is low.','Excellent anti-guilt tool; keep to 1-3.','Few lines.','notebook','No Hobonichi field.'),
'highlight_of_day': C('One highlight.','boxed','One line.','Overlaps wins.','Easy to finish.','One box.','notebook','Pick either this or wins.'),
'lessons_learned': C('Lessons from the week.','open box','Reflective.','Can feel evaluative.','Weekly only.','Open box.','notebook','Weekly add-on.'),
'review_prompts': C('Open reflection questions.','prompt + open space','Flexible.','Many prompts = heavy.','One prompt a week is plenty.','Prompt text adds reading.','notebook','Weekly add-on.'),
'priority_review': C('Score progress on priorities.','score / percent field','Fast.','Can feel judgemental.','Optional.','Simple.','notebook','Optional.'),
'improve_next': C('What to continue or change.','ruled lines','Forward-looking.','Another prompt.','Good if framed kindly.','Few lines.','notebook','Weekly add-on.'),
'challenge': C('Optional challenge.','single challenge box','Low load.','Optional.','Optional.','One box.','notebook','Optional add-on.'),
'end_of_day_check': C('Quick end-of-day check.','three kind options','No failure option.','Extra field.','Very friendly.','Three boxes.','notebook','Optional add-on.'),
'tomorrow_first_step': C('One next step for tomorrow.','labelled dotted line','Great restart cue after a gap.','Easy to forget.','Strong re-entry help.','One line.','notebook','Optional add-on.'),
'feelings_check': C('Name an emotion.','custom: row of 5 faces','One mark.','Needs faces.','Quick.','Quiet.','notebook','Optional.'),
'leave_behind': C('Release a worry.','boxed list','Vent space.','Optional.','Optional.','Small box.','notebook','Optional.'),
'identity_statement': C('Short statement of intent.','prompted open box','Sets tone.','Abstract.','Optional.','Simple.','notebook','Optional.'),
'mood_impact': C('Sort what affected mood.','3-column box','Pattern finding.','Needs weekly time.','Weekly only.','Clear edges.','notebook','Optional weekly.'),
'life_area_goals': C('Goals by life area.','custom: 2-3 boxes','Balanced view.','Six areas overwhelm.','Pick 2-3.','Boxed layout.','notebook','Optional.'),
'resistance_check': C('Therapy-style prompts.','ANT / resistance prompts','Insight.','Heavy.','Too heavy for daily.','Text-dense.','notebook','Skip unless you want it.'),
'reward': C('Pair a task with a reward.','custom: one reward line','Motivation.','Easy to forget.','Strong motivator if concrete.','One line.','notebook','Good light add-on.'),
# capture
'brain_dump': C('Unsorted dump space.','open box with label','No sorting, forgiving.','Open space can feel empty.','Great for racing thoughts.','Open box.','notebook','Hobonichi grid also works, but dotted notebook is ideal.'),
'notes': C('Free space.','dotted free space','Zero pressure; dots suit your notebook.','None.','Excellent: no demands.','Dots are calm.','either','Hobonichi has grid notes; the notebook dots are the natural free-write space.'),
# decorative
'color_key': C('Colour legend.','custom: 3 colours max','Cuts decisions.','Needs pens.','Good if pens are at hand.','Keep to 2-3.','notebook','Optional.'),
'banner': C('Label/ribbon style.','colour label tab','Visual structure.','Cosmetic.','Optional.','Keep subtle.','notebook','Optional.'),
}
