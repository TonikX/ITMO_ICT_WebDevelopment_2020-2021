from django.db import models
from users.models import User
from item.models import Item


class Order(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through='OrderedItem')
    description = models.TextField("Описание", max_length=200)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f'{self.id}-{self.person.username}'


class OrderedItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField('Количество', default=1)
