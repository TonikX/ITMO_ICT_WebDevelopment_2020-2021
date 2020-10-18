from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

subjects = [
    ('Web programming', 'Web programming'),
    ('Web design', 'Web design'),
    ('Operation systems', 'Operation systems'),
    ('Front-end', 'Front-end')
    ]
    
group_numbers = [
    ('K33401', 'K33401'),
    ('K33402', 'K33402'),
    ('K33421', 'K33421'),
    ('K33422', 'K33422'),
]
    
roles = [
    ('teacher', 'преподаватель'),
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