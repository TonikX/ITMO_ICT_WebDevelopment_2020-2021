# Generated by Django 3.1.2 on 2020-10-15 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='country_number',
            new_name='official_number',
        ),
    ]