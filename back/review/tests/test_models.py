"""
Tests for the Review model
"""
from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

from datetime import datetime

from decimal import Decimal

from django.core.exceptions import ValidationError

from appointment.models import Appointment
from review.models import Review
from professional.models import Professional
from user.models import User
from service.models import Service

class ReviewModelTestCase(TestCase):
    """Test cases for the Review model."""
    def setUp(self):
        """Set up a user, professional, service, appointment, and review instance for testing."""
        self.user = User.objects.create_user(
            full_name="Test User",
            email="newuser@example.com",
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
        self.appointment = Appointment.objects.create(
            user=self.user,
            service=self.service,
            start_time = timezone.make_aware(datetime(2026, 6, 1, 10, 0)),
            status="scheduled",
            professional=self.professional,
        )

    def test_create_review_with_valid_data(self):
        """Test creating a review with valid data."""
        review = Review.objects.create(
            appointment=self.appointment,
            rating=5,
            comment="Great service!"
        )
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(review.appointment, self.appointment)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, "Great service!")

    def test_create_review_without_required_fields(self):
        """Test creating a review without required fields should raise IntegrityError."""
        with self.assertRaises(IntegrityError):
            Review.objects.create(
                appointment=self.appointment
            )

    def test_rating_validators(self):
        """Test that the rating field has the correct validators."""
        rating_field = Review._meta.get_field("rating")
        validators = rating_field.validators
        self.assertIn(MinValueValidator(1), validators)
        self.assertIn(MaxValueValidator(5), validators)

    def test_rating_out_of_bounds_raises_validation_error(self):
        """Test that creating a review with an out-of-bounds rating raises a ValueError."""
        review = Review(appointment=self.appointment, rating=6)
        with self.assertRaises(ValidationError):
            review.full_clean()  

    def test_rating_below_minimum_raises_validation_error(self):
        """Test that creating a review with a rating below the minimum raises a ValueError."""
        review = Review(appointment=self.appointment, rating=0)
        with self.assertRaises(ValidationError):
            review.full_clean()

    def test_str_method(self):
        """Test the string representation of the Review model."""
        review = Review.objects.create(
            appointment=self.appointment,
            rating=4,
            comment="Good service."
        )
        expected_str = f"Review for Appointment {self.appointment.id} - Rating: 4"
        self.assertEqual(str(review), expected_str)