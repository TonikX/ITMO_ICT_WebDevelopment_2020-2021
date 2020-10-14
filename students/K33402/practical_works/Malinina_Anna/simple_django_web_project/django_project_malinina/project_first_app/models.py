from django.contrib.auth.models import AbstractUser
from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=10)

    def __str__(self):
        return "{} {}".format(self.brand, self.model)


class CarOwner(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    birthday = models.DateField()
    cars = models.ManyToManyField(Car, through='Ownership')

    def __str__(self):
        return "{} {}".format(self.name, self.surname)


class Ownership(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    date_start = models.DateField()
    date_end = models.DateField(null=True)


class DriverLicense(models.Model):
    CATEGORIES = (
        ('A', 'мотоциклы'),
        ('B', 'легковые автомобили'),
        ('C', 'грузовые автомобили'),
        ('D', 'пассажирские автомобили'),
        ('M', 'мопеды и легкие квадроциклы'),
        ('Tm', 'трамваи'),
        ('Tb', 'троллейбусы'),
    )
    id_number = models.IntegerField(primary_key=True)
    date = models.DateField()
    type = models.CharField(max_length=2, choices=CATEGORIES)
    driver = models.ForeignKey(CarOwner, on_delete=models.SET_NULL, null=True)
