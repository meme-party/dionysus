from .base import *  # noqa: F401, F403

DATABASES = {
    "default": {
        "ENGINE": "psqlextra.backend",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": "localhost",
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

# ========== Logging settings ==========

LOGGING = get_logging_config(BASE_DIR, debug=DEBUG, environment="test")

# ========== END Logging settings ==========
