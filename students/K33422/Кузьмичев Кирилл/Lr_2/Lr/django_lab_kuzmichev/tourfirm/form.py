from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='Почта', widget=forms.TextInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    passport = forms.CharField(label='Паспорт', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name',
            'passport'
        ]


class CreateReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = (
            'username',
            'name'
        )

    def __init__(self, *args, **kwargs):
        super(CreateReserveForm, self).__init__(*args, **kwargs)
        self.fields['username'].disabled = True
        self.fields['name'].disabled = True


class CreateReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = (
            'username',
            'start_date',
            'end_date',
            'rate',
            'comment'
        )

    def __init__(self, *args, **kwargs):
        super(CreateReviewForm, self).__init__(*args, **kwargs)
        self.fields['username'].disabled = True
