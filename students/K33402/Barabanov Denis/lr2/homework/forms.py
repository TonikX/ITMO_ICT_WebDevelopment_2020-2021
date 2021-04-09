from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

subjects = [
    ('Mathematics', 'Mathematics'),
    ('Physics', 'Physics'),
    ('Biology', 'Biology'),
    ('Informatics', 'Informatics')
    ]
    
group_numbers = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
]
    
roles = [
    ('teacher', 'учитель'),
    ('student', 'студент'),
]

class TeacherCreationForm(UserCreationForm):
    role = forms.Select(choices=roles)
    subject = forms.Select(choices=subjects)
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'role',
            'subject',
            'name',
        ]


class StudentCreationForm(UserCreationForm):
    role = forms.Select(choices=roles)
    group_number = forms.Select(choices=group_numbers)
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'role',
            'group_number',
            'name',
        ]


class AddHomework(forms.ModelForm):
    class Meta:
        model = Homework
        exclude = ['teacher']
        fields = ['group_number',
                  'subject',
                  'deadline',
                  'description']
                  
                  
class AddAssignment(forms.ModelForm):
    class Meta:
        model = Assignment
        exclude = ['student', 'homework']
        fields = ['solution']
        
        
class AddAssessment(forms.ModelForm):
    class Meta:
        model = Assessment
        exclude = ['student', 'homework']
        fields = ['grade']