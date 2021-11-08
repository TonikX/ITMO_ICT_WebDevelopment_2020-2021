# Generated by Django 3.1.3 on 2020-11-23 11:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels_app', '0002_auto_20201123_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
    ]
