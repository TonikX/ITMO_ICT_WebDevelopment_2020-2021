from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import datetime


class User(AbstractUser):
    phone = models.CharField("Телефон", max_length=15, blank=True, null=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Airline(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.name)


class CityAirport(models.Model):
    cityName = models.CharField(max_length=30)
    airportName = models.CharField(max_length=30)

    def __str__(self):
        return "{}: {}".format(self.cityName, self.airportName)


class Flight(models.Model):
    company = models.ForeignKey(Airline, on_delete=models.CASCADE)
    num_flight = models.IntegerField()
    numberOfPackages = models.IntegerField()
    departure = models.ForeignKey(CityAirport, verbose_name='Город, аэропорт', related_name="departure",
                                  on_delete=models.CASCADE)
    arrival = models.ForeignKey(CityAirport, verbose_name='Город, аэропорт', related_name="Arrival",
                                on_delete=models.CASCADE)
    departure_date = models.DateTimeField(null=True)
    arrival_date = models.DateTimeField(null=True)

    def __str__(self):
        return "{} → {}".format(self.departure, self.arrival)


class Place(models.Model):
    num_flight = models.ForeignKey(Flight, on_delete=models.CASCADE, verbose_name='Рейс', blank=True,
                                   related_name='numberFlight')
    passenger = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пассажир', blank=True,
                                  null=True)

    def __str__(self):
        return "{} → {}".format(self.num_flight, self.passenger)


class Comment(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, verbose_name='Рейс', blank=True, null=True,
                               related_name='Flight')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец комментария', blank=True,
                               null=True)
    create_date = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    text = models.TextField(verbose_name='Текст комментария')
    status = models.BooleanField(verbose_name='Видимость комментария', default=True)

    def __str__(self):
        return "{} → {}".format(self.flight, self.author)
