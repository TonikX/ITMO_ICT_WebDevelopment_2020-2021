from django import forms
from django.forms import fields
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "number_guest",
            "marks",
            "model",
            "color",
        ]
