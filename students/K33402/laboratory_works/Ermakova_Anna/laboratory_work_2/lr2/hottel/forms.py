from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import *
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model


class ReservateRoomForm(forms.Form):
    begin_date = forms.DateField()
    end_date = forms.DateField()


class AddCommentForm(forms.Form):
    text = forms.CharField(max_length=410)
    accommodation = forms.ModelChoiceField(queryset=UserRoom.objects.all())


class EditReservationForm(forms.ModelForm):
    class Meta:
        model = RoomReservation
        fields = ['begin_date', 'end_date']


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
