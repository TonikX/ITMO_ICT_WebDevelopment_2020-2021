from django.db import models


# Модель автовладелец
class CarOwner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()


# Водительское удостоверение
class Card(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.SET_NULL, null=True)
    number_card = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    release_date = models.DateField()


# Автомобиль
class Car(models.Model):
    G_num = models.CharField(max_length=15)
    mark = models.CharField(max_length=20)
    model_car = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


# Владение
class Owner(models.Model):
    car_owner = models.ForeignKey(CarOwner, on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    data_start = models.DateField()
    data_end = models.DateField()


class ExampleModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Publisher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
