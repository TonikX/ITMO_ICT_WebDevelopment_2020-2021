from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import datetime
from django.utils import timezone

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
    
    def __str__(self):
        return '{}'.format(self.name)


class Coach(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return '{}'.format(self.name)
           
           
class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return '{}'.format(self.name)
    
    
class Session(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    weekday = models.CharField(max_length=3, choices=weekdays)
    time = models.TimeField()
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{} {} {}'.format(self.weekday, self.lesson, self.time)
    
    
class Booking(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()
    
    def __str__(self):
        return '{} {} {}'.format(self.client.username, self.session.lesson.name, self.date)
    

    