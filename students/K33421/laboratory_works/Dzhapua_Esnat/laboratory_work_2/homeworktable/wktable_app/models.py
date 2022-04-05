from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    tasks = models.ManyToManyField('Task', through='Submission')


class Task(models.Model):
    subject = models.CharField(max_length=15)
    teacher = models.TextField(max_length=40)
    receive_date = models.DateField()
    due_date = models.DateField()
    description = models.TextField(max_length=1000)
    punishment = models.TextField(max_length=50)

    def __str__(self):
        return "{}-{}-{}".format(self.id, self.subject, self.receive_date)


class Submission(models.Model):
    student_subm = models.ForeignKey(User, on_delete=models.CASCADE)
    task_subm = models.ForeignKey(Task, on_delete=models.CASCADE)
    grade_subm = models.CharField(max_length=1)
    submission = models.TextField(max_length=400)