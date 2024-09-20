from django.contrib import admin

from core_apps.venue.models import (
    Stadium,
    Seat,
    Match,
    Ticket
)


@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active", "vip_seats", "normal_seats"]
    list_filter = ["is_active", "vip_seats", "normal_seats"]
    search_fields = ["id", "title"]


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ["stadium", "number", "is_active", "is_vip"]
    list_filter = ["is_active", "is_vip"]
    search_fields = ["id", "number", "stadium__title"]
    ordering = ["stadium__title", "number"]


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ["title", "stadium", "is_active", "normal_price", "vip_price", "start_time", "end_time"]
    search_fields = ["id", "title", "stadium__title"]
    list_filter = ["is_active", "stadium"]
    ordering = ["create_time"]


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ["price", "status", "user", "match", "seat", "is_vip", "match__start_time", "match__end_time"]
    search_fields = ["user__id", "user__mobile", "match__id", "match__title", "match__stadium__title"]
    list_filter = ["is_vip", "match", "status"]
    ordering = ["create_time"]
