from django.apps import AppConfig


class PaymentConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.payment"

    verbose_name = "payment"
    verbose_name_plural = "payments"
