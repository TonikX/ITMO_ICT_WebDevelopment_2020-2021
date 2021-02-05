from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Member, Team


class MemberForm(UserCreationForm):
    class Meta:
        model = Member
        fields = [
            "first_name",
            "last_name",
            "username",
            "age",
        ]


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            "title",
            "description",
            "captain",
            "people",
        ]
        widgets = {'captain': forms.HiddenInput()}