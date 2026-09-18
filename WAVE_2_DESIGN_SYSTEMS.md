# Wave 2 — Layout Architecture & Design Systems

Wave 2 converts the twelve Wave 1 route shells into distinct branded interface systems. Each demo retains exactly five top-level pages while gaining shared chrome, responsive rules, typography/color tokens, reusable component classes, and a unique homepage composition.

| Demo | Stack | Typography | Core palette | Homepage architecture |
|---|---|---|---|---|
| Blackridge Build Co. | Django / Python | Cormorant Garamond + Inter | Charcoal #141414, Limestone #D6CBB8, Bronze #8B6F47, Warm White #F8F7F4 | Architectural editorial hero, credibility rail, asymmetric project grid |
| Ember & Thyme | Next.js / TypeScript | Fraunces + Source Sans 3 | Ember #C2410C, Sage #556B2F, Cream #EADCC8, Espresso #2B1B12 | Split culinary hero, sensory plate treatment, menu rail, dish gallery |
| Hale Mercer Legal | Laravel / PHP | Libre Baskerville + Manrope | Navy #0F2D5B, Oxblood #8B1E3F, Parchment #E8E1D6, Slate #2F3E46 | Authority-led editorial hero, proof strip, practice focus, counsel band |
| Northwell Family Health | Flask / Python | DM Sans + Merriweather | Teal #28A6A6, Mist Blue #94C5D3, Mist #EEF8FA, Navy #18344A | Reassuring care hero, care-orbit visual, pathway cards, low-friction care band |
| Juniper Row Realty | Next.js / TypeScript | Playfair Display + Inter | Deep Green #183A2E, Ivory #EDE8DD, Clay #B06F52, Black #0F0F0F | Editorial property hero, listing facts bar, property mosaic, neighborhood intelligence |
| Forge & Field Supply | Astro / TypeScript | Archivo Black + IBM Plex Sans | Forest #1F4D2E, Sand #D4A373, Rust #B7410E, Ink #1A1A1A | Rugged catalog hero, category rail, product field picks, journal section |
| Redline Motorworks | Next.js / TypeScript | Rajdhani + Inter | Black #050505, Steel #687280, Red #EF4444, White #F5F5F5 | Performance hero, vehicle stage, metrics rail, workshop cards, dyno treatment |
| Open Table Project | FastAPI + Jinja / Python | Nunito Sans + Lora | Sunflower #FFBF24, Sky #38BDF8, Navy #1E3A8A, Cream #F8F7F1 | Community-story hero, impact metrics, story mosaic, participation CTA |
| OrbitStack | SvelteKit / TypeScript | Space Grotesk + JetBrains Mono | Midnight #081026, Violet #7C3AED, Cyan #06B6D4, Gray #E5E7EB | SaaS terminal hero, operational metrics, primitive cards, architecture node map |
| ClearSpring Plumbing | Django / Python | Poppins + Roboto Slab | Cobalt #174A9B, Aqua #26C9BD, Sky #EAF7FF, Navy #16314B | Emergency/service chrome, trust hero, core-service cards, review proof band |
| The Alder House | Nuxt / Vue | Cormorant Garamond + Inter | Moss #2E382B, Burgundy #722F37, Bone #D9C9B8, Paper #F8F5EE | Quiet-luxury split hero, booking strip, room gallery, local experience band |
| Static Bloom Studio | Astro / TypeScript | Syne + Space Mono | Acid #EFFF00, Blue #2563EB, Black #000000, Off-white #F4F4F5 | Experimental oversized type, poster composition, kinetic ticker, asymmetric work grid |

## Shared Wave 2 requirements

- Brand-specific header and footer.
- Brand-specific design tokens rather than a shared theme.
- Responsive container/grid systems.
- Primary and secondary CTA treatments.
- Card, feature, proof, or information modules appropriate to the industry.
- Mobile breakpoints that collapse navigation and multi-column layouts.
- Distinct homepage composition for every demo.
- Secondary-page shells now inherit each site’s design system rather than standalone bare HTML.
- No demo imports another demo’s CSS or components.

## Scope boundary

Wave 2 establishes presentation architecture. Production content depth, real imagery/assets, form processing, structured data, accessibility QA, performance optimization, analytics, CMS/data integrations, and deployment qualification remain later waves.
