from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core_apps.common.models import BaseTimeStampedModel
from core_apps.account.models.managers import UserManager
from core_apps.account.models.validators import validate_phone_number


class User(AbstractBaseUser, PermissionsMixin, BaseTimeStampedModel):
    mobile = models.CharField(
        verbose_name=("mobile"),
        max_length=15,
        unique=True,
        validators=[validate_phone_number],
        help_text=_("User phone number")
    )
    is_staff = models.BooleanField(
        verbose_name=_("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "mobile"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_info(self):
        return self.mobile

    def __str__(self):
        return self.mobile

    def __repr__(self):
        return f"User(id={self.id}, mobile={self.mobile})"
