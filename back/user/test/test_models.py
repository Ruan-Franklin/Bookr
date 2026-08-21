from django.contrib.auth import get_user_model
from django.test import TestCase
from django.db.utils import IntegrityError

User = get_user_model()

class UserManagerTestCase(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            full_name="testuser",
            email="testuser@example.com",
            password="testpassword"
        )
        self.assertEqual(user.full_name, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.check_password("testpassword"))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_hashed_password(self):
        user = User.objects.create_user(
            full_name="Test User",
            email="testuser@example.com",
            password="testpassword"
        )
        self.assertNotEqual(user.password, "testpassword")

    def test_create_user_without_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(
                full_name="Test User",
                email="",
                password="testpassword"
            )


    def test_create_user_normalizes_email(self):
        user = User.objects.create_user(
            full_name="Test User",
            email="TESTUSER@EXAMPLE.COM",
            password="testpassword"
        )
        self.assertEqual(user.email, "testuser@example.com")

    def test_email_uniqueness_is_enforced(self):
        User.objects.create_user(
            email="duplicado@teste.com", password="123", full_name="Primeiro"
        )
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                email="duplicado@teste.com", password="456", full_name="Segundo"
            )



class SuperUserManagerTestCase(TestCase):
    def test_create_superuser_sets_flags_correctly(self):
        superuser = User.objects.create_superuser(
            full_name="superuser",
            email="superuser@gmail.com",
            password="superpassword",
        )
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_create_superuser_with_is_false_raises_error(self):
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                full_name="superuser",
                email="superman@gmail.com",
                password="superpassword",
                is_staff=False,
            )

    def test_create_superuser_with_is_superuser_false_raises_error(self):
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                full_name="superuser",
                email="superman@gmail.com",
                password="superpassword",
                is_superuser=False,
            )

class UserModelTestCase(TestCase):
    def test_str_returns_email(self):
        user = User.objects.create_user(
            full_name="Test User",
            email="testuser@example.com",
            password="testpassword"
        )
        self.assertEqual(str(user), "testuser@example.com")

    def test_if_change_user_update_the_updated_by_field(self):
        user = User.objects.create_user(
            full_name="Test User",
            email="leonidasdasilva@example.com",
            password="testpassword"
        )
        user.full_name = "Updated Test User"
        user.save(user=user)
        self.assertEqual(user.updated_by, user)

    
