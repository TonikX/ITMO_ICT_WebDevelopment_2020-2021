from django import forms
from .models import CarOwner


class CarOwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner

        fields = [
            "surname",
            "name",
            "birthday",
            "passport_number",
            "home_address",
            "nationality"
        ]
