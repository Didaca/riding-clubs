from django.test import TestCase

from riding_sport_clubs.web_clubs.models import Club
from riding_sport_clubs.base_validators.validators import ValidationError


class ClubPhoneTests(TestCase):
    ClubForTest = {
        'club_name': 'Ema-nu',
        'owner': 'Deyan Ivanov',
        'email_club': 't@gmeil.com',
        'club_phone_number': '+359000000000',
        'award_gold': 0,
        'award_silver': 0,
        'award_bronze': 0,
        'rating': 0
    }

    def setUp(self):
        self.clubFortest = Club.objects.create(**self.ClubForTest)

    def test_ClubPhone__whenPhoneNumberNotContainPlus__shouldRaiseError(self):
        self.clubFortest.club_phone_number = self.ClubForTest['club_phone_number'][1:]

        with self.assertRaises(ValidationError) as ctx:
            self.clubFortest.full_clean()
            self.clubFortest.save()
        self.assertIsNotNone(ctx.exception)

    def test_ClubPhone__whenPhoneNumberNotContainOnlyDigits__shouldRaiseError(self):
        self.clubFortest.club_phone_number = self.ClubForTest['club_phone_number'][:3]\
                                             + ' ' + self.ClubForTest['club_phone_number'][3:]

        with self.assertRaises(ValidationError) as ctx:
            self.clubFortest.full_clean()
            self.clubFortest.save()
        self.assertIsNotNone(ctx.exception)

    def test_ClubPhone__whenPhoneNumberContainLetter__shouldRaiseError(self):
        self.clubFortest.club_phone_number = self.ClubForTest['club_phone_number'][:3]\
                                             + 'a' + self.ClubForTest['club_phone_number'][3:]

        with self.assertRaises(ValidationError) as ctx:
            self.clubFortest.full_clean()
            self.clubFortest.save()
        self.assertIsNotNone(ctx.exception)
