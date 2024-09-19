from django.urls import path

from core_apps.payment.api.v1.views import (
    GatewaysListAPIView,
    BuyTicketAPIView,
    PurchaseDetailsAPIView
)

app_name = "v1"

urlpatterns = [
    path("gateways-list/", GatewaysListAPIView.as_view(), name="gateways-list"),
    path("buy-ticket/", BuyTicketAPIView.as_view(), name="buy-ticket"),
    path("purchase-detail/<int:id>/", PurchaseDetailsAPIView.as_view(), name="purchase-detail"),
]
