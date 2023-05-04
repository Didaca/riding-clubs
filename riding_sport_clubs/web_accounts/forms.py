from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from riding_sport_clubs.base_validators import validators
from riding_sport_clubs.web_accounts.models import SiteUser


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=SiteUser.FIRST_NAME_MAX_LENGTH,
        label='First name',
    )
    last_name = forms.CharField(
        max_length=SiteUser.LAST_NAME_MAX_LENGTH,
        label='Last name',
    )
    email = forms.EmailField(
        label='Email',
    )
    gender = forms.ChoiceField(
        choices=(
            ('male', 'male'),
            ('female', 'female'),
        ),
        label='Gender',
    )
    picture = forms.ImageField(
        label='Image',
    )
    phone_number = forms.CharField(
        max_length=SiteUser.PHONE_NUMBER_MAX_LENGTH,
        label='Phone',
        widget=forms.TextInput(attrs={'placeholder': '+ XXX XXXXXXXXX'}),
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phone_number',
                  'gender', 'picture',)
        labels = {
            'username': 'Username',
        }


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
