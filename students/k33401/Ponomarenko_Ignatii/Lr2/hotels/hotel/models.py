from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Guest(AbstractUser):
	first_name = models.CharField(max_length=30, null=True)
	last_name = models.CharField(max_length=30, null=True)
	passport = models.IntegerField(null=True)

class RoomType(models.Model):
	name = models.CharField(max_length=30, null=True)
	cost = models.IntegerField(null=True)

	def __str__(self):
		return f'{self.name} ({self.cost}/день)'

class Hotel(models.Model):
	name = models.CharField(max_length=30, null=True)
	hotel_host = models.CharField(max_length=30, null=True)
	address = models.CharField(max_length=100, null=True)
	description = models.CharField(max_length=200, null=True)
	room_types = models.ManyToManyField(RoomType)
	rooms = models.IntegerField(null=True)
	comfort = models.CharField(max_length=200, null=True)

	def __str__(self):
		return f'{self.name}'

class Booking(models.Model):
	guest = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
	room = models.IntegerField(null=True)
	start = models.DateField()
	end = models.DateField()

	def __str__(self):
		return f'{self.hotel} {self.room}: {self.start}/{self.end}'

RATING_TYPE = []
for i in range(1, 11):
	RATING_TYPE.append((i, i))

class Review(models.Model):
	hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
	text = models.CharField(max_length=1000, null=True)
	rating = models.IntegerField(null=True, choices=RATING_TYPE)

	def __str__(self):
		return f'{self.hotel}: {self.text}'