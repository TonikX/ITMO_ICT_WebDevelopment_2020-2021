from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
import datetime


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birth_date = models.DateField(default=datetime.datetime.today)
    passport = models.CharField(max_length=12, default="1111")
    home_address = models.CharField(max_length=120, default="St. Petersburg")
    nationality = models.CharField(max_length=30, default="Russian")

    def __str__(self) -> str:
        return self.name + ' ' + self.surname + ' ' + str(self.birth_date)

class Car(models.Model):
    brand = models.CharField(max_length=30)
    car_model = models.CharField(max_length=30)
    color = models.CharField(max_length=25)
    number = models.CharField(max_length=8, default="A111AA")
    owners = models.ManyToManyField(get_user_model(), through='Possession')

    def __str__(self) -> str:
        return self.brand + ' ' + self.car_model + ' ' + str(self.number)

class Possession(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start = models.DateField(default=datetime.datetime.today)
    end = models.DateField(default=datetime.datetime.today)

class Certification(models.Model):
    number = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    type = models.IntegerField(choices=[
        (1, 'A'),
        (2, 'B')
    ])
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

