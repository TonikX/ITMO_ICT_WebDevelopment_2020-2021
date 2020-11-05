from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Owner(AbstractUser):
    birthday = models.DateField(blank=True, null=True)
    passport = models.CharField(max_length=100, blank=True, null=True)


class Licence(models.Model):
    LICENCE_TYPES = (
        ('A', 'Motorbike'),
        ('B', 'Car'),
        ('C', 'Truck'),
        ('D', 'Bus')
    )
    licence_id = models.IntegerField(primary_key=True)
    licence_date = models.DateField()
    type = models.CharField(max_length=1, choices=LICENCE_TYPES)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)


class Vehicle(models.Model):
    id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=50)
    owning = models.ManyToManyField(Owner, through="Ownership")


class Ownership(models.Model):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    buy_date = models.DateField(blank=True, null=True)
    sell_date = models.DateField(blank=True, null=True)
