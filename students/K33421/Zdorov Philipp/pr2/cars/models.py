from django.db import models
from django.contrib.auth.models import AbstractUser
from random import randint


class Owner(AbstractUser):
    birth_date = models.DateField(default=None, null=True)
    passport = models.CharField(max_length=10, default='0000000000')
    nationality = models.CharField(max_length=15, default=None, null=True)
    home_address = models.CharField(max_length=40, default=None, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {str(self.birth_date)}'


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    license_plate = models.CharField(max_length=6, unique=True)
    owner = models.ManyToManyField(to=Owner, through='Ownership')

    def __str__(self):
        return f'{self.license_plate} {self.brand} {self.color}'


class Ownership(models.Model):
    owner = models.ForeignKey(to=Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(to=Car, on_delete=models.CASCADE)
    start_ownership_date = models.DateField()
    end_ownership_date = models.DateField(null=True, default=None)


class DrivingLicense(models.Model):
    number = models.CharField(max_length=50, unique=True)
    date_of_issue = models.DateField()
    owner = models.ForeignKey(to=Owner, on_delete=models.CASCADE)

    driving_license_types = (
        ('A', 'motorcycles'),
        ('В', 'cars'),
        ('C', 'trucks'),
        ('D', 'public transport'),
    )
    license_type = models.CharField(max_length=2, choices=driving_license_types)

    def __str__(self):
        return f'{self.number} {self.license_type}'
