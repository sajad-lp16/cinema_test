from django.urls import (
    path,
    include
)

app_name = "account"

urlpatterns = [
    path("api/", include("core_apps.account.api.urls")),
]
