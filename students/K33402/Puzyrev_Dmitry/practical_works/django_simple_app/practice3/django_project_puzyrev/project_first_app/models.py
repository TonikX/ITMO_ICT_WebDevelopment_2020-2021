from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models


class Driver(AbstractUser):
	first_name = models.CharField(max_length=100, null=True)
	last_name = models.CharField(max_length=100, null=True)
	birthday = models.DateField(null=True)
	passport = models.CharField(max_length=10, unique=True, null=True)
	address = models.CharField(max_length=200, default='No address')
	nationality = models.CharField(max_length=30, default='Citizen of the world')



class Car(models.Model):
	brand = models.CharField(max_length=100)
	model = models.CharField(max_length=100)
	color = models.CharField(max_length=30)
	official_number = models.CharField(max_length=30)
	owners = models.ManyToManyField(Driver, through='Ownership')

	def __str__(self):
		return f'{self.brand} ({self.model}), {self.color} color, official number: {self.official_number}'

	# id_number = models.IntegerField(primary_key=True)


class Ownership(models.Model):
	owner = models.ForeignKey(Driver, on_delete=models.CASCADE)
	car = models.ForeignKey(Car, on_delete=models.CASCADE)
	start_date = models.DateField()
	end_date = models.DateField()

	def __str__(self):
		return f'{self.owner}: {self.car}, {self.start_date:%d.%m.%y} - {self.end_date:%d.%m.%y}'


class DrivingLicence(models.Model):
	LICENCE_TYPES = (
		('A', 'Motorcycles'),
		('B', 'Cars'),
		('D', 'Buses'),
	)
	number = models.IntegerField()
	date_of_issue = models.DateField()
	type = models.CharField(max_length=1, choices=LICENCE_TYPES)
	owner = models.ForeignKey(Driver, on_delete=models.CASCADE)

	def __str__(self):
		return f'number: {self.number}, owner: {self.owner}'