from django import forms
from .models import *
from django.conf import settings
from django.contrib.auth import get_user_model


class CarownerAddForm(forms.ModelForm):
    class Meta:
        model = Carowner
        fields = [
            'firstname',
            'lastname',
            'birthday',
            'passportnum',
            'address',
            'ethnicity',
            'username',
            'password',
        ]