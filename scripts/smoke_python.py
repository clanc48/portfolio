from __future__ import annotations
import compileall
import importlib.util
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = sys.argv[1] if len(sys.argv) > 1 else ""
BASE = ROOT / "demos" / SITE

if not BASE.is_dir():
    raise SystemExit(f"Unknown demo: {SITE}")

if not compileall.compile_dir(BASE, quiet=1):
    raise SystemExit(f"Python compilation failed for {SITE}")

def assert_ok(status: int, route: str) -> None:
    if status != 200:
        raise SystemExit(f"{SITE}: {route} returned {status}")

if SITE in {"blackridge-build-co", "clearspring-plumbing"}:
    os.chdir(BASE)
    sys.path.insert(0, str(BASE))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sitecore.settings")
    import django
    django.setup()
    from django.conf import settings
    from django.test import Client
    if "testserver" not in settings.ALLOWED_HOSTS:
        settings.ALLOWED_HOSTS.append("testserver")
    client = Client()
    routes = {
        "blackridge-build-co": ["/", "/projects/", "/services/", "/process/", "/contact/"],
        "clearspring-plumbing": ["/", "/services/", "/service-areas/", "/reviews/", "/request-service/"],
    }[SITE]
    for route in routes:
        assert_ok(client.get(route).status_code, route)
    post_route = "/contact/" if SITE == "blackridge-build-co" else "/request-service/"
    assert_ok(client.post(post_route, {"name":"Demo","email":"demo@example.com","summary":"Demo","details":"Demo"}).status_code, post_route)
    print(f"{SITE}: Django smoke passed ({len(routes)} GET + 1 POST)")
elif SITE == "northwell-family-health":
    os.chdir(BASE)
    spec = importlib.util.spec_from_file_location("northwell_demo", BASE / "app.py")
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    client = module.app.test_client()
    routes = ["/", "/services", "/providers", "/patient-resources", "/appointments"]
    for route in routes:
        assert_ok(client.get(route).status_code, route)
    assert_ok(client.post("/appointments", data={"name":"Demo","email":"demo@example.com"}).status_code, "/appointments")
    print("northwell-family-health: Flask smoke passed (5 GET + 1 POST)")
elif SITE == "open-table-project":
    os.chdir(BASE)
    sys.path.insert(0, str(BASE))
    from app.main import app
    from fastapi.testclient import TestClient
    client = TestClient(app)
    routes = ["/", "/programs", "/impact", "/get-involved", "/donate"]
    for route in routes:
        assert_ok(client.get(route).status_code, route)
    print("open-table-project: FastAPI smoke passed (5 GET)")
else:
    raise SystemExit(f"No Python smoke profile for {SITE}")
