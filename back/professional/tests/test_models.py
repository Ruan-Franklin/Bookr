"""
Test cases for the professional app models.
"""
from django.contrib.auth import get_user_model

from django.test import TestCase
from professional.models import Professional
from decimal import Decimal
from user.models import User

from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError


user = get_user_model()

class ProfessionalModelTestCase(TestCase):
    """Test cases for the Professional model."""
    
    def setUp(self):
        """Set up a user and a professional instance for testing."""
        self.user = User.objects.create_user(
            full_name="Test User",
            email="testuser@example.com",
            password="testpassword",
            is_professional=True
        )
        self.professional = Professional.objects.create(
            user=self.user,
            bio="Test bio",
            specialty="Test specialty",
            rating_average=Decimal("4.5"),
            total_reviews=10
        )

    def test_professional_creation_with_valid_data(self):
        """Test that a Professional instance is created with valid data."""
        self.assertEqual(self.professional.user, self.user)
        self.assertEqual(self.professional.bio, "Test bio")
        self.assertEqual(self.professional.specialty, "Test specialty")
        self.assertEqual(self.professional.rating_average, Decimal("4.5"))
        self.assertEqual(self.professional.total_reviews, 10)

    def test_professional_str_method(self):
        """Test the string representation of the Professional model."""
        self.assertEqual(str(self.professional), self.user.full_name)

    def test_professional_user_relationship(self):
        """Test the one-to-one relationship between Professional and User."""
        self.assertEqual(self.professional.user.professional_profile, self.professional)

    def test_professional_rating_average_default(self):
        """Test that the default rating_average is set to 0.00."""
        new_professional = Professional.objects.create(
            user=User.objects.create_user(
                full_name="Another User",
                email="anotheruser@example.com",
                password="anotherpassword",
                is_professional=True
            )
        )
        self.assertEqual(new_professional.rating_average, Decimal("0.00"))


    def test_professional_rating_average_its_not_negative(self):
        """Test that the rating_average cannot be negative."""
        professional = Professional.objects.create(
                user=User.objects.create_user(
                    full_name="Negative Rating User",
                    email="negativeratinguser@example.com",
                    password="negativeratingpassword",
                    is_professional=True
                ),
                rating_average=Decimal("-1.0")
            )
  
        with self.assertRaises(ValidationError):
            professional.full_clean()

                

    def test_professional_rating_rejects_negative_values(self):
        """Test that the rating_average cannot be negative."""
        professional = Professional.objects.create(
                user=User.objects.create_user(
                    full_name="Negative Rating User",
                    email="negativeratinguser@example.com",
                    password="negativeratingpassword",
                    is_professional=True
                ),
                rating_average=Decimal("-1.0")
            )
        with self.assertRaises(ValidationError):
            professional.full_clean()


    def test_professional_total_reviews_default(self):
        """Test that the default total_reviews is set to 0."""
        new_professional = Professional.objects.create(
            user=User.objects.create_user(
                full_name="Another User",
                email="anotheruser@example.com",
                password="anotherpassword",
                is_professional=True
            )
        )
        self.assertEqual(new_professional.total_reviews, 0)

    def test_professional_total_reviews_its_not_negative(self):
        """Test that the total_reviews cannot be negative."""
        with self.assertRaises(IntegrityError):
            Professional.objects.create(
                user=User.objects.create_user(
                    full_name="Negative Reviews User",
                    email="negativereviewsuser@example.com",
                    password="negativereviewspassword",
                    is_professional=True
                ),
                total_reviews=-1
            )

    def test_bio_can_have_a_thousand_characters(self):
        """Test that the bio field can have a thousand characters."""
        long_bio = "a" * 1000
        professional_with_long_bio = Professional.objects.create(
            user=User.objects.create_user(
                full_name="Long Bio User",
                email="longbiouser@example.com",
                password="longbiopassword",
                is_professional=True
            ),
            bio=long_bio
        )
        self.assertEqual(professional_with_long_bio.bio, long_bio)

