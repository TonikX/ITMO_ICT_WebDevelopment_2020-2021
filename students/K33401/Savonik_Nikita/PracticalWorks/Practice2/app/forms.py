from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class CarOwnerForm(forms.ModelForm):
    class Meta:
        model = Car_owner

        fields = [
            'first_name',
            'last_name',
            'date_of_birth',
        ]
