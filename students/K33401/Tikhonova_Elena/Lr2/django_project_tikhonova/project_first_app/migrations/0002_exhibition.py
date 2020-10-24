# Generated by Django 3.1.2 on 2020-10-18 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ex', models.CharField(max_length=100)),
                ('date_b', models.DateField()),
                ('date_c', models.DateField()),
                ('type', models.CharField(choices=[('C1', 'CACIB'), ('C2', 'CAC'), ('M', 'MONO')], max_length=2)),
            ],
        ),
    ]
