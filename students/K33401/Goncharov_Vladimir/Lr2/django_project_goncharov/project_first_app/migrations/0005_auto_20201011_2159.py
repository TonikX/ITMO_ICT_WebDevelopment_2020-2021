# Generated by Django 3.1.2 on 2020-10-11 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0004_auto_20201011_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
