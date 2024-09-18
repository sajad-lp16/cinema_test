from django.urls import (
    path,
    include
)

app_name = "payment"

urlpatterns = [
    path("api/", include("core_apps.payment.api.urls")),
]
