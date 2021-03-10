from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ('username', 'email', 'first_name', 'last_name', 'classe', 'password1', 'password2')


class AddSubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['student', 'task', 'submission']

    def __init__(self, *args, **kwargs):
        super(AddSubmissionForm, self).__init__(*args, **kwargs)
        self.fields['student'].disabled = True
        self.fields['task'].disabled = True