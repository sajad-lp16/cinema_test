from django.urls import (
    path,
    include
)

app_name = "venue"

urlpatterns = [
    path("api/", include("core_apps.venue.api.urls")),
]
