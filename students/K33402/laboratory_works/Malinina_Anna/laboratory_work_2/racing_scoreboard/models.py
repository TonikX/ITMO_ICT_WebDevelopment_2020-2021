from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.db import models

# Create your models here.
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from laboratory_work_2 import settings


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Racer(models.Model):
    RACER_CLASS = [
        ('A', 'мотоциклы'),
        ('B', 'легковые автомобили'),
        ('C', 'грузовые автомобили'),
        ('D', 'пассажирские автомобили'),
        ('M', 'мопеды и легкие квадроциклы'),
    ]
    description = models.CharField(max_length=200)
    car_description = models.CharField(max_length=200)
    experience_year = models.IntegerField(default=0)
    racer_class = models.CharField(max_length=30, choices=RACER_CLASS)
    user_info = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    team = models.CharField(max_length=100)

    def __str__(self):
        return self.user_info.__str__()

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('racer-detail', args=[str(self.id)])


@receiver(post_save, sender=Racer)
def create_racer(sender, instance, created, **kwargs):
    if created:
        g = Group.objects.get(name='racer')
        g.user_set.add(instance.user_info)


class Race(models.Model):
    name = models.CharField(max_length=200)
    datetime = models.DateTimeField(blank=True, null=True)
    racer = models.ManyToManyField(Racer, through='RaceRacer')

    class Meta:
        ordering = ['-datetime']

    def __str__(self):
        return self.name

    @property
    def sorted_racers_set(self):
        return self.raceracer_set.order_by(F('finish_time').asc(nulls_last=True))

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('race-detail', args=[str(self.id)])


class Comment(models.Model):
    CATEGORIES = [
        ('cooperation', 'сотрудничество'),
        ('race', 'вопрос о гонках'),
        ('other', 'иное'),
    ]
    RATING = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    ]
    type = models.CharField(max_length=15, choices=CATEGORIES)
    text = models.CharField(max_length=300, null=True, blank=True)
    rating = models.IntegerField(choices=RATING)
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class RaceRacer(models.Model):
    racer = models.ForeignKey(Racer, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    finish_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['finish_time']
