from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    address = models.TextField(max_length=300)

    REQUIRED_FIELDS = ('address', 'first_name', 'last_name')

    def __str__(self):
        return self.username


class Car(models.Model):
    name = models.CharField(max_length=12)
    breed = models.TextField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(auto_now=True)
    cars = models.ManyToManyField(Car, through='CarToOrder')

    def __str__(self):
        return f'{self.id}_{self.user.username}'


class CarToOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'Car_{self.car.id}_Order_{self.order.id}'








