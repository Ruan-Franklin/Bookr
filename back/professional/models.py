"""
Professional model with relationship with user model and other relevant fields.
"""

from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from base.models import BaseModel

class Professional(BaseModel):
    """
    Professional model that extends the system BaseModel
    """
    bio = models.TextField(blank=True, null=True)
    specialty = models.CharField(max_length=100, blank=True, null=True)
    rating_average = models.DecimalField(max_digits=3,
                                        decimal_places=2,
                                        validators=[MinValueValidator(0.0)],
                                        default=Decimal("0.00"))
    total_reviews = models.PositiveIntegerField(default=0,
                                                validators=[MinValueValidator(0)])
    user = models.OneToOneField(
        "user.User",
        on_delete=models.CASCADE,
        related_name="professional_profile",
    )

    class Meta:
        verbose_name = "Professional"
        verbose_name_plural = "Professionals"
        ordering = ["user__full_name"]

    def __str__(self):
        return self.user.full_name

    