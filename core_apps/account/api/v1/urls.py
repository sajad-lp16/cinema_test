from django.urls import path

from core_apps.account.api.v1.views import (
    LoginAPIView,
    RefreshAPIView,
    UserRegisterAPIView
)

app_name = "v1"

urlpatterns = [
    path("register/", UserRegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("refresh/", RefreshAPIView.as_view(), name="refresh"),
]
