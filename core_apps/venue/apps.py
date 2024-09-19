from django.apps import AppConfig


class VenueConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.venue"

    verbose_name = "Venue"
    verbose_name_plural = "Venues"

    def ready(self):
        from core_apps.venue import signals
