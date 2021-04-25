from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'passport']


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user','tour', 'rating', 'text')

    def __init__(self, *args, **kwargs):
        super(CreateCommentForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True
        self.fields['tour'].disabled = True


class CreateReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('user', 'tour', 'begin_date', 'end_date')

    def __init__(self, *args, **kwargs):
        super(CreateReservationForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True
        self.fields['tour'].disabled = True
