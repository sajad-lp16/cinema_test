from django.contrib import admin
from django.urls import (
    path,
    include
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("core_apps.account.urls", namespace="account")),
    path("venue/", include("core_apps.venue.urls", namespace="venue")),
    path("payment/", include("core_apps.payment.urls", namespace="payment")),
]
