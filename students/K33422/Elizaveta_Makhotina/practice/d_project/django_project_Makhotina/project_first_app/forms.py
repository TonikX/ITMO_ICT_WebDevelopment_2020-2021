from django import forms
from .models import Owner


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner

        fields = [
            "first_name",
            "second_name",
            "b_date"]
