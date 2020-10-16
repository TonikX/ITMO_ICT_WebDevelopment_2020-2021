from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
     passport = models.IntegerField(default=0000)
     address = models.CharField(max_length=100)
     nationality = models.CharField(max_length=100)

class Person(models.Model):
    optional = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = models.TextField()
    surname = models.TextField()
    birthday = models.DateField()

class Car(models.Model):
    brand = models.TextField()
    model = models.TextField()
    color = models.TextField()
    number = models.CharField(max_length=8)
    owner = models.ManyToManyField(Person, through='Ownership', null=True)

class DriverLicence(models.Model):
    CATEGORIES = (
        ('A', 'Moto'),
        ('B', 'Car'),
        ('C', 'Truck'),
        ('D', 'Bus'),
    )
    number = models.PositiveIntegerField()
    date = models.DateField()
    category = models.CharField(max_length=1, choices=CATEGORIES)
    driver = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    
class Ownership(models.Model):
    start = models.DateField(default="1970-01-01")
    end = models.DateField(default="1970-01-01")
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    driver = models.ForeignKey(Person, on_delete=models.CASCADE)
    