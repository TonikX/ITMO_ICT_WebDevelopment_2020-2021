from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('user', 'room', 'begin_date', 'end_date')

    def __init__(self, *args, **kwargs):
        super(CreateBookingForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True
        self.fields['room'].disabled = True


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('user', 'room', 'hotel', 'begin_date', 'end_date', 'rating', 'text')
        widgets = {
            'arrival': forms.DateInput(attrs={'type': 'date'},
                                       format='d-%m-%Y'),
            'departure': forms.DateInput(attrs={'type': 'date'},
                                         format='d-%m-%Y'),
            'comment': forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super(CreateReviewForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True
        self.fields['room'].disabled = True
        self.fields['hotel'].disabled = True
