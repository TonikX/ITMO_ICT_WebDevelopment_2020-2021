from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, username, password=None, **extra_fields):

        if username is None:
            raise TypeError('Users must have username')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password, **extra_fields):

        if username is None:
            raise TypeError('Users must have username')

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(
            username,
            password,
            first_name='Админ',
            last_name='Админ',
            passport_number=1000000000,
            **extra_fields
            )
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class Car(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    licence_number = models.CharField(max_length=15, null=False)
    make = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.make} {self.model}'


class Owner(AbstractUser):
    id = models.AutoField(primary_key=True, null=False)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField(null=True)
    passport_number = models.IntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)], null=False)
    home_address = models.CharField(max_length=100, null=True, blank=True)
    nationality = models.CharField(max_length=100, null=False, default='Русский')
    car = models.ManyToManyField(Car, through='Ownership')

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class DriverLicence(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=False)
    number = models.CharField(max_length=10, null=False)
    type = models.CharField(max_length=10, null=False)
    date_issued = models.DateField(null=True)

    def __str__(self):
        return f'{self.owner} - {self.number}'


class Ownership(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
    date_issued = models.DateField(null=False)
    date_expired = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.owner} - {self.car}'
