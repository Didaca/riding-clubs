from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse

from riding_sport_clubs.base_validators.validators import name_validator, phone_number_validator
from riding_sport_clubs.web_accounts.managers import Manager


class SiteUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_MAX_LENGTH = 30
    FIRST_NAME_MAX_LENGTH = 25
    LAST_NAME_MAX_LENGTH = 35
    PHONE_NUMBER_MIN_LENGTH = 8
    PHONE_NUMBER_MAX_LENGTH = 16
    GENDER_MAX_LENGTH = 6
    UPLOAD_PICTURE = 'profile_picture'
    CLUB_NAME_MAX_LENGTH = 50

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )

    USERNAME_FIELD = 'username'
    objects = Manager()

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            name_validator,
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            name_validator,
        ),
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.CharField(
        max_length=GENDER_MAX_LENGTH,
        choices=(
            ('male', 'male'),
            ('female', 'female'),
        ),
    )

    picture = models.ImageField(
        upload_to=UPLOAD_PICTURE,
        null=True,
        blank=True,
    )

    phone_number = models.CharField(
        max_length=PHONE_NUMBER_MAX_LENGTH,
        validators=(
            MinLengthValidator(PHONE_NUMBER_MIN_LENGTH),
            phone_number_validator,
        ),
        null=True,
        blank=True,
    )

    data_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    lk_clubs = ArrayField(
        models.CharField(max_length=CLUB_NAME_MAX_LENGTH), default=list, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('details profile', kwargs={'pk': self.pk})
