from django.contrib.auth.models import AbstractUser
from django.db import models
from django_project_malinina import settings

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    user_info = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cars = models.ManyToManyField(Car, through='Ownership')

    def __str__(self):
        return "{} {}".format(self.name, self.surname)

class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=50)

    def __str__(self):
        return "{} {}".format(self.brand, self.model)

class License(models.Model):
    CATEGORIES = (
        ('A', 'Мотоциклы, мотороллеры и другой мощный тяжёлый двухколёсный мототранспорт'),
        ('B', 'Легковые автомобили и небольшие грузовики'),
        ('C', 'Грузовые автомобили'),
        ('D', 'Автобусы')
    )
    id_number = models.IntegerField(primary_key=True)
    date = models.DateField()
    type = models.CharField(max_length=1, choices=CATEGORIES)
    driver = models.ForeignKey(CarOwner, on_delete=models.SET_NULL, null=True)

class Ownership(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    date_start = models.DateField()
    date_end = models.DateField(null=True)

class User(AbstractUser):
    passport = models.CharField(max_length=14)
    address = models.CharField(max_length=100)
    nationality = models.CharField(max_length=30)