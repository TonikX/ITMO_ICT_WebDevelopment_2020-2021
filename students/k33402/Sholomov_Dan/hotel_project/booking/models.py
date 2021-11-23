from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    passport = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    room = models.ManyToManyField('Room', through='Booking')


class Hotel(models.Model):
    name = models.CharField(max_length=40)
    owner = models.CharField(max_length=40)
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.CharField(max_length=4)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE)

    class RoomType(models.TextChoices):
        s = 's', "Small"
        m = 'st', "Medium"
        l = 'l', "Large"
        xl = 'xl', "Premium"

    room_type = models.CharField(max_length=2, choices=RoomType.choices)
    price = models.IntegerField()
    num_persons = models.IntegerField()

    def __str__(self):
        return self.number


class Booking(models.Model):
    date_in = models.DateField()
    date_out = models.DateField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    checked_in = models.BooleanField(default=False)


class Review(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    class Rating(models.TextChoices):
        f = '1'
        d = '2'
        c = '3'
        b = '4'
        a = '5'

    hotel = models.ForeignKey('Hotel', on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    rating = models.CharField(max_length=1, choices=Rating.choices)
    date_in = models.DateField()
    date_out = models.DateField()
    body = models.CharField(max_length=1000)
