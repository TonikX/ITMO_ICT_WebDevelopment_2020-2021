from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings


class Driver(AbstractUser):
    id = models.AutoField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    birthday = models.DateField(null=True)
    passport = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, null=True)
    nationality = models.CharField(max_length=50, null=True)


class DriverLicence(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    date = models.DateField()
    type = {
        ("A", "Motorcycle"),
        ("B", "Car"),
        ("C", "Truck"),
        ("D", "Bus"),
        ("M", "Moped")
    }
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)


class Car(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    owner = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Ownership')


class Ownership(models.Model):
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
