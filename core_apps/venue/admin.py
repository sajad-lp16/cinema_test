from django.contrib import admin

from core_apps.venue.models import (
    Stadium,
    Seat,
    Match
)


@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    pass


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    pass


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    pass
