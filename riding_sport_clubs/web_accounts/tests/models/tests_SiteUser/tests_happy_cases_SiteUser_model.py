from django.test import TestCase

from riding_sport_clubs.web_accounts.models import SiteUser


class ProfileTests(TestCase):

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

    def test_user_profile_first_name__whenFirstNameIsCorrect__shouldDoNoting(self):
        first_name = self.profile.first_name
        self.profile.full_clean()
        self.profile.save()

        self.assertEqual(first_name, self.UserData['first_name'])

    def test_user_profile_last_name__whenLastNameIsCorrect__shouldDoNoting(self):
        last_name = self.profile.last_name
        self.profile.full_clean()
        self.profile.save()

        self.assertEqual(last_name, self.UserData['last_name'])

    def test_user_profile_phone__whenPhoneNumberIsCorrect__shouldDoNoting(self):
        phone = self.profile.phone_number
        self.profile.full_clean()
        self.profile.save()

        self.assertEqual(phone, self.UserData['phone_number'])

    def test_user_profile__whenFullNameIsCorrect__shouldDoNoting(self):
        full_name = self.profile.full_name
        self.profile.full_clean()
        self.profile.save()

        self.assertEqual(full_name, f'{self.UserData["first_name"]} {self.UserData["last_name"]}')
