# Generated by Django 3.1.5 on 2021-02-04 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hackathon.team'),
            preserve_default=False,
        ),
    ]
