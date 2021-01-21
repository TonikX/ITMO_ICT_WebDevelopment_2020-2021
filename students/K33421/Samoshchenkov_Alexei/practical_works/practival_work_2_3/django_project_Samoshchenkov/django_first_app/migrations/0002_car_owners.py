# Generated by Django 3.1.3 on 2020-11-24 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='owners',
            field=models.ManyToManyField(through='django_first_app.Ownership', to='django_first_app.Driver'),
        ),
    ]
