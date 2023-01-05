from pathlib import Path
from gerenciador.adminUI import *
from dotenv import load_dotenv, dotenv_values
import os

config_env = dotenv_values(".env") 

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_ROOT_ADMIN = os.path.join(BASE_DIR, "media")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gerenciador.settings")


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-(&t@8cp0amg4w&w5vwd^q#hqu1)*c9b+7^o3#(=mp4pzxg9)dy"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(config_env['DEBUG_DJANGO'])

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # novos
    "tarefas",
    "utils",
    "treinamento",
    "NR10",
    "Estoque",
    "saq",
    # externos
    "django_summernote",
    "import_export",
    "rangefilter",
    "crispy_forms",
    "fontawesomefree",
    "admin_extra_buttons",
    'rest_framework',
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "gerenciador.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR, os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "gerenciador.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    # },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    # {
    #     "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    # },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# admin ui config jazmin
JAZZMIN_SETTINGS = JAZZMIN_SETTINGS
JAZZMIN_UI_TWEAKS = JAZZMIN_UI_TWEAKS

# ssummernote
X_FRAME_OPTIONS = "SAMEORIGIN"
SUMMERNOTE_THEME = "bs4"
SUMMERNOTE_CONFIG = {
    "iframe": True,
    "summernote": {
        "airMode": False,
        # https://summernote.org/deep-dive/#custom-toolbar-popover
        "toolbar": [
            ["style", ["style"]],
            ["font", ["bold", "underline", "clear"]],
            ["fontname", ["fontname"]],
            ["color", ["color"]],
            ["para", ["ul", "ol", "paragraph"]],
            ["table", ["table"]],
            ["insert", ["link", "picture"]],
            [
                "view",
                [
                    "fullscreen",
                ],
            ],
        ],
    },
    # You can completely disable the attachment feature.
    "disable_attachment": False,
    # Set to `True` to return attachment paths in absolute URIs.
    "attachment_absolute_uri": True,
}


# IMPORT AND EXPORT DATA
IMPORT_EXPORT_USE_TRANSACTIONS = True
IMPORT_EXPORT_SKIP_ADMIN_LOG = True

# CSS
CRISPY_TEMPLATE_PACK = "bootstrap4"


# EMAIL
if not DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
    EMAIL_FILE_PATH = "./temp/app-messages"
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_USER = config_env['EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = config_env['EMAIL_HOST_PASSWORD']
    EMAIL_PORT = config_env['EMAIL_PORT']
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = "default from email"


# API
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}