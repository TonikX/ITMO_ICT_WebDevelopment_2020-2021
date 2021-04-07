# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    passport = models.CharField(max_length=10, blank=False, null=False, unique=True)
    address = models.TextField(max_length=200, blank=False, null=False)
    nationality = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField(null=True)


class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    l_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=20, null=True)

    def __str__(self):
        return "{} {}".format(self.brand, self.model)


class CarOwner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True)
    cars = models.ManyToManyField(Car, through='Ownership')

    def __str__(self):
        return "{} {}".format(self.surname, self.name)


class DriverLicense(models.Model):
    license_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_of_issue = models.DateField()


class Ownership(models.Model):
    ownership_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Car, on_delete=models.CASCADE)
    beginning_date = models.DateField()
    expiring_date = models.DateField(null=True)

    def __str__(self):
        return "{} {}".format(self.owner, self.vehicle)
