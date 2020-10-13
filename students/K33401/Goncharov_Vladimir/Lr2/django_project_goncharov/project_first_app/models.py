from django.db import models
from datetime import date
import datetime


class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(default=date(2000, 1, 27))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Car(models.Model):
    id_number = models.CharField(max_length=9)
    owner = models.ManyToManyField(Driver, through='Ownership')
    model = models.CharField(max_length=30)
    label = models.CharField(max_length=30)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id_number} {self.model} {self.label}"


class Ownership(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField(default=date(2000, 1, 1))
    date_end = models.DateField(default=date(2000, 1, 1))


class DriverLicense(models.Model):
    TYPE_EX = (
        ('a', 'motorcycles'),
        ('b', 'car'),
        ('c', 'truck'),
    )
    id = models.IntegerField(primary_key=True)
    owner = models.ForeignKey(Driver, on_delete=models.CASCADE)
    type = models.CharField(max_length=2,
                            choices=TYPE_EX)
    issue_date = models.DateField(default=datetime.date.today())
