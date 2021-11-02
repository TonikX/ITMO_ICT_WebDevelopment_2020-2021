from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Guest, Booking, Review


class GuestForm(UserCreationForm):
    class Meta:
        model = Guest
        fields = [
            "first_name",
            "last_name",
            "passport",
            "username",
        ]

class BookingForm(forms.ModelForm):
	class Meta:
		model = Booking
		fields = [
			"hotel",
			"room",
			"start",
			"end",
		]
		widgets = {'hotel': forms.HiddenInput()}

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = [
			"hotel",
			"text",
			"rating",
		]
		widgets = {'hotel': forms.HiddenInput()}