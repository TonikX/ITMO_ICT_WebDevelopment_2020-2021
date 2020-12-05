from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    date_of_birth = models.DateField(verbose_name='Дата рождения', default='2000-01-01')
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Pizza(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.IntegerField(default=0, verbose_name='Цена')

    def __str__(self):
        return self.name


class Order(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    pizzas = models.ManyToManyField(Pizza, through='OrderedPizzas', verbose_name='Пиццы')

    def __str__(self):
        return f'{self.id}-{self.person.username}'


class OrderedPizzas(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1, verbose_name='Количество')
