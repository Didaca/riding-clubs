from django.test import TestCase

from riding_sport_clubs.web_clubs.models import Club


class ClubTests(TestCase):
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

    def test_clubOwnerName__whenNameIsValid__shouldDoNothing(self):
        ownerName = self.clubFortest.owner

        self.clubFortest.full_clean()
        self.clubFortest.save()

        self.assertEqual(ownerName, self.ClubForTest['owner'])

    def test_clubPhoneNumber__whenPhoneIsValid__shouldDoNothing(self):
        phone = self.clubFortest.club_phone_number

        self.clubFortest.full_clean()
        self.clubFortest.save()

        self.assertEqual(phone, self.ClubForTest['club_phone_number'])
