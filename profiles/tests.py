from datetime import timedelta
from django.test import TestCase, TransactionTestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Profile


class ProfileTestCase(TransactionTestCase):

    def setUp(self):
        self.user = User.objects.create_user('testuser0', 'testpassword0')

    def test_creating_user_creates_profile(self):
        self.assertEquals(User.objects.count(), 1)
        self.assertEquals(Profile.objects.count(), 1)
        self.user_1 = User.objects.create_user('testuser', 'testpassword')
        self.assertEquals(User.objects.count(), 2)
        self.assertEquals(Profile.objects.count(), 2)

    def test_random_integer_assigned(self):
        self.assertTrue(0 < self.user.profile.randint < 101)

    def test_allowed(self):
        # 24 hours before 13-years birthday
        self.user.profile.birthday = timezone.now().date() - timedelta(
            seconds=13*365.25*24*60*60) + timedelta(hours=24)
        self.user.save()
        self.assertFalse(self.user.profile.allowed())

        # user is 13 years old.
        self.user.profile.birthday = timezone.now().date() - timedelta(
            seconds=13 * 365.25 * 24 * 60 * 60)
        self.user.save()
        self.assertTrue(self.user.profile.allowed())

    def test_bizz_fuzz(self):
        self.user.profile.randint = 9
        self.assertEquals('Bizz', self.user.profile.bizz_fuzz())
        self.user.profile.randint = 10
        self.assertEquals('Fuzz', self.user.profile.bizz_fuzz())
        self.user.profile.randint = 15
        self.assertEquals('BizzFuzz', self.user.profile.bizz_fuzz())
