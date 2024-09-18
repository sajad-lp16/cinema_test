from cinema_test.settings.general import BASE_DIR

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "simple": {
            "format": "%(levelname)s %(asctime)s %(module)s -> %(message)s"
        },
    },
    "handlers": {
        "django_file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "logs" / "django.log",
            "formatter": "simple"
        },
        "account_file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "logs" / "account.log",
            "formatter": "simple"
        },
        "payment_file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "logs" / "payment.log",
            "formatter": "simple"
        },
        "venue_file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "logs" / "venue.log",
            "formatter": "simple"
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["django_file"],
            "level": "WARNING",
            "propagate": True,
        },
        "account": {
            "handlers": ["account_file"],
            "level": "INFO",
            "propagate": True,
        },
        "payment": {
            "handlers": ["payment_file"],
            "level": "INFO",
            "propagate": True,
        },
        "venue": {
            "handlers": ["venue_file"],
            "level": "INFO",
            "propagate": True,
        },
    },
}
