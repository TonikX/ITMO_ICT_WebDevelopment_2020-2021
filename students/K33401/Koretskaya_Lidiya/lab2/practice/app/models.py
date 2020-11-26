from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Car_owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()

class Car(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    number = models.CharField(max_length=30)

class Driving_license(models.Model):
    license_number = models.IntegerField()
    date_of_issue = models.DateField()
    type_choices = [
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
        ('m', 'M'),
        ('tm', 'Tm'),
        ('tb', 'Tb'),
    ]
    type = models.CharField(max_length=30, choices=type_choices, default='a')
    car_owner = models.ForeignKey(Car_owner, on_delete=models.CASCADE)

class Ownership(models.Model):
    car_owner = models.ForeignKey(Car_owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_finish = models.DateField()

class Owner_info(Car_owner):
    passport_number = models.CharField(max_length=30, blank=True, null=True)
    home_address = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=30, blank=True, null=True)

