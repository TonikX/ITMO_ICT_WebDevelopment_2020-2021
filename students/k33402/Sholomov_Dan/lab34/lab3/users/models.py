from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db import models
from django.apps import apps
from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(self.model._meta.app_label,
                                         self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        username = email.split("@")[0]
        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        error_messages={
            "unique": "Пользователь с данным email уже зарегистрирован.",
        },
    )
    city = models.CharField("Город", max_length=80, null=True, blank=True)
    country_code = models.CharField("Код Страны", max_length=4, null=True, blank=True)
    country = models.CharField("Страна", max_length=80, null=True, blank=True)
    phone_number = models.CharField(
        "Номер телефона", max_length=30, blank=True, null=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.get_full_name()
