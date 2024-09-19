from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from core_apps.common.models import BaseTimeStampedModel
from core_apps.venue.models.managers import (
    StadiumManager,
    SeatManager,
    MatchManager
)


class Stadium(BaseTimeStampedModel):
    title = models.CharField(
        verbose_name=_("title"),
        max_length=255,
        unique=True
    )
    is_active = models.BooleanField(
        verbose_name=_("is active"),
        default=True
    )
    vip_seats = models.IntegerField(
        verbose_name=_("vip seats")
    )
    normal_seats = models.IntegerField(
        verbose_name=_("normal seats")
    )

    objects = models.Manager()
    enable_objects = StadiumManager()

    class Meta:
        verbose_name = _("Stadium")
        verbose_name_plural = _("Stadiums")

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Stadium(id={self.id}, title={self.title})"


class Seat(BaseTimeStampedModel):
    stadium = models.ForeignKey(
        verbose_name=_("stadium"),
        to=Stadium,
        on_delete=models.CASCADE,
        related_name="seats"
    )
    number = models.PositiveIntegerField(
        verbose_name=_("number"),
    )
    is_active = models.BooleanField(
        verbose_name=_("is active"),
        default=True
    )
    is_vip = models.BooleanField(
        verbose_name=_("is vip"),
        default=False
    )

    objects = models.Manager()
    enable_objects = SeatManager()

    class Meta:
        verbose_name = _("Seat")
        verbose_name_plural = _("Seats")
        constraints = [
            models.UniqueConstraint(fields=["stadium_id", "number"], name="stadium_number_unique")
        ]

    def __str__(self):
        if not self.is_vip:
            return f"{self.stadium.title}-{self.number}"
        return f"{self.stadium.title}-{self.number}-VIP"

    def __repr__(self):
        return f"Seat(id={self.id}, number={self.number}, stadium_title={self.stadium.title})"


class Match(BaseTimeStampedModel):
    title = models.CharField(
        verbose_name=_("title"),
        max_length=255
    )
    stadium = models.ForeignKey(
        verbose_name=_("stadium"),
        to=Stadium,
        on_delete=models.CASCADE,
        related_name="matches"
    )
    is_active = models.BooleanField(
        verbose_name=_("is active"),
        default=True
    )
    vip_price = models.PositiveIntegerField(
        verbose_name=_("vip price"),
    )
    normal_price = models.PositiveIntegerField(
        verbose_name=_("normal price")
    )
    start_time = models.DateTimeField(
        verbose_name=_("start time"),
    )
    end_time = models.DateTimeField(
        verbose_name=_("start time"),
    )

    objects = models.Manager()
    enable_objects = MatchManager()

    def check_time_collision(self):
        has_collision = Match.enable_objects.exclude(id=self.id).filter(
            Q(start_time__gte=self.start_time, start_time__lte=self.end_time) |
            Q(end_time__gte=self.start_time, end_time__lte=self.end_time)
        ).exists()

        if has_collision:
            raise ValidationError({
                "code": "time_collision",
                "detail": _("match times have collision with others")
            })

    def save(self, *args, **kwargs):
        self.check_time_collision()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Match")
        verbose_name_plural = _("Matches")

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"Match(id={self.id}, title={self.title})"
