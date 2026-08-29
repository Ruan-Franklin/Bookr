"""
Base admin module for the Bookr application. Other admin modules should import from this module to ensure consistent behavior across the application.
"""
from django.utils import timezone
from django.contrib import admin

class BaseModelAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        """
        Override the save_model method to automatically set the created_by and updated_by fields
        based on the current user.
        """
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        """
        Override the delete_model method to perform a soft delete by setting is_active to False
        and deleted_at to the current time.
        """
        obj.updated_by = request.user
        obj.deleted()

    def delete_queryset(self, request, queryset):
        """
        Override the delete_queryset method to perform a soft delete on a queryset by setting is_active to False
        and deleted_at to the current time for each object in the queryset.
        """
        queryset.update(
            is_active=False,
            deleted_at=timezone.now(),
            updated_by=request.user
        )