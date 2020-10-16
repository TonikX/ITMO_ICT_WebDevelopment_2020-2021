from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

"""class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)"""

class Homework(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()

class Assignment(models.Model):
    hw_id = models.ForeignKey(Homework, on_delete=models.CASCADE)
    text = models.TextField()
    mark = models.DecimalField(max_digits=1, decimal_places=0, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
