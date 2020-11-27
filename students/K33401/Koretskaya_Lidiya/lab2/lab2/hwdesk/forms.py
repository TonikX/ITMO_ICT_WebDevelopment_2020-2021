from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class CustomUserCreationForm(UserCreationForm):
    type_choices = [
        ('teacher', 'учитель'),
        ('pupil', 'ученик'),
    ]

    type = forms.Select(choices=type_choices)

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'type',
            'first_name',
            'last_name',
        ]

    '''
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.type = self.cleaned_data["type"]
        if commit:
            user.set_password(user.password)
            user.save()
        return user
    '''
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'type',
            'first_name',
            'last_name',
        ]

class AddTaskTeacher(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['teacher', 'date_of_publication', ]
        fields = ['class_name',
                  'subject',
                  'deadline',
                  'task_text',
                  'fines_info']


class LoadTaskPupil(forms.ModelForm):
    class Meta:
        model = LoadTask
        exclude = ['pupil', 'task']
        fields = ['decision']

class CheckTaskTeacher(forms.ModelForm):
    class Meta:
        model = CheckTask
        exclude = ['pupil', 'task']
        fields = ['mark', 'comment']