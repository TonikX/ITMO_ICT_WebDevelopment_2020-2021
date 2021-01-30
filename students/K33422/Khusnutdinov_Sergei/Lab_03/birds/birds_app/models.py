from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    passport = models.CharField(max_length=100, blank=True, null=True)
    salary = models.IntegerField(default=0)
    username = models.CharField(max_length=20, blank=True, null=True, unique=True)
    cell = models.ManyToManyField('Cell', through="Service")

    REQUIRED_FIELDS = ['first_name', 'last_name', 'passport']

    def __str__(self):
        return self.username


class Chicken(models.Model):
    weight = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE)
    egg_amount = models.IntegerField(default=0)
    cell = models.ForeignKey('Cell', on_delete=models.CASCADE)


class Breed(models.Model):
    PROD = (
      ("low", "Low"),
      ("avg", "Average"),
      ("high", "High")
    )
    breed = models.CharField(max_length=50)
    productivity = models.CharField(max_length=4, choices=PROD)
    avg_weight = models.IntegerField(default=0)
    diet = models.TextField()

    def __str__(self):
        return self.breed


class Cell(models.Model):
    tsekh = models.ForeignKey('Tsekh', on_delete=models.CASCADE)
    row = models.ForeignKey('Row', on_delete=models.CASCADE)
    cell = models.IntegerField(default=0)

    def __str__(self):
        return str(self.cell)


class Row(models.Model):
    tsekh = models.ForeignKey('Tsekh', on_delete=models.CASCADE)
    row = models.IntegerField(default=0)

    def __str__(self):
        return str(self.row)


class Tsekh(models.Model):
    tsekh = models.IntegerField(default=0)

    def __str__(self):
        return str(self.tsekh)


class Service(models.Model):
    username = models.ForeignKey('User', on_delete=models.CASCADE)
    cell = models.ForeignKey('Cell', on_delete=models.CASCADE)
    status = models.BooleanField(blank=True, null=True)