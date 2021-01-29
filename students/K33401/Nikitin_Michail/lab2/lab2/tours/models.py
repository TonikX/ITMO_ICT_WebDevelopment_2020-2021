from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=False)
    passport = models.IntegerField(null=True)
    comments = models.ForeignKey()


class Tour(models.Model):
    name = models.CharField(max_length=30, default='tour_name', unique=True)
    tour_agency = models.CharField(max_length=60)
    description = models.CharField(max_length=150, null=True)
    date_of_tour = models.DateField(null=True)
    tour_duration = models.IntegerField(null=True)
    payment = models.IntegerField(default=10000)
    count_of_place = models.IntegerField(default=15)
    count_of_booked = models.IntegerField(default=0)


class UsersComments(models.Model):
    RATING = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), ]
    text = models.CharField(max_length=150)
    rate = models.IntegerField(choices=RATING)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Booked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
