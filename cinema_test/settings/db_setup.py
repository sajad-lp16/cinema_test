from cinema_test.settings.general import config

# TODO => config using URL when docker network is initiated
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("DB_NAME", cast=str),
        "HOST": config("DB_HOST", cast=str),
        "PORT": config("DB_PORT", cast=int),
        "USER": config("DB_USER", cast=str),
        "PASSWORD": config("DB_PASSWORD", cast=str),
    }
}
