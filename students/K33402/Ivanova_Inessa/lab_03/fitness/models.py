from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import datetime
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

weekdays = [
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wen', 'Wensday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
    ('Sat', 'Saturday'),
    ('Sun', 'Sunday')
]

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return '{}'.format(self.username)
        

class Client(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    tel = models.CharField(max_length=12)
    bookings = models.ManyToManyField('LessonSession', through='Booking')
    
    def __str__(self):
        return '{}'.format(self.name)


class Coach(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return '{}'.format(self.name)
           
           
class LessonType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return '{}'.format(self.name)
    
    
class LessonSession(models.Model):
    lesson_type = models.ForeignKey(LessonType, on_delete=models.CASCADE)
    weekday = models.CharField(max_length=3, choices=weekdays)
    time = models.TimeField()
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{} {}'.format(self.weekday, self.lesson_type, self.time)
    
    
class Booking(models.Model):
    session = models.ForeignKey(LessonSession, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    def __str__(self):
        return '{} {}'.format(self.client.username, self.session.lesson_type.name)
    

    