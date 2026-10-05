# Batch 6: the user's own Hobonichi pages (25 daily, 26 weekly). Coordinates are read off a 2000x1500 display of a 2576x1932 original.
K = 2576 / 2000
def B(x0, y0, x1, y1): return (round(x0*K), round(y0*K), round(x1*K), round(y1*K))
REGIONS = {25: B(270,225,1665,1265) + ('spread',), 26: B(305,205,1790,1315) + ('spread',)}
ENTRIES = {
25: [
 ('date_header','boxed date: month, big day number, weekday tab, moon phase, day-of-year',B(377,275,596,347),'Printed box: small month, large day number, weekday tab (Sunday in a colour block), moon-phase glyph and day-of-year.',{'adhd+':'Already printed, so zero setup.'}),
 ('time_blocks','vertical 24h axis (3-hour labels) over fine grid',B(365,358,700,790),'Hour labels down the left edge every 3 hours with tick dots between, over a fine square grid that runs the full page.',{'daily':2,'adhd+':'Axis is a guide only; the open grid does not demand every hour be filled.','sens+':'Grid is pale and even; very low noise.'}),
 ('notes','full-page fine square grid',B(365,360,975,1100),'Whole writing area is a pale fine grid with no boxes or prompts.',{}),
 ('quote_mantra','printed quote at page foot',B(390,1098,785,1195),'Small grey quote text from an interview at the foot of the page; attribution on the facing page.',{}),
 ('monthly_calendar','tiny month grid with current day circled',B(1485,1110,1600,1205),'Mini month calendar at the foot of the right page with the current date ringed.',{}),
 ('month_year_strip','edge month tab',B(1578,890,1640,945),'Coloured square tab with the month number sitting on the page edge.',{}),
 ('date_header','boxed date (facing page)',B(1012,278,1236,352),'Same box layout for the next day, with a thin weekday tab.',{}),
],
26: [
 ('week_header','month banner: year, month, big month name',B(340,272,575,350),'Dark banner at top left with year and month in kanji and a big OCT.',{}),
 ('monthly_calendar','mini month with current week ringed + week number',B(415,355,545,515),'"41st week" label over a small month calendar; the current week is ringed and Sundays are coloured.',{}),
 ('notes','grid free space beside month block',B(415,545,575,1215),'Narrow strip of fine grid under the mini calendar for week notes.',{}),
 ('date_header','date number + weekday tag per column (Sunday in red)',B(575,258,1760,305),'Each column starts with a large date number and a boxed weekday tag; Saturday dark, Sunday red.',{}),
 ('time_blocks','hourly tick axis per day column over grid',B(575,315,720,1250),'Hour labels (5 to 4) with tick marks down the left of each day column; fine grid behind.',{'daily':2,'adhd+':'Hourly labels are quiet; tasks can be written at any size.'}),
 ('week_at_a_glance','7 vertical day columns each with 24h axis',B(575,258,1760,1260),'Seven tall columns (Mon-Sun) across a spread, each with its own date tag and axis.',{'draw':3,'adhd+':'Very tall columns suit time-blocking, but empty hours may read as unfilled.','sens+':'Pale lines and even spacing; low noise.'}),
],
}
