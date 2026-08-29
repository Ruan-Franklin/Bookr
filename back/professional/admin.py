from django.contrib import admin
from base.admin import BaseModelAdmin
# Register your models here.
from .models import Professional

@admin.register(Professional)
class ProfessionalAdmin(BaseModelAdmin):
    list_display = ("user", "specialty", "rating_average", "total_reviews", "created_at", "updated_at")
    search_fields = ("user__full_name", "specialty")
    list_filter = ("specialty",)