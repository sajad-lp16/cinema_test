from django.contrib.auth import get_user_model

from rest_framework import (
    generics,
    status
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.tokens import RefreshToken

from core_apps.account.api.v1.serializers import UserSerializer


User = get_user_model()


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = AllowAny,

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
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
