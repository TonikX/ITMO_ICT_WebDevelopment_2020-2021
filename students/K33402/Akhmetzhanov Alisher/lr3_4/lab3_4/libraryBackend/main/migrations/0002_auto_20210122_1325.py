# Generated by Django 3.1.2 on 2021-01-22 13:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=210)),
                ('author', models.CharField(max_length=410)),
                ('realise_date', models.DateField(default=datetime.date.today)),
                ('publishing_house', models.CharField(max_length=210)),
            ],
        ),
        migrations.CreateModel(
            name='Replica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cipher', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book')),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reader_ticket', models.IntegerField()),
                ('passport', models.CharField(max_length=300)),
                ('birth_date', models.DateField(default=datetime.date.today)),
                ('address', models.CharField(blank=True, max_length=210)),
                ('phone', models.CharField(blank=True, max_length=14)),
                ('is_scientist', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reader_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryHall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('title', models.CharField(max_length=210)),
                ('capacity', models.IntegerField(default=10)),
                ('readers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.CharField(default='Опыт есть', max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='librarian_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookReplica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book')),
                ('library_hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.libraryhall')),
                ('replica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.replica')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='copies',
            field=models.ManyToManyField(related_name='book_copies', through='main.BookReplica', to='main.Replica'),
        ),
    ]
