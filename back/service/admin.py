from django.contrib import admin
from .models import Service
from base.admin import BaseModelAdmin

@admin.register(Service)
class ServiceAdmin(BaseModelAdmin):
    list_display = ("name", "professional", "price", "duration_in_minutes", "created_at", "updated_at")
    search_fields = ("name", "description", "professional__user__full_name")
    list_filter = ("professional",)