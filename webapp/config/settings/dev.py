from .base import *

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": "db",
        "PORT": env("POSTGRES_PORT"),
    }
}


# Static files (CSS, JavaScript, Images)

STATIC_DIR = f"{BASE_DIR}/static"
STATIC_ROOT = f"{BASE_DIR}/static"
STATIC_URL = "/static/"

# Media files
MEDIA_ROOT = f"{BASE_DIR}/media"
MEDIA_URL = "media/"
