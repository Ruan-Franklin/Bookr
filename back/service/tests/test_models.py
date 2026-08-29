"""
Tests for the Service model.
"""

from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

from decimal import Decimal

from user.test.test_models import User
from ..models import Service
from professional.models import Professional

class ServiceModelTestCase(TestCase):
    """Test cases for the Service model."""

    """Set up a professional and a service instance for testing."""
    def setUp(self):
        self.professional = Professional.objects.create(
            user=User.objects.create_user(
                full_name="Test User",
                email="test@example.com",
                password="testpassword",
                is_professional=True
            ),
            bio="Test bio",
            specialty="Test specialty",
            rating_average=Decimal("4.5"),
            total_reviews=10
        )
        self.service = Service.objects.create(
            name="Test Service",
            description="Test description",
            price=Decimal("100.00"),
            duration_in_minutes=60,
            professional=self.professional
        )

    def test_service_creation_with_valid_data(self):
        """Test that a Service instance is created with valid data."""
        self.assertEqual(self.service.name, "Test Service")
        self.assertEqual(self.service.description, "Test description")
        self.assertEqual(self.service.price, Decimal("100.00"))
        self.assertEqual(self.service.duration_in_minutes, 60)
        self.assertEqual(self.service.professional, self.professional)

    def test_service_str_method(self):
        """Test the string representation of the Service model."""
        self.assertEqual(str(self.service), "Test Service")

    def test_service_professional_relationship(self):
        """Test the relationship between Service and Professional."""
        self.assertEqual(self.service.professional, self.professional)

    def test_its_not_possible_to_create_a_service_without_the_required_fields(self):
        """Test that creating a Service without required fields raises an error."""
        with self.assertRaises(IntegrityError):
            Service.objects.create(
                name="Incomplete Service",
                price=Decimal("50.00"),
            )

    def test_service_price_must_be_non_negative(self):
        """Test that the price of a Service must be non-negative."""
        with self.assertRaises(ValidationError):
            service = Service(
                name="Negative Price Service",
                description="Test description",
                price=Decimal("-10.00"),
                duration_in_minutes=30,
                professional=self.professional
            )
            service.full_clean() 

    def test_service_duration_must_be_non_negative(self):
        """Test that the duration of a Service must be non-negative."""
        with self.assertRaises(ValidationError):
            service = Service(
                name="Negative Duration Service",
                description="Test description",
                price=Decimal("50.00"),
                duration_in_minutes=-30,
                professional=self.professional
            )
            service.full_clean()

    
    