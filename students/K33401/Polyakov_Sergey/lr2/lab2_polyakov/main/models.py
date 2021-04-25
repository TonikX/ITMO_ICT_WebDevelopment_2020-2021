from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=15, blank=True, null=True, unique=True)
    passport = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    tours = models.ManyToManyField('Tour', through="Reservation")


class Tour(models.Model):
    PAYMENTS = [('Банковская карта', 'Банковская карта'), ('Наличные деньги', 'Наличные деньги'),
               ('Веб-сервисы', 'Веб-сервисы')]
    name = models.CharField(max_length=80)
    agency = models.CharField(max_length=80)
    country = models.CharField(max_length=50)
    begin_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=500)
    pay = models.CharField(max_length=25, choices=PAYMENTS, default='Банковская карта')

    def __str__(self):
        return f'{self.name}, {self.country} ({self.begin_date} - {self.end_date})'


class Comment(models.Model):
    RATING_CHOICES = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), ]
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    tour = models.ForeignKey("Tour", on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=RATING_CHOICES)


class Reservation(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    tour = models.ForeignKey("Tour", on_delete=models.CASCADE)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    confirmed = models.BooleanField(blank=True, null=True, default=False)
