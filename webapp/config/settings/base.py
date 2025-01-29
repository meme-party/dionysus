"""
Django settings for dionysus project.
"""

import logging
from datetime import timedelta
from typing import List

import environ
from django.templatetags.static import static

# Default Environment Variables

PROJECT_DIR = environ.Path(__file__) - 4
BASE_DIR = environ.Path(__file__) - 3

env = environ.Env(DEBUG=(bool, False))

env.read_env(f"{PROJECT_DIR}/.env")
env.read_env(f"{BASE_DIR}/.env")

SECRET_KEY = env("DJANGO_SECRET_KEY")
DEBUG = env("DEBUG") == "True" or bool(env("DEBUG"))

SITE_ID = 1

# Network settings

ALLOWED_HOSTS = ["*"]

# Application definition

PRE_PACKAGE_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.inlines",
    "unfold.contrib.import_export",
    "unfold.contrib.guardian",
    "unfold.contrib.simple_history",
]

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PACKAGE_APPS = [
    "nplusone.ext.django",
    "silk",
    "rest_framework",
    "drf_spectacular",
    "safedelete",
    "django_filters",
    "django_guid",
    "drf_api_logger",
    "markdownx",
    "rest_framework.authtoken",
    "allauth",
    "allauth.socialaccount",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.kakao",
    "allauth.socialaccount.providers.github",
]

CUSTOM_APPS: List[str] = [
    "api",
    "bookmark",
    "meme",
    "account",
    "file_manager",
    "tag",
]

INSTALLED_APPS = PRE_PACKAGE_APPS + DJANGO_APPS + PACKAGE_APPS + CUSTOM_APPS

# Middleware settings

PRE_PACKAGE_MIDDLEWARES = [
    "django_guid.middleware.guid_middleware",
    "nplusone.ext.django.NPlusOneMiddleware",
    "silk.middleware.SilkyMiddleware",
]

DJANGO_MIDDLEWARES = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

PACKAGE_MIDDLEWARES = [
    "drf_api_logger.middleware.api_logger_middleware.APILoggerMiddleware"
]

CUSTOM_MIDDLEWARES: List[str] = []

MIDDLEWARE = (
    PRE_PACKAGE_MIDDLEWARES
    + DJANGO_MIDDLEWARES
    + PACKAGE_MIDDLEWARES
    + CUSTOM_MIDDLEWARES
)

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "config.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "ko-kr"
TIME_ZONE = "Asia/Seoul"
USE_I18N = True
USE_TZ = True

# User model settings

AUTH_USER_MODEL = "account.User"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ========== DRF settings ==========

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_PAGINATION_CLASS": ("rest_framework.pagination.PageNumberPagination"),
    "PAGE_SIZE": 10,
}

REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_COOKIE": "dionysus-app-auth",
    "JWT_AUTH_REFRESH_COOKIE": "dionysus-app-refresh",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Dionysus API",
    "DESCRIPTION": "Meme Project",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "CONTACT": {
        "name": "shinkeonkim",
        "email": "dev.shinkeonkim@gmail.com",
    },
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "theme": "dark",
        "validatorUrl": None,
    },
}

REST_USE_JWT = True

ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "email"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=2),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
}

# ========== END DRF Spectacular settings ==========

# ========== Logging settings ==========

NPLUSONE_LOGGER = logging.getLogger("nplusone")
NPLUSONE_LOG_LEVEL = logging.WARN

LOGGING = {
    "version": 1,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "medium",
            "filters": ["correlation_id"],
        },
    },
    "filters": {"correlation_id": {"()": "django_guid.log_filters.CorrelationId"}},
    "formatters": {
        "medium": {
            "format": "%(levelname)s %(asctime)s [%(correlation_id)s] %(name)s %(message)s"
        }
    },
    "loggers": {
        "nplusone": {
            "handlers": ["console"],
            "level": "WARN",
        },
    },
}

# ========== END Logging settings ==========

# ========== drf-api-logger settings ==========

DRF_API_LOGGER_DATABASE = True

# TODO: APILogsModel에 대해 DB 인덱스를 추가하는것이 좋아보임.

DRF_LOGGER_QUEUE_MAX_SIZE = 50
DRF_LOGGER_INTERVAL = 10

DRF_API_LOGGER_SKIP_NAMESPACE: List[str] = []
DRF_API_LOGGER_SKIP_URL_NAME: List[str] = []
DRF_API_LOGGER_EXCLUDE_KEYS = [
    "password",
    "token",
    "access",
    "refresh",
]  # TODO: 보안 정보에 대한 키워드를 추가하기

DRF_API_LOGGER_DEFAULT_DATABASE = (
    "default"  # TODO: 별도 로깅을 위한 데이터베이스 설정하는게 좋아보임.
)

DRF_API_LOGGER_SLOW_API_ABOVE = (
    200  # TODO: 200ms 보다 더 빠르게 처리할 수 있는지 확인하기
)


# ========== END drf-api-logger settings ==========

# ========== Unfold settings ==========

UNFOLD = {
    "STYLES": [
        lambda request: static("css/styles.css"),
    ],
    "SCRIPTS": [
        lambda request: static("js/scripts.js"),
    ],
}

# ========== END Unfold settings ==========

AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

# ========== Silk settings ==========

SILKY_AUTHENTICATION = True
SILKY_AUTHORISATION = True

# ========== END Silk settings ==========

# TODO: CORS 설정 추가하기
