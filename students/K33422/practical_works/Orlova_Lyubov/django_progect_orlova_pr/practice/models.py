# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser


class CarOwner(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    passport = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=30, blank=True, null=True)


class Car(models.Model):
    color = models.CharField(max_length=20)
    reg_num = models.CharField(max_length=10)
    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=20)
    use = models.ManyToManyField(CarOwner, through="Ownership")

    def __str__(self):
        return "{} {} {}".format(self.reg_num, self.brand, self.model)


class Ownership(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)


class DriverLicense(models.Model):
    TYPES = (
        ('A', 'Motocycle'),
        ('B', 'Car'),
        ('C', 'Truck'),
        ('D', 'Bus')
    )
    license_num = models.IntegerField()
    date_of_issue = models.DateField()
    type = models.CharField(max_length=1, choices=TYPES)
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
