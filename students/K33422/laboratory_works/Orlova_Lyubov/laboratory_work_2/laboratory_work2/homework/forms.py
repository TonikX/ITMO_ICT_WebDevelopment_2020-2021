from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Submission


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class AddSubmissionForm(forms.ModelForm):

    class Meta:
        model = Submission
        fields = ['student_subm', 'task_subm', 'submission']

    def __init__(self, *args, **kwargs):
        super(AddSubmissionForm, self).__init__(*args, **kwargs)
        self.fields['student_subm'].disabled = True
        self.fields['task_subm'].disabled = True
