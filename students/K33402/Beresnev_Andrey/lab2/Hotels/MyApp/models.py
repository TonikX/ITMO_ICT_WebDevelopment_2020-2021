from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings


class Client(AbstractUser):
    username = models.CharField(
        max_length=30, unique=True)
    password = models.CharField(max_length=30)
    is_superuser = models.BooleanField(default=False)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True)
    passport = models.IntegerField(null=True)
    nationality = models.CharField(max_length=30)


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    rating = models.IntegerField()
    adress = models.CharField(max_length=30)
    stars = models.IntegerField()


class Room(models.Model):
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.IntegerField()
    price = models.IntegerField()
    rating = models.IntegerField(null=True)
    capacity = models.IntegerField()


class ReservedRooms(models.Model):
    client_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True)


class Review(models.Model):
    TYPES = (
        ('5', 'Excellent'),
        ('4', 'Good'),
        ('3', 'Decent'),
        ('2', 'Bad'),
        ('1', 'Very Bad')
    )
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    client_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE)
    rating = models.CharField(max_length=5, choices=TYPES)
    description = models.CharField(max_length=1000)
