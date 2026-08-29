"""
Class for testing the Appointment model in the Appointment app. This class inherits from Django's TestCase.
"""

from django.test import TestCase
from django.db.utils import IntegrityError
from django.utils import timezone
from datetime import datetime

from decimal import Decimal

from user.models import User

from professional.models import Professional

from service.models import Service

from ..models import Appointment

class AppointmentModelTestCase(TestCase):
    """Test cases for the Appointment model."""
    def setUp(self):
        """Set up a user, professional, service, and appointment instance for testing."""
        self.user = User.objects.create_user(
            full_name="Test User",
            email="testuser@example.com",
            password="testpassword",
            is_professional=True
        )
        self.professional = Professional.objects.create(
            user=self.user,
            bio="This is a test professional.",
            specialty="Test Specialty",
            rating_average=Decimal("4.5"),
            total_reviews=10
        )
        self.service = Service.objects.create(
            name="Test Service",
            description="This is a test service.",
            price=Decimal("100.00"),
            professional=self.professional
        )

    def test_create_appointment_with_valid_data(self):
        """Test creating an appointment with valid data."""
        appointment = Appointment.objects.create(
            user=self.user,
            professional=self.professional,
            service=self.service,
            start_time=timezone.make_aware(datetime(2026, 6, 1, 10, 0)),
            status="scheduled"
        )
        self.assertEqual(Appointment.objects.count(), 1)
        self.assertEqual(appointment.user, self.user)
        self.assertEqual(appointment.professional, self.professional)
        self.assertEqual(appointment.service, self.service)

    def test_create_appointment_without_required_fields(self):
        """Test creating an appointment without required fields should raise IntegrityError."""
        with self.assertRaises(IntegrityError):
            Appointment.objects.create(
                user=self.user,
                professional=self.professional
            )
    def test_appointment_str_method(self):
        """Test the string representation of the Appointment model."""
        appointment = Appointment.objects.create(
            user=self.user,
            professional=self.professional,
            service=self.service,
            start_time=timezone.make_aware(datetime(2026, 6, 1, 10, 0)),
            status="scheduled"
        )
        expected_str = f"Appointment {appointment.id} - {appointment.status} - {appointment.start_time}"
        self.assertEqual(str(appointment), expected_str)
