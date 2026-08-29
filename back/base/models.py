"""Base class for all models in the project."""

from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

class BaseModel(models.Model):
    """Base class for all models in the project."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(
        to="user.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="%(class)s_created_by"
    )
    updated_by = models.ForeignKey(
        to="user.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="%(class)s_updated_by"
    )
    is_active = models.BooleanField(default=True)



    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False, user=None):
        """Soft delete the object by setting is_active to False and deleted_at to the current time."""
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save(user=user)

    def restore(self, user=None):
        """Restore the object by setting is_active to True and deleted_at to None."""
        self.is_active = True
        self.deleted_at = None
        self.save(user=user)

    def save(self, *args, **kwargs):
        """Override the save method to update the updated_at and updated_by fields."""
        user = kwargs.pop("user", None)
        self.updated_at = timezone.now()

        if user is not None and hasattr(self, "updated_by"):
            self.updated_by = user

        super().save(*args, **kwargs)