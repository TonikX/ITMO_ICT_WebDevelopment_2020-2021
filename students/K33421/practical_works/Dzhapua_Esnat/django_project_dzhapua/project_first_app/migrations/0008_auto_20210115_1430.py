# Generated by Django 3.1.2 on 2021-01-15 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0007_auto_20210115_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='type',
            field=models.CharField(choices=[('A', 'Motorcycle'), ('C', 'Truck'), ('D', 'Bus'), ('B', 'Car')], default='Choose', max_length=2),
        ),
    ]
