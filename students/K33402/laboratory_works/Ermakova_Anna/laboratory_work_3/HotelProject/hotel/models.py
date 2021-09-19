from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import date


class User(AbstractUser):
    phone = models.CharField("Телефон", max_length=15, blank=True, null=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    def __str__(self):
        return "{}".format(self.username)


class Hotel(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField(verbose_name="Адрес")
    def __str__(self):
        return "{}. Адрес: {}".format(self.name, self.address)


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    num_room = models.IntegerField()
    places = models.IntegerField()

    def __str__(self):
        return "{}:{}".format(self.hotel, self.num_room)


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Отель', blank=True,
                             related_name='room')
    guest = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Гость', blank=True,
                              null=True)
    CheckIn = models.DateTimeField(null=True)
    CheckOut = models.DateTimeField(null=True)

    def __str__(self):
        return "{} -> {}".format(self.room, self.guest)


class Comments(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='Отель', blank=True, null=True,
                              related_name='Hotel')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец комментария', blank=True,
                               null=True)
    create_date = models.DateTimeField(auto_now=True)
    Rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    text = models.TextField(verbose_name='Текст комментария')

    def __str__(self):
        return "{} -> {}".format(self.hotel, self.author)


