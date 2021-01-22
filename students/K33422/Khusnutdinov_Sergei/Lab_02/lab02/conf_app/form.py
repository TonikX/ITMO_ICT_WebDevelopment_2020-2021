from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name'
        ]


class CreateReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = (
            'username',
            'name',
            'start_date',
            'end_date'
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