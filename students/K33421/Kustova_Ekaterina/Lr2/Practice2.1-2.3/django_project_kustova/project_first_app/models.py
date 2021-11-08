from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()
    more_info = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return "{} {} ".format(self.first_name, self.last_name)


class Licence(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    type = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    date_of_giving = models.DateField()

    def __str__(self):
        return "{} {} {}".format(self.owner, self.type, self.number)


class Car(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    gov_number = models.CharField(max_length=30)
    owner = models.ManyToManyField(Owner, through='Possession')

    def __str__(self):
        return "{} {} {} {}".format(self.brand, self.model, self.color, self.gov_number)


class Possession(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_of_beginning = models.DateField()
    date_of_ending = models.DateField()

    def __str__(self):
        return "{} {}".format(self.owner, self.car)


class User(AbstractUser):
    passport = models.IntegerField(default=0000)
    address = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
