from django import forms
from django.contrib.auth import get_user_model

from racing_scoreboard.models import Comment, Racer

User = get_user_model()


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    username = forms.CharField(label='Логин')
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(label='Повторите пароль:', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Логин занят")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists() and email != '':
            raise forms.ValidationError("Такой адрес уже зарегистрирован")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Пароли не совпадают")
        return data


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['commentator', 'datetime', 'race']


class CreateRacerForm(forms.ModelForm):
    class Meta:
        model = Racer
        exclude = ['user_info']
