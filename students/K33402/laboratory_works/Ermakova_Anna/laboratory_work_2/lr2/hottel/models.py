
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class Comentator(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="comentator_profile")
    DEFAULT_PK=1
    rating = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user.username + " Рейтинг: " + str(self.rating)


class Hotel(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=400, blank=True)
    owner = models.CharField(max_length=300, default="владелец")

    def __str__(self) -> str:
        return self.title + self.address


class Сonvenience(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.title


class HotelRoom(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms", default=1)
    number = models.IntegerField(default=1)
    type = models.IntegerField(choices=[
        (1, "Эконом"),
        (2, "Люкс"),
        (3, "Комфорт")
    ])
    prise = models.CharField(max_length=100)
    capacity = models.IntegerField(default=1)
    conveniences = models.ManyToManyField(Сonvenience, blank=True)
    free = models.BooleanField(default=True)

    def __str__(self) -> str:
        return "Отель: " + self.hotel.title + " Тип: " + str(self.type)


class UserRoom(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="user_history")
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name="room_history")
    begin_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)

    def __str__(self) -> str:
        return "Отель: " + self.hotel.title + " Пользователь: " + self.user.username


class RoomReservation(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="reservations")
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name="history")
    begin_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)

    def __str__(self) -> str:
        return "Пользователь: " + self.user.username + " Номер: " + str(self.room.number)


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="commentator_comments")
    accommodation = models.ForeignKey(UserRoom, on_delete=models.CASCADE, related_name="comments")
    text = models.CharField(max_length=410)

    def __str__(self) -> str:
        return "Пользователь: " + self.user.username + " Номер: " + str(self.accommodation.room.number)


