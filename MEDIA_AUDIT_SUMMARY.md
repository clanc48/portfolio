# Portfolio Media Audit Summary

Branch: `wave-4-build-qualification`

All 12 fictional demo brands now have an audited, brand-aligned media system wired into their page layouts.

## Inventory

| Demo | Home | Page 2 | Page 3 | Page 4 | Page 5 | Unique assets |
|---|---:|---:|---:|---:|---:|---:|
| Blackridge Build Co. | 5 | Projects 3 | Services 1 | Process 1 | Contact 1 | 8 |
| ClearSpring Plumbing | 2 | Services 3 | Service Areas 1 | Reviews 1 | Request Service 1 | 8 |
| Ember & Thyme | 5 | Menu 4 | Story 2 | Events 3 | Reservations 1 | 8 |
| Forge & Field Supply | 4 | Shop 4 | Collections 3 | Field Journal 3 | Support 1 | 8 |
| Hale Mercer Legal | 2 | Practice Areas 3 | Attorneys 2 | Insights 3 | Consultation 1 | 8 |
| Juniper Row Realty | 3 | Properties 4 | Neighborhoods 3 | Agents 3 | Contact 1 | 8 |
| Northwell Family Health | 2 | Services 3 | Providers 3 | Patient Resources 1 | Appointments 1 | 8 |
| Open Table Project | 3 | Programs 4 | Impact 2 | Get Involved 3 | Donate 1 | 8 |
| OrbitStack | 3 | Product 2 | Solutions 2 | Pricing 1 | Docs 2 | 8 |
| Redline Motorworks | 3 | Services 3 | Builds 4 | Performance 2 | Book Service 1 | 8 |
| The Alder House | 3 | Rooms 4 | Experiences 3 | Journal 3 | Book 1 | 8 |
| Static Bloom Studio | 4 | Work 4 | Services 2 | Studio 2 | Contact 1 | 8 |

**Totals:** 96 unique media assets, 147 deliberate page placements across 60 pages.

## Format contract

- Portfolio delivery format: SVG with a 1600×1000 viewBox (8:5 landscape).
- SVG is used here because it is resolution-independent, lightweight, and safe to write through the connected GitHub workflow.
- Every site has its own `MEDIA_AUDIT.md` in the site media directory with exact page-to-asset mapping.
- CSS uses cover/overlay treatment so text contrast remains controlled.
- For a real client deployment using photography, retain the slot names/selectors and replace the art with optimized AVIF/WebP exports as appropriate.

## Brand alignment

Each visual set follows the supplied 12-brand board: luxury contractor, restaurant, law firm, family health, real estate, outdoor e-commerce, automotive, nonprofit, SaaS, plumbing, boutique hotel, and creative agency. Palettes and visual motifs are isolated per demo so the portfolio does not read as one repeated template.

## Verification

`scripts/verify_media.py` checks that every audited site has its manifest, at least eight SVG media assets, and no missing local media URL referenced from its primary stylesheet.
