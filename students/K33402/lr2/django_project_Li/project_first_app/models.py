from django.db import models
from datetime import date
from django.conf import settings

# Create your models here.



class Driver(models.Model):
    optional_information = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birthday = models.DateField(default=date(2000, 1, 1))
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Car(models.Model):
    id_number = models.IntegerField(primary_key=True)
    session = models.ManyToManyField(Driver, through='Possession')
    model = models.CharField(max_length=30)
    label = models.CharField(max_length=30)
    color = models.CharField(max_length=30)

    def __str__(self):
        return "{} {} {}".format(self.id_number, self.model, self.label)


class Possession(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField(default=date(2000, 1, 1))
    date_end = models.DateField(default=date(2000, 1, 1))

    def __str__(self):
        return "{} {} {} - {}".format(self.driver, self.car.model,  self.date_start, self.date_end)


class DriverDocument(models.Model):
    TYPE_EX = (
        ('t1', 'type1'),
        ('t2', 'type2'),
        ('t2', 'type2'),
    )
    id = models.IntegerField(primary_key=True)
    driver_document = models.ForeignKey(Driver, on_delete=models.CASCADE)
    type = models.CharField(max_length=2,
                            choices=TYPE_EX)
    class_dog = models.CharField(max_length=30)
