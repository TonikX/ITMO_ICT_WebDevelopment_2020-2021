# Generated by Django 3.1.3 on 2020-12-03 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels_app', '0011_auto_20201203_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='status',
        ),
        migrations.DeleteModel(
            name='RoomStatus',
        ),
    ]
