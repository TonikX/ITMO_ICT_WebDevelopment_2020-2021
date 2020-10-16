from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models


class Driver(AbstractUser):
    date_of_birth = models.DateField(null=True)
    passport = models.CharField(max_length=10, blank=False, null=False, unique=True)
    address = models.CharField(max_length=200, blank=False, null=False)
    nationality = models.CharField(max_length=30, blank=True, null=True)


class Car(models.Model):
    id_number = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    color = models.CharField(max_length=30)
    official_number = models.CharField(max_length=30)
    owners = models.ManyToManyField(Driver, through='Owning')


class Owning(models.Model):
    owner = models.ForeignKey(Driver, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    begin_date = models.DateField(default=date(2000, 1, 1))
    end_date = models.DateField(default=date(2001, 1, 1))


class DrivingLicence(models.Model):
    TYPE_EX = (
        ('t1', 'type1'),
        ('t2', 'type2'),
        ('t2', 'type2'),
    )
    number = models.IntegerField(primary_key=True)
    owner = models.ForeignKey(Driver, on_delete=models.CASCADE)
    date_of_issue = models.DateField(default=date(1990, 1, 1))
    type = models.CharField(max_length=3, choices=TYPE_EX)

