# Generated by Django 3.1.4 on 2020-12-05 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0003_auto_20201205_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charity',
            name='description',
            field=models.CharField(max_length=300, verbose_name='Описание сбора'),
        ),
    ]