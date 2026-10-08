# Presentation validation

Read `design-quality-standard.md` before reviewing. Structural checks do not establish visual or editorial quality.

1. Check authored source for unique slide IDs, provenance, offline assets, safe event listeners, and source-backed facts.
2. Run `scripts/render_review.py` against the local deck to capture every slide and generate a contact sheet. Use a fresh output directory. It blocks network requests; do not upload to rendering services.
3. Inspect every slide image and the full contact sheet. Compare with the annotated patterns in the quality standard. Check hierarchy, readability, redundancy, clipping, alignment, and purposeful contrast.
4. Test navigation and narrow-screen behavior. Check print only when required and report its status separately.
5. Fix issues and re-render affected slides; re-review the contact sheet for deck-wide changes.

Report independently: structural/runtime result, rendered visual review, editorial/factual review, and user acceptance. If visual review is skipped or unavailable, explicitly mark it unverified. Do not claim a design passes because a parser passes.

The older `validate_deck.py` can be used for its compatible structural checks on legacy shells. Its typography, animation, title, CDN, and required-slide conventions do not override the current quality standard. Do not delete useful content just to satisfy a legacy check.
