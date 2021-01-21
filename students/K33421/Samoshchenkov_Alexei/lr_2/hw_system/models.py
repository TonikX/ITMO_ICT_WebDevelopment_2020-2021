from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    homeworks = models.ManyToManyField('Homework', through='Answer')


class Homework(models.Model):
    course = models.CharField(max_length=100)
    teacher = models.CharField(max_length=80)
    date = models.DateField()
    deadline = models.DateField()
    description = models.TextField(max_length=10000)

    def __str__(self):
        return "{}:{}:{}".format(self.id, self.course, self.date)


class Answer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    grade = models.CharField(max_length=3)
    answer = models.TextField(max_length=1000)