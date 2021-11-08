from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, unique=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return self.username


class Room(models.Model):
    ROOM_TYPE = (
        ('3', '3 beds'),
        ('2', '2 beds'),
        ('1', '1 bed'))

    number = models.IntegerField(primary_key=True, unique=True)
    type = models.CharField(max_length=1, choices=ROOM_TYPE)
    price = models.IntegerField()
    floor = models.IntegerField()
    cleaners = models.ManyToManyField('Staff', through='Cleaning')


class Guest(models.Model):
    passport_number = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    from_location = models.CharField(max_length=100)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    room = models.ForeignKey('Room', on_delete=models.PROTECT, related_name='guests')

    def __str__(self):
        return "{} {}".format(self.first_name, self.surname)


class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)

    def __str__(self):
        return "{} {}".format(self.first_name, self.surname)


class Cleaning(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='cleaning')
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='cleaning')
    date_time = models.DateTimeField()
