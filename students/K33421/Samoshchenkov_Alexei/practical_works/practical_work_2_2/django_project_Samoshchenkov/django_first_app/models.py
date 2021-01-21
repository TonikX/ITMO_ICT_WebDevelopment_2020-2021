from datetime import date
from django.db import models


class Driver(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    date_of_birth = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.date_of_birth:%d.%m.%y}'


class Car(models.Model):
    owners = models.ManyToManyField(Driver, through='Ownership')
    brand = models.CharField(max_length=80)
    model = models.CharField(max_length=80)
    colour = models.CharField(max_length=20)
    id_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.brand} {self.model} {self.colour} {self.id_number}'


class Ownership(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()

    def __str__ (self):
        return f'{self.driver} {self.car} {self.start:%d.%m.%y}-{self.end:%d.%m.%y}'


class Licence(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    id_licence = models.IntegerField()
    date_of_obtainment = models.DateField()
    CHOICES = (('A', 'Motocycles'), ('B', 'Cars'), ('C', 'Trucks'), ('D', 'Buses'), ('M', 'Mopeds'))
    type_of_licence = models.CharField(max_length=1, choices=CHOICES)

    def __str__(self):
        return f'{self.id_licence} : {self.driver}'
