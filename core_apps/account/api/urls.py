from django.urls import (
    path,
    include
)

app_name = "api"

urlpatterns = [
    path("v1/", include("core_apps.account.api.v1.urls")),
]
