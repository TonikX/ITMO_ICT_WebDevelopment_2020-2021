from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

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

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
"""class CustomUser(AbstractUser):
    type_choices = [
        ('teacher', 'преподаватель'),
        ('student', 'студент'),
    ]
    type = models.CharField(max_length=10, choices=type_choices)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
        
class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    group_number = models.CharField(max_length=5)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Homework(models.Model):
    group_number = models.CharField(max_length=5)
    subject = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    deadline = models.DateField()
    description = models.TextField(max_length=10000)
    assessments = models.TextField(max_length=1000)

    def __str__(self):
        return '{} {} {}'.format(self.class_name, self.subject, self.date_of_publication)


class Assignment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.TextField(max_length=10000)

    def __str__(self):
        return '{} - {} {}'.format(self.pupil, self.task.subject, self.task.date_of_publication)


class Assessment(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return '{} - {} {}'.format(self.pupil, self.task.subject, self.task.date_of_publication)
"""

