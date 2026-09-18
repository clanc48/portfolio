# Portfolio Demo Lab

A multi-stack portfolio containing twelve independently branded five-page website demos.

## Current milestone: Wave 3

Wave 1 established the frameworks and exact five-page hierarchy.

Wave 2 established twelve independent visual systems and responsive layout architectures.

Wave 3 adds substantive secondary-page content, industry-specific interaction patterns, forms/filters/toggles/search, accessibility semantics, metadata, structured-data markers, and structural CI verification.

Documentation:

- [Wave 1 — Site Hierarchy](./WAVE_1_SITE_HIERARCHY.md)
- [Wave 2 — Design Systems](./WAVE_2_DESIGN_SYSTEMS.md)
- [Wave 3 — Content, Interactions, SEO & Accessibility](./WAVE_3_CONTENT_INTERACTIONS_SEO.md)

## Validation

Run:

```bash
python scripts/verify_wave3.py
```

The verifier enforces the twelve-demo / sixty-page contract, shared layout and design-system presence, skip-link and structured-data markers, and at least one richer interaction path per demo.

## Architecture principle

These demos are intentionally not template reskins. Each site owns its framework conventions, brand language, information architecture, visual system, interaction pattern, and responsive behavior.
