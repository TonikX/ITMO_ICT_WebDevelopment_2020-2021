from django.db import models


class Car(models.Model):
    state_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

    def __str__(self):
        return "{} {}".format(self.brand, self.model)


class CarOwner(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birthday = models.DateField()
    cars = models.ManyToManyField(Car, through='Ownership')

    def __str__(self):
        return "{} {}".format(self.name, self.surname)


class Ownership(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    date_start = models.DateField()
    date_end = models.DateField(null=True)


class DriverLicense(models.Model):
    CATEGORIES = (
        ('A', 'Мотоциклы'),
        ('B', 'Легковые автомобили'),
        ('C', 'Грузовые автомобили'),
        ('D', 'Пассажирские автомобили'),
        ('M', 'Мопеды и легкие квадроциклы'),
        ('Tm', 'Трамваи'),
        ('Tb', 'Троллейбусы'),
    )

    driver = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    id_number = models.IntegerField()
    type = models.CharField(max_length=2, choices=CATEGORIES)
    date = models.DateField()

