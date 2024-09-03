import os
import dj_database_url
from dotenv import load_dotenv
from pathlib import Path

TIME_ZONE = 'UTC'
USE_TZ = True

# DEBUG_TOOLBAR_CONFIG = {
#     'INTERCEPT_REDIRECTS': False,
# }

# Загрузка переменных окружения из .env файла
load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['3.92.49.13', 'ec2-3-92-49-13.compute-1.amazonaws.com', '127.0.0.1']

INTERNAL_IPS = [
    '127.0.0.1',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'admin_interface',
    'colorfield',
    'whitenoise.runserver_nostatic',
    'rest_framework_simplejwt',
    'drf_spectacular',
    'drf_yasg',
    'library',
    'lagerhouse',
    'task_manager',
    'project_tasks',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'mypro.urls'  # Убедитесь, что это правильно
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

SWAGGER_SETTINGS = {
    'ENUM_NAME_OVERRIDES': {
        'StatusEnum': 'your_app.models.StatusChoices',
        'AnotherStatusEnum': 'another_app.models.StatusChoices',
    },
}

WSGI_APPLICATION = 'mypro.wsgi.application'

# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL, conn_max_age=500)
}

# Условие для SQLite
if DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3':
    DATABASES['default'].pop('sslmode', None)


REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
}

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (BASE_DIR / 'static',)

# Whitenoise settings for serving static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'lagerhouse': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}
