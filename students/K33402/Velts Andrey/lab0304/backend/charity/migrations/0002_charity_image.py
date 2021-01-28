# Generated by Django 3.1.4 on 2020-12-05 15:45

import charity.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='charity',
            name='image',
            field=models.ImageField(default='avatar/default.png', upload_to=charity.utils.path_and_rename, verbose_name='Изображение'),
        ),
    ]