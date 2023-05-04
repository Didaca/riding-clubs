from django import forms

from riding_sport_clubs.web_clubs.models import Club, Trainer, HorseBreed


class CreateClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ('club_name', 'owner', 'email_club', 'address', 'description', 'club_logo')
        labels = {
            'club_name': 'Club name',
            'owner': 'Club owner',
            'email_club': 'Email',
            'address': 'Club address',
            'description': 'Description',
            'club_logo': 'Club logo',

        }
        widgets = {
            'owner': forms.TextInput(
                attrs={
                    'placeholder': 'First & Last name'
                },
            ),
        }


class CreateTrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ('trainer_first_name', 'trainer_last_name', 'trainer_age', 'trainer_info', 'trainer_photo')
        labels = {
            'trainer_first_name': 'First Name',
            'trainer_last_name': 'Last Name',
            'trainer_age': 'Age',
            'trainer_info': 'Trainer info',
            'trainer_photo': 'Picture',
        }


class CreateBreedForm(forms.ModelForm):
    class Meta:
        model = HorseBreed
        fields = ('breed', 'average_height', 'horse_color', 'common_uses', 'breed_description', 'breed_photo')
        labels = {
            'breed': 'Breed',
            'average_height': 'Average Height',
            'horse_color': 'Color',
            'common_uses': 'Uses',
            'breed_description': 'Info',
            'breed_photo': 'Image',
        }
