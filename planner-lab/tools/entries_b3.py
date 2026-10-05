# Batch 3: images 12-16 (15 is a duplicate of 12: not extracted)
REGIONS = {12:(0,0,1195,890,'spread'), 13:(110,100,1200,1200,'portrait'), 14:(725,315,1480,1445,'portrait'),
           16:(0,0,1027,1500,'portrait')}
ENTRIES = {
12: [
 ('week_header','week-of write-in line',(20,82,345,108),'"Week of /" label with a ruled line, under a coloured top band.',{}),
 ('focus_theme','weekly focus line',(350,82,1170,108),'"Weekly focus:" long ruled line.',{}),
 ('focus_theme','sentence frame: this week will be ___ because ___',(350,118,1170,137),'Fill-in-the-blank sentence for theme and reason.',{}),
 ('week_at_a_glance','7 equal day boxes with shaded header',(22,140,1168,290),'Sun-Sat in one row; each shaded header has a date slash over an open dotted-divided box.',{'adhd+':'Short boxes force one-line highlights, not full lists.'}),
 ('top_priorities','3 numbered inline write-in lines',(315,305,1168,330),'Three numbered circles each with a short ruled line, in one row.',{}),
 ('focus_areas','titled column: header box + 8 circle-bullet lines (first 3 shaded)',(22,342,300,640),'A header box for the project/area name over eight circle-bullet lines; the first three are shaded to mark the priority tasks.',{}),
 ('habit_tracker','habit lines x 3x7 rounded checkboxes',(313,660,880,770),'Ruled habit lines at left, Sun-Sat header and rounded checkboxes in three rows.',{}),
 ('notes','dotted free space',(313,770,880,870),'Dotted grid beneath the daily tracker.',{}),
],
13: [
 ('time_blocks','vertical checkbox column + dotted lines (start .. optional mid-break)',(255,130,700,1200),'A column of small rounded checkboxes down the left of dotted time lines, with a labelled "start" and an optional "mid break" band in a warm colour.',{'draw':3,'daily':3,'skip':'low','adhd+':'Boxes become tiny wins as each block is done; an optional break is built in.','sens+':'Two-colour code (blue/orange) is clear but busy.'}),
 ('top_priorities','3 numbered tags + write-in lines (solid)',(655,215,1200,500),'Three filled numbered tags 01-03 each with a long write-in line; "Task description" hint under the first.',{'adhd+':'"Realistic expectations" message limits the day to 3 tasks.'}),
 ('secondary_tasks','optional extras 04-07 (outlined numbers)',(670,500,1200,815),'Four outlined numbers 04-07 with lines, under "Got extra time? Clear your mind and go for it!".',{}),
 ('notes','dotted free area with hour labels',(695,820,1200,1200),'"What else is going on today?" over a dotted grid with hour numbers at the left.',{}),
 ('banner','tinted title tab',(640,125,900,205),'Pale-blue title tab with product name.',{}),
],
14: [
 ('week_header','title only, no date',(750,355,1250,405),'Condensed caps title with no date field.',{}),
 ('wins','3 checkbox rows under pill label',(750,425,1100,580),'Pill label then three rows each with a square checkbox.',{}),
 ('lessons_learned','3 checkbox rows under pill label',(1118,425,1470,580),'Pill label then three rows each with a square checkbox.',{}),
 ('improve_next','3 checkbox rows under pill label',(750,595,1100,745),'Pill label then three rows each with a square checkbox.',{}),
 ('top_priorities','next-week priorities: 3 checkbox rows (one starred)',(1118,595,1470,745),'Pill label then three checkbox rows; a red star marks the key one.',{}),
 ('life_area_goals','6 shaded boxes in 2x3 (personal, career, ...)',(750,765,1470,1105),'Six labelled shaded boxes with one goal each.',{'adhd+':'Six areas can overwhelm; use two or three.'}),
 ('habit_tracker','numbered habit lines x M-S shaded cells (5 rows)',(750,1130,1470,1415),'Five numbered habit lines with a grid of shaded cells; tick marks fill them.',{}),
],
16: [
 ('date_header','title left, date write-in, day circles right',(55,50,975,105),'Large spaced title, a short "DATE /" write-in and a row of weekday circles.',{}),
 ('weekday_circles','S M T W T F S with circles',(720,55,975,105),'Seven letters each over an empty circle.',{}),
 ('quote_mantra','pill banner with affirmation',(55,112,970,145),'Dark rounded banner with a printed affirmation.',{}),
 ('focus_box','goals: 2 dotted lines',(55,170,487,280),'"Goals" heading, one dotted line and a solid rule.',{}),
 ('top_priorities','3 circle lines',(55,292,487,442),'Header then three circle bullets each with a dotted line.',{}),
 ('todo_list','9 circle lines',(55,455,487,852),'Header then nine circle bullets with dotted lines.',{}),
 ('brain_dump','ruled lines (notes / brain release)',(55,865,487,1222),'Eight solid ruled lines under "Notes / brain release".',{}),
 ('meals','single dotted line',(55,1275,487,1345),'One dotted line labelled meals.',{}),
 ('water_tracker','row of 8 circles',(55,1348,487,1388),'Eight empty circles beside the label.',{}),
 ('day_part_schedule','morning / afternoon / evening / night circle lines',(540,200,972,1265),'Four labelled sections (7, 7, 5, 3 lines) each line with a circle bullet; rules between sections.',{}),
 ('highlight_of_day','highlight: big or small, one line',(540,1275,972,1388),'Bold heading, hint, one dotted line.',{}),
],
}
