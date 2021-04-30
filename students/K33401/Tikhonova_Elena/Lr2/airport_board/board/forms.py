from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.db.models.query import EmptyQuerySet
from datetime import date as d_date


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['rating', 'text', 'flight', 'user', 'fligh_date']
        widgets = {
            'rating': forms.TextInput(attrs={'class': 'form-control mb-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            # 'flight': forms.HiddenInput(),
            # 'user': forms.HiddenInput(),
            # 'fligh_date': forms.HiddenInput(),
        }


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'passenger', 'flight', 'seat']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'passenger': forms.HiddenInput(attrs={'class': 'm-0'}),
            'flight': forms.HiddenInput(attrs={'class': 'm-0'}),
            'seat': forms.HiddenInput(attrs={'class': 'm-0'}),
        }


class ReservationEditForm(forms.ModelForm):

    class Meta:
        seats = []
        for i in range(1, 10):
            for s in ['a', 'b', 'c', 'd']:
                seats.append(str(i)+s)
        model = Reservation
        fields = ['date', 'seat']
        widgets = {'date': forms.DateInput(attrs={'class': 'form-control mb-5', 'type': 'date'}),
                   'seat': forms.TextInput(attrs={'class': 'form-control'})
                   }

    # def clean_date(self):
    #     date = self.cleaned_data['date']
    #     if date - d_date.today() not in range(1, 15):
    #         raise ValidationError(
    #             'You can reservate seat for day from tomorrow to 2 weeks later')
    #     return date
