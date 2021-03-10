from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(AbstractUser):
    id = models.AutoField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    classe = models.CharField(max_length=3)
    tasks = models.ManyToManyField('Task', through='Submission')

    def __str__(self):
        return "{}-{}-{}".format(self.first_name, self.last_name, self.classe)


class Task(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    subject = models.CharField(max_length=15)
    teacher = models.TextField(max_length=40)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(max_length=1000)
    punishment = models.TextField(max_length=50)

    def __str__(self):
        return "{}-{}-{}".format(self.subject, self.teacher, self.end_date)


class Submission(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    grade = models.CharField(blank=True, null=True, max_length=2)
    submission = models.TextField(max_length=400)

    def __str__(self):
        return "{}-{}".format(self.student, self.task)