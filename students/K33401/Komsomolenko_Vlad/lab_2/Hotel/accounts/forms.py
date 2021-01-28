from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from userprofile.models import UserProfile


class SignUpForm(UserCreationForm):
    typeUser = [
        ('admin', 'admin'),
        ('user', 'user'),
    ]
    type = forms.ChoiceField(choices=typeUser)

    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name', 'type',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name', 'type',)