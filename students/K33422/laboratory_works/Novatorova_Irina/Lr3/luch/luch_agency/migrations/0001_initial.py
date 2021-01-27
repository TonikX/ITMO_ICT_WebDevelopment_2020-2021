# Generated by Django 3.1.5 on 2021-01-20 13:14

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата заявки')),
                ('ad_product', models.CharField(max_length=40, verbose_name='Рекламный продукт')),
                ('amount', models.CharField(max_length=40, verbose_name='Объем работ')),
                ('status', models.CharField(choices=[('p', 'payed'), ('n', 'not payed')], max_length=20, verbose_name='Состояние заявки')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=50, verbose_name='Контактное лицо')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=50, verbose_name='Электронный адрес')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_service', models.CharField(choices=[('b', 'banner'), ('f', 'film'), ('p', 'paper')], max_length=30, verbose_name='Тип материала')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование материала')),
                ('desc', models.CharField(max_length=150, verbose_name='Характеристики')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_service', models.CharField(choices=[('w', 'widescreen street banner'), ('p', 'polygraphy'), ('t', 'transport ads'), ('m', 'media ads')], max_length=30, verbose_name='Название услуги')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование услуги')),
                ('price', models.IntegerField(verbose_name='Цена (руб)')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('work_exp', models.IntegerField(verbose_name='Опыт работы (лет)')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(verbose_name='Дата оплаты')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luch_agency.application', verbose_name='Заявка')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luch_agency.client', verbose_name='Клиент')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luch_agency.service', verbose_name='Услуга')),
            ],
        ),
        migrations.CreateModel(
            name='Manufactory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Количество (шт)')),
                ('total_price', models.IntegerField(verbose_name='Стоимость (руб)')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luch_agency.application', verbose_name='Заявка')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luch_agency.material', verbose_name='Материал')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luch_agency.service', verbose_name='Услуга')),
            ],
        ),
        migrations.CreateModel(
            name='Application_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luch_agency.application', verbose_name='Заявка')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luch_agency.service', verbose_name='Услуга')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luch_agency.worker', verbose_name='Сотрудник')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luch_agency.client', verbose_name='Клиент'),
        ),
        migrations.AddField(
            model_name='application',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luch_agency.service', verbose_name='Услуга'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]