from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from riding_sport_clubs.web_accounts.models import SiteUser


class UserLoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text"
    }), label='username')

    password = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password"
    }), label='password')

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "input"
        }), label='username')

    first_name = forms.CharField(
        max_length=SiteUser.FIRST_NAME_MAX_LENGTH,
        widget=forms.TextInput(attrs={
            "class": "input"
        }), label="first name")

    last_name = forms.CharField(
        max_length=SiteUser.LAST_NAME_MAX_LENGTH,
        widget=forms.TextInput(attrs={
            "class": "input"
        }), label="first name")

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "input"
        }), label="email")

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "input"
        }), label="password")

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "input"
        }), label="password")

    gender = forms.MultipleChoiceField(
        widget=forms.Select(attrs={
            'class': 'gen-selector'
        }),
        choices=[('male', 'male'), ('female', 'female')]
    )

    picture = forms.ImageField(
        widget=forms.FileInput(attrs={
            "class": "input",
            "style": "opacity: 0"
        }), label="profile picture")

    phone_number = forms.CharField(
        max_length=SiteUser.PHONE_NUMBER_MAX_LENGTH,
        widget=forms.TextInput(attrs={
            "class": "input phone",
            "placeholder": "+xxx xxx xxx xxx"
        }), label="phone number")

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phone_number',
                  'gender', 'picture')


User = get_user_model()


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
