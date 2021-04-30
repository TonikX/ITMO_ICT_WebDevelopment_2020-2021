from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class Flight(models.Model):
    number = models.CharField(max_length=20, unique=True)
    airline = models.CharField(max_length=50)
    is_departure = models.BooleanField()
    gate = models.DecimalField(
        max_digits=2, blank=True, null=True, decimal_places=0)
    dep_time = models.TimeField()
    arr_time = models.TimeField()

    def get_absolute_url(self):
        return reverse('flight_detail_url', kwargs={'number': self.number})

    def get_reservation_url(self):
        return reverse('create_reservation_url', kwargs={'number': self.number})

    def get_comment_url(self):
        return reverse('comment_url', kwargs={'number': self.number})

    def get_passenger_list_url(self):
        return reverse('passenger_list_url', kwargs={'number': self.number})

    class Meta:
        ordering = ['dep_time', 'number']


class User(AbstractUser):
    flights = models.ManyToManyField(
        Flight, through='Reservation', related_name='passengers')
    first_name = models.CharField(_('first name'), max_length=150, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.CharField(max_length=3)
    ticket_number = models.DecimalField(
        max_digits=6, unique=True, null=True, decimal_places=0)
    date = models.DateField()

    def get_edit_reservation_url(self):
        return reverse('edit_reservation_url', kwargs={'pk': self.id, 'number': self.flight.number})

    class Meta:
        ordering = ['date', 'seat']


class Comment(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=0)
    fligh_date = models.DateField()
