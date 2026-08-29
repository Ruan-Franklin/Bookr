"""
 This module contains the models for the Appointment app. The Appointment model represents an appointment in the system and includes fields for start time, status, user, professional, and service. It inherits from BaseModel, which provides common fields such as created_at and updated_at.
"""

from django.db import models
from base.models import BaseModel
# Create your models here.

class Appointment(BaseModel):
    """
    Model class for the Appointment app. This class inherits from BaseModel and represents an appointment in the system.
    """
    start_time = models.DateTimeField()
    status = models.CharField(max_length=20,
                             choices=[('scheduled', 'Scheduled'),
                                       ('confirmed', 'Confirmed'),
                                      ('completed', 'Completed'),
                                      ('canceled', 'Canceled')],
                             default='scheduled')
    
    user = models.ForeignKey('user.User',
                              on_delete=models.PROTECT,
                              related_name='appointments')
    professional = models.ForeignKey('professional.Professional',
                                     on_delete=models.PROTECT,
                                     related_name='appointments')
    service = models.ForeignKey('service.Service',
                                 on_delete=models.PROTECT,
                                 related_name='appointments')

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"
        ordering = ["start_time"]

    def __str__(self):
        return f"Appointment {self.id} - {self.status} - {self.start_time}"