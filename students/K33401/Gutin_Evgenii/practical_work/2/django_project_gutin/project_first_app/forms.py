from django import forms
from .models import Vehicle, User


class VehicleForm(forms.ModelForm):
    class Meta(object):
        model = Vehicle
        fields = ['manufacturer', 'model', 'color', 'plate']


class OwnerForm(forms.ModelForm):
    class Meta(object):
        model = User
        fields = ['first_name', 'last_name', 'date_of_birth', 'passport', 'nationality', 'address']