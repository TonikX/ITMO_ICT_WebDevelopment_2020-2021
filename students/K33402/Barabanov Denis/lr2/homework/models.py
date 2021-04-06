from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

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


class CustomUser(AbstractUser):
    role = models.CharField(max_length=10, choices=roles, null=True)
    group_number = models.CharField(max_length=6, choices=group_numbers, null=True)
    subject = models.CharField(max_length=50, choices=subjects, null=True)
    name = models.CharField(max_length=100, null=True)
    def __str__(self):
        return '{}'.format(self.name)
        
        
class Teacher(models.Model):
    name = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=50, choices=subjects, null=True)
    def __str__(self):
        return '{}'.format(self.name)


class Student(models.Model):
    name = models.CharField(max_length=100, null=True)
    group_number = models.CharField(max_length=6, choices=group_numbers, null=True)
    def __str__(self):
        return '{}'.format(self.name)


class Homework(models.Model):
    group_number = models.CharField(max_length=6, choices=group_numbers, null=True)
    subject = models.CharField(max_length=50, choices=subjects)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    deadline = models.DateField()
    description = models.TextField(max_length=10000)

    def __str__(self):
        return '{} {}'.format(self.group_number, self.subject)
        

class Assignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.TextField(max_length=10000)

    def __str__(self):
        return '{} - {}'.format(self.student, self.homework.subject)


class Assessment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return '{} - {}'.format(self.student, self.homework.subject)