from django.db import models

#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.CharField(max_length=200, unique=True)

    REQUIRED_FIELDS = ['email']
    def __str__(self):
        return self.username



class Newspaper(models.Model):
    newspapers_name = models.CharField(max_length=120, verbose_name='Название газеты')
    editors_surname = models.CharField(max_length=20, verbose_name='Фамилия редактора')
    editors_name = models.CharField(max_length=20, verbose_name='Имя редактора')
    index = models.IntegerField(verbose_name='Индекс', default=0000)
    price = models.IntegerField(verbose_name='Цена', default=0)

    def __str__(self):
        return self.newspapers_name

class NewspapersParty(models.Model):
    party_number = models.IntegerField(verbose_name='Номер партии', default=0)
    amount_of_copies = models.IntegerField(verbose_name='Количесво экземпляров', default=0)
    newspapers_name = models.ForeignKey('newspapers_distribution.Newspaper', verbose_name='Газета', on_delete=models.CASCADE)

    def __int__(self):
        return self.party_number

class Print(models.Model):
    print_id = models.IntegerField(verbose_name='Номер печати', default=0)
    printery_name = models.ForeignKey('Printery', verbose_name='Название типографии', on_delete=models.CASCADE)
    party_number = models.ForeignKey('NewspapersParty', verbose_name='Партия',  on_delete=models.CASCADE)
    print_amount = models.IntegerField(verbose_name='Количесво печатаемых экземпляров', default=0)

    def __int__(self):
        return self.print_id


class Printery(models.Model):
    printery_name = models.CharField(max_length=120, verbose_name='Название типографии')
    printery_address = models.CharField(max_length=200, verbose_name='Адрес типографии')
    opening_time = models.TimeField(verbose_name='Время открытия', default='00:00:00')
    closing_time = models.TimeField(verbose_name='Время закрытия', default='00:00:00')

    def __str__(self):
        return self.printery_name

class PostOffice(models.Model):
    office_number = models.IntegerField(verbose_name='Номер отделения', default=0)
    office_address = models.CharField(max_length=200, verbose_name='Адрес отделения')

    def __int__(self):
        return self.office_number

class DistributionReport(models.Model):
    report_number = models.IntegerField(verbose_name='Номер отчёта', default=0)
    party_number = models.ForeignKey('NewspapersParty', verbose_name='Партия', on_delete=models.CASCADE)
    office_number = models.ForeignKey('PostOffice', verbose_name='Отделение', on_delete=models.CASCADE)
    print_amount = models.IntegerField(verbose_name='Количесво печатаемых экземпляров', default=0)

    def __int__(self):
        return self.report_number
