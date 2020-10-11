# Generated by Django 3.1.2 on 2020-10-11 20:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id_number', models.IntegerField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=30)),
                ('label', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birthday', models.DateField(default=datetime.date(2000, 1, 27))),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(default=datetime.date(2000, 1, 1))),
                ('date_send', models.DateField(default=datetime.date(2000, 1, 1))),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.car')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.driver')),
            ],
        ),
        migrations.CreateModel(
            name='DriverLicense',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('a', 'motorcycles'), ('b', 'car'), ('c', 'truck')], max_length=2)),
                ('issue_date', models.DateField(default=datetime.date(2020, 10, 11))),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.driver')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='session',
            field=models.ManyToManyField(through='project_first_app.Ownership', to='project_first_app.Driver'),
        ),
    ]
