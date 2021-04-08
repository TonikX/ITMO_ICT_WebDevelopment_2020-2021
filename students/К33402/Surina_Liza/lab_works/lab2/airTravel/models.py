from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse


# Create your models here.


class Schedule(models.Model):
    flight_number = models.CharField(max_length=100, db_index=True, unique=True)
    airline_company = models.CharField(max_length=100)
    date_of_departure = models.DateTimeField()
    arrival_date = models.DateTimeField()
    type = models.CharField(max_length=100)
    gate = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.flight_number)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'flight_number': self.flight_number})


class Booking(models.Model):
    user = models.ForeignKey(User,
                             verbose_name="Пользователь",
                             on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    surname = models.TextField(max_length=100)
    place = models.CharField(max_length=100)
    moderation = models.BooleanField("Модерация", default=False)
    plane = models.ForeignKey(Schedule,
                              verbose_name="Авиарейс",
                              on_delete=models.CASCADE)


class Comments(models.Model):
    user = models.ForeignKey(User,
                             verbose_name="Пользователь",
                             on_delete=models.CASCADE)
    flight = models.ForeignKey(Schedule,
                               verbose_name="Авиарейс",
                               on_delete=models.CASCADE)
    text = models.TextField("")
    created = models.DateTimeField("Дата добавления", auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"

    def __str__(self):
        return "{}".format(self.user)
