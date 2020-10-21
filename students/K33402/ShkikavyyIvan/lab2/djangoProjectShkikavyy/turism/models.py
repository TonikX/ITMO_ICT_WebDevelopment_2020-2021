from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=15, blank=True, null=True, unique=True)
    passport = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    tour = models.ManyToManyField('Tour', through="Reservation")


class Tour(models.Model):
    PAYMENT = [('Банковская карта', 'Банковская карта'), ('Наличные деньги', 'Наличные деньги'),
               ('Веб-сервисы', 'Веб-сервисы')]
    name = models.CharField(max_length=80)
    tour_agency = models.CharField(max_length=80)
    country = models.CharField(max_length=50)
    begin_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=500)
    pay = models.CharField(max_length=25, choices=PAYMENT)


class Comment(models.Model):
    RATING = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), ]
    begin_date = models.DateField()
    end_date = models.DateField()
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    rating = models.IntegerField(choices=RATING)


class Reservation(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    nameoftour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)
