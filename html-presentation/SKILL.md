---
name: html-presentation
description: "Create, revise, restyle, and review ALL HTML presentation slides: complete decks, single slides, executive briefings, technical briefings, and slide diagrams. Uses a content-led visual quality standard, content-led layouts, and rendered review. Invoke even for a standalone HTML slide or an already-approved outline. Not for ordinary HTML reports or non-HTML presentation exports."
---

# HTML Presentation

## Scope and precedence

This is the presentation-design entry point for HTML slides across workspaces. Load `html-authoring` as well for HTML safety and provenance requirements. User requirements override defaults; safety requirements remain mandatory.

**Read `references/design-quality-standard.md` before planning or changing slides.** It governs content, design, and acceptance. Older component/reference examples are implementation aids, not competing instructions. Do not inherit their automatic agenda, BLUF, CTA, QR appendix, remote-font links, word caps, forced dark theme, or executive seven-slide cap.

Use `templates/briefing-design.css` for new light-theme slides. Inline its CSS into the deliverable; never ship a runtime dependency on a skill folder. User-supplied exemplar decks are design references, not a source of customer facts or reusable sales language.

## Defaults

- White canvas, Snowflake blue, deep-blue focus surfaces, restrained shadows and tinted panels.
- 1920 x 1080 logical canvas, fit to viewport; narrow screens reflow or provide an explicitly tested reading mode.
- Embedded fonts and icons or system fonts and local inline SVG. No runtime network dependencies.
- Neutral descriptive sentence-case titles and factual prose. No slogans, CTA strips, forced first/second-person language, or marketing conclusions.
- Speaker notes off unless requested. Slide count follows the user's scope and necessary explanation, not job title.
- Detailed executive briefings are valid. No universal word cap; establish hierarchy and readability instead of deleting necessary qualifications.
- Existing approved source/outline/preferences count as answers. Ask only for a genuinely missing decision.

## Workflow

### 1. Establish content and purpose

Read the supplied sources and relevant existing deck before editing. Preserve unrelated changes. Record audience, presentation versus read-ahead use, requested depth, source boundaries, and required output format. Do not mine additional customer sources without authorization.

For a small revision, do the revision directly and validate affected slides. For a single slide, use the same design standard without full-deck ceremony. For a substantial deck, maintain a storyboard and build/QA status in the project. Keep provenance and internal quality notes out of rendered customer copy.

### 2. Storyboard the explanation

For each slide define:

| Field | Purpose |
|---|---|
| Question answered | The specific audience need |
| New information | What this slide adds beyond its neighbors |
| Evidence/source | Facts, example, or clearly identified proposed design |
| Visual grammar | Timeline, lanes, layers, comparison, matrix, decision flow, evidence, etc. |
| Focal element | What the viewer should inspect first |
| Required detail | Qualifications and implementation details that must survive |

Use source sections as inputs, not a mandatory slide list. Avoid repeated principle statements on every phase. Give each phase its own mechanism, artifact, dependency, or decision to explain. Repeated layouts are appropriate for deliberate comparison, not as an automatic phase template. Three consecutive identical primary layouts trigger editorial review; do not introduce random variety to satisfy a quota.

If material decisions remain, enter plan mode BEFORE `create_plan`, then seek approval. If the user already authorized a concrete demonstration or outline, proceed without re-asking.

### 3. Design and build

Choose content-specific layouts using the pattern guide. Establish common typography, spacing, legend meanings, and footer/navigation once. Use deep surfaces and shadows to establish importance, not on every container. Preserve labels and evidence; never invent metrics to fill a design.

Build one representative dense slide early to calibrate readability. Save incrementally. Direct authoring is supported; delegation is optional and subject to available tools. If delegating, give each writer the full storyboard, shared CSS, quality standard, current and neighboring slide purpose, source facts, and notes setting. Writers must not invent their own theme or modify the shared shell concurrently.

For new decks use `.slide` wrappers, `.body` or `[data-slide-content]` content regions, `.footer` or `[data-slide-footer]` footer regions, `data-layout` naming the primary grammar, unique slide IDs, and a local navigation mechanism. Include a `snowflake-report-metadata` JSON block mapping each slide ID to provenance. Use `data-purpose` to record the slide's unique question for editorial inspection. All required visible content must exist in the authored HTML, not only in speaker notes.

Legacy helpers remain available via `scripts/run_script.py`: `generate_shell.py`, `insert_slide.py`, `replace_slide.py`, `embed_image.py`, `svg_calc.py`, and image helpers. Inspect generated shells for remote resources and incompatible defaults before use. Do not interpret legacy validator rules as permission to remove necessary detail or insert a CTA.

### 4. Verify structure, render, and review

Use `scripts/render_review.py` for local self-contained decks, or equivalent browser tooling. It blocks runtime network access, captures every slide, produces a contact sheet, and reports basic geometry, asset, navigation, and narrow-screen checks. It does not evaluate factual correctness or design quality.

```bash
uv run --with playwright --with Pillow python /absolute/skill/scripts/render_review.py /absolute/deck.html --output /absolute/review-directory
```

The output directory must be new or explicitly authorized for replacement. The script uses installed Google Chrome when available; otherwise install Playwright Chromium explicitly. Do not upload confidential slides to external rendering services.

Review **every slide image and the contact sheet**. Apply the editorial/visual rubric in the quality standard. Re-render after fixes. For dense slides also inspect at a normal 1280 x 720 viewing size. Test navigation separately; screenshots alone do not prove it works.

Record separate outcomes:
- Structural/runtime checks: pass, fail, or untested.
- Rendered visual review: pass, needs revision, or unverified.
- Editorial/factual review: pass, needs revision, or unverified.
- User acceptance: pending or accepted.

If tools are unavailable or the user declines checks, state the limitation. Never call the deck presentation-ready on static validation alone. Never bypass a declined tool by silently performing the same action elsewhere.

### 5. Deliver and iterate

Return the local deck and contact sheet with a concise summary of changes and actual validation. Preserve the original when demonstrating an alternative. Do not replace it unless requested.

Re-render changed slides after copy/layout edits, and review the whole contact sheet after reordering or introducing a layout change. Ask only for meaningful design decisions or acceptance; do not repeatedly request known settings.

PowerPoint export is optional and only offered/performed when relevant. Existing `export_to_pptx.py` produces rasterized slides, not editable slide elements; disclose that if used.

## Reusable references

- `references/design-quality-standard.md`: required content/design rubric and reusable layout patterns.
- `templates/briefing-design.css`: portable tokens, surfaces, typography, responsive utilities.
- `scripts/render_review.py`: offline rendering and structural checks with screenshots/contact sheet.
- `references/content-rules.md`: factual discipline and supporting content rules.
- `references/graphics-embedding.md`: local image/font embedding patterns; apply HTML safety rules over obsolete CDN examples.
- `references/visual-components.md`: additional component ideas, adapted to current palette and safety constraints.

## Durable installation

For a local installation, register the `html-presentation-skill/html-presentation` directory. Changes then apply to that installed source, not the bundled application directory. Commit local changes before updating the skill repository. Do not modify the skill registry, hooks, or profile prompts unnecessarily. Use the user's global memory index as a routing reminder, not as the only copy of the design standard.
