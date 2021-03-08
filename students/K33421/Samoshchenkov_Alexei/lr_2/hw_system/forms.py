from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Answer


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]


class AddAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            'student',
            'homework',
            'answer'
        ]

    def __init__(self, *args, **kwargs):
        super(AddAnswerForm, self).__init__(*args, **kwargs)
        self.fields['student'].disabled = True
        self.fields['homework'].disabled = True