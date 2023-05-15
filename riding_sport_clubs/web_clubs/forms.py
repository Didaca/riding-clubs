from django import forms
from django.core.validators import MinLengthValidator

from riding_sport_clubs.base_validators.validators import owner_name_validator, phone_number_validator
from riding_sport_clubs.web_clubs.models import Club, Trainer, HorseBreed


class ClubForm(forms.ModelForm):

    class Meta:
        model = Club
        fields = ('club_name', 'owner', 'email_club', 'address', 'club_phone_number', 'description', 'club_logo')
        widgets = {
            'club_name': forms.TextInput(attrs={
                "class": "club_name"
            }),
            'owner': forms.TextInput(attrs={
                "class": "owner_name",
                "placeholder": "First & Last name"
            }),
            'email_club': forms.EmailInput(attrs={
                "class": "club_email",
                "placeholder": "example@email"
            }),
            'address': forms.TextInput(attrs={
                "class": "club_address"
            }),
            'club_phone_number': forms.TextInput(attrs={
                "class": "club_phone",
                "placeholder": "+ xxx xxx xxx xxx"
            }),
            'description': forms.Textarea(attrs={
                "class": "club_desc"
            }),
            'club_logo': forms.FileInput(attrs={
                "class": "club_logo",
                "style": "opacity: 0"
            })
        }
        error_messages = {
            'club_name': {
                'max_length': Club.CLUB_NAME_MAX_LENGTH,
                'validators': Club.CLUB_NAME_MIN_LENGTH
            },
            'owner': {
                'max_length': Club.OWNER_NAME_MAX_LENGTH,
                'validators': (MinLengthValidator(Club.OWNER_NAME_MIN_LENGTH), owner_name_validator,)
            },
            'club_phone_number': {
                'max_length': Club.CLUB_NUMBER_MAX_LENGTH,
                'validators': (MinLengthValidator(Club.CLUB_NUMBER_MIN_LENGTH), phone_number_validator,)
            }
        }


class EditClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ('club_name', 'owner', 'email_club', 'address', 'club_phone_number', 'description', 'club_logo')


class CreateTrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ('trainer_first_name', 'trainer_last_name', 'trainer_age', 'trainer_info', 'trainer_photo')


class CreateBreedForm(forms.ModelForm):
    class Meta:
        model = HorseBreed
        fields = ('breed', 'average_height', 'horse_color', 'common_uses', 'breed_description', 'breed_photo')
