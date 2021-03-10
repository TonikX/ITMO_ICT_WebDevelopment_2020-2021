from django.contrib.auth.models import AbstractUser
from django.db import models
from practice_2 import settings


class User(AbstractUser):
    passport = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    nationality = models.CharField(max_length=30)


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    number = models.CharField(max_length=10)

    def __str__(self):
        return "{} {}".format(self.brand, self.model)


class Driver(models.Model):
    user_info = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    birthday = models.DateField(null=True)
    cars = models.ManyToManyField(Car, through='Ownership')

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Ownership(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True)


class DriverLicense(models.Model):
    id_number = models.IntegerField(primary_key=True)
    type = {
        ("A", "Motorcycle"),
        ("B", "Car"),
        ("C", "Truck"),
        ("D", "Bus"),
        ("M", "Moped")
    }
    date = models.DateField()
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
