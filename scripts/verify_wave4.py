from pathlib import Path
import json
import sys

ROOT=Path(__file__).resolve().parents[1]
errors=[]

node_sites=[
 "ember-and-thyme","juniper-row-realty","redline-motorworks",
 "forge-and-field-supply","static-bloom-studio","orbitstack","the-alder-house"
]
for site in node_sites:
    package=ROOT/"demos"/site/"package.json"
    if not package.is_file():
        errors.append(f"{site}: package.json missing")
        continue
    data=json.loads(package.read_text())
    if "build" not in data.get("scripts",{}):
        errors.append(f"{site}: build script missing")
    for group in ("dependencies","devDependencies"):
        for name,version in data.get(group,{}).items():
            if version.startswith(("^","~",">","<","*")):
                errors.append(f"{site}: unpinned {group} dependency {name}={version}")

for site in ("blackridge-build-co","clearspring-plumbing","northwell-family-health","open-table-project"):
    req=ROOT/"demos"/site/"requirements.txt"
    if not req.is_file():
        errors.append(f"{site}: requirements.txt missing")
        continue
    for line in req.read_text().splitlines():
        line=line.strip()
        if line and "==" not in line:
            errors.append(f"{site}: unpinned Python dependency {line}")

laravel=ROOT/"demos"/"hale-mercer-legal"
for rel in [
 "composer.json","artisan","bootstrap/app.php","bootstrap/providers.php",
 "config/app.php","config/cache.php","config/session.php","config/view.php",
 "public/index.php","routes/web.php","routes/console.php","tests/smoke.php"
]:
    if not (laravel/rel).is_file():
        errors.append(f"hale-mercer-legal: missing {rel}")

for rel in [
 "demos/orbitstack/vite.config.ts","demos/orbitstack/src/app.html",
 "scripts/smoke_python.py",".github/workflows/portfolio-build.yml"
]:
    if not (ROOT/rel).is_file():
        errors.append(f"repository: missing {rel}")

if errors:
    print("Wave 4 verification FAILED")
    for e in errors:
        print(" -",e)
    sys.exit(1)
print("Wave 4 verification PASSED")
print(" - 7 Node builds configured with exact direct dependency versions")
print(" - 4 Python runtimes pinned and smoke-testable")
print(" - Laravel application bootstrap and smoke route test present")
