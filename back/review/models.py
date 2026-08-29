"""
Models for the Review app
"""
from django.core.validators import (MinValueValidator,
                                    MaxValueValidator)
from django.db import models

from base.models import BaseModel

class Review(BaseModel):
    """
    Review model that extends the system BaseModel
    """
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)
    appointment = models.OneToOneField(
        "appointment.Appointment",
        on_delete=models.PROTECT,
        related_name="review",
    )

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ["-created_at"]
        constraints = [
            models.CheckConstraint(
                check=models.Q(rating__gte=1) & models.Q(rating__lte=5),
                name="rating_between_1_and_5"
            )
        ]
    def __str__(self):
        return f"Review for Appointment {self.appointment.id} - Rating: {self.rating}"
