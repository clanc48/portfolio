from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'wave-1-dev-key'
DEBUG = True
ALLOWED_HOSTS = []
ROOT_URLCONF = 'sitecore.urls'
INSTALLED_APPS = ['django.contrib.staticfiles', 'pages']
MIDDLEWARE = []
TEMPLATES = [{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR / 'templates'],'APP_DIRS':True,'OPTIONS':{'context_processors':[]}}]
STATIC_URL = 'static/'
