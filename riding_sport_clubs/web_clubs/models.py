from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.urls import reverse

from riding_sport_clubs.base_validators.validators import owner_name_validator, name_validator, phone_number_validator


class Club(models.Model):
    CLUB_NAME_MIN_LENGTH = 2
    CLUB_NAME_MAX_LENGTH = 50
    OWNER_NAME_MIN_LENGTH = 2
    OWNER_NAME_MAX_LENGTH = 35
    CLUB_NUMBER_MAX_LENGTH = 16
    CLUB_NUMBER_MIN_LENGTH = 8
    UPLOAD_CLUB_LOGO = 'clubs_logo'

    club_name = models.CharField(
        max_length=CLUB_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(CLUB_NAME_MIN_LENGTH),
        ),
        unique=True,
    )

    owner = models.CharField(
        max_length=OWNER_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(OWNER_NAME_MIN_LENGTH),
            owner_name_validator,
        ),
    )

    email_club = models.EmailField()

    club_phone_number = models.CharField(
        max_length=CLUB_NUMBER_MAX_LENGTH,
        validators=(
            MinLengthValidator(CLUB_NUMBER_MIN_LENGTH),
            phone_number_validator,
        ),
        null=True,
        blank=True,
    )

    award_gold = models.IntegerField(
        default=0,
    )

    award_silver = models.IntegerField(
        default=0,
    )

    award_bronze = models.IntegerField(
        default=0,
    )

    rating = models.IntegerField(
        default=0,
    )

    address = models.TextField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    club_logo = models.ImageField(
        upload_to=UPLOAD_CLUB_LOGO,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.club_name

    def get_absolute_url(self):
        return reverse('club info', kwargs={'pk': self.pk})


class Trainer(models.Model):
    TRAINER_FIRST_NAME_MAX_LENGTH = 25
    TRAINER_LAST_NAME_MAX_LENGTH = 25
    AGE_MIN_VALUE = 1
    TRAINER_NUMBER_MAX_LENGTH = 16
    TRAINER_NUMBER_MIN_LENGTH = 8
    UPLOAD_TRAINER_PHOTO = 'trainer_photos'

    trainer_first_name = models.CharField(
        max_length=TRAINER_FIRST_NAME_MAX_LENGTH,
        validators=(
            name_validator,
        ),
    )

    trainer_last_name = models.CharField(
        max_length=TRAINER_LAST_NAME_MAX_LENGTH,
        validators=(
            name_validator,
        ),
    )

    trainer_age = models.IntegerField(
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        ),
    )

    trainer_phone_number = models.CharField(
        max_length=TRAINER_NUMBER_MAX_LENGTH,
        validators=(
            MinLengthValidator(TRAINER_NUMBER_MIN_LENGTH),
            phone_number_validator,
        ),
        null=True,
        blank=True,
    )

    trainer_photo = models.ImageField(
        upload_to=UPLOAD_TRAINER_PHOTO,
        null=True,
        blank=True,
    )

    trainer_info = models.TextField(
        null=True,
        blank=True,
    )

    clubs = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.trainer_first_name}  {self.trainer_last_name}"


class HorseBreed(models.Model):
    BREED_MAX_LENGTH = 35
    COLOR_MAX_LENGTH = 40
    USES_MAX_LENGTH = 40
    DESCRIPTION_MAX_LENGTH = 400000
    BREED_UPLOAD_PHOTO = 'breeds_photo'

    breed = models.CharField(
        max_length=BREED_MAX_LENGTH,
    )

    average_height = models.IntegerField()

    horse_color = models.CharField(
        max_length=COLOR_MAX_LENGTH,
    )

    common_uses = models.CharField(
        max_length=USES_MAX_LENGTH,
    )

    breed_description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
    )

    breed_photo = models.ImageField(
        upload_to=BREED_UPLOAD_PHOTO,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.breed
