from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings


class Carowner(AbstractUser):
    id = models.AutoField(unique=True, primary_key=True)
    lastname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    birthday = models.DateField(null=True)
    passportnum = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=50, null=True)
    ethnicity = models.CharField(max_length=30, null=True)


class License(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    carowner = models.ForeignKey(Carowner, on_delete=models.CASCADE)
    LICTYPE = {
        ("A", "Motorcycle"),
        ("B", "Car"),
        ("C", "Truck"),
        ("D", "Bus"),
    }
    type = models.CharField(max_length=2, choices=LICTYPE, default='Choose')
    licnumber = models.CharField(max_length=10)
    date = models.DateField()


class Car(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    number = models.CharField(max_length=15)
    mark = models.CharField(max_length=20)
    carmodel = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    carowner = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Ownership')


class Ownership(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    carowner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField(null=True)