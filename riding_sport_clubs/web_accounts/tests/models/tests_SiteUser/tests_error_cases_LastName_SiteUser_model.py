from django.core.exceptions import ValidationError
from django.test import TestCase

from riding_sport_clubs.web_accounts.models import SiteUser


class ProfileLastNameTests(TestCase):

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

    def test_user_profile_last_name__whenLastNameIsNotOnlyLetters_withNumber__shouldRaiseError(self):
        self.profile.last_name = self.UserData['last_name'] + '1'

        with self.assertRaises(ValidationError) as ctx:
            self.profile.full_clean()
            self.profile.save()
        self.assertIsNotNone(ctx.exception)

    def test_user_profile_last_name__whenLastNameIsNotOnlyLetters_withSpace__shouldRaiseError(self):
        self.profile.last_name = self.UserData['last_name'] + ' '

        with self.assertRaises(ValidationError) as ctx:
            self.profile.full_clean()
            self.profile.save()
        self.assertIsNotNone(ctx.exception)

    def test_user_profile_last_name__whenLastNameIsNotOnlyLetters__shouldRaiseError(self):
        self.profile.last_name = self.UserData['last_name'] + '$'

        with self.assertRaises(ValidationError) as ctx:
            self.profile.full_clean()
            self.profile.save()
        self.assertIsNotNone(ctx.exception)

    def test_user_profile_last_name__whenLastNameIsNotValid__shouldRaiseError(self):
        self.profile.last_name = ' ' + self.UserData['last_name']

        with self.assertRaises(ValidationError) as ctx:
            self.profile.full_clean()
            self.profile.save()
        self.assertIsNotNone(ctx.exception)
