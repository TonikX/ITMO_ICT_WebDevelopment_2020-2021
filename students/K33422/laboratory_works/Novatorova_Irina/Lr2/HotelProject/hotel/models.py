from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    owner = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(AbstractUser):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    room = models.ManyToManyField('Room', through='Booking')

    def __str__(self):
        return self.username


class Room(models.Model):
    room_num = models.IntegerField(default=101)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE)

    room_type = (
        ('S', 'Standart'),
        ('C', 'Comfort'),
        ('L', 'Luxe'),
        ('S', 'Suite')
    )
    room_type = models.CharField(max_length=30, choices=room_type)
    price = models.IntegerField(default=1000)

    def __str__(self):
        return "{}-{}-{}".format(self.hotel.name, self.room_num, self.room_type)


class Review(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    hotel = models.ForeignKey('Hotel', on_delete=models.SET_NULL, null=True)
    begin_date = models.DateField("Дата заезда", default=datetime.date.today)
    end_date = models.DateField("Дата выезда", default=datetime.date.today)
    rating = (
        ('5', 'все отлично'),
        ('4', 'могло быть и хуже'),
        ('3', 'не отлично, но и не ужасно'),
        ('2', 'могло быть и лучше'),
        ('1', 'все плохо')
    )
    rating = models.CharField(max_length=30, choices=rating, verbose_name='Оцените ваше пребывание в отеле')
    text = models.CharField(max_length=1000, verbose_name='Текст отзыва', null=True)
    created = models.DateTimeField("Дата добавления", auto_now_add=True, null=True)


class Booking(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    is_reserved = models.BooleanField(default=False)
    begin_date = models.DateField("Begin Date", default=datetime.date.today)
    end_date = models.DateField("End Date", default=datetime.date.today)

    def __str__(self):
        return "{}-{}".format(self.user.username, self.room.room_num)
