from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from .utils import path_and_rename


class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        error_messages={
            "unique": "Пользователь с данным email уже зарегистрирован.",
        },
    )
    image = models.ImageField(
        "Изображение",
        upload_to=path_and_rename,
        default="avatar/default.png",
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
