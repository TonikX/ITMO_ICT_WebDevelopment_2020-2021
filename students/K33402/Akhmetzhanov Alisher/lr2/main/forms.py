from django.db.models import fields
from main.models import RoomReservation, UserRoom
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
