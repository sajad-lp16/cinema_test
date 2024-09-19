from django.db.models import Manager
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager

from core_apps.account.utils.functions import normalize_mobile


class UserManager(BaseUserManager):
    def _create_user(self, mobile: str, password: str, **extra_fields):
        if not mobile:
            raise ValueError("Mobile field is required")

        mobile = normalize_mobile(mobile)

        user_already_exist = self.model.objects.filter(mobile=mobile).exists()
        if user_already_exist:
            raise ValidationError("User with such mobile already exists.")

        if not password:
            raise ValueError("Password field is required")

        user = self.model(mobile=mobile, password=password, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, mobile, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(mobile, password, **extra_fields)

    def create_superuser(self, mobile, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(mobile, password, **extra_fields)
