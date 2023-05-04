from django.test import TestCase

from riding_sport_clubs.web_clubs.models import Trainer, Club


class TrainerTests(TestCase):

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

    TrainerData = {
        'trainer_first_name': 'Deyan',
        'trainer_last_name': 'Ivanov',
        'trainer_age': 43,
        'trainer_phone_number': '+359877041238',
    }

    def setUp(self):
        self.club = Club.objects.create(**self.ClubForTest)

        self.TrainerData['clubs'] = self.club
        self.trainer = Trainer.objects.create(**self.TrainerData)

    def test_trainer_first_name__whenFirstNameIsCorrect__shouldDoNoting(self):
        first_name = self.trainer.trainer_first_name
        self.trainer.full_clean()
        self.trainer.save()

        self.assertEqual(first_name, self.TrainerData['trainer_first_name'])

    def test_trainer_last_name__whenLastNameIsCorrect__shouldDoNoting(self):
        last_name = self.trainer.trainer_last_name
        self.trainer.full_clean()
        self.trainer.save()

        self.assertEqual(last_name, self.TrainerData['trainer_last_name'])

    def test_trainer_phone__whenPhoneNumberIsCorrect__shouldDoNoting(self):
        phone = self.trainer.trainer_phone_number
        self.trainer.full_clean()
        self.trainer.save()

        self.assertEqual(phone, self.TrainerData['trainer_phone_number'])
