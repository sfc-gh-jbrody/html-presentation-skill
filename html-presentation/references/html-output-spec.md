# Legacy shell output spec

This reference describes the legacy shell helpers, not the default design workflow. `design-quality-standard.md` and the installed `html-authoring` safety rules take precedence. The structural conventions below apply when using that shell; direct-authored slides follow `SKILL.md` instead.

Final output must be a self-contained HTML file with embedded approved fonts and images, or system fonts and inline SVG. The legacy shell still contains remote font links: remove or embed them before delivery. No runtime CDN requests are permitted.

**Slide Structure:** Each slide MUST follow this exact structure:
```html
<div id="sN" class="slide">
  <div class="slide-inner">
    [content]
  </div>
  <!-- optional: <div class="speaker-notes">...</div> -->
</div>
```
The `.slide-inner` wrapper is mandatory — it applies the standardized padding `clamp(1rem, 3.5vh, 2.75rem) clamp(1rem, 3.5vw, 3rem)` and `max-width: min(1600px, 96vw)`. Slides without it will display content flush to the slide edge or in wrong positions. Exception: title slides with `class="slide gradient-bg"` may place ambient glow orbs before `.slide-inner`.

**Layout:** Fullscreen slides (100vw × 100vh), content centered, max-width `min(1600px, 96vw)`, padding `clamp(1rem, 3.5vh, 2.75rem) clamp(1rem, 3.5vw, 3rem)`. Fill viewport — don't waste space with large side margins.

**Colors (theme-aware — reference the CSS vars, never hardcode):** The shell sets these per theme via the `<body>` theme class.
- **Light theme (DEFAULT):** background `#FFFFFF`, text `#1A2331`, secondary `#5B6776`, cards `#FFFFFF` (soft shadow), borders `#E2E8F0`, plus a thin accent gradient band across the top of every slide. Snowflake blue `#29B5E8` is the default accent.
- **Dark theme (`--theme dark`):** background `#0a0a0a`, text `#ffffff`, secondary `#a0a0a0`, cards `#1a1a1a`, borders `#2a2a2a`.
- One accent per deck (see `references/accent-colors.md`). Use `var(--bg)`, `var(--text)`, `var(--secondary)`, `var(--card)`, `var(--border)`, `var(--accent)` so slides adapt to either theme — do not hardcode background/text hex values.

**Typography:** Use relative units — no hardcoded `px` for font sizes or spacing. Reference values:
- H2 slide titles: `clamp(2.75rem, 4.4vw, 5rem)`
- H3 eyebrow labels: `clamp(1rem, 1.5vw, 1.35rem)`
- Body / list items: `clamp(1.2rem, 1.9vw, 2rem)`
- Stat numbers: `clamp(4.4rem, 7.7vw, 6.6rem)` in accent color
- Code blocks: `clamp(1rem, 1.4vw, 1.35rem)` monospace
- Small captions: `clamp(0.875rem, 1.2vw, 1.1rem)`

For spacing (padding, margin, gap) use `vh`/`vw` or `rem` instead of `px`. `px` is acceptable only for `border-width`, `border-radius`, and `letter-spacing` — **never for `font-size`** (including Material Icon sizes, which must use `rem` like all other font sizes) and never for layout dimensions.

**Navigation:** Arrow keys, counter in bottom-right, click-to-advance. Nav block MUST be preceded by `<div class="counter"></div>` — required by `generate_qr_appendix.py` as insertion point. Renders as frosted-glass pill fixed bottom-right with accent arrow buttons. JS init block MUST include `document.getElementById('total').textContent = slides.length;` before `show(0)` — self-corrects counter at runtime.

**Slide Transitions:** Fade crossfade via `opacity` + `pointer-events`. Never toggle `display: none / display: flex` — breaks CSS transitions.

**Speaker Notes:**

> [CONDITION: skip this block if `speaker_notes: false` in config]

When requested, store each slide's notes in hidden `<div class="speaker-notes">` inside the slide. Two mutually exclusive modes — opening one closes the other:

**Speaker notes formatting rule:** Text presenter reads aloud = plain prose. Text **not** meant to be spoken — stage directions, click cues, reminders — MUST be wrapped in square brackets: `[Pause here]`, `[Click to advance]`, `[Reference the chart on the left]`.
- `N` — popup window (dual-monitor)
- `B` — bottom panel that shrinks slide area upward (single-monitor)

Read `references/presentation-runtime.md` for complete nav HTML/CSS, slide transition CSS, speaker notes CSS/HTML/JS.

**Visuals:** Use inline SVG for diagrams, flow arrows, progress rings. CSS gradients (radial, linear, conic) for decorative backgrounds. All visual elements self-contained — no external images. **Material Symbols Rounded** is the icon system — ALWAYS use `class="material-symbols-rounded"`. NEVER use `class="material-icons"` (legacy API; renders icon names as literal text instead of glyphs). Icons default to filled style (`FILL:1`) via shell CSS; override with `style="font-variation-settings:'FILL' 0;"` for outlined.

**CSS Animations:** Read `references/css-animations.md` for approved patterns (fade-in, stagger, counter roll-up, progress ring, SVG draw, pulse) and rules including `prefers-reduced-motion`.
