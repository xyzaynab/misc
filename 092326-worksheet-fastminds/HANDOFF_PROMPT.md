# Handoff prompt — expanding or reconciling this workbook

Copy-paste the block below into a fresh Claude Code session to pick this project back up. Fill in the bracketed parts first.

---

I'm expanding a printable recovery/health workbook I built with Claude previously (FAST MINDS, an ADHD workbook). I want to [add worksheets from `[book/resource name]` / reconcile it with `[other guide name]` / add materials from my IOP program], following the same design system.

Read `DESIGN_SYSTEM.md` in this project first — it documents the typeface (Gaegu headers / Noto Sans body), color tokens, the four-stage "Worksheet Rhythm" (ORIENT / NOTICE / WORK WITH IT / CARRY FORWARD), the reusable HTML components (`.prompt-box`, `.dot-grid`, `.checklist-item`, guide boxes, Key Points pages, appendix templates), and the print-margin setup. Also skim `fast_minds_printable_workbook.html` directly as the working example — copy its actual CSS classes rather than reinventing them.

New material to add: [describe what you're adding — book title, author, which chapters/sections, or "worksheets from my IOP intake packet," etc. Attach the source PDF(s) if you have them.]

Important constraints, learned the hard way last time:
1. **Don't copy the source's prose verbatim.** Extract the structure (guiding questions, key points, worksheet fields) faithfully, but write the instructional/orienting text in your own words. Large verbatim extraction of a copyrighted book gets blocked by content filtering anyway, so paraphrase from the start.
2. **Match the existing rhythm stages** — don't just dump new pages in. Figure out which of ORIENT/NOTICE/WORK WITH IT/CARRY FORWARD each new exercise is, and badge it accordingly.
3. **Blank response areas are dot-grids, not underscored lines.** Reuse the `.dot-grid-*` size classes.
4. **Renumber pages programmatically after every structural edit** — don't hand-edit `<span>Page N</span>` values. There's a python renumbering snippet pattern used throughout the build history if you need to reconstruct it (regex over the page footers in document order).
5. **Render and visually check every new/changed page before calling it done** — use headless Chrome (`--print-to-pdf --no-pdf-header-footer`) and read the resulting PDF pages back as images to catch overflow before shipping. This caught real bugs every single time we skipped straight to "looks right in the code."
6. **For any print variant involving page rotation or multiple pages per sheet, do it at the PDF level (PyMuPDF / a PDF tool), not via CSS transforms inside Chrome's print pipeline** — that combination produced silently wrong output every time.

If reconciling two guides into one: tell me explicitly whether you want them merged into a single continuous chapter sequence, kept as separate labeled sections/parts within one book, or produced as separate files that share the same design system. That's a real content decision, not just a layout one — don't let me guess.
