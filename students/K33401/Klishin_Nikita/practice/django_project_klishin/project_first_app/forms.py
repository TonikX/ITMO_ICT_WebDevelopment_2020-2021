from django import forms
from django.db import models
from django.db.models import fields
from .models import User, Car

class CarCreationForm(forms.ModelForm):
    
    class Meta:

        model=Car

        fields=[
            "brand",
            "car_model",
            "color",
            "number"
        ]

class UserCreationForm(forms.ModelForm):

    class Meta:

        model=User

        fields=[
            "name",
            "surname",
            "birth_date",
            'passport',
            'home_address',
            'nationality'
        ]

