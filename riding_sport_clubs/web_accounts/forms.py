from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.core.validators import MinLengthValidator

from riding_sport_clubs.base_validators.validators import name_validator, phone_number_validator
from riding_sport_clubs.web_accounts.models import SiteUser

User = get_user_model()


class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                "class": "input"
            }),
            'password': forms.PasswordInput(attrs={
                "class": "input"
            })
        }


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phone_number',
                  'gender', 'picture')
        widgets = {
            'username': forms.TextInput(attrs={
                "class": "input"
            }),
            'first_name': forms.TextInput(attrs={
                "class": "input"
            }),
            'last_name': forms.TextInput(attrs={
                "class": "input"
            }),
            'email': forms.EmailInput(attrs={
                "class": "input"
            }),
            'password1': forms.PasswordInput(attrs={
                "class": "input"
            }),
            'password2': forms.PasswordInput(attrs={
                "class": "input"
            }),
            'gender': forms.Select(attrs={
                'class': 'gen-selector'
            }),
            'picture': forms.FileInput(attrs={
                "class": "input image",
                "style": "opacity: 0"
            }),
            'phone_number': forms.TextInput(attrs={
                "class": "input phone",
                "placeholder": "+xxx xxx xxx xxx"
            })
        }

        error_messages = {
            'username': {
                'max_length': SiteUser.USERNAME_MAX_LENGTH
            },
            'first_name': {
                'max_length': SiteUser.FIRST_NAME_MAX_LENGTH,
                'validators': name_validator,
            },
            'last_name': {
                'max_length': SiteUser.LAST_NAME_MAX_LENGTH,
                'validators': name_validator,
            },
            'phone_number': {
                'max_length': SiteUser.PHONE_NUMBER_MAX_LENGTH,
                'validators': (MinLengthValidator(SiteUser.PHONE_NUMBER_MIN_LENGTH), phone_number_validator),
            }
        }


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []

    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        instance = super(GroupForm, self).save()
        self.save_m2m()
        return instance
