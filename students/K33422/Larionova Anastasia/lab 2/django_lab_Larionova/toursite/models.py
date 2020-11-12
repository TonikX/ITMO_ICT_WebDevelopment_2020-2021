from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=10, blank=True, null=True, unique=True)
    passport = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    tour = models.ManyToManyField('Tour', through="Reserve")


class Tour(models.Model):
    PAY = (
      ("card", "card"),
      ("cash", "cash")
    )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    tour_agency = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    country = models.CharField(max_length=30)
    payment = models.CharField(max_length=4, choices=PAY)



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
    name = models.ForeignKey('Tour', on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)