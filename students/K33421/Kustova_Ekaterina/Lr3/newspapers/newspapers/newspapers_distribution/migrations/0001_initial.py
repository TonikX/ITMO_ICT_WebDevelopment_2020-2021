# Generated by Django 3.1.2 on 2021-01-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newspaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newspapers_name', models.CharField(max_length=120, verbose_name='Название газеты')),
                ('editors_surname', models.CharField(max_length=20, verbose_name='Фамилия редактора')),
                ('editors_name', models.CharField(max_length=20, verbose_name='Имя редактора')),
                ('index', models.IntegerField(default=0, verbose_name='Индекс')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='PostOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_number', models.IntegerField(default=0, verbose_name='Номер отделения')),
                ('office_address', models.CharField(max_length=200, verbose_name='Адрес отделения')),
            ],
        ),
        migrations.CreateModel(
            name='Printery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('printery_name', models.CharField(max_length=120, verbose_name='Название типографии')),
                ('printery_address', models.CharField(max_length=200, verbose_name='Адрес типографии')),
                ('opening_time', models.TimeField(default='00:00:00', verbose_name='Время открытия')),
                ('closing_time', models.TimeField(default='00:00:00', verbose_name='Время закрытия')),
            ],
        ),
    ]
