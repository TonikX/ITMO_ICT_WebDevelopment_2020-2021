from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=30, blank=True, null=True, unique=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    conf = models.ManyToManyField('Conf', through="Reserve")


class Conf(models.Model):
    THEMES = (
      ("it", "IT"),
      ("economy", "Economy"),
      ("biology", "Biology"),
      ("government", "Government")
    )
    conf_name = models.CharField(max_length=100)
    conf_theme = models.CharField(max_length=15, choices=THEMES)
    conf_location = models.CharField(max_length=50)
    conf_start_date = models.DateField()
    conf_end_date = models.DateField()
    conf_description = models.CharField(max_length=300)
    conf_location_description = models.CharField(max_length=100)
    conf_req = models.CharField(max_length=100)



class Review(models.Model):
    MARKS = (
      ("1", "1"),
      ("2", "2"),
      ("3", "3"),
      ("4", "4"),
      ("5", "5"),
      ("6", "6"),
      ("7", "7"),
      ("8", "8"),
      ("9", "9"),
      ("10", "10")
    )
    start_date = models.DateField()
    end_date = models.DateField()
    username = models.ForeignKey('User', on_delete=models.CASCADE)
    comment = models.TextField(max_length=300)
    rate = models.CharField(max_length=2, choices=MARKS)


class Reserve(models.Model):
    username = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.ForeignKey('Conf', on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)