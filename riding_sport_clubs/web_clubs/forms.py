from django import forms

from riding_sport_clubs.web_clubs.models import Club, Trainer, HorseBreed


class CreateClubForm(forms.ModelForm):
    club_name = forms.CharField(
        max_length=Club.CLUB_NAME_MAX_LENGTH,
        widget=forms.TextInput(attrs={
            "class": "club_name"
        }),
        label="Club Name"
    )

    owner = forms.CharField(
        max_length=Club.OWNER_NAME_MAX_LENGTH,
        widget=forms.TextInput(attrs={
            "class": "owner_name",
            "placeholder": "First & Last name"
        }),
        label="Owner Name"
    )

    email_club = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "club_email",
            "placeholder": "example@email"
        }),
        label="Club Email"
    )

    address_club = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "club_address"
        }),
        label="Club Address"
    )

    club_phone = forms.CharField(
        max_length=Club.CLUB_NUMBER_MAX_LENGTH,
        widget=forms.TextInput(attrs={
            "class": "club_phone",
            "placeholder": "+ xxx xxx xxx xxx"
        }),
        label="Club Phone Number"
    )

    description_club = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "club_desc"
        }),
        label="Description"
    )

    club_logo = forms.ImageField(
        widget=forms.FileInput(attrs={
            "class": "club_logo",
            "style": "opacity: 0"
        }),
        label="Club Logo"
    )

    class Meta:
        model = Club
        fields = ('club_name', 'owner', 'email_club', 'address', 'club_phone_number', 'description', 'club_logo')


class EditClubForm(forms.ModelForm):

    club_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "club_name",
            "disabled": ''
        }),
        label="Club Name"
    )

    owner = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "owner_name",
            "placeholder": "First & Last name"
        }),
        label="Owner Name"
    )

    email_club = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "club_email",
            "placeholder": "example@email",
            "disabled": ''
        }),
        label="Club Email"
    )

    address_club = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "club_address",
            "disabled": ''
        }),
        label="Club Address"
    )

    club_phone = forms.CharField(
        max_length=Club.CLUB_NUMBER_MAX_LENGTH,
        widget=forms.TextInput(attrs={
            "class": "club_phone",
            "placeholder": "+ xxx xxx xxx xxx"
        }),
        label="Club Phone Number"
    )

    description_club = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "club_desc"
        }),
        label="Description"
    )

    club_logo = forms.ImageField(
        widget=forms.FileInput(attrs={
            "class": "club_logo",
            "style": "opacity: 0"
        }),
        label="Club Logo"
    )

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
