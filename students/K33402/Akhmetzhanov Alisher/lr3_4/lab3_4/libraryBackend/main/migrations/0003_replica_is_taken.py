# Generated by Django 3.1.2 on 2021-01-22 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210122_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='replica',
            name='is_taken',
            field=models.BooleanField(default=False),
        ),
    ]
