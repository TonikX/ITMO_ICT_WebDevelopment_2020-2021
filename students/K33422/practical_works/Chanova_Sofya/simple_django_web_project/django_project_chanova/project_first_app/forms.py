from django import forms
from .models import Owner, Car


class AddOwner(forms.ModelForm):

    class Meta:
        model = Owner

        fields = [
            'username',
            'first_name',
            'last_name',
            'birth_date',
            'passport',
            'address',
            'nationality'
        ]


class AddCar(forms.ModelForm):

    class Meta:
        model = Car

        fields = [
            'brand',
            'model',
            'color',
            'plate_number'
        ]
