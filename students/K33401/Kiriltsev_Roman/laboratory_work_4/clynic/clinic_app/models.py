from django.db import models
from django.contrib.auth.models import AbstractUser


class Doctor(AbstractUser):
    id = models.AutoField(unique=True, primary_key=True)
    fio = models.CharField(max_length=60, null=False, verbose_name='ФИО')
    speciality = models.CharField(max_length=30, verbose_name='Специальность')
    education_types = (
        ('VSH', "Высшее"),
        ('VSN', "Высшее неоконченное"),
        ('SRD', "Среднее"),
        ('SRS', "Среднее специальное"),
    )
    education = models.CharField(choices=education_types, max_length=3, verbose_name='Уровень образования')
    birthdate = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    work_years = models.IntegerField(verbose_name='Трудовой стаж')
    cabinet = models.ManyToManyField('Cabinet', through='Schedule')

    REQUIRED_FIELDS = ['email', 'fio', 'work_years']

    def __str__(self):
        return "{}".format(self.fio)


class Cabinet(models.Model):
    number = models.IntegerField(unique=True, primary_key=True, verbose_name='Номер кабинета')
    owner = models.CharField(max_length=50, verbose_name='Ответственный')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')

    def __str__(self):
        return "{}".format(self.number)


class Schedule(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    id_doctor = models.ForeignKey('Doctor', verbose_name='Врач', on_delete=models.CASCADE)
    number_cabinet = models.ForeignKey('Cabinet', verbose_name='Номер кабинета', on_delete=models.CASCADE)
    start_time = models.TimeField(verbose_name='Время начала')
    end_time = models.TimeField(verbose_name='Время конца')
    day = models.CharField(max_length=60, verbose_name='День недели')


class Price(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Название услуги')
    price = models.IntegerField(verbose_name='Стоимость (в рублях)')

    def __str__(self):
        return "{}".format(self.name)


class Patient(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    fio = models.CharField(max_length=60, verbose_name='ФИО пациента')
    birthdate = models.DateField(verbose_name='Дата рождения')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')
    passport = models.CharField(max_length=10, verbose_name='Паспортные данные')

    def __str__(self):
        return "{}".format(self.fio)


class Diagnosis(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=50, verbose_name="Название диагноза")

    def __str__(self):
        return "{}".format(self.name)


class Medcard(models.Model):
    id_patient = models.ForeignKey('Patient', verbose_name='Пациент', on_delete=models.CASCADE)
    id_diagnosis = models.ForeignKey('Diagnosis', verbose_name='Диагноз', on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name='Дата установки диагноза')
    status = models.CharField(max_length=60, verbose_name='Статус заболевания')


class Meeting(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    id_patient = models.ForeignKey('Patient', verbose_name='Пациент', on_delete=models.CASCADE)
    id_doctor = models.ForeignKey('Doctor', verbose_name='Врач', on_delete=models.CASCADE)
    id_price = models.ForeignKey('Price', verbose_name='Услуга', on_delete=models.CASCADE)
    date_meet = models.DateField(verbose_name='Дата приёма')
    time_meet = models.TimeField(verbose_name='Время приёма')
    status = models.CharField(max_length=50, verbose_name='Текущее состояние')
    price_status = models.BooleanField(default=False, verbose_name='Оплачено')