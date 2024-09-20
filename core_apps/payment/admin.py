from django.contrib import admin

from core_apps.payment.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["id", "user__id", "user", "price", "status", "ticket", "gateway"]
    list_filter = ["status", "gateway"]
    search_fields = ["id", "price", "status", "user__mobile", "user__id"]
    ordering = ["create_time"]
