# FAST MINDS Workbook — Visual Design System

Reference doc for extending this workbook or reconciling it with other guides.
The full working example is `fast_minds_printable_workbook.html` — when in doubt, read that file; this doc explains *why* it's built the way it is so you don't have to re-derive it.

## Page mechanics

- Format: single HTML file, one `<div class="page">` per printed page, rendered to PDF via headless Chrome (`--print-to-pdf --no-pdf-header-footer`).
- Page size: US Letter, `8.5in x 11in`, `box-sizing: border-box`.
- **Margins are set ONLY on the `.page` div's own padding, never on the CSS `@page` rule.** `@page { margin: 0; }` is intentional — if `@page` also sets a margin, Chrome's print engine shrinks the whole page to fit inside an already-shrunk printable area, doubling every margin. This bit us once; don't reintroduce it.
- Current margins: `padding: 1.0in 0.55in 0.55in 1.0in` (top/right/bottom/left) — generous top *and* left because the workbook supports two binding styles (side gutter for a 3-ring binder, top gutter for a top-mounted folder / turned-sideways reading). If a future guide only needs one binding style, you can shrink the unused side.
- Every page ends with a `.footer-bar` containing `FAST MINDS • Chapter N` (left) and `Page N` (right). Page numbers are **not** hand-typed — after any edit that adds/removes a page, run a renumbering pass (regex over `<span>Page \d+</span>` in document order) rather than fixing numbers by hand.

## Typography

- Headers/titles: `'Gaegu', cursive` — the handwritten-marker look (`--font-title`). Used for all `<h1>`, `<h2>`, and section-style headers.
- Body text: `'Noto Sans', sans-serif` (`--font-body`). Used for everything else — paragraphs, table cells, checklist items, footer/header bars.
- Both loaded from Google Fonts in the `<head>`.
- `<h1>` ~2.1rem, `<h2>` ~1.25–1.75rem depending on context; sizes get dialed down page-by-page when a long title needs to fit one line (`font-size` inline override) rather than by shrinking the whole page's type scale.

## Color tokens (CSS custom properties on `:root`)

```
--primary: #1e293b        /* headers, primary text */
--primary-light: #334155
--accent: #4f46e5         /* indigo — prompt-box left border, bullet markers */
--accent-light: #e0e7ff
--bg-subtle: #f8fafc      /* table header bg, subtle fills */
--border-color: #cbd5e1   /* table borders, dot-grid box borders */
--text-main: #0f172a
--text-muted: #64748b     /* subheads, captions, "quick recap" lines */
--dot-color: #cbd5e1       /* the dot-grid pattern itself */
```

Rhythm-stage badge colors (small pill labels, not full backgrounds):
- `badge-orient` — light blue `#e0e7ff` / text `#3730a3`
- `badge-notice` — light amber `#fef3c7` / text `#92400e`
- `badge-work` — light green `#dcfce7` / text `#166534`
- `badge-carry` — light purple `#f3e8ff` / text `#6b21a8`
- `badge-review` — light red `#fee2e2` / text `#991b1b` (reusable forms / reference pages)

Key Points box: solid `#94a3b8` gray header bar, white uppercase bold text, bulleted list below in a bordered box (not a badge color — deliberately neutral so it doesn't compete with the rhythm badges).

All these pastel-bg/dark-text pairs hold up fine when converted to true grayscale (Ghostscript `DeviceGray`) — verified when we built the B&W version.

## The "Worksheet Rhythm" — the actual content model

This is the structural idea that makes the workbook feel coherent, not just a pile of forms. Every worksheet page is tagged with one rhythm-badge:

| Badge | Purpose |
|---|---|
| **ORIENT** | Brief context needed to understand the exercise |
| **NOTICE** | Recognition / self-inventory prompts |
| **WORK WITH IT** | The main writing / thought-record / planning exercise |
| **CARRY FORWARD** | Short synthesis or reusable takeaway |

When reconciling a new source book into this system, the first job is figuring out which rhythm stage each of *its* exercises maps to — don't just dump content in as generic pages.

## Recurring components (copy these patterns, don't reinvent)

- **`.prompt-box`** — light-bg, indigo left-border callout. Used for instructional/orienting text above an exercise. Write this in your own words, summarizing the source's guidance — **never paste the source's copyrighted prose verbatim** (copyright limits this to short quotes; long paraphrase is the safe and correct approach, and it's what we did throughout).
- **Guide box** (`guide_box()` pattern in the build scripts) — a tinted box with a small uppercase label and bulleted sub-questions, used to give a worksheet the "book's own voice" without copying its sentences. Comes in a couple of tint variants (indigo/notice-amber/work-green) to match the badge on that page.
- **`.dot-grid` / `.dot-grid-xs` / `.dot-grid-sm` / `.dot-grid-md` / `.dot-grid-lg` / `.dot-grid-full` / `.dot-grid-fill`** — the handwriting response areas. Prefer these over literal blank underscored lines everywhere; we converted every leftover blank-line pattern to dot-grid boxes as a deliberate style decision.
- **`.checklist-item` + `.checkbox`** — square checkbox self-inventory items.
- **`.rating-scale`** — 0–10 intensity scale, used in thought-record-style exercises.
- **Key Points page** — one per chapter, gray header bar + bullets + a final "One Thing I Want to Remember" dot-grid. Added to every chapter as a closing beat.
- **Appendix / reusable-form pages** — blank templates (Thought Record, Trait Tracker, etc.) live in lettered appendices at the back, separate from the in-chapter versions, matching how the source book itself separates "do this now" from "reusable tool for later."

## Print variants built for this workbook (all derived from the same HTML source)

1. **Standard portrait** — `FAST_MINDS_Printable_Workbook.pdf`, one 8.5x11 page per sheet.
2. **Rotated landscape** — same content, each page rotated 90° at the *PDF* level (not CSS — Chrome's print engine doesn't handle CSS `transform: rotate()` + `@page landscape` reliably together; use `rotate_pdf_pages` / a PDF tool instead). Left gutter lands on the long top edge, matching a top-mounted / turn-the-binder reading style.
3. **2-up stacked (11x17 Tabloid, portrait)** — two rotated-landscape pages stacked top/bottom, 1:1 scale, no shrinking. Built with PyMuPDF (`show_pdf_page` compositing), not Chrome print — same reliability issue as above.
4. **2-up side-by-side (17x11 Tabloid, landscape)** — two *original* portrait pages placed left/right at 1:1 scale (8.5×2 = 17 exactly, so no scaling waste). This is the one you'll likely reach for most.
5. **Grayscale** — any of the above run through Ghostscript (`-sColorConversionStrategy=Gray -dProcessColorModel=/DeviceGray`), which desaturates the actual vector content rather than rasterizing, so it stays crisp.

**Lesson learned, worth repeating:** for anything involving page rotation or multi-page-per-sheet imposition, don't fight Chrome's headless print CSS — do it at the PDF level (PyMuPDF or a PDF tool). CSS `transform: rotate()` on content inside a paginated print context produced silently wrong, unpredictable layouts every time we tried it.
