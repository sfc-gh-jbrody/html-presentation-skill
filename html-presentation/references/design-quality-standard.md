# HTML slide design quality standard

## Reference and intent

Use content-specific composition, deliberate hierarchy, and dimensional treatment for all HTML decks and standalone slides. Preserve the audience's voice and technical detail; do not copy exemplar decks' promotional language or unsupported claims.

The standard is a system for making decisions, not one template to repeat.

## Reusable layout patterns

These patterns are self-contained guidance; no private reference deck is required. If the user supplies an exemplar, inspect it locally and generalize its visual mechanisms without copying customer or business content. Embed approved fonts and block remote requests during review.

| Pattern | Visual mechanism worth preserving | Appropriate use | Avoid copying |
|---|---|---|---|
| Temporal progression | Shared rail, clear temporal direction, repeated milestones, selective emphasis on the relevant endpoint | Evolution, migration sequence, maturity changes | Tiny chips at presentation size; emphasis implying an unproven recommendation |
| Responsibility layers | Unequal layer sizes communicate changing responsibility; one emphasized platform layer and a directional rail | Architecture, responsibility, control/data separation | Fixed generic layer names or its marketing conclusion |
| Aligned comparison | Aligned comparison rows; colored headers and category markers; depth without clutter | Ownership, retained/retired assets, before/after | Automatic green-good/amber-bad meaning or forced closing CTA |
| Operating capabilities | Clear icon-label-explanation hierarchy, white elevated panels and selective high-contrast focus | Parallel operating capabilities | Card grid as universal fallback; slogan or repetitive conclusion banner |

## Visual vocabulary

Use `templates/briefing-design.css`, inlined into the output.

- White and pale blue are the working surfaces. Deep blue is a focal surface. Green and amber identify explicit, labeled categories or conditions only.
- Use a consistent spacing scale: 8, 16, 24, 32, 48, 64 logical pixels.
- One primary focal treatment per slide. Secondary panels can be quiet. Shadows separate layers; do not give every panel equal visual weight.
- Rounded corners, local line icons, chips and eyebrows have a purpose. Remove any that simply restate adjacent copy.
- At a 1920-wide logical canvas: title approximately 48-60px, body 24-28px, supporting labels 20-22px. Smaller sources can be 16-18px; never put a necessary qualification in illegible footnote text.
- Equal semantic roles have equal typography. Column labels and body cells remain consistent, even where a cell has a tinted background.
- Prefer neutral sentence-case titles. Accent only the phrase carrying the structural distinction, not arbitrary keywords.
- Embed fonts and assets. Inline SVG line icons are allowed; icon libraries may not require internet access.
- Use labeled connectors and legends when meaning is not obvious. Color is never the sole carrier of status or ownership.

## Content-led layout selection

| Audience question | Preferred structure |
|---|---|
| Where does responsibility sit? | Account lanes / ownership bands |
| What changes over time? | Timeline or aligned operating states |
| How does something work? | Input-transform-output or annotated flow |
| What differs between alternatives? | Aligned comparison / decision matrix |
| What must happen before action? | Dependency graph / explicit gates |
| What does this phase produce? | Transformation from inputs to reviewed artifact, with example fields |
| What evidence establishes readiness? | Evidence-to-condition mapping / acceptance panel |
| Which features serve which requirements? | Staged mechanism with feature labels and operational conditions |

Detailed phase slides must contribute new substance: concrete artifact, worked example, dependency, boundary, or tradeoff. Shared principles belong on their own slide or in one consistent legend, not repeated as prose throughout the deck.

## Storyboard acceptance

Each slide has a unique question, new information, source, visual grammar, focal element, and required qualifications. Inspect neighboring slides together. Do not accept a slide whose only distinction is its phase number.

Review three consecutive identical primary layouts. Either explain the comparison purpose or redesign the explanation. This is an editorial warning, not a mandatory random-layout quota.

Do not invent an illustrative number or customer-specific ownership assignment. Hypothetical examples must be labeled. Detailed executive briefings are not subject to a universal word limit or seven-slide cap. Fit density to the communication task and verify legibility at actual viewing size.

## Review and release gates

1. **Factual:** source-backed claims; provisional designs labeled; qualifiers preserved; no inappropriate absolute guarantees.
2. **Editorial:** every slide adds information; no repeated summary-as-body; no promotional default ending; sequence answers the audience's questions.
3. **Visual:** hierarchy is obvious; focal treatment meaningful; layouts explain relationships; typography, spacing and category colors consistent.
4. **Rendered:** inspect all slides individually plus a contact sheet. Check clipping, small text, overlays, footer collision, icon fallback, visual monotony and empty-space imbalance.
5. **Runtime:** arrows/buttons, first/last states, assets offline, narrow viewport, and print if requested.

Automated scripts can flag geometry and repeated layouts; they cannot approve prose or composition. Human/agent visual review is recorded separately from structural checks. Keep review records local and mark user acceptance pending until obtained.

## Regression examples

- Phase-grid repetition: activities list plus rationale/readiness sidebars on nearly every phase. Replace with phase-specific artifacts and mechanisms; do not merely recolor the cards.
- Repeated current/foundation/target flows: assign separate roles to these slides or combine them; swapping labels in the same diagram is insufficient.
- Missing readiness-column labels: always label columns when their role is not self-evident.
- Unequal row typography: do not inflate a label merely because it sits in a bubble.

## Maintenance

Keep this reference and the portable CSS in the registered skill. The global memory reminder routes here. Preserve user-supplied exemplar files. When new slides are accepted as exemplars, record why they succeeded and add a generalized pattern rather than embedding private project assumptions into global defaults.
