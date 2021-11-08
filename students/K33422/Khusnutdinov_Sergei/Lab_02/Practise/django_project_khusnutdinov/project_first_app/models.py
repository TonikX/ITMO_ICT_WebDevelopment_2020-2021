from django.db import models

# Create your models here.
class Owner(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	date_of_b = models.DateField()

class Driver_License(models.Model):
	owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
	TYPES = (
		('A', 'Moto'),
		('B', 'Auto'),
		('C', 'Track'),
	)
	number_of_license = models.CharField(max_length=10)
	type = models.CharField(max_length=10, choices=TYPES)
	date_of_given = models.DateField()

class Car(models.Model):
	name = models.CharField(max_length=50)
	model = models.CharField(max_length=50)
	color = models.CharField(max_length=50)
	gov_numb = models.CharField(max_length=50)
	owners = models.ManyToManyField('Owner', through='Membership')

class Membership(models.Model):
	owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
	car = models.ForeignKey('Car', on_delete=models.CASCADE)
	date_of_beginning = models.DateField()
	date_of_ending = models.DateField()

class SAdmin(models.Model):
	name = models.CharField(max_length=30)
		