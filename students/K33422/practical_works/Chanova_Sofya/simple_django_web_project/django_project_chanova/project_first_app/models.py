from django.db import models
from django.contrib.auth.models import AbstractUser


class Owner(AbstractUser):
    #first_name = models.CharField(max_length=50)
    #last_name = models.CharField(max_length=50)
    birth_date = models.DateField(blank=True, null=True)
    car = models.ManyToManyField('Car', through='CarOwnership')
    passport = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=40, blank=True, null=True)


class DriverLicense(models.Model):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50)
    issue_date = models.DateField()

    class LicenseType(models.TextChoices):
        A = 'A', "motorcycle"
        B = 'B', "car"
        C = 'C', "truck"
        D = 'D', "bus"
        M = 'M', "moped"

    license_type = models.CharField(
        max_length=2,
        choices=LicenseType.choices)


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    plate_number = models.CharField(max_length=50)


class CarOwnership(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    begin_date = models.DateField()
    end_date = models.DateField()
