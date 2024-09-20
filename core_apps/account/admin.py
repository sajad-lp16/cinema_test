from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["mobile", "is_staff", "is_superuser", "is_active"]
    search_fields = ["id", "mobile"]
