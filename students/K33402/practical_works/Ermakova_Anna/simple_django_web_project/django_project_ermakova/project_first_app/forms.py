from django import forms
from .models import Person


class AddPerson(forms.ModelForm):
    class Meta:
        model = Person

        fields = [
            "name",
            "surname",
            "birthday"
        ]
