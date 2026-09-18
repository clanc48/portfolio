from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SITES = {
    "blackridge-build-co": ("pages/static/site.css", "pages/static/media"),
    "clearspring-plumbing": ("pages/static/site.css", "pages/static/media"),
    "ember-and-thyme": ("app/globals.css", "public/media"),
    "forge-and-field-supply": ("src/styles/site.css", "public/media"),
    "hale-mercer-legal": ("public/css/site.css", "public/media"),
    "juniper-row-realty": ("app/globals.css", "public/media"),
    "northwell-family-health": ("static/site.css", "static/media"),
    "open-table-project": ("static/site.css", "static/media"),
    "orbitstack": ("src/app.css", "static/media"),
    "redline-motorworks": ("app/globals.css", "public/media"),
    "static-bloom-studio": ("src/styles/site.css", "public/media"),
    "the-alder-house": ("assets/css/main.css", "public/media"),
}

URL_RE = re.compile(r"url\((?:['\"])?([^)'\"]+\.(?:svg|webp|png|jpe?g|avif))(?:['\"])?\)", re.I)

errors: list[str] = []

for site, (css_rel, media_rel) in SITES.items():
    base = ROOT / "demos" / site
    css = base / css_rel
    media = base / media_rel
    manifest = media / "MEDIA_AUDIT.md"

    if not css.is_file():
        errors.append(f"{site}: missing stylesheet {css_rel}")
        continue
    if not manifest.is_file():
        errors.append(f"{site}: missing media manifest {manifest.relative_to(ROOT)}")
    if not media.is_dir():
        errors.append(f"{site}: missing media directory {media.relative_to(ROOT)}")
        continue

    svgs = list(media.glob("*.svg"))
    if len(svgs) < 8:
        errors.append(f"{site}: expected at least 8 SVG assets, found {len(svgs)}")

    css_text = css.read_text(encoding="utf-8")
    for raw in URL_RE.findall(css_text):
        if "media/" not in raw:
            continue
        asset = media / raw.split("/")[-1]
        if not asset.is_file():
            errors.append(f"{site}: stylesheet references missing asset {raw}")

if errors:
    raise SystemExit("Media verification failed:\n- " + "\n- ".join(errors))

print(f"Media verification passed for {len(SITES)} sites.")
