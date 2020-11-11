from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
import random
import string
from django.conf import settings


def get_random_string(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

class CarOwner(AbstractUser):
	username = models.CharField(max_length=30, default=get_random_string, unique=True)
	password = models.CharField(max_length=230)
	last_login = models.DateField(default=datetime.datetime.now)
	is_superuser = models.BooleanField(default=False)

	first_name = models.CharField(max_length=30, null=True)
	last_name = models.CharField(max_length=30, null=True)
	birth = models.DateField(null=True)
	cars = models.ManyToManyField('Car', through='Ownership')
	passport = models.IntegerField(null=True)
	address = models.CharField(max_length=100, null=True)
	nationality = models.CharField(max_length=30, null=True)

	def __str__(self):
		return f'{self.last_name} {self.first_name}'

class Car(models.Model):
	# owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
	brand = models.CharField(max_length=30)
	model = models.CharField(max_length=30)
	color = models.CharField(max_length=30)
	number = models.CharField(max_length=30)
	
	def __str__(self):
		return f'{self.brand} {self.model}'

class Ownership(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	car = models.ForeignKey(Car, on_delete=models.CASCADE)
	ownership_start = models.DateField()
	ownership_end = models.DateField()

	def __str__(self):
		return f'{self.owner} {self.car} н: {self.ownership_start} к: {self.ownership_end}'

class License(models.Model):
	LICENSE_TYPES = (
		('A', 'Тип A'),
		('B', 'Тип B'),
		('C', 'Тип C'),
		('D', 'Тип D'),
	)
	number = models.IntegerField()
	issued_at = models.DateField()
	license_type = models.CharField(max_length=1, choices=LICENSE_TYPES)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)