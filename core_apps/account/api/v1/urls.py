from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)

from core_apps.account.api.v1.views import UserRegisterAPIView

app_name = "v1"

urlpatterns = [
    path("register/", UserRegisterAPIView.as_view(), name="register"),
    path("token/", TokenObtainSlidingView.as_view(), name="token"),
    path("token/refresh/", TokenRefreshSlidingView.as_view(), name="refresh"),
]
