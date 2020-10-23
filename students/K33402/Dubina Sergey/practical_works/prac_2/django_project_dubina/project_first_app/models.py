from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings



class Owner(AbstractUser):
    birthday = models.DateField(null=True)
    passport = models.CharField(max_length=10, blank=False, null=False, unique=True)
    address = models.CharField(max_length=200, blank=False, null=False)
    nationality = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    surname = models.CharField(max_length=200, blank=False, null=False)

class Car (models.Model):
	brand = models.CharField(max_length = 50)
	model = models.CharField(max_length = 50)
	color = models.CharField(max_length = 50)
	num = models.CharField(max_length = 50)
	session = models.ManyToManyField(Owner, through='Ownership')

	def __str__(self):
		return "{} {}".format(self.brand, self.model)

class Ownership (models.Model):
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
	car = models.ForeignKey(Car, on_delete=models.CASCADE)
	dateStart = models.DateField()
	dateEnd = models.DateField()

	def __str__(self):
		return "{} {} {}".format(self.owner, self.car, self.dateStart)

class DriverDocument (models.Model):
	TYPE_EX = (
		('t1', 'type1'),
		('t2', 'type2'),
		('t3', 'type3'))
	num = models.IntegerField(primary_key=True)
	owner = models.ForeignKey(Owner, on_delete = models.CASCADE)
	typeOfDoc = models.CharField(max_length=2, choices=TYPE_EX)
	date = models.DateField(default=date(2001, 4, 3))

	def __str__(self):
		return "{} {}".format(self.owner, self.num)

