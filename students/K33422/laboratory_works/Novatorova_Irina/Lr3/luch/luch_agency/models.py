from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, unique=True)

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username


class Application(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='Клиент')
    service = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name='Услуга')
    date = models.DateField(verbose_name='Дата заявки')
    ad_product = models.CharField(max_length=40, verbose_name='Рекламный продукт')
    amount = models.CharField(max_length=40, verbose_name='Объем работ')

    status = (
        ('p', 'payed'),
        ('n', 'not payed'),
    )
    status = models.CharField(max_length=20, choices=status, verbose_name='Состояние заявки')

    def __str__(self):
        return "{}-{}-{}".format(self.client.client, self.service.title, self.date)


class Application_list(models.Model):
    application = models.ForeignKey('Application', verbose_name='Заявка', on_delete=models.CASCADE)
    worker = models.ForeignKey('Worker', verbose_name='Сотрудник', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name='Услуга')

    def __str__(self):
        return "{}-{}".format(self.application.ad_product, self.worker.name)


class Client(models.Model):
    client = models.CharField(max_length=50, verbose_name='Контактное лицо')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(max_length=50, verbose_name='Электронный адрес')

    def __str__(self):
        return self.client


class Manufactory(models.Model):
    application = models.ForeignKey('Application', verbose_name='Заявка', on_delete=models.CASCADE)
    material = models.ForeignKey('Material', verbose_name='Материал', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name='Услуга')
    quantity = models.IntegerField(verbose_name='Количество (шт)')
    total_price = models.IntegerField(verbose_name='Стоимость (руб)')

    def __str__(self):
        return "{}-{}".format(self.material.title, self.quantity)


class Material(models.Model):
    type_material = (
        ('b', 'banner'),
        ('f', 'film'),
        ('p', 'paper')
    )
    type_service = models.CharField(max_length=30, choices=type_material, verbose_name='Тип материала')
    title = models.CharField(max_length=50, verbose_name='Наименование материала')
    desc = models.CharField(max_length=150, verbose_name='Характеристики')

    def __str__(self):
        return self.title


class Payment_order(models.Model):
    payment_date = models.DateField(verbose_name='Дата оплаты')
    application = models.ForeignKey('Application', verbose_name='Заявка', on_delete=models.CASCADE)
    client = models.ForeignKey('Client', verbose_name='Клиент', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name='Услуга')

    def __str__(self):
        return "{}-{}".format(self.client.client, self.payment_date)


class Service(models.Model):
    type_service = (
        ('w', 'widescreen street banner'),
        ('p', 'polygraphy'),
        ('t', 'transport ads'),
        ('m', 'media ads')
    )
    type_service = models.CharField(max_length=30, choices=type_service, verbose_name='Название услуги')
    title = models.CharField(max_length=50, verbose_name='Наименование услуги')
    price = models.IntegerField(verbose_name='Цена (руб)')

    def __str__(self):
        return self.title


class Worker(models.Model):
    name = models.CharField(max_length=50, verbose_name='ФИО')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    work_exp = models.IntegerField(verbose_name='Опыт работы (лет)')

    def __str__(self):
        return self.name
