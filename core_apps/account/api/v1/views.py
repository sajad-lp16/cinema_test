import logging

from django.contrib.auth import get_user_model

from rest_framework import (
    generics,
    status
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from drf_yasg.utils import swagger_auto_schema

from core_apps.account.utils.functions import normalize_mobile
from core_apps.account.api.v1.serializers import UserSerializer
from core_apps.account.api.v1.swagger_schema import (
    LOGIN_API_SCHEMA,
    REGISTER_API_SCHEMA
)

User = get_user_model()
Logger = logging.getLogger("account")


class UserRegisterAPIView(generics.CreateAPIView):
    """Better to be 2Step register, no verification implemented to simplify the scenario"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses=REGISTER_API_SCHEMA)
    def post(self, request: Request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        headers = self.get_success_headers(serializer.data)

        response_data = {
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }
        # in serious scenario this logger should be decorator and contain more data, like user_ip etc...
        Logger.info(f"RegisterLog UserINFO={serializer.data}")

        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)


class LoginAPIView(TokenObtainPairView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses=LOGIN_API_SCHEMA)
    def post(self, request: Request, *args, **kwargs) -> Response:
        """Override to make login accept both `+98` & `09` formats"""
        data = request.data

        if mobile := data.get("mobile"):
            request.data["mobile"] = normalize_mobile(mobile)

        # in serious scenario this logger should be decorator and contain more data, like user_ip etc...
        Logger.info(f"LoginAttempt UserINFO={data}")
        return super().post(request, *args, **kwargs)


class RefreshAPIView(TokenRefreshView):
    permission_classes = [AllowAny]
