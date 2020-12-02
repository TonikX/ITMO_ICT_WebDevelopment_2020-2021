from django import forms
from project_first_app.models import Driver


class DriverForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = [
            "first_name",
            "last_name",
            "date_of_birth",
            "passport",
            "address",
            "nationality",
            'username'
        ]
