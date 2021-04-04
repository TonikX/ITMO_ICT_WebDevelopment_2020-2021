from django import forms
from .models import Driver


class AddDriver(forms.ModelForm):
    class Meta:
        model = Driver
        fields = [
            "first_name",
            "last_name",
            "birthday",
        ]