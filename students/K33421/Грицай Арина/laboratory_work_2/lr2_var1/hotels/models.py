from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    passport = models.CharField(max_length=10, blank=True, null=True)
    telephone = models.CharField(max_length=11, blank=True, null=True)
    room = models.ManyToManyField('Room', through='Booking')


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    owner = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.CharField(max_length=4)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE)

    class RoomType(models.TextChoices):
        SGL = 'SGL', "Single"
        DBL = 'DBL', "Double"
        TRPL = 'TRPL', "Triple"
        FR = 'FR', "Family Room"
        DL = 'DL', "DeLuxe"

    room_type = models.CharField(choices=RoomType.choices, max_length=4)
    price = models.CharField(max_length=10)
    guests = models.CharField(max_length=1)

    def __str__(self):
        return self.number


class Booking(models.Model):
    arrival = models.DateField()
    departure = models.DateField()
    check_in = models.BooleanField(default=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)


class Review(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    class Rating(models.TextChoices):
        a = '1', "Awful"
        b = '2', "Bad"
        c = '3', "Not bad"
        d = '4', "Well"
        e = '5', "Excellent"

    rating = models.CharField(choices=Rating.choices, max_length=2)
    arrival = models.DateField()
    departure = models.DateField()
    comment = models.CharField(max_length=1000)
    hotel = models.ForeignKey('Hotel', on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
