from django import forms
from .models import *
from django.conf import settings
from django.contrib.auth import get_user_model


class AddDriverForm(forms.ModelForm):
    class Meta:
        model = Driver

        fields = [
            "first_name",
            "last_name",
            "birthday",
            "passport",
            "address",
            "nationality",
            "password",
            "username",
        ]
