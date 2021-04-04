from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, label="Login")
    first_name = forms.CharField(max_length=30, required=True, label="First Name")
    last_name = forms.CharField(max_length=30, required=True, label="Last Name")
    experience = forms.CharField(max_length=30, required=True, label="Your Experience")
    car = forms.CharField(max_length=30, required=True, label="Car")



    class Meta:
        model = Participant
        fields = ('username', 'first_name', 'last_name',  'experience',  'car')



class RaceRegistrationForm(forms.ModelForm):
    class Meta:
        model = Race_Registration
        fields = ('race', 'participant')

    def __init__(self, *args, **kwargs):
        super(RaceRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['race'].disabled = True
        self.fields['participant'].disabled = True

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'comment', 'comment_type', 'rating_list', 'race')
        widgets = {
            'comment': forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True



