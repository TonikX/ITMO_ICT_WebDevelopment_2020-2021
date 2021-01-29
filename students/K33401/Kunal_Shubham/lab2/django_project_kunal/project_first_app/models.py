from datetime import date
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CarOwner(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    passport = models.CharField(max_length=10, blank=True, unique=True)
    address = models.CharField(max_length=200, blank=True)
    nationality = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class DriverIdentity(models.Model):
    driver = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    number_identification = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_of_issue = models.DateField(default=now)

    def __str__(self):
        return f'{self.driver.last_name} {self.driver.first_name}'


class Car(models.Model):
    number_guest = models.CharField(max_length=15)
    marks = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.model


class Possession(models.Model):
    owner = ForeignKey(CarOwner, on_delete=models.CASCADE,
                       related_name='owner')
    car = ForeignKey(Car, on_delete=models.CASCADE, related_name='car')
    start_date = models.DateField(default=date(1997, 4, 10))
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.owner.last_name} - {self.car.model}'
