from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from core_apps.common.models import BaseTimeStampedModel
from core_apps.venue.models.models import Ticket
from core_apps.payment.gateways import get_all_gateways_name

User = get_user_model()


class Transaction(BaseTimeStampedModel):
    class StatusOptions(models.IntegerChoices):
        PENDING = 1, _("Pending")
        FAILED = 2, _("Failed")
        SUCCESSFUL = 3, _("Successful")
        REFUNDED = 4, _("Refunded")

    user = models.ForeignKey(
        verbose_name=_("user"),
        to=User,
        on_delete=models.PROTECT,
        related_name="transactions"
    )
    # The correct price type is `DecimalField` but here we are interacting with RialIR:)
    price = models.PositiveIntegerField(
        verbose_name=_("price"),
    )
    status = models.PositiveSmallIntegerField(
        verbose_name=_("status"),
        choices=StatusOptions.choices,
        default=StatusOptions.PENDING,
        db_index=True
    )
    ticket = models.ForeignKey(
        verbose_name=_("ticket"),
        to=Ticket,
        on_delete=models.PROTECT,
        related_name="transactions",
    )
    gateway = models.CharField(
        verbose_name=_("gateway"),
        max_length=255,
        choices=list(zip(get_all_gateways_name(), get_all_gateways_name())),
    )

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")

    def __str__(self):
        return f"user:{self.user_id} - ticket:{self.ticket_id}, status:{self.get_status_display()}"

    def __repr__(self):
        return f"Transaction(id={self.id}, user_id={self.user_id}, status={self.get_status_display()})"
