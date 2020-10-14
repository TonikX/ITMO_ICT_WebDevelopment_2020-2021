from django.db import models
from userprofile.models import UserProfile


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return '{}'.format(self.name)


class Room(models.Model):
    typeRoom = [
        ('standard', 'standard'),
        ('improved', 'improved'),
        ('luxury', 'luxury'),
    ]
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    type = models.CharField(max_length=15, choices=typeRoom, default='standard')
    cost = models.IntegerField()
    capacity = models.IntegerField()
    conveniences = models.CharField(max_length=50)


class Reserve(models.Model):
    typeReserve = [
        ('generated', 'generated'),
        ('confirmed', 'confirmed'),
        ('refused', 'refused'),
        ('completed', 'completed'),
    ]
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    type = models.CharField(max_length=15, choices=typeReserve, default='generated')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return '{} - {}'.format(self.start_date, self.end_date)


class Feedback(models.Model):
    typeRating = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    ]
    reserve = models.ForeignKey(Reserve, on_delete=models.CASCADE)
    rating = models.CharField(max_length=15, choices=typeRating, default='5')
    description = models.CharField(max_length=250)

    def __str__(self):
        return '{}'.format(self.reserve.user.first_name)


