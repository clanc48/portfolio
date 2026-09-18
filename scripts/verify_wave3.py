from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

sites = {
    "blackridge-build-co": [
        "templates/home.html","templates/projects.html","templates/services.html","templates/process.html","templates/contact.html"
    ],
    "ember-and-thyme": [
        "app/page.tsx","app/menu/page.tsx","app/story/page.tsx","app/events/page.tsx","app/reservations/page.tsx"
    ],
    "hale-mercer-legal": [
        "resources/views/home.blade.php","resources/views/practice-areas.blade.php","resources/views/attorneys.blade.php","resources/views/insights.blade.php","resources/views/consultation.blade.php"
    ],
    "northwell-family-health": [
        "templates/home.html","templates/services.html","templates/providers.html","templates/patient-resources.html","templates/appointments.html"
    ],
    "juniper-row-realty": [
        "app/page.tsx","app/properties/page.tsx","app/neighborhoods/page.tsx","app/agents/page.tsx","app/contact/page.tsx"
    ],
    "forge-and-field-supply": [
        "src/pages/index.astro","src/pages/shop.astro","src/pages/collections.astro","src/pages/field-journal.astro","src/pages/support.astro"
    ],
    "redline-motorworks": [
        "app/page.tsx","app/services/page.tsx","app/builds/page.tsx","app/performance/page.tsx","app/book-service/page.tsx"
    ],
    "open-table-project": [
        "templates/home.html","templates/programs.html","templates/impact.html","templates/get-involved.html","templates/donate.html"
    ],
    "orbitstack": [
        "src/routes/+page.svelte","src/routes/product/+page.svelte","src/routes/solutions/+page.svelte","src/routes/pricing/+page.svelte","src/routes/docs/+page.svelte"
    ],
    "clearspring-plumbing": [
        "templates/home.html","templates/services.html","templates/service-areas.html","templates/reviews.html","templates/request-service.html"
    ],
    "the-alder-house": [
        "pages/index.vue","pages/rooms.vue","pages/experiences.vue","pages/journal.vue","pages/book.vue"
    ],
    "static-bloom-studio": [
        "src/pages/index.astro","src/pages/work.astro","src/pages/services.astro","src/pages/studio.astro","src/pages/contact.astro"
    ],
}

layouts = {
    "blackridge-build-co":"templates/base.html",
    "ember-and-thyme":"app/layout.tsx",
    "hale-mercer-legal":"resources/views/layouts/app.blade.php",
    "northwell-family-health":"templates/base.html",
    "juniper-row-realty":"app/layout.tsx",
    "forge-and-field-supply":"src/layouts/SiteLayout.astro",
    "redline-motorworks":"app/layout.tsx",
    "open-table-project":"templates/base.html",
    "orbitstack":"src/routes/+layout.svelte",
    "clearspring-plumbing":"templates/base.html",
    "the-alder-house":"app.vue",
    "static-bloom-studio":"src/layouts/SiteLayout.astro",
}

styles = {
    "blackridge-build-co":"pages/static/site.css",
    "ember-and-thyme":"app/globals.css",
    "hale-mercer-legal":"public/css/site.css",
    "northwell-family-health":"static/site.css",
    "juniper-row-realty":"app/globals.css",
    "forge-and-field-supply":"src/styles/site.css",
    "redline-motorworks":"app/globals.css",
    "open-table-project":"static/site.css",
    "orbitstack":"src/app.css",
    "clearspring-plumbing":"pages/static/site.css",
    "the-alder-house":"assets/css/main.css",
    "static-bloom-studio":"src/styles/site.css",
}

interactive = {
    "blackridge-build-co":["<form","method=\"post\""],
    "ember-and-thyme":["ReservationForm","useState"],
    "hale-mercer-legal":["consult-form","addEventListener"],
    "northwell-family-health":["<form","method=\"post\""],
    "juniper-row-realty":["PropertyBrowser","useState"],
    "forge-and-field-supply":["data-filter","addEventListener"],
    "redline-motorworks":["BookingForm","useState"],
    "open-table-project":["<form","demo-result"],
    "orbitstack":["bind:value","pricingToggle"],
    "clearspring-plumbing":["<form","method=\"post\""],
    "the-alder-house":["@submit.prevent","ref(false)"],
    "static-bloom-studio":["data-filter","contact-form"],
}

errors=[]
page_total=0
for slug, pages in sites.items():
    base=ROOT/"demos"/slug
    if len(pages)!=5:
        errors.append(f"{slug}: expected exactly five page definitions")
    for rel in pages:
        path=base/rel
        page_total += 1
        if not path.is_file():
            errors.append(f"{slug}: missing page {rel}")
    layout=base/layouts[slug]
    style=base/styles[slug]
    if not layout.is_file():
        errors.append(f"{slug}: missing shared layout {layouts[slug]}")
    if not style.is_file():
        errors.append(f"{slug}: missing design-system stylesheet {styles[slug]}")
    if layout.is_file():
        text=layout.read_text(encoding="utf-8")
        if "Skip to content" not in text:
            errors.append(f"{slug}: layout missing skip link")
        if "schema.org" not in text:
            errors.append(f"{slug}: layout missing structured-data marker")
    corpus="\n".join(p.read_text(encoding="utf-8",errors="ignore") for p in base.rglob("*") if p.is_file() and p.suffix in {".html",".tsx",".ts",".astro",".svelte",".vue",".php",".py"})
    for marker in interactive[slug]:
        if marker not in corpus:
            errors.append(f"{slug}: interaction marker missing: {marker}")

if page_total != 60:
    errors.append(f"repository: expected 60 page files, checked {page_total}")

if errors:
    print("Wave 3 verification FAILED")
    for error in errors:
        print(" -",error)
    sys.exit(1)

print("Wave 3 verification PASSED")
print(f" - {len(sites)} demos")
print(f" - {page_total} page files")
print(f" - {len(layouts)} shared layouts with skip-link + schema markers")
print(f" - {len(styles)} independent design-system stylesheets")
print(f" - interaction markers present for every demo")
