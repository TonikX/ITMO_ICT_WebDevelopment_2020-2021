from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Client(AbstractUser):
    id = models.AutoField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return "{}".format(self.username)


class RoomType(models.Model):
    room_type = models.CharField("Type", max_length=50)

    class Meta:
        verbose_name = "Room_Type"
        verbose_name_plural = "Room_Types"

    def __str__(self):
        return self.room_type


class Facilities(models.Model):
    facilities = models.CharField("Facilities", max_length=50)

    def __str__(self):
        return self.facilities


class Room(models.Model):
    is_reserved = models.BooleanField("Reservation", default=False)
    owner = models.ManyToManyField('Client', verbose_name="Owner", through='Reservation')
    hotel = models.ForeignKey('Hotel', verbose_name="Hotel", on_delete=models.SET_NULL, null=True)
    number = models.IntegerField("Number")
    room_type = models.ForeignKey('RoomType', verbose_name="Type", on_delete=models.SET_NULL, null=True)
    capacity = models.IntegerField("Capacity")
    price = models.IntegerField("Price")

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def __str__(self):
        return "{}".format("Room: " + str(self.number) + str(", Hotel: ") + str(self.hotel))


class Hotel(models.Model):
    name = models.CharField("Name", max_length=50)
    address = models.CharField("Address", max_length=100)
    desc = models.TextField("Description", max_length=300)
    capacity = models.IntegerField("Capacity")
    facilities = models.ManyToManyField('Facilities', verbose_name="Facilities_")

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"

    def __str__(self):
        return "{}".format(self.name)


class Review(models.Model):
    start_date = models.DateField("StartDate", null=True)
    end_date = models.DateField("EndDate", null=True)
    user = models.ForeignKey('Client', verbose_name="User", on_delete=models.CASCADE)
    room = models.ForeignKey('Room', verbose_name="Room", on_delete=models.CASCADE)
    text = models.TextField("Review")
    created = models.DateTimeField("Date", auto_now_add=True, null=True)

    class Rating(models.IntegerChoices):
        very_unsatisfied = 1
        unsatisfied = 2
        neutral = 3
        satisfied = 4
        very_satisfied = 5

    rating_list = models.IntegerField(choices=Rating.choices, null=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return "{}".format(self.user)


class Reservation(models.Model):
    owner = models.ForeignKey('Client', verbose_name="Owner", on_delete=models.CASCADE)
    room = models.ForeignKey('Room', verbose_name="Room", on_delete=models.CASCADE)
    start_date = models.DateField("StartDate", null=True)
    end_date = models.DateField("EndDate", null=True)

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"

    def __str__(self):
        return "{}".format("Nickname: " + str(self.owner) + str(", ") + str(self.room))

# class GuestsBase(models.Model):
#     name = models.ForeignKey('Client', verbose_name="Name", on_delete=models.CASCADE)
#     room = models.ForeignKey('Room', verbose_name="Room", on_delete=models.CASCADE)
#     start_date = models.DateTimeField("StartDate", null=True)
#     end_date = models.DateTimeField("EndDate", null=True)
#
#     class Meta:
#         verbose_name = "Guests base"
#         verbose_name_plural = "Guests base"
#
#     def __str__(self):
#         return "{}".format("Nickname: " + str(self.name) + str(", ") + str(self.room))
