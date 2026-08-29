"""
Models for the service app.
"""
from django.db import models
from django.core.validators import MinValueValidator

from decimal import Decimal

from base.models import BaseModel



class Service(BaseModel):
    """
    Service model that extends the system  BaseModel and represents a service offered by a professional.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,
                                   null=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                default=Decimal("0.00"),
                                validators=[MinValueValidator(Decimal("0.00"))]
                                )
    duration_in_minutes = models.PositiveIntegerField(default=0,
                                                      validators=[MinValueValidator(0)]
                                                      )
    image = models.ImageField(upload_to="service_images/", blank=True, null=True)
    professional = models.ForeignKey(
        "professional.Professional",
        on_delete=models.CASCADE,
        related_name="services",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["name"]

        constraints = [
            models.CheckConstraint(
                check=models.Q(price__gte=0),
                name="price_non_negative"
            )
        ]
