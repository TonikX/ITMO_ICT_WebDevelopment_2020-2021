# Generated by Django 3.1.7 on 2021-04-06 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='num_hotel',
            new_name='room',
        ),
    ]
