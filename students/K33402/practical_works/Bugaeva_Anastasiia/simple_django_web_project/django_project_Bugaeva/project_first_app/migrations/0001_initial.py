# Generated by Django 3.2 on 2021-04-06 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_number', models.CharField(max_length=15)),
                ('brand', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CarOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField(null=True)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_first_app.car')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_first_app.carowner')),
            ],
        ),
        migrations.CreateModel(
            name='DriverLicense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.IntegerField()),
                ('type', models.CharField(choices=[('A', 'Мотоциклы'), ('B', 'Легковые автомобили'), ('C', 'Грузовые автомобили'), ('D', 'Пассажирские автомобили'), ('M', 'Мопеды и легкие квадроциклы'), ('Tm', 'Трамваи'), ('Tb', 'Троллейбусы')], max_length=2)),
                ('date', models.DateField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.carowner')),
            ],
        ),
        migrations.AddField(
            model_name='carowner',
            name='cars',
            field=models.ManyToManyField(through='project_first_app.Ownership', to='project_first_app.Car'),
        ),
    ]
