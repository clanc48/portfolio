# Portfolio Demo Lab

A multi-stack portfolio containing twelve independently branded five-page website demos.

## Current milestone: Wave 4 — Build Qualification

- **Wave 1:** frameworks and exact five-page hierarchy.
- **Wave 2:** twelve independent responsive design systems.
- **Wave 3:** substantive content, industry-specific interactions, accessibility, metadata, and schema.
- **Wave 4:** exact direct dependency pins, missing framework bootstraps, executable smoke tests, and multi-stack production-build CI.

Documentation:

- [Wave 1 — Site Hierarchy](./WAVE_1_SITE_HIERARCHY.md)
- [Wave 2 — Design Systems](./WAVE_2_DESIGN_SYSTEMS.md)
- [Wave 3 — Content, Interactions, SEO & Accessibility](./WAVE_3_CONTENT_INTERACTIONS_SEO.md)
- [Wave 4 — Build Qualification](./WAVE_4_BUILD_QUALIFICATION.md)

## Local structural validation

```bash
python scripts/verify_wave3.py
python scripts/verify_wave4.py
```

## Build qualification

GitHub Actions performs framework-native qualification:

- Django / Flask / FastAPI HTTP smoke tests.
- Next.js / Astro / SvelteKit / Nuxt production builds.
- Laravel Composer install, route enumeration, Blade compilation, and HTTP smoke rendering.

A site is not described as build-qualified until its CI job is green.
