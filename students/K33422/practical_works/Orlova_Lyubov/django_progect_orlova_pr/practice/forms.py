from django import forms
from .models import CarOwner


# Форма для ввода владельцев функционально

class OwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner

        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "birth_date",
            "passport",
            "address",
            "nationality",
        ]