from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from rest_framework.request import Request

from core_apps.account.utils.functions import normalize_mobile

User = get_user_model()


class AuthBackend(ModelBackend):
    """makes auth mechanism accept both `+98`, `09` mobile formats"""

    def authenticate(self, request: Request, username=None, password=None, **kwargs) -> User | None:
        mobile = normalize_mobile(username)
        try:
            user = User.objects.get(mobile=mobile)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
