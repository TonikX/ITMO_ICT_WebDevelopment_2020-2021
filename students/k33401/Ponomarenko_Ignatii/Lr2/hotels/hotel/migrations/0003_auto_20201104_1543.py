# Generated by Django 2.0.1 on 2020-11-04 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20201103_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('cost', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='comfort',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_host',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='rooms',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='room_types',
            field=models.ManyToManyField(to='hotel.RoomType'),
        ),
    ]
