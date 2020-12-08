from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Client, ReservedRooms, Review


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Client
        fields = [
            "first_name",
            "last_name",
            "username",
            "date_of_birth",
            "passport",
            "nationality"
        ]


class BookForm(forms.ModelForm):
    class Meta:
        model = ReservedRooms
        fields = [
            "start_date",
            "end_date"
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "rating",
            "description"
        ]
