from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Student(AbstractUser):
    group_id = models.CharField(max_length=10, unique=True)


class Subject(models.Model):
    title = models.CharField(max_length=100)
    credit = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.title


class Assignment(models.Model):
    title = models.CharField(max_length=250)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name='assignment')
    teacher = models.CharField(max_length=100)
    date_of_issue = models.DateTimeField(auto_now_add=True, blank=True)
    deadline = models.DateTimeField()
    description = models.CharField(max_length=1000)
    penalties = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.subject.title} - {self.title}'


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="submission")
    solution = models.CharField(max_length=1000)
    date_of_submission = models.DateTimeField(auto_now_add=True, blank=True)
    grade = models.IntegerField(null=True, blank=True)
    remarks = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f'{ self.student.last_name } - { self.assignment.title }'
