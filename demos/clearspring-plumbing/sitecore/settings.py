from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "wave-3-demo-key"
DEBUG = True
ALLOWED_HOSTS = []
ROOT_URLCONF = "sitecore.urls"
INSTALLED_APPS = ["django.contrib.staticfiles", "pages"]
MIDDLEWARE = ["django.middleware.security.SecurityMiddleware","django.middleware.common.CommonMiddleware","django.middleware.csrf.CsrfViewMiddleware"]
TEMPLATES = [{"BACKEND":"django.template.backends.django.DjangoTemplates","DIRS":[BASE_DIR / "templates"],"APP_DIRS":True,"OPTIONS":{"context_processors":["django.template.context_processors.request"]}}]
STATIC_URL = "static/"
