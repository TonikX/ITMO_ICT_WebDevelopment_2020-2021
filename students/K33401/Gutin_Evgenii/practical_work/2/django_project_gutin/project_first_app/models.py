from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_of_birth = models.DateField(null=True)
    passport = models.CharField(max_length=10, blank=False, null=False, unique=True)
    address = models.TextField(max_length=200, blank=False, null=False)
    nationality = models.CharField(max_length=30, blank=True, null=True)


class DriverLicense(models.Model):
    license_id = models.AutoField(primary_key=True)
    date_of_issue = models.DateField()
    allowed_types = models.CharField(max_length=8)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Vehicle(models.Model):
    manufacturer = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    plate = models.CharField(max_length=7)
    owners = models.ManyToManyField(
        User,
        through='Property',
        through_fields=('vehicle', 'owner')
    )


class Property(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date_of_issue = models.DateField()
    date_of_expiring = models.DateField()
