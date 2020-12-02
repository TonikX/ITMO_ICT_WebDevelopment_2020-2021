from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date
from django.utils.timezone import now
from django.conf import settings


class Driver(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(default=date(2000, 1, 27))
    passport = models.CharField(max_length=10, blank=True, unique=True)
    address = models.TextField(max_length=200, blank=True)
    nationality = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Car(models.Model):
    id_number = models.CharField(max_length=9)
    owner = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Ownership')
    model = models.CharField(max_length=30)
    label = models.CharField(max_length=30)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id_number} {self.model} {self.label}"


class Ownership(models.Model):
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField(default=date(2000, 1, 1))
    date_end = models.DateField(default=date(2000, 1, 1))


class DriverLicense(models.Model):
    TYPE_EX = (
        ('a', 'motorcycles'),
        ('b', 'car'),
        ('c', 'truck'),
    )
    id = models.IntegerField(primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=2,
                            choices=TYPE_EX)
    issue_date = models.DateField(default=now)
