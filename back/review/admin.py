"""
Admin configuration for the Review app
"""

from django.contrib import admin
from base.admin import BaseModelAdmin
from .models import Review

@admin.register(Review)
class ReviewAdmin(BaseModelAdmin):
    list_display = ("id", "rating", "appointment", "created_at", "updated_at")
    search_fields = ("appointment__id", "comment")
    list_filter = ("rating", "created_at", "updated_at")

