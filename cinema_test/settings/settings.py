"""It"s better to create settings for each host [local, dev, production]"""

from datetime import timedelta

from cinema_test.settings.general import *
from cinema_test.settings.db_setup import *
from cinema_test.settings.log_setup import *

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Token", "token"),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "SIGNING_KEY": SECRET_KEY,
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "UPDATE_LAST_LOGIN": True,
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

AUTHENTICATION_BACKENDS = [
    "core_apps.account.authentication.AuthBackend",
    "django.contrib.auth.backends.ModelBackend",
]

REDIS_HOST = config("REDIS_HOST", default="redis://127.0.0.1:6379/")
REDIS_USER = config("REDIS_USER", default="")
REDIS_PASS = config("REDIS_PASS", default="")
REDIS_BACKEND = "django_redis.cache.RedisCache"
REDIS_CLIENT_CLASS = "django_redis.client.DefaultClient"

DEFAULT_CACHE = "default"
DEFAULT_CACHE_TTL = None

CACHES = {
    "default": {
        "BACKEND": REDIS_BACKEND,
        "LOCATION": REDIS_HOST,
        "KEY_PREFIX": DEFAULT_CACHE,
        "TIMEOUT": DEFAULT_CACHE_TTL,
        "OPTIONS": {
            "CLIENT_CLASS": REDIS_CLIENT_CLASS,
            "USERNAME": REDIS_USER,
            "PASSWORD": REDIS_PASS,
        }
    }
}
