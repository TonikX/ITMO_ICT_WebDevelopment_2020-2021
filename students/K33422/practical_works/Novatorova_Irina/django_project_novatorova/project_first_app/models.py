from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings

class Driver(AbstractUser):
    id = models.AutoField(unique= True, primary_key=True, default =1)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField(null=True)
    passport = models.CharField(max_length=50, blank = True, null = True)
    address = models.CharField(max_length=100, null= True)
    nationality = models.CharField(max_length=50, null= True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class DriverLicence(models.Model):
    id = models.AutoField(unique = True, primary_key=True)
    date = models.DateField()
    type = {
    ("A", "Motorcycle"),
    ("B", "Car"),
    ("C", "Truck"),
    ("D", "Bus"),
    ("M", "Moped")
    }
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.driver, self.type)


class Car(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    usage = models.ManyToManyField(settings.AUTH_USER_MODEL, through="Ownership")

    def __str__(self):
        return "{} {}".format(self.brand, self.model)


class Ownership(models.Model):
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return "{} {}".format(self.driver, self.car)

