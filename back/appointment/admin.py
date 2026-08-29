from django.contrib import admin
from base.admin import BaseModelAdmin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(BaseModelAdmin):
    list_display = ('id', 'start_time', 'status', 'user', 'professional', 'service')
    list_filter = ('status', 'start_time', 'user', 'professional', 'service')
    search_fields = ('user__full_name', 'professional__user__full_name', 'service__name')