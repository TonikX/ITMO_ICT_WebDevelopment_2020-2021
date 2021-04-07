from django import forms

from .models import CarOwner


class CarOwnerForm(forms.ModelForm):
    class Meta(object):
        model = CarOwner
        fields = ["surname", "name", "birth_date"]
