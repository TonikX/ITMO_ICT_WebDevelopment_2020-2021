from django.forms import ModelForm
from .models import *


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('text', 'rating_list', 'start_date', 'end_date')


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ('start_date', 'end_date')

