# Wave 4 — Build Qualification

Wave 4 changes the portfolio from structurally complete demos into independently build-checked applications.

## Qualification architecture

### Python
- Blackridge Build Co. — Django
- ClearSpring Plumbing — Django
- Northwell Family Health — Flask
- Open Table Project — FastAPI + Jinja

Each runtime dependency is pinned exactly. CI compiles the Python source and performs HTTP smoke requests against all five routes. The Django and Flask form demos also receive a POST smoke request.

### Node
CI performs a clean `npm install` followed by the framework production build for:
- Ember & Thyme — Next.js
- Juniper Row Realty — Next.js
- Redline Motorworks — Next.js
- Forge & Field Supply — Astro
- Static Bloom Studio — Astro
- OrbitStack — SvelteKit
- The Alder House — Nuxt

Direct Node dependencies are exact-version pinned. OrbitStack now includes the missing Vite/SvelteKit application bootstrap files required for an actual production build.

### PHP
Hale Mercer Legal is now a bootstrapped Laravel 12 application rather than a loose routes/views sample. Wave 4 adds:
- Artisan runtime
- Laravel application bootstrap
- application provider
- app/cache/session/view/logging configuration needed by the demo runtime
- public front controller
- console routes
- runtime storage directories
- environment example
- HTTP route smoke test

CI installs Composer dependencies, generates a local application key, enumerates routes, compiles Blade views, runs the custom status command, and renders all five pages through Laravel's HTTP kernel.

## CI

`.github/workflows/portfolio-build.yml` contains independent jobs for:
1. structural contracts,
2. Python runtime smoke tests,
3. seven Node production builds,
4. Laravel bootstrap/view/HTTP qualification.

The matrix uses `fail-fast: false` so one broken demo does not hide failures in the other demos.

## Dependency policy

Wave 4 pins direct runtime/build dependencies to exact versions instead of floating caret/range specifications. Transitive package locks are not claimed until generated and committed from successful framework installs.

## Definition of qualified

A demo is Wave-4-qualified only after its relevant GitHub Actions job completes successfully. Repository structure alone is not treated as build evidence.
