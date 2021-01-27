from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Booking, Review
from datetime import date


class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class EditProfForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'passport', 'telephone')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email is already in use.')
        return email

    def save(self, commit=True):
        user = super(EditProfForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('user', 'room', 'arrival', 'departure')
        widgets = {
            'arrival': forms.DateInput(attrs={'type': 'date'},
                                       format='d-%m-%Y'),
            'departure': forms.DateInput(attrs={'type': 'date'},
                                         format='d-%m-%Y'),
        }

    def __init__(self, *args, **kwargs):
        super(CreateBookingForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True
        self.fields['room'].disabled = True

    def clean(self):
        cleaned_data = super().clean()
        arrival = cleaned_data.get("arrival")
        departure = cleaned_data.get("departure")
        today = date.today()

        if departure < arrival:
            raise forms.ValidationError("Date of arrival shouldn't be greater than date of departure")

        if arrival < today:
            raise forms.ValidationError("Reservation is not possible on past dates")


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('user', 'hotel', 'room', 'rating', 'arrival', 'departure', 'comment')
        widgets = {
            'arrival': forms.DateInput(attrs={'type': 'date'},
                                       format='d-%m-%Y'),
            'departure': forms.DateInput(attrs={'type': 'date'},
                                         format='d-%m-%Y'),
            'comment': forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super(CreateReviewForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True
        self.fields['room'].disabled = True
        self.fields['hotel'].disabled = True
