from django.contrib import admin

from .models import User
from base.admin import BaseModelAdmin

@admin.register(User)
class UserAdmin(BaseModelAdmin):
    list_display = ("id", "full_name", "email", "is_active", "created_at", "updated_at")
    list_filter = ("is_active", "created_at", "updated_at")
    search_fields = ("full_name", "email")
    ordering = ("-created_at",)

