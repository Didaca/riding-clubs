from django.core.exceptions import ValidationError
from django.test import TestCase

from riding_sport_clubs.web_accounts.models import SiteUser


class ProfilePhoneTests(TestCase):

    UserData = {
        'username': 'D',
        'password': 1,
        'first_name': 'Deyan',
        'last_name': 'Ivanov',
        'email': 'd.v.ivanov.dvi@gmail.com',
        'gender': 'male',
        'phone_number': '+359877041238'
    }

    def setUp(self):
        self.profile = SiteUser.objects.create(**self.UserData)

    def test_user_profile_phone__whenPhoneNumberNotContainPlus__shouldRaiseError(self):
        self.profile.phone_number = self.UserData['phone_number'][1:]

        with self.assertRaises(ValidationError) as ctx:
            self.profile.full_clean()
            self.profile.save()
        self.assertIsNotNone(ctx.exception)

    def test_user_profile_phone__whenPhoneNumberNotContainOnlyDigits__shouldRaiseError(self):
        self.profile.phone_number = self.UserData['phone_number'][:3] + ' ' + self.UserData['phone_number'][3:]

        with self.assertRaises(ValidationError) as ctx:
            self.profile.full_clean()
            self.profile.save()
        self.assertIsNotNone(ctx.exception)

    def test_user_profile_phone__whenPhoneNumberContainLetter__shouldRaiseError(self):
        self.profile.phone_number = self.UserData['phone_number'][:3] + 'a' + self.UserData['phone_number'][3:]

        with self.assertRaises(ValidationError) as ctx:
            self.profile.full_clean()
            self.profile.save()
        self.assertIsNotNone(ctx.exception)
