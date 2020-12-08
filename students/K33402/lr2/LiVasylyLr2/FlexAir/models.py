from distutils.command import register

from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django import template


class Airlines(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.name)




class Flight(models.Model):
    company = models.ForeignKey(Airlines, on_delete=models.CASCADE)
    num_flight = models.IntegerField()
    departure = models.TextField(max_length=200, verbose_name='Город, аэропорт')  # отлет
    Arrival = models.TextField(max_length=200, verbose_name='Город, аэропорт')  # прилет
    NumberOfPackages = models.IntegerField()
    departure_date = models.DateTimeField(null=True)
    Arrival_date = models.DateTimeField(null=True)

    def __str__(self):
        return "{} -> {}".format(self.departure, self.departure)

    @property
    def is_past_due(self):
        return date.today() > self.departure_date

    def count(self):
        return range(self.NumberOfPackages)


class Place(models.Model):
    num_flight = models.ForeignKey(Flight, on_delete=models.CASCADE, verbose_name='Рейс', blank=True,
                                   related_name='numberFlight')
    passenger = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пассажир', blank=True,
                                  null=True)

    def save(self, *args, **kwargs):
        if self.num_flight.numberFlight.all().count() >= self.num_flight.NumberOfPackages:
            return
        super(Place, self).save(*args, **kwargs)

    def __str__(self):
        return "{} -> {}".format(self.num_flight, self.passenger)


class Comments(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, verbose_name='Рейс', blank=True, null=True,
                               related_name='Flight')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец комментария', blank=True,
                               null=True)
    create_date = models.DateTimeField(auto_now=True)
    Rating = models.IntegerField()
    text = models.TextField(verbose_name='Текст коммпентария')
    status = models.BooleanField(verbose_name='Видимость комментария', default=True)

    def __str__(self):
        return "{} -> {}".format(self.flight, self.author)
